# Analyzing a Video Stored in an Amazon S3 Bucket with Java or Python \(SDK\)<a name="video-analyzing-with-sqs"></a>

This procedure shows you how to detect labels in a video by using Amazon Rekognition Video label detection operations, a video stored in an Amazon S3 bucket, and an Amazon SNS topic\. The procedure also shows how to use an Amazon SQS queue to get the completion status from the Amazon SNS topic\. For more information, see [Calling Amazon Rekognition Video Operations](api-video.md)\. You aren't restricted to using an Amazon SQS queue\. For example, you can use an AWS Lambda function to get the completion status\. For more information, see [Invoking Lambda functions using Amazon SNS notifications](https://docs.aws.amazon.com/sns/latest/dg/sns-lambda.html)\.

The procedure shows you how to use the [Amazon SNS console](https://console.aws.amazon.com/sns/v2/home) to do the following:
+ Create the Amazon SNS topic\.
+ Create the Amazon SQS queue\.
+ Give Amazon Rekognition Video permission to publish the completion status of a video analysis operation to the Amazon SNS topic\.
+ Subscribe the Amazon SQS queue to the Amazon SNS topic\.

**Note**  
This procedure uses a single Amazon SQS queue and a single Amazon SNS topic for all video analysis requests\. 

The example code in the procedure shows you how to do the following: 

1. Start the video analysis request by calling [StartLabelDetection](API_StartLabelDetection.md)\. 

1. Get the completion status from the Amazon SQS queue\. The example tracks the job identifier \(`JobId`\) that's returned in `StartLabelDetection` and only gets the results for matching job identifiers that are read from the completion status\. This is an important consideration if other applications are using the same queue and topic\. For simplicity, the example deletes jobs that don't match\. Consider adding them to an Amazon SQS dead\-letter queue for further investigation\.

1. Get and display the video analysis results by calling [GetLabelDetection](API_GetLabelDetection.md)\.

## Prerequisites<a name="video-prerequisites"></a>

To run this procedure, you need to have the AWS SDK for Java installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account that you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. 

**To Detect Labels in a Video**

1. Configure user access to Amazon Rekognition Video and configure Amazon Rekognition Video access to Amazon SNS\. For more information, see [Configuring Amazon Rekognition Video](api-video-roles.md)\.

1. [Create an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) by using the [Amazon SNS console](https://console.aws.amazon.com/sns/v2/home)\. Prepend the topic name with *AmazonRekognition*\. Note the topic Amazon Resource Name \(ARN\)\. Ensure the topic is in the same region as the AWS endpoint that you are using\.

1. [Create an Amazon SQS standard queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-create-queue.html) by using the [Amazon SQS console](https://console.aws.amazon.com/sqs/)\. Note the queue ARN\.

1. [Subscribe the queue to the topic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-subscribe-queue-sns-topic.html) you created in step 2\.

1. [Give permission to the Amazon SNS topic to send messages to the Amazon SQS queue](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToSQS.html#SendMessageToSQS.sqs.permissions)\.

1. Upload an MOV or MPEG\-4 format video file to your S3 Bucket\. For test purposes, upload a video that's no longer than 30 seconds in length\.

   For instructions, see [Uploading Objects into Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. Use the following AWS SDK for Java code to detect labels in a video\. 
   + Replace `topicArn` and `queueUrl` with the Amazon SNS topic ARN and the Amazon SQS queue URL that you previously noted\.
   + Replace `roleArn` with the ARN of the IAM service role that you created in step 3 of [To configure Amazon Rekognition Video](api-video-roles.md#configure-rekvid-procedure)\.
   + Replace the values of `bucket` and `video` with the bucket and video file name that you specified in step 6\. 

------
#### [ Java ]

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   package com.amazonaws.samples;
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
   import com.amazonaws.services.rekognition.model.FaceSearchSortBy;
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
   import com.amazonaws.services.rekognition.model.Instance;
   import com.amazonaws.services.rekognition.model.Label;
   import com.amazonaws.services.rekognition.model.LabelDetection;
   import com.amazonaws.services.rekognition.model.LabelDetectionSortBy;
   import com.amazonaws.services.rekognition.model.NotificationChannel;
   import com.amazonaws.services.rekognition.model.Parent;
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
   import com.amazonaws.services.sqs.AmazonSQS;
   import com.amazonaws.services.sqs.AmazonSQSClientBuilder;
   import com.amazonaws.services.sqs.model.Message;
   import com.fasterxml.jackson.databind.JsonNode;
   import com.fasterxml.jackson.databind.ObjectMapper;
   import java.util.*;
   
   public class VideoDetect {
   
       private static String bucket = "";
       private static String video = ""; 
       private static String queueUrl =  "";
       private static String topicArn="";
       private static String roleArn="";
         
       private static AmazonSQS sqs = null;
       private static AmazonRekognition rek = null;
       
       private static NotificationChannel channel= new NotificationChannel()
               .withSNSTopicArn(topicArn)
               .withRoleArn(roleArn);
   
   
       private static String startJobId = null;
   
   
       public static void main(String[] args)  throws Exception{
   
   
           sqs = AmazonSQSClientBuilder.defaultClient();
           rek = AmazonRekognitionClientBuilder.defaultClient();
   
           //=================================================
           StartLabels(bucket, video);
           //=================================================
           System.out.println("Waiting for job: " + startJobId);
           //Poll queue for messages
           List<Message> messages=null;
           int dotLine=0;
           boolean jobFound=false;
   
           //loop until the job status is published. Ignore other messages in queue.
           do{
               messages = sqs.receiveMessage(queueUrl).getMessages();
               if (dotLine++<20){
                   System.out.print(".");
               }else{
                   System.out.println();
                   dotLine=0;
               }
   
               if (!messages.isEmpty()) {
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
                           //Delete unknown message. Consider moving message to dead letter queue
                           sqs.deleteMessage(queueUrl,message.getReceiptHandle());
                       }
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
                   long seconds=detectedLabel.getTimestamp();
                   Label label=detectedLabel.getLabel();
                   System.out.println("Millisecond: " + Long.toString(seconds) + " ");
                   
                   System.out.println("   Label:" + label.getName()); 
                   System.out.println("   Confidence:" + detectedLabel.getLabel().getConfidence().toString());
         
                   List<Instance> instances = label.getInstances();
                   System.out.println("   Instances of " + label.getName());
                   if (instances.isEmpty()) {
                       System.out.println("        " + "None");
                   } else {
                       for (Instance instance : instances) {
                           System.out.println("        Confidence: " + instance.getConfidence().toString());
                           System.out.println("        Bounding box: " + instance.getBoundingBox().toString());
                       }
                   }
                   System.out.println("   Parent labels for " + label.getName() + ":");
                   List<Parent> parents = label.getParents();
                   if (parents.isEmpty()) {
                       System.out.println("        None");
                   } else {
                       for (Parent parent : parents) {
                           System.out.println("        " + parent.getName());
                       }
                   }
                   System.out.println();
               }
           } while (labelDetectionResult !=null && labelDetectionResult.getNextToken() != null);
   
       }    
   }
   ```

------
#### [ Python ]

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   import json
   import sys
   
   
   class VideoDetect:
       jobId = ''
       rek = boto3.client('rekognition')
       queueUrl = ''
       roleArn = ''
       topicArn = ''
       bucket = ''
       video = ''
   
       def main(self):
   
           jobFound = False
           sqs = boto3.client('sqs')
          
   
           #=====================================
           response = self.rek.start_label_detection(Video={'S3Object': {'Bucket': self.bucket, 'Name': self.video}},
                                            NotificationChannel={'RoleArn': self.roleArn, 'SNSTopicArn': self.topicArn})
           #=====================================
           print('Start Job Id: ' + response['JobId'])
           dotLine=0
           while jobFound == False:
               sqsResponse = sqs.receive_message(QueueUrl=self.queueUrl, MessageAttributeNames=['ALL'],
                                             MaxNumberOfMessages=10)
   
               if sqsResponse:
                   
                   if 'Messages' not in sqsResponse:
                       if dotLine<20:
                           print('.', end='')
                           dotLine=dotLine+1
                       else:
                           print()
                           dotLine=0    
                       sys.stdout.flush()
                       continue
   
                   for message in sqsResponse['Messages']:
                       notification = json.loads(message['Body'])
                       rekMessage = json.loads(notification['Message'])
                       print(rekMessage['JobId'])
                       print(rekMessage['Status'])
                       if str(rekMessage['JobId']) == response['JobId']:
                           print('Matching Job Found:' + rekMessage['JobId'])
                           jobFound = True
                           #=============================================
                           self.GetResultsLabels(rekMessage['JobId'])
                           #=============================================
   
                           sqs.delete_message(QueueUrl=self.queueUrl,
                                          ReceiptHandle=message['ReceiptHandle'])
                       else:
                           print("Job didn't match:" +
                                 str(rekMessage['JobId']) + ' : ' + str(response['JobId']))
                       # Delete the unknown message. Consider sending to dead letter queue
                       sqs.delete_message(QueueUrl=self.queueUrl,
                                      ReceiptHandle=message['ReceiptHandle'])
   
           print('done')
   
   
       def GetResultsLabels(self, jobId):
           maxResults = 10
           paginationToken = ''
           finished = False
   
           while finished == False:
               response = self.rek.get_label_detection(JobId=jobId,
                                               MaxResults=maxResults,
                                               NextToken=paginationToken,
                                               SortBy='TIMESTAMP')
   
               print(response['VideoMetadata']['Codec'])
               print(str(response['VideoMetadata']['DurationMillis']))
               print(response['VideoMetadata']['Format'])
               print(response['VideoMetadata']['FrameRate'])
   
               for labelDetection in response['Labels']:
                   label=labelDetection['Label']
   
                   print("Timestamp: " + str(labelDetection['Timestamp']))
                   print("   Label: " + label['Name'])
                   print("   Confidence: " +  str(label['Confidence']))
                   print("   Instances:")
                   for instance in label['Instances']:
                       print ("      Confidence: " + str(instance['Confidence']))
                       print ("      Bounding box")
                       print ("        Top: " + str(instance['BoundingBox']['Top']))
                       print ("        Left: " + str(instance['BoundingBox']['Left']))
                       print ("        Width: " +  str(instance['BoundingBox']['Width']))
                       print ("        Height: " +  str(instance['BoundingBox']['Height']))
                       print()
                   print()
                   print ("   Parents:")
                   for parent in label['Parents']:
                       print ("      " + parent['Name'])
                   print ()
   
                   if 'NextToken' in response:
                       paginationToken = response['NextToken']
                   else:
                       finished = True
   
   
   if __name__ == "__main__":
   
       analyzer=VideoDetect()
       analyzer.main()
   ```

------

1. Build and run the code\. The operation might take a while to finish\. After it's finished, a list of the labels detected in the video is displayed\. For more information, see [Detecting Labels in a Video](labels-detecting-labels-video.md)\.