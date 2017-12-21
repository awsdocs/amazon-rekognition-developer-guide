# Recognizing Celebrities<a name="celebrities"></a>

Amazon Rekognition can recognize thousands of celebrities in a wide range of categories, such as entertainment and media, sports, business, and politics\. With Amazon Rekognition you can recognize celebrities in images and in stored videos\. You can also get additional information for recognized celebrities\.


+ [Celebrities in Images](#recognize-celebrities-calling-image)
+ [Celebrities in Video](#recognize-celebrities-calling-video)
+ [Recognizing Celebrities in an Image](celebrities-procedure-image.md)
+ [Recognizing Celebrities in a Stored Video \(SDK for Java\)](celebrities-video-sqs.md)
+ [Getting Information about a Celebrity](get-celebrity-info-procedure.md)

## Celebrities in Images<a name="recognize-celebrities-calling-image"></a>

To recognize celebrities within images and get additional information about recognized celebrities, use the [RecognizeCelebrities](API_RecognizeCelebrities.md) non\-storage API operation\. For example, in social media or news and entertainment industries where information gathering can be time critical, you can use the `RecognizeCelebrities` operation to identify as many as 100 celebrities in an image and return links to celebrity web pages, if they are available\. Amazon Rekognition doesn't remember which image it detected a celebrity in\. Your application must store this information\. For an example, see [Recognizing Celebrities in an Image](celebrities-procedure-image.md)\.

If you haven't stored the additional information for a celebrity returned by `RecognizeCelebrities` and you want to avoid reanalyzing an image to get it, use [GetCelebrityInfo](API_GetCelebrityInfo.md)\. To call `GetCelebrityInfo`, you need the unique identifier that Rekognition assigns to each celebrity\. The identifier is returned as part of the `RecognizeCelebrities` response for each celebrity recognized in an image\. 

If you have a large collection of images to process for celebrity recognition, consider using [AWS Batch](http://docs.aws.amazon.com/batch/latest/userguide/) to process calls to `RecognizeCelebrities` in batches in the background\. When you add a new image to your collection, you can use an AWS Lambda function to recognize celebrities by calling `RecognizeCelebrities` as the image is uploaded into an S3 bucket\.

You provide an input image to `RecognizeCelebrities` either as image bytes or by referencing an image stored in an S3 bucket\. The image must be either a \.png or \.jpg formatted file\. For information about input image recommendations, see [Working with Images](images.md)\. The input image quality \(brightness and sharpness\) is returned by `RecognizeCelebrities`\. 

`RecognizeCelebrities` returns an array of recognized celebrities and an array of unrecognized faces, as shown in the following example: 

```
{
    "CelebrityFaces": [{
        "Face": {
            "BoundingBox": {
                "Height": 0.617123007774353,
                "Left": 0.15641026198863983,
                "Top": 0.10864841192960739,
                "Width": 0.3641025722026825
            },
            "Confidence": 99.99589538574219,
            "Landmarks": [{
                "Type": "eyeLeft",
                "X": 0.2837241291999817,
                "Y": 0.3637104034423828
            }, {
                "Type": "eyeRight",
                "X": 0.4091649055480957,
                "Y": 0.37378931045532227
            }, {
                "Type": "nose",
                "X": 0.35267341136932373,
                "Y": 0.49657556414604187
            }, {
                "Type": "mouthLeft",
                "X": 0.2786353826522827,
                "Y": 0.5455248355865479
            }, {
                "Type": "mouthRight",
                "X": 0.39566439390182495,
                "Y": 0.5597742199897766
            }],
            "Pose": {
                "Pitch": -7.749263763427734,
                "Roll": 2.004552125930786,
                "Yaw": 9.012002944946289
            },
            "Quality": {
                "Brightness": 32.69192123413086,
                "Sharpness": 99.9305191040039
            }
        },
        "Id": "3Ir0du6",
        "MatchConfidence": 98.0,
        "Name": "Jeff Bezos",
        "Urls": ["www.imdb.com/name/nm1757263"]
    }],
    "OrientationCorrection": "ROTATE_0",
    "UnrecognizedFaces": [{
        "BoundingBox": {
            "Height": 0.5345501899719238,
            "Left": 0.48461538553237915,
            "Top": 0.16949152946472168,
            "Width": 0.3153846263885498
        },
        "Confidence": 99.92860412597656,
        "Landmarks": [{
            "Type": "eyeLeft",
            "X": 0.5863404870033264,
            "Y": 0.36940744519233704
        }, {
            "Type": "eyeRight",
            "X": 0.6999204754829407,
            "Y": 0.3769848346710205
        }, {
            "Type": "nose",
            "X": 0.6349524259567261,
            "Y": 0.4804527163505554
        }, {
            "Type": "mouthLeft",
            "X": 0.5872702598571777,
            "Y": 0.5535582304000854
        }, {
            "Type": "mouthRight",
            "X": 0.6952020525932312,
            "Y": 0.5600858926773071
        }],
        "Pose": {
            "Pitch": -7.386096477508545,
            "Roll": 2.304218292236328,
            "Yaw": -6.175624370574951
        },
        "Quality": {
            "Brightness": 37.16635513305664,
            "Sharpness": 99.884521484375
        }
    }]
}
```

The response includes the following:

+ **Recognized celebrities** – `Celebrities` is an array of recognized celebrities\. Each [Celebrity](API_Celebrity.md) object in the array contains the celebrity name and a list of URLs pointing to related content; for example, the celebrity's IMDB link\. Amazon Rekognition returns an [ComparedFace](API_ComparedFace.md) object that your application can use to determine where the celebrity's face is on the image and a unique identifier for the celebrity\. Use the unique identifier to retrieve celebrity information later with the [GetCelebrityInfo](API_GetCelebrityInfo.md) API operation\. 

+ **Unrecognized faces** – `UnrecognizedFaces` is an array of faces that didn't match any known celebrities\. Each [ComparedFace](API_ComparedFace.md) object in the array contains a bounding box \(as well as other information\) that you can use to locate the face in the image\.

+ **Image orientation** – Image orientation information is provided to allow you to correctly display of the image\.

## Celebrities in Video<a name="recognize-celebrities-calling-video"></a>

To recognize celebrities in a video stored in an Amazon S3 bucket, you use [StartCelebrityRecognition](API_StartCelebrityRecognition.md) and [GetCelebrityRecognition](API_GetCelebrityRecognition.md)\. Analyzing videos stored in an Amazon S3 bucket is an asynchronous workflow\. For more information, see [Working with Stored Videos](video.md)\. For an example, see [ Recognizing Celebrities in a Stored Video \(SDK for Java\)Recognizing Celebrities in a Stored Video  You can recognize celebrities in a video stored in an Amazon S3 bucket\. This procedure expands on the code in [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md) which uses an Amazon Simple Queue Service queue to get the completion status of a video analysis request\.  Prerequisites To run this procedure, you need to have the AWS SDK for Java installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. You also need an video file that contains one or more celebrity faces\.  To detect celebrities in a video stored in an Amazon S3 bucket Perform [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md)\. Add the following code to the project created in step one\. 

   ```
      // Celebrities=====================================================================
      private static void StartCelebrities(String bucket, String video) throws Exception{
          
          StartCelebrityRecognitionRequest req = new StartCelebrityRecognitionRequest()
                  .withVideo(new Video()
                          .withS3Object(new S3Object()
                              .withBucket(bucket)
                              .withName(video)))
                  .withNotificationChannel(channel);
                               
                             
           
           StartCelebrityRecognitionResult startCelebrityRecognitionResult = rek.startCelebrityRecognition(req);
           startJobId=startCelebrityRecognitionResult.getJobId();
           
       } 
       
       private static void GetResultsCelebrities() throws Exception{
           
           int maxResults=10;
           String paginationToken=null;
           GetCelebrityRecognitionResult celebrityRecognitionResult=null;
           
           do{
               if (celebrityRecognitionResult !=null){
                   paginationToken = celebrityRecognitionResult.getNextToken();
               }
               celebrityRecognitionResult = rek.getCelebrityRecognition(new GetCelebrityRecognitionRequest()
                    .withJobId(startJobId)
                    .withNextToken(paginationToken)
                    .withSortBy(CelebrityRecognitionSortBy.TIMESTAMP)
                    .withMaxResults(maxResults));
               
               
               System.out.println("File info for page");
               VideoMetadata videoMetaData=celebrityRecognitionResult.getVideoMetadata();
                   
               System.out.println("Format: " + videoMetaData.getFormat());
               System.out.println("Codec: " + videoMetaData.getCodec());
               System.out.println("Duration: " + videoMetaData.getDurationMillis());
               System.out.println("FrameRate: " + videoMetaData.getFrameRate());
               
               System.out.println("Job");
               
               System.out.println("Job status: " + celebrityRecognitionResult.getJobStatus());
               System.out.println("Failure reason: " + celebrityRecognitionResult.getFailureReason());
                   
                 
               //Show celebrities
               List<CelebrityRecognition> celebs= celebrityRecognitionResult.getCelebrities();
                        
               for (CelebrityRecognition celeb: celebs) { 
                   long seconds=celeb.getTimestamp()/1000;
                   System.out.print("Sec: " + Long.toString(seconds) + " ");
                   CelebrityDetail details=celeb.getCelebrity();
                   System.out.println("Name: " + details.getName());
                   System.out.println("Id: " + details.getId());
                   System.out.println(); 
               }
           } while (celebrityRecognitionResult !=null && celebrityRecognitionResult.getNextToken() != null);
           
             
       }
   ```  In the function `main`, replace the line   `StartLabels("bucket","file");`  with  `StartCelebrities("bucket","file");`  If you have already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace will be different\.  In the call to `StartCelebrities`, replace *bucket* and *file* with the Amazon S3 bucket name and file name of the video you want to analyze\. In the function `main`, replace the line  `GetResultsLabels();` with `GetResultsCelebrities();` If you have already run a video example other than [ Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for JavaAnalyzing a Video \(SDK for Java\)  This procedure shows you how to detect labels in a video by using Rekognition Video label detection operations, a video stored in an Amazon S3 bucket, and an Amazon SNS topic\. The procedure also shows how to use an Amazon SQS queue to get the completion status from the Amazon SNS topic\. For more information, see [](api-video.md)\. You aren't restricted to using an Amazon SQS queue\. For example, you can use an AWS Lambda function to get the completion status\. For more information, see [Invoking Lambda functions using Amazon SNS notifications](http://docs.aws.amazon.com/sns/latest/dg/sns-lambda.html)\. The procedure shows you how to use the [Amazon SNS console](https://console.aws.amazon.com/sns/v2/home) to do the following:  Create the Amazon SNS topic\. Create the Amazon SQS queue\. Give Rekognition Video permission to publish the completion status of a video analysis operation to the Amazon SNS topic\. Subscribe the Amazon SQS queue to the Amazon SNS topic\.  This procedure uses a single Amazon SQS queue and a single Amazon SNS topic for all video analysis requests\.  The example code in the procedure shows you how to do the following:   Start the video analysis request by calling [StartLabelDetection](API_StartLabelDetection.md)\.  Get the completion status from the Amazon SQS queue\. The sample tracks the job identifier \(`JobId`\) that's returned in `StartLabelDetection` and only gets the results for matching job identifiers that are read from the completion status\. This is an important consideration if other applications are using the same queue and topic\. Any other jobs are ignored\. Get and display the video analysis results by calling [GetLabelDetection](API_GetLabelDetection.md)\.  Prerequisites To run this procedure, you need to have the AWS SDK for Java installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account that you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\.   To Detect Labels in a Video  If you haven't already, create an IAM service role to give Rekognition Video access to your Amazon SNS topics\. Note the ARN\. For more information, see [](api-video-roles.md#api-video-roles-all-topics)\. [Create an Amazon SNS topic](http://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) by using the [Amazon SNS console](https://console.aws.amazon.com/sns/v2/home)\. Prepend the topic name with *AmazonRekognition*\. Note the topic Amazon Resource Name \(ARN\)\.  [Create an Amazon SQS standard queue](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-create-queue.html) by using the [Amazon SQS console](https://console.aws.amazon.com/sqs/)\. Note the queue ARN\. [Subscribe the queue to the topic](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-subscribe-queue-sns-topic.html) you created in step 2\.  Upload an \.mp4, \.mov or \.avi format video file to your S3 Bucket\. For test purposes, upload a video that's no longer than 30 seconds in length\. For instructions, see [Uploading Objects into Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.  Use the following AWS SDK for Java code to detect labels in a video\.   Replace `TopicArn`, `RoleArn`, and `QueueURL` with the Amazon SNS topic ARN, IAM role ARN, and Amazon SQS queue URL that you previously noted\. Replace `Bucket` and `VideoFile` with the bucket and video file name that you uploaded in step 5\.   Replace `Endpoint` and `Region` with the AWS endpoint and region that you're using\. Update `.withRegion` parameters to the region you are using\. Change `RekognitionUser` to an AWS account that has permissions to call Rekognition Video operations\.   

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
   ```  Build and run the code\. The operation might take a while to finish\. After it's finished, a list of the labels detected in the video is displayed\.    ](video-analyzing-with-sqs.md), the function name to replace will be different\.  Run the code\. Information about the celebrities recognized in the video is shown\.  ](celebrities-video-sqs.md)\.

The response from `GetCelebrityDetection` includes an array, `Celebrities`, of celebrities \([CelebrityRecognition](API_CelebrityRecognition.md)\) recognized in the video and the time\(s\) they were recognized\. The following is an example JSON response\.

```
{
    "Celebrities": [
        {
            "Celebrity": {
                "BoundingBox": {
                    "Height": 0.8842592835426331,
                    "Left": 0,
                    "Top": 0.11574073880910873,
                    "Width": 0.24427083134651184
                },
                "Confidence": 0.699999988079071,
                "Face": {
                    "BoundingBox": {
                        "Height": 0.20555555820465088,
                        "Left": 0.029374999925494194,
                        "Top": 0.22333332896232605,
                        "Width": 0.11562500149011612
                    },
                    "Confidence": 99.89837646484375,
                    "Landmarks": [
                        {
                            "Type": "eyeLeft",
                            "X": 0.06857934594154358,
                            "Y": 0.30842265486717224
                        },
                        {
                            "Type": "eyeRight",
                            "X": 0.10396526008844376,
                            "Y": 0.300625205039978
                        },
                        {
                            "Type": "nose",
                            "X": 0.0966852456331253,
                            "Y": 0.34081998467445374
                        },
                        {
                            "Type": "mouthLeft",
                            "X": 0.075217105448246,
                            "Y": 0.3811396062374115
                        },
                        {
                            "Type": "mouthRight",
                            "X": 0.10744428634643555,
                            "Y": 0.37407416105270386
                        }
                    ],
                    "Pose": {
                        "Pitch": -0.9784082174301147,
                        "Roll": -8.808176040649414,
                        "Yaw": 20.28228759765625
                    },
                    "Quality": {
                        "Brightness": 43.312068939208984,
                        "Sharpness": 99.80813598632812
                    }
                },
                "Id": "XXXXXX",
                "Name": "Celeb A",
                "Urls": []
            },
            "Timestamp": 367
       },......
    ],
    "JobStatus": "SUCCEEDED",
    "NextToken": "XfXnZKiyMOGDhzBzYUhS5puM+g1IgezqFeYpv/H/+5noP/LmM57FitUAwSQ5D6G4AB/PNwolrw==",
    "VideoMetadata": {
        "Codec": "h264",
        "DurationMillis": 67301,
        "FileExtension": "mp4",
        "Format": "QuickTime / MOV",
        "FrameHeight": 1080,
        "FrameRate": 29.970029830932617,
        "FrameWidth": 1920
    }
}
```

The response includes the following:

+ **Recognized celebrities** – `Celebrities` is an array of celebrities and the time\(s\) they are recognized in a video\. An [CelebrityRecognition](API_CelebrityRecognition.md) object exists for each time the celebrity is recognized in the video\. Each `CelebrityRecognition` contains information about a recognized celebrity \( [CelebrityDetail](API_CelebrityDetail.md)\) and the time \(`Timestamp`\) the celebrity was recognized in the video\. Timestamp is measured in milliseconds from the start of the video\. 

+ **CelebrityDetail** – Contains information about a recognized celebrity\. It includes the celebrity name \(`Name`\), identifer \(`ID`\), and a list of URLs pointing to related content \(`Urls`\)\. It also includes the bounding box for the celebrity's body, The confidence Rekognition Video has in the accuracy of the recognition, and details about the celebrity's face, [FaceDetail](API_FaceDetail.md)\. If you need to get the related content later, you can use `ID` with [GetCelebrityInfo](API_GetCelebrityInfo.md)\. 

+ **VideoMetadata** – Information about the video that was analyzed\.