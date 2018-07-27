# Detecting Unsafe Stored Videos<a name="procedure-moderate-videos"></a>

Amazon Rekognition Video unsafe content detection in stored videos is an asynchronous operation\. To started detecting unsafe content, call [StartContentModeration](API_StartContentModeration.md)\. Amazon Rekognition Video publishes the completion status of the video analysis to an Amazon Simple Notification Service topic\. If the video analysis is succesful, call [GetContentModeration](API_GetContentModeration.md) to get the analysis results\. For more information about starting video analysis and getting the results, see [Calling Amazon Rekognition Video Operations](api-video.md)\.

 This procedure expands on the code in [Analyzing a Video Stored in an Amazon S3 Bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md), which uses an Amazon Simple Queue Service queue to get the completion status of a video analysis request\.

**To detect unsafe content in a video stored in an Amazon S3 bucket \(SDK\)**

1. Perform [Analyzing a Video Stored in an Amazon S3 Bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md)\.

1. Add the following code to the class `VideoDetect` that you created in step 1\.

------
#### [ Java ]

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
       //Content moderation ==================================================================
       private static void StartModerationLabels(String bucket, String video) throws Exception{
           
           StartContentModerationRequest req = new StartContentModerationRequest()
                   .withVideo(new Video()
                           .withS3Object(new S3Object()
                               .withBucket(bucket)
                               .withName(video)))
                   .withNotificationChannel(channel);
                                
                                
            
            StartContentModerationResult startModerationLabelDetectionResult = rek.startContentModeration(req);
            startJobId=startModerationLabelDetectionResult.getJobId();
            
        } 
        
        private static void GetResultsModerationLabels() throws Exception{
            
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

   2a\. In the function `main`, replace the line: 

    `StartLabels(bucket,video);` 

   with:

    `StartModerationLabels(bucket,video);` 

   2b\. Replace the line:

   `GetResultsLabels();`

   with:

   `GetResultsModerationLabels();`

------
#### [ Python ]

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
       def GetResultsModerationLabels(self, jobId):
           maxResults = 10
           paginationToken = ''
           finished = False
   
           while finished == False:
               response = self.rek.get_content_moderation(JobId=jobId,
                                                   MaxResults=maxResults,
                                                   NextToken=paginationToken)
   
               print(response['VideoMetadata']['Codec'])
               print(str(response['VideoMetadata']['DurationMillis']))
               print(response['VideoMetadata']['Format'])
               print(response['VideoMetadata']['FrameRate'])
   
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

   2a\. In the function `main`, replace the line:

   ```
           response = self.rek.start_label_detection(Video={'S3Object': {'Bucket': self.bucket, 'Name': self.video}},
                                            NotificationChannel={'RoleArn': self.roleArn, 'SNSTopicArn': self.topicArn})
   ```

   with:

   ```
           response = self.rek.start_content_moderation(Video={'S3Object':{'Bucket':self.bucket,'Name':self.video}},
               NotificationChannel={'RoleArn':self.roleArn, 'SNSTopicArn':self.topicArn})
   ```

   2b\. Replace the line:

   ```
                           self.GetResultsLabels(rekMessage['JobId'])
   ```

   with:

   ```
                           self.GetResultsModerationLabels(rekMessage['JobId'])
   ```

------
**Note**  
If you've already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md), the function name to replace is different\.

1. Run the code\. A list of unsafe content labels detected in the video is shown\.

## GetContentModeration Operation Response<a name="getcontentmoderation-operationresponse"></a>

The response from `GetContentModeration` is an array, `ModerationLabels`, of [ContentModerationDetection](API_ContentModerationDetection.md) objects\. The array contains an element for each time a moderation label is detected\. Within a `ContentModerationDetectionObject` object, [ModerationLabel](API_ModerationLabel.md) contains information for a detected item of suggestive or adult content\. `Timestamp` is the time, in milliseconds from the start of the video, when the label was detected\. The labels are organized hierarchically in the same manner as the moderation labels detected by image analysis\. For more information, see [Detecting Unsafe Content](moderation.md)\.

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