# Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java<a name="video-analyzing-with-sqs"></a>

This procedure shows you how to detect labels in a video by using Rekognition Video label detection operations, a video stored in an Amazon S3 bucket, and an Amazon SNS topic\. The procedure also shows how to use an Amazon SQS queue to get the completion status from the Amazon SNS topic\. For more information, see [Calling Rekognition Video Operations](api-video.md)\. You aren't restricted to using an Amazon SQS queue\. For example, you can use an AWS Lambda function to get the completion status\. For more information, see [Invoking Lambda functions using Amazon SNS notifications](http://docs.aws.amazon.com/sns/latest/dg/sns-lambda.html)\.

The procedure shows you how to use the [Amazon SNS console](https://console.aws.amazon.com/sns/v2/home) to do the following:

+ Create the Amazon SNS topic\.

+ Create the Amazon SQS queue\.

+ Give Rekognition Video permission to publish the completion status of a video analysis operation to the Amazon SNS topic\.

+ Subscribe the Amazon SQS queue to the Amazon SNS topic\.

**Note**  
This procedure uses a single Amazon SQS queue and a single Amazon SNS topic for all video analysis requests\. 

The example code in the procedure shows you how to do the following: 

1. Start the video analysis request by calling [StartLabelDetection](API_StartLabelDetection.md)\. 

1. Get the completion status from the Amazon SQS queue\. The sample tracks the job identifier \(`JobId`\) that's returned in `StartLabelDetection` and only gets the results for matching job identifiers that are read from the completion status\. This is an important consideration if other applications are using the same queue and topic\. Any other jobs are ignored\.

1. Get and display the video analysis results by calling [GetLabelDetection](API_GetLabelDetection.md)\.

## Prerequisites<a name="video-prerequisites"></a>

To run this procedure, you need to have the AWS SDK for Java installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account that you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. 

**To Detect Labels in a Video**

1. If you haven't already, create an IAM service role to give Rekognition Video access to your Amazon SNS topics\. Note the ARN\. For more information, see [Giving Access to Multiple Amazon SNS Topics](api-video-roles.md#api-video-roles-all-topics)\.

1. [Create an Amazon SNS topic](http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) by using the [Amazon SNS console](https://console.aws.amazon.com/sns/v2/home)\. Prepend the topic name with *AmazonRekognition*\. Note the topic Amazon Resource Name \(ARN\)\. 

1. [Create an Amazon SQS standard queue](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-create-queue.html) by using the [Amazon SQS console](https://console.aws.amazon.com/sqs/)\. Note the queue ARN\.

1. [Subscribe the queue to the topic](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-subscribe-queue-sns-topic.html) you created in step 2\.

1. Upload an \.mp4, \.mov or \.avi format video file to your S3 Bucket\. For test purposes, upload a video that's no longer than 30 seconds in length\.

   For instructions, see [Uploading Objects into Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. Use the following AWS SDK for Java code to detect labels in a video\. 

   + Replace `TopicArn`, `RoleArn`, and `QueueURL` with the Amazon SNS topic ARN, IAM role ARN, and Amazon SQS queue URL that you previously noted\.

   + Replace `Bucket` and `VideoFile` with the bucket and video file name that you uploaded in step 5\. 

   +  Replace `Endpoint` and `Region` with the AWS endpoint and region that you're using\.

   + Update `.withRegion` parameters to the region you are using\.

   + Change `RekognitionUser` to an AWS account that has permissions to call Rekognition Video operations\. 

   ```
   package com.amazonaws.samples;
   import com.amazonaws.AmazonClientException;
   import com.amazonaws.auth.AWSCredentials;
   import com.amazonaws.auth.AWSStaticCredentialsProvider;
   import com.amazonaws.auth.profile.ProfileCredentialsProvider;
   import com.amazonaws.client.builder.AwsClientBuilder.EndpointConfiguration;
   import com.amazonaws.regions.Regions;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.CelebrityDetail;
   import com.amazonaws.services.rekognition.model.CelebrityRecognition;
   import com.amazonaws.services.rekognition.model.CelebrityRecognitionSortBy;
   import com.amazonaws.services.rekognition.model.ContentModerationDetection;
   import com.amazonaws.services.rekognition.model.ContentModerationSortBy;
   import com.amazonaws.services.rekognition.model.Face;
   import com.amazonaws.services.rekognition.model.FaceDetection;
   import com.amazonaws.services.rekognition.model.FaceMatch;
   import com.amazonaws.services.rekognition.model.GetCelebrityRecognitionRequest;
   import com.amazonaws.services.rekognition.model.GetCelebrityRecognitionResult;
   import com.amazonaws.services.rekognition.model.GetContentModerationRequest;
   import com.amazonaws.services.rekognition.model.GetContentModerationResult;
   import com.amazonaws.services.rekognition.model.GetFaceDetectionRequest;
   import com.amazonaws.services.rekognition.model.GetFaceDetectionResult;
   import com.amazonaws.services.rekognition.model.GetFaceSearchRequest;
   import com.amazonaws.services.rekognition.model.GetFaceSearchResult;
   import com.amazonaws.services.rekognition.model.GetLabelDetectionRequest;
   import com.amazonaws.services.rekognition.model.GetLabelDetectionResult;
   import com.amazonaws.services.rekognition.model.GetPersonTrackingRequest;
   import com.amazonaws.services.rekognition.model.GetPersonTrackingResult;
   import com.amazonaws.services.rekognition.model.LabelDetection;
   import com.amazonaws.services.rekognition.model.LabelDetectionSortBy;
   import com.amazonaws.services.rekognition.model.NotificationChannel;
   import com.amazonaws.services.rekognition.model.PersonDetection;
   import com.amazonaws.services.rekognition.model.PersonMatch;
   import com.amazonaws.services.rekognition.model.PersonTrackingSortBy;
   import com.amazonaws.services.rekognition.model.S3Object;
   
   import com.amazonaws.services.rekognition.model.StartCelebrityRecognitionRequest;
   import com.amazonaws.services.rekognition.model.StartCelebrityRecognitionResult;
   import com.amazonaws.services.rekognition.model.StartContentModerationRequest;
   import com.amazonaws.services.rekognition.model.StartContentModerationResult;
   import com.amazonaws.services.rekognition.model.StartFaceDetectionRequest;
   import com.amazonaws.services.rekognition.model.StartFaceDetectionResult;
   import com.amazonaws.services.rekognition.model.StartFaceSearchRequest;
   import com.amazonaws.services.rekognition.model.StartFaceSearchResult;
   import com.amazonaws.services.rekognition.model.StartLabelDetectionRequest;
   import com.amazonaws.services.rekognition.model.StartLabelDetectionResult;
   import com.amazonaws.services.rekognition.model.StartPersonTrackingRequest;
   import com.amazonaws.services.rekognition.model.StartPersonTrackingResult;
   import com.amazonaws.services.rekognition.model.Video;
   import com.amazonaws.services.rekognition.model.VideoMetadata;
   import com.amazonaws.services.sns.AmazonSNS;
   import com.amazonaws.services.sns.AmazonSNSClientBuilder;
   import com.amazonaws.services.sqs.AmazonSQS;
   import com.amazonaws.services.sqs.AmazonSQSClientBuilder;
   import com.amazonaws.services.sqs.model.Message;
   import com.fasterxml.jackson.databind.JsonNode;
   import com.fasterxml.jackson.databind.ObjectMapper;
   import java.sql.Time;
   import java.util.*;
   
   public class VideoDetect {
      private static AmazonSNS sns = null;
      private static AmazonSQS sqs = null;
      private static AmazonRekognition rek = null;
      private static NotificationChannel channel= new NotificationChannel()
            .withSNSTopicArn("TopicArn")
            .withRoleArn("RoleArn");
   
      private static String queueUrl =  "QueueURL";
      private static String startJobId = null;
   
   
      public static void main(String[] args)  throws Exception{
   
   
         AWSCredentials credentials;
   
         try {
            credentials = new ProfileCredentialsProvider("RekognitionUser").getCredentials();
         } catch (Exception e) {
            throw new AmazonClientException("Cannot load the credentials from the credential profiles file. "
                  + "Please make sure that your credentials file is at the correct "
                  + "location (/Users/userid>.aws/credentials), and is in valid format.", e);
         }
   
         sns = AmazonSNSClientBuilder
               .standard()
               .withRegion(Regions.US_EAST_1)
               .withCredentials(new AWSStaticCredentialsProvider(credentials))
               .build();
   
         sqs = AmazonSQSClientBuilder
               .standard()
               .withRegion(Regions.US_EAST_1)
               .withCredentials(new AWSStaticCredentialsProvider(credentials))
               .build();
   
   
         rek = AmazonRekognitionClientBuilder.standard().withCredentials( new ProfileCredentialsProvider("RekognitionUser"))
               .withEndpointConfiguration(new EndpointConfiguration("Endpoint", "Region")).build();  
   
   
         //=================================================
         StartLabels("Bucket", "VideoFile");
         //=================================================
         System.out.println("Waiting for job: " + startJobId);
         //Poll queue for messages
         List<Message> messages=null;
         int dotLine=0;
         boolean jobFound=false;
   
         //loop until the job status is published. Ignore other messages in queue.
         do{
            //Get messages.
            do{
               messages = sqs.receiveMessage(queueUrl).getMessages();
               if (dotLine++<20){
                  System.out.print(".");
               }else{
                  System.out.println();
                  dotLine=0;
               }
            }while(messages.isEmpty());
   
            System.out.println();
   
            //Loop through messages received.
            for (Message message: messages) {
               String notification = message.getBody();
   
               // Get status and job id from notification.
               ObjectMapper mapper = new ObjectMapper();
               JsonNode jsonMessageTree = mapper.readTree(notification);
               JsonNode messageBodyText = jsonMessageTree.get("Message");
               ObjectMapper operationResultMapper = new ObjectMapper();
               JsonNode jsonResultTree = operationResultMapper.readTree(messageBodyText.textValue());
               JsonNode operationJobId = jsonResultTree.get("JobId");
               JsonNode operationStatus = jsonResultTree.get("Status");
               System.out.println("Job found was " + operationJobId);
               // Found job. Get the results and display.
               if(operationJobId.asText().equals(startJobId)){
                  jobFound=true;
                  System.out.println("Job id: " + operationJobId );
                  System.out.println("Status : " + operationStatus.toString());
                  if (operationStatus.asText().equals("SUCCEEDED")){
                     //============================================
                     GetResultsLabels();
                     //============================================
                  }
                  else{
                     System.out.println("Video analysis failed");
                  }
   
                  sqs.deleteMessage(queueUrl,message.getReceiptHandle());
               }
   
               else{
                  System.out.println("Job received was not job " +  startJobId);
               }
            }
         } while (!jobFound);
   
   
         System.out.println("Done!");
      }
   
   
      private static void StartLabels(String bucket, String video) throws Exception{
   
         StartLabelDetectionRequest req = new StartLabelDetectionRequest()
               .withVideo(new Video()
                     .withS3Object(new S3Object()
                           .withBucket(bucket)
                           .withName(video)))
               .withMinConfidence(50F)
               .withJobTag("DetectingLabels")
               .withNotificationChannel(channel);
   
         StartLabelDetectionResult startLabelDetectionResult = rek.startLabelDetection(req);
         startJobId=startLabelDetectionResult.getJobId();
   
      }
   
      private static void GetResultsLabels() throws Exception{
   
         int maxResults=10;
         String paginationToken=null;
         GetLabelDetectionResult labelDetectionResult=null;
   
         do {
            if (labelDetectionResult !=null){
               paginationToken = labelDetectionResult.getNextToken();
            }
   
            GetLabelDetectionRequest labelDetectionRequest= new GetLabelDetectionRequest()
                  .withJobId(startJobId)
                  .withSortBy(LabelDetectionSortBy.TIMESTAMP)
                  .withMaxResults(maxResults)
                  .withNextToken(paginationToken);
   
   
            labelDetectionResult = rek.getLabelDetection(labelDetectionRequest);
   
            VideoMetadata videoMetaData=labelDetectionResult.getVideoMetadata();
   
            System.out.println("Format: " + videoMetaData.getFormat());
            System.out.println("Codec: " + videoMetaData.getCodec());
            System.out.println("Duration: " + videoMetaData.getDurationMillis());
            System.out.println("FrameRate: " + videoMetaData.getFrameRate());
   
   
            //Show labels, confidence and detection times
            List<LabelDetection> detectedLabels= labelDetectionResult.getLabels();
   
            for (LabelDetection detectedLabel: detectedLabels) {
               long seconds=detectedLabel.getTimestamp()/1000;
               System.out.print("Sec: " + Long.toString(seconds) + " ");
               System.out.println("\t" + detectedLabel.getLabel().getName() +
                     "     \t" +
                     detectedLabel.getLabel().getConfidence().toString());
               System.out.println();
            }
         } while (labelDetectionResult !=null && labelDetectionResult.getNextToken() != null);
   
      }
   }
   ```

1. Build and run the code\. The operation might take a while to finish\. After it's finished, a list of the labels detected in the video is displayed\. 