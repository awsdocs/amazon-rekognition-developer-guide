# Tracking People through a Stored Video \(SDK for Java\)<a name="video-sqs-persons"></a>

The following procedure shows how to track people through a video stored in an Amazon S3 bucket\. The example expands on the code in [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md) which uses an Amazon Simple Queue Service queue to get the completion status of a video analysis request\. 

## Prerequisites<a name="track-persons-prerequisites"></a>

To run these procedures, you need to have the AWS SDK for Java installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. You also need an image file that contains one or more celebrity faces\.

**To detect people in a video stored in an Amazon S3 bucket**

1. Perform [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md)\.

1. Add the following code to the project created in step one\.

   ```
     //Persons========================================================================
      
      private static void StartPersons(String bucket, String video) throws Exception{
          
          int maxResults=10;
          String paginationToken=null;
          
       StartPersonTrackingRequest req = new StartPersonTrackingRequest()
               .withVideo(new Video()
                       .withS3Object(new S3Object()
                           .withBucket(bucket)
                           .withName(video)))
               .withNotificationChannel(channel);
                              
           
          
       StartPersonTrackingResult startPersonDetectionResult = rek.startPersonTracking(req);
       startJobId=startPersonDetectionResult.getJobId();
          
      } 
      
      private static void GetResultsPersons() throws Exception{
          int maxResults=10;
          String paginationToken=null;
          GetPersonTrackingResult personTrackingResult=null;
          
          do{
              if (personTrackingResult !=null){
                  paginationToken = personTrackingResult.getNextToken();
              }
              
              personTrackingResult = rek.getPersonTracking(new GetPersonTrackingRequest()
                   .withJobId(startJobId)
                   .withNextToken(paginationToken)
                   .withSortBy(PersonTrackingSortBy.TIMESTAMP)
                   .withMaxResults(maxResults));
        
              VideoMetadata videoMetaData=personTrackingResult.getVideoMetadata();
                  
              System.out.println("Format: " + videoMetaData.getFormat());
              System.out.println("Codec: " + videoMetaData.getCodec());
              System.out.println("Duration: " + videoMetaData.getDurationMillis());
              System.out.println("FrameRate: " + videoMetaData.getFrameRate());
                  
                  
              //Show persons, confidence and detection times
              List<PersonDetection> detectedPersons= personTrackingResult.getPersons();
           
              for (PersonDetection detectedPerson: detectedPersons) { 
                  
                 long seconds=detectedPerson.getTimestamp()/1000;
                 System.out.print("Sec: " + Long.toString(seconds) + " ");
                 System.out.println("Person Identifier: "  + detectedPerson.getPerson().getIndex());
                    System.out.println();             
              }
          }  while (personTrackingResult !=null && personTrackingResult.getNextToken() != null);
          
      }
   ```

1. In the function `main`, replace the line 

    `StartLabels("bucket","file");` 

   with

    `StartPersons("bucket","file");` 

   If you have already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace will be different\.

1. In the call to `StartPersons`, replace *bucket* and *file* with the Amazon S3 bucket name and file name of the video you want to analyze\.

1. In the function `main`, replace the line 

   `GetResultsLabels();`

   with

   `GetResultsPersons();`

   If you have already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace will be different\.

1. Run the code\. The unique identifiers for tracked people are shown along with the time, in seconds, the people were tracked\.