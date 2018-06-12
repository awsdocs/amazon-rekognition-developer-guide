# Recognizing Celebrities in a Stored Video \(AWS SDK for Java\)<a name="celebrities-video-sqs"></a>

To recognize celebrities in a video stored in an Amazon S3 bucket, you use [StartCelebrityRecognition](API_StartCelebrityRecognition.md) and [GetCelebrityRecognition](API_GetCelebrityRecognition.md)\. Analyzing videos stored in an Amazon S3 bucket is an asynchronous workflow\. For more information, see [Working with Stored Videos](video.md)\. 

You can recognize celebrities in a video stored in an Amazon S3 bucket\. This procedure expands on the code in [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), which uses an Amazon SQS queue to get the completion status of a video analysis request\. 

## Recognizing celebrities in a stored video \(SDK\)<a name="recognize-video-example"></a>

To run this procedure, you need to have the AWS SDK for Java installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. You also need a video file that contains one or more celebrity faces\.

**To detect celebrities in a video stored in an Amazon S3 bucket**

1. Perform [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md)\.

1. Add the following code to the project created in step 1\.

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

1. In the function `main`, replace the line 

    `StartLabels("bucket","file");` 

   with

    `StartCelebrities("bucket","file");` 

   If you have already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace is different\. 

1. In the call to `StartCelebrities`, replace *bucket* and *file* with the Amazon S3 bucket name and file name of the video that you want to analyze\.

1. In the function `main`, replace the line 

   `GetResultsLabels();`

   with

   `GetResultsCelebrities();`

   If you have already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace is different\. 

1. Run the code\. Information about the celebrities recognized in the video is shown\.

## GetCelebrityRecognition Operation Response<a name="getcelebrityrecognition-operation-output"></a>

The response from `GetCelebrityRecognition` includes an array, `Celebrities`, of celebrities \([CelebrityRecognition](API_CelebrityRecognition.md)\) that were recognized in the video and the times they were recognized\. The following is an example JSON response\.

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
+ **Recognized celebrities** – `Celebrities` is an array of celebrities and the times that they are recognized in a video\. A [CelebrityRecognition](API_CelebrityRecognition.md) object exists for each time the celebrity is recognized in the video\. Each `CelebrityRecognition` contains information about a recognized celebrity \([CelebrityDetail](API_CelebrityDetail.md)\) and the time \(`Timestamp`\) the celebrity was recognized in the video\. `Timestamp` is measured in milliseconds from the start of the video\. 
+ **CelebrityDetail** – Contains information about a recognized celebrity\. It includes the celebrity name \(`Name`\), identifier \(`ID`\), and a list of URLs pointing to related content \(`Urls`\)\. It also includes the bounding box for the celebrity's body, the confidence level that Amazon Rekognition Video has in the accuracy of the recognition, and details about the celebrity's face, [FaceDetail](API_FaceDetail.md)\. If you need to get the related content later, you can use `ID` with [GetCelebrityInfo](API_GetCelebrityInfo.md)\. 
+ **VideoMetadata** – Information about the video that was analyzed\.