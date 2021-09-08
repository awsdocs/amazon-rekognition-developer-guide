# Detecting inappropriate stored videos<a name="procedure-moderate-videos"></a>

Amazon Rekognition Video inappropriate or offensive content detection in stored videos is an asynchronous operation\. To start detecting inappropriate or offensive content, call [ StartContentModeration ](API_StartContentModeration.md)\. Amazon Rekognition Video publishes the completion status of the video analysis to an Amazon Simple Notification Service topic\. If the video analysis is successful, call [ GetContentModeration ](API_GetContentModeration.md) to get the analysis results\. For more information about starting video analysis and getting the results, see [Calling Amazon Rekognition Video operations](api-video.md)\. For a list of moderation labels in Amazon Rekognition, see [Using the image and video moderation APIs](https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html#moderation-api)\.

 This procedure expands on the code in [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md), which uses an Amazon Simple Queue Service queue to get the completion status of a video analysis request\.

**To detect inappropriate or offensive content in a video stored in an Amazon S3 bucket \(SDK\)**

1. Perform [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md)\.

1. Add the following code to the class `VideoDetect` that you created in step 1\.

------
#### [ Java ]

   ```
       //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
       //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
           //Content moderation ==================================================================
           private static void StartUnsafeContentDetection(String bucket, String video) throws Exception{
           
               NotificationChannel channel= new NotificationChannel()
                       .withSNSTopicArn(snsTopicArn)
                       .withRoleArn(roleArn);
               
               StartContentModerationRequest req = new StartContentModerationRequest()
                       .withVideo(new Video()
                               .withS3Object(new S3Object()
                                   .withBucket(bucket)
                                   .withName(video)))
                       .withNotificationChannel(channel);
                                    
                                    
                
                StartContentModerationResult startModerationLabelDetectionResult = rek.startContentModeration(req);
                startJobId=startModerationLabelDetectionResult.getJobId();
                
            } 
            
            private static void GetUnsafeContentDetectionResults() throws Exception{
                
                int maxResults=10;
                String paginationToken=null;
                GetContentModerationResult moderationLabelDetectionResult =null;
                
                do{
                    if (moderationLabelDetectionResult !=null){
                        paginationToken = moderationLabelDetectionResult.getNextToken();
                    }
                    
                    moderationLabelDetectionResult = rek.getContentModeration(
                            new GetContentModerationRequest()
                                .withJobId(startJobId)
                                .withNextToken(paginationToken)
                                .withSortBy(ContentModerationSortBy.TIMESTAMP)
                                .withMaxResults(maxResults));
                            
                    
           
                    VideoMetadata videoMetaData=moderationLabelDetectionResult.getVideoMetadata();
                        
                    System.out.println("Format: " + videoMetaData.getFormat());
                    System.out.println("Codec: " + videoMetaData.getCodec());
                    System.out.println("Duration: " + videoMetaData.getDurationMillis());
                    System.out.println("FrameRate: " + videoMetaData.getFrameRate());
                        
                        
                    //Show moderated content labels, confidence and detection times
                    List<ContentModerationDetection> moderationLabelsInFrames= 
                            moderationLabelDetectionResult.getModerationLabels();
                 
                    for (ContentModerationDetection label: moderationLabelsInFrames) { 
                        long seconds=label.getTimestamp()/1000;
                        System.out.print("Sec: " + Long.toString(seconds));
                        System.out.println(label.getModerationLabel().toString());
                        System.out.println();           
                    }  
                } while (moderationLabelDetectionResult !=null && moderationLabelDetectionResult.getNextToken() != null);
                
            }
   ```

   In the function `main`, replace the lines: 

   ```
           StartLabelDetection(bucket, video);
   
           if (GetSQSMessageSuccess()==true)
           	GetLabelDetectionResults();
   ```

   with:

   ```
           StartUnsafeContentDetection(bucket, video);
   
           if (GetSQSMessageSuccess()==true)
           	GetUnsafeContentDetectionResults();
   ```

------
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/VideoDetectInappropriate.java)\.

   ```
       public static void startModerationDetection(RekognitionClient rekClient,
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
   
               StartContentModerationRequest modDetectionRequest = StartContentModerationRequest.builder()
                       .jobTag("Moderation")
                       .notificationChannel(channel)
                       .video(vidOb)
                       .build();
   
               StartContentModerationResponse startModDetectionResult = rekClient.startContentModeration(modDetectionRequest);
               startJobId=startModDetectionResult.jobId();
   
           } catch(RekognitionException e) {
               System.out.println(e.getMessage());
               System.exit(1);
           }
       }
   
       public static void GetModResults(RekognitionClient rekClient) {
   
           try {
               String paginationToken=null;
               GetContentModerationResponse modDetectionResponse=null;
               Boolean finished = false;
               String status="";
               int yy=0 ;
   
               do{
   
                   if (modDetectionResponse !=null)
                       paginationToken = modDetectionResponse.nextToken();
   
                   GetContentModerationRequest modRequest = GetContentModerationRequest.builder()
                           .jobId(startJobId)
                           .nextToken(paginationToken)
                           .maxResults(10)
                           .build();
   
                   // Wait until the job succeeds
                   while (!finished) {
   
                       modDetectionResponse = rekClient.getContentModeration(modRequest);
                       status = modDetectionResponse.jobStatusAsString();
   
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
                   VideoMetadata videoMetaData=modDetectionResponse.videoMetadata();
   
                   System.out.println("Format: " + videoMetaData.format());
                   System.out.println("Codec: " + videoMetaData.codec());
                   System.out.println("Duration: " + videoMetaData.durationMillis());
                   System.out.println("FrameRate: " + videoMetaData.frameRate());
                   System.out.println("Job");
   
                   List<ContentModerationDetection> mods = modDetectionResponse.moderationLabels();
                   for (ContentModerationDetection mod: mods) {
                       long seconds=mod.timestamp()/1000;
                       System.out.print("Mod label: " + seconds + " ");
                       System.out.println(mod.moderationLabel().toString());
                       System.out.println();
                   }
   
               } while (modDetectionResponse !=null && modDetectionResponse.nextToken() != null);
   
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
   
       # ============== Unsafe content =============== 
       def StartUnsafeContent(self):
           response=self.rek.start_content_moderation(Video={'S3Object': {'Bucket': self.bucket, 'Name': self.video}},
               NotificationChannel={'RoleArn': self.roleArn, 'SNSTopicArn': self.snsTopicArn})
   
           self.startJobId=response['JobId']
           print('Start Job Id: ' + self.startJobId)
   
       def GetUnsafeContentResults(self):
           maxResults = 10
           paginationToken = ''
           finished = False
   
           while finished == False:
               response = self.rek.get_content_moderation(JobId=self.startJobId,
                                                   MaxResults=maxResults,
                                                   NextToken=paginationToken)
   
               print('Codec: ' + response['VideoMetadata']['Codec'])
               print('Duration: ' + str(response['VideoMetadata']['DurationMillis']))
               print('Format: ' + response['VideoMetadata']['Format'])
               print('Frame rate: ' + str(response['VideoMetadata']['FrameRate']))
               print()
   
               for contentModerationDetection in response['ModerationLabels']:
                   print('Label: ' +
                       str(contentModerationDetection['ModerationLabel']['Name']))
                   print('Confidence: ' +
                       str(contentModerationDetection['ModerationLabel']['Confidence']))
                   print('Parent category: ' +
                       str(contentModerationDetection['ModerationLabel']['ParentName']))
                   print('Timestamp: ' + str(contentModerationDetection['Timestamp']))
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
       analyzer.StartUnsafeContent()
       if analyzer.GetSQSMessageSuccess()==True:
           analyzer.GetUnsafeContentResults()
   ```

------
**Note**  
If you've already run a video example other than [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md), the code to replace might be different\.

1. Run the code\. A list of inappropriate content labels detected in the video is shown\.

## GetContentModeration operation response<a name="getcontentmoderation-operationresponse"></a>

The response from `GetContentModeration` is an array, `ModerationLabels`, of [ ContentModerationDetection ](API_ContentModerationDetection.md) objects\. The array contains an element for each time an inappropriate content label is detected\. Within a `ContentModerationDetectionObject` object, [ ModerationLabel ](API_ModerationLabel.md) contains information for a detected item of inappropriate or offensive content\. `Timestamp` is the time, in milliseconds from the start of the video, when the label was detected\. The labels are organized hierarchically in the same manner as the labels detected by inappropriate content image analysis\. For more information, see [Moderating content](moderation.md)\.

The following is an example response from `GetContentModeration`\.

```
{
    "JobStatus": "SUCCEEDED",
    "ModerationLabels": [
        {
            "ModerationLabel": {
                "Confidence": 93.02153015136719,
                "Name": "Male Swimwear Or Underwear",
                "ParentName": "Suggestive"
            },
            "Timestamp": 0
        },
        {
            "ModerationLabel": {
                "Confidence": 93.02153015136719,
                "Name": "Suggestive",
                "ParentName": ""
            },
            "Timestamp": 0
        },
        {
            "ModerationLabel": {
                "Confidence": 98.29075622558594,
                "Name": "Male Swimwear Or Underwear",
                "ParentName": "Suggestive"
            },
            "Timestamp": 1000
        },
        {
            "ModerationLabel": {
                "Confidence": 98.29075622558594,
                "Name": "Suggestive",
                "ParentName": ""
            },
            "Timestamp": 1000
        },
        {
            "ModerationLabel": {
                "Confidence": 97.91191101074219,
                "Name": "Male Swimwear Or Underwear",
                "ParentName": "Suggestive"
            },
            "Timestamp": 1999
        }
    ],
    "NextToken": "w5xfYx64+QvCdGTidVVWtczKHe0JAcUFu2tJ1RgDevHRovJ+1xej2GUDfTMWrTVn1nwSMHi9",
    "VideoMetadata": {
        "Codec": "h264",
        "DurationMillis": 3533,
        "Format": "QuickTime / MOV",
        "FrameHeight": 1080,
        "FrameRate": 30,
        "FrameWidth": 1920
    }
}
```