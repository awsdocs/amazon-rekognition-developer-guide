# Detecting Unsafe Stored Videos \(SDK for Java\)<a name="procedure-moderate-videos"></a>

To detect suggestive and adult content in a video stored in an Amazon S3 bucket, you use [StartContentModeration](API_StartContentModeration.md) and [GetContentModeration](API_GetContentModeration.md)\. Analyzing videos stored in an Amazon S3 bucket is an asynchronous workflow\. For more information, see [Working with Stored Videos](video.md)\.

## Detecting Unsafe Content in a Stored Video \(SDK\)<a name="moderate-video-example"></a>

 This procedure expands on the code in [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), which uses an Amazon Simple Queue Service queue to get the completion status of a video analysis request\.

To run these procedures, you need to have the AWS CLI and AWS SDK for Java installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. 

**To detect unsafe content in a video stored in an Amazon S3 bucket**

1. Perform [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md)\.

1. Add the following code to the project created in step one\.

   ```
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

1. In the function `main`, replace the line 

    `StartLabels("bucket","file");` 

   with

    `StartModerationLabels("bucket","file");` 

   If you have already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace will be different\. 

1. In the call to `StartModerationLabels`, replace *bucket* and *file* with the Amazon S3 bucket name and file name of the video you want to analyze\.

1. In the function `main`, replace the line 

   `GetResultsLabels();`

   with

   `GetResultsModerationLabels();`

   If you have already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace will be different\.

1. Run the code\. A list of unsafe content labels detected in the video is shown\.

## Operation Response<a name="getcontentmoderation-operationresponse"></a>

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

The response from `GetContentModeration` is an array, `ModerationLabels`, of [ContentModerationDetection](API_ContentModerationDetection.md) objects\. The array contains an element for each time a moderation label is detected\. Within a `ContentModerationDetectionObject` object, [ModerationLabel](API_ModerationLabel.md) contains information for a detected item of suggestive or adult content\. `Timestamp` is the time, in milliseconds from the start of the video, when the label was detected\. The labels are organized hierarchically in the same manner as the moderation labels detected by image analysis\. For more information, see [Detecting Unsafe Content](moderation.md)\.