# Recognizing celebrities in a stored video<a name="celebrities-video-sqs"></a>

Amazon Rekognition Video celebrity recognition in stored videos is an asynchronous operation\. To recognize celebrities in a stored video, use [ StartCelebrityRecognition ](API_StartCelebrityRecognition.md) to start video analysis\. Amazon Rekognition Video publishes the completion status of the video analysis to an Amazon Simple Notification Service topic\. If the video analysis is succesful, call [ GetCelebrityRecognition ](API_GetCelebrityRecognition.md)\. to get the analysis results\. For more information about starting video analysis and getting the results, see [Calling Amazon Rekognition Video operations](api-video.md)\. 

This procedure expands on the code in [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md), which uses an Amazon SQS queue to get the completion status of a video analysis request\. To run this procedure, you need a video file that contains one or more celebrity faces\.

**To detect celebrities in a video stored in an Amazon S3 bucket \(SDK\)**

1. Perform [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md)\.

1. Add the following code to the class `VideoDetect` that you created in step 1\.

------
#### [ Java ]

   ```
           //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
           //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
         // Celebrities=====================================================================
         private static void StartCelebrityDetection(String bucket, String video) throws Exception{
       	  
               NotificationChannel channel= new NotificationChannel()
                       .withSNSTopicArn(snsTopicArn)
                       .withRoleArn(roleArn);
     
              StartCelebrityRecognitionRequest req = new StartCelebrityRecognitionRequest()
                    .withVideo(new Video()
                          .withS3Object(new S3Object()
                                .withBucket(bucket)
                                .withName(video)))
                    .withNotificationChannel(channel);
     
     
     
              StartCelebrityRecognitionResult startCelebrityRecognitionResult = rek.startCelebrityRecognition(req);
              startJobId=startCelebrityRecognitionResult.getJobId();
     
           } 
     
           private static void GetCelebrityDetectionResults() throws Exception{
     
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
   ```

   In the function `main`, replace the line: 

   ```
           StartLabelDetection(bucket, video);
   
           if (GetSQSMessageSuccess()==true)
           	GetLabelDetectionResults();
   ```

   with:

   ```
           StartCelebrityDetection(bucket, video);
   
           if (GetSQSMessageSuccess()==true)
           	GetCelebrityDetectionResults();
   ```

------
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/VideoCelebrityDetection.java)\.

   ```
       public static  void StartCelebrityDetection(RekognitionClient rekClient,
                                                   NotificationChannel channel,
                                                   String bucket,
                                                   String video) {
           try {
               S3Object s3Obj = S3Object.builder()
                       .bucket(bucket)
                       .name(video)
                       .build();
   
               Video vidOb = Video.builder()
                       .s3Object(s3Obj)
                       .build();
   
               StartCelebrityRecognitionRequest recognitionRequest = StartCelebrityRecognitionRequest.builder()
                       .jobTag("Celebrities")
                       .notificationChannel(channel)
                       .video(vidOb)
                       .build();
   
               StartCelebrityRecognitionResponse startCelebrityRecognitionResult = rekClient.startCelebrityRecognition(recognitionRequest);
               startJobId = startCelebrityRecognitionResult.jobId();
   
   
           } catch(RekognitionException e) {
               System.out.println(e.getMessage());
               System.exit(1);
           }
       }
   
       public static void GetCelebrityDetectionResults(RekognitionClient rekClient) {
   
           try {
               String paginationToken=null;
               GetCelebrityRecognitionResponse recognitionResponse = null;
               Boolean finished = false;
               String status="";
               int yy=0 ;
   
               do{
                   if (recognitionResponse !=null)
                       paginationToken = recognitionResponse.nextToken();
   
                   GetCelebrityRecognitionRequest recognitionRequest = GetCelebrityRecognitionRequest.builder()
                               .jobId(startJobId)
                               .nextToken(paginationToken)
                               .sortBy(CelebrityRecognitionSortBy.TIMESTAMP)
                               .maxResults(10)
                               .build();
   
                   // Wait until the job succeeds
                   while (!finished) {
   
                       recognitionResponse = rekClient.getCelebrityRecognition(recognitionRequest);
                       status = recognitionResponse.jobStatusAsString();
   
                       if (status.compareTo("SUCCEEDED") == 0)
                           finished = true;
                       else {
                           System.out.println(yy + " status is: " + status);
                           Thread.sleep(1000);
                       }
                       yy++;
                   }
   
                   finished = false;
   
                   // Proceed when the job is done - otherwise VideoMetadata is null
                   VideoMetadata videoMetaData=recognitionResponse.videoMetadata();
   
                   System.out.println("Format: " + videoMetaData.format());
                   System.out.println("Codec: " + videoMetaData.codec());
                   System.out.println("Duration: " + videoMetaData.durationMillis());
                   System.out.println("FrameRate: " + videoMetaData.frameRate());
                   System.out.println("Job");
   
                   List<CelebrityRecognition> celebs= recognitionResponse.celebrities();
                   for (CelebrityRecognition celeb: celebs) {
                       long seconds=celeb.timestamp()/1000;
                       System.out.print("Sec: " + Long.toString(seconds) + " ");
                       CelebrityDetail details=celeb.celebrity();
                       System.out.println("Name: " + details.name());
                       System.out.println("Id: " + details.id());
                       System.out.println();
                   }
   
               } while (recognitionResponse !=null && recognitionResponse.nextToken() != null);
   
           } catch(RekognitionException | InterruptedException e) {
               System.out.println(e.getMessage());
               System.exit(1);
       }
     }
   ```

------
#### [ Python ]

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
       # ============== Celebrities ===============
       def StartCelebrityDetection(self):
           response=self.rek.start_celebrity_recognition(Video={'S3Object': {'Bucket': self.bucket, 'Name': self.video}},
               NotificationChannel={'RoleArn': self.roleArn, 'SNSTopicArn': self.snsTopicArn})
   
           self.startJobId=response['JobId']
           print('Start Job Id: ' + self.startJobId)
   
       def GetCelebrityDetectionResults(self):
           maxResults = 10
           paginationToken = ''
           finished = False
   
           while finished == False:
               response = self.rek.get_celebrity_recognition(JobId=self.startJobId,
                                                       MaxResults=maxResults,
                                                       NextToken=paginationToken)
   
               print(response['VideoMetadata']['Codec'])
               print(str(response['VideoMetadata']['DurationMillis']))
               print(response['VideoMetadata']['Format'])
               print(response['VideoMetadata']['FrameRate'])
   
               for celebrityRecognition in response['Celebrities']:
                   print('Celebrity: ' +
                       str(celebrityRecognition['Celebrity']['Name']))
                   print('Timestamp: ' + str(celebrityRecognition['Timestamp']))
                   print()
   
               if 'NextToken' in response:
                   paginationToken = response['NextToken']
               else:
                   finished = True
   ```

   In the function `main`, replace the lines:

   ```
       analyzer.StartLabelDetection()
       if analyzer.GetSQSMessageSuccess()==True:
           analyzer.GetLabelDetectionResults()
   ```

   with:

   ```
       analyzer.StartCelebrityDetection()
       if analyzer.GetSQSMessageSuccess()==True:
           analyzer.GetCelebrityDetectionResults()
   ```

------
**Note**  
If you've already run a video example other than [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md), the code to replace might be different\.

1. Run the code\. Information about the celebrities recognized in the video is shown\.

## GetCelebrityRecognition operation response<a name="getcelebrityrecognition-operation-output"></a>

The following is an example JSON response\. The response includes the following:
+ **Recognized celebrities** – `Celebrities` is an array of celebrities and the times that they are recognized in a video\. A [ CelebrityRecognition ](API_CelebrityRecognition.md) object exists for each time the celebrity is recognized in the video\. Each `CelebrityRecognition` contains information about a recognized celebrity \([ CelebrityDetail ](API_CelebrityDetail.md)\) and the time \(`Timestamp`\) the celebrity was recognized in the video\. `Timestamp` is measured in milliseconds from the start of the video\. 
+ **CelebrityDetail** – Contains information about a recognized celebrity\. It includes the celebrity name \(`Name`\), identifier \(`ID`\), the celebrity's known gender\(`KnownGender`\), and a list of URLs pointing to related content \(`Urls`\)\. It also includes the confidence level that Amazon Rekognition Video has in the accuracy of the recognition, and details about the celebrity's face, [ FaceDetail ](API_FaceDetail.md)\. If you need to get the related content later, you can use `ID` with [ GetCelebrityInfo ](API_GetCelebrityInfo.md)\. 
+ **VideoMetadata** – Information about the video that was analyzed\.

```
{
    "Celebrities": [
        {
            "Celebrity": {
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
                        "Sharpness": 99.9305191040039
                    }
                },
                "Id": "XXXXXX",
                "KnownGender": {
                    "Type": "Female"
                },
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