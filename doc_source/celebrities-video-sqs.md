# Recognizing Celebrities in a Stored Video \(SDK for Java\)<a name="celebrities-video-sqs"></a>

You can recognize celebrities in a video stored in an Amazon S3 bucket\. This procedure expands on the code in [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md) which uses an Amazon Simple Queue Service queue to get the completion status of a video analysis request\. 

## Prerequisites<a name="recognize-celebrities-video-prerequisites"></a>

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

   If you have already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace will be different\. 

1. In the call to `StartCelebrities`, replace *bucket* and *file* with the Amazon S3 bucket name and file name of the video you want to analyze\.

1. In the function `main`, replace the line 

   `GetResultsLabels();`

   with

   `GetResultsCelebrities();`

   If you have already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace will be different\. 

1. Run the code\. Information about the celebrities recognized in the video is shown\.