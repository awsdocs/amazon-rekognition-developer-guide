# Detecting Faces in a Stored Video \(SDK for Java\)<a name="faces-sqs-video"></a>

Amazon Rekognition can detected faces in a video stored in an Amazon S3 bucket\. This procedure expands on the code in [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md) which uses an Amazon Simple Queue Service queue to get the completion status of a video analysis request\. 

## Prerequisites<a name="moderate-images-prerequisites"></a>

To run this procedure, you need to have the AWS SDK for Java installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. 

**To detect faces in a video stored in an Amazon S3 bucket**

1. Perform [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md)\.

1. Add the following code to the project created in step 1\.

   ```
    //Faces=======================================================================
      
      private static void StartFaces(String bucket, String video) throws Exception{
          
          StartFaceDetectionRequest req = new StartFaceDetectionRequest()
                  .withVideo(new Video()
                          .withS3Object(new S3Object()
                              .withBucket(bucket)
                              .withName(video)))
                  .withNotificationChannel(channel);
                              
                              
          
          StartFaceDetectionResult startLabelDetectionResult = rek.startFaceDetection(req);
          startJobId=startLabelDetectionResult.getJobId();
          
      } 
      
      private static void GetResultsFaces() throws Exception{
          
          int maxResults=10;
          String paginationToken=null;
          GetFaceDetectionResult faceDetectionResult=null;
          
          do{
              if (faceDetectionResult !=null){
                  paginationToken = faceDetectionResult.getNextToken();
              }
          
              faceDetectionResult = rek.getFaceDetection(new GetFaceDetectionRequest()
                   .withJobId(startJobId)
                   .withNextToken(paginationToken)
                   .withMaxResults(maxResults));
          
              VideoMetadata videoMetaData=faceDetectionResult.getVideoMetadata();
                  
              System.out.println("Format: " + videoMetaData.getFormat());
              System.out.println("Codec: " + videoMetaData.getCodec());
              System.out.println("Duration: " + videoMetaData.getDurationMillis());
              System.out.println("FrameRate: " + videoMetaData.getFrameRate());
                  
                  
              //Show faces, confidence and detection times
              List<FaceDetection> faces= faceDetectionResult.getFaces();
           
              for (FaceDetection face: faces) { 
                  long seconds=face.getTimestamp()/1000;
                  System.out.print("Sec: " + Long.toString(seconds) + " ");
                  System.out.println(face.getFace().toString());
                  System.out.println();           
              }
          } while (faceDetectionResult !=null && faceDetectionResult.getNextToken() != null);
            
              
      }
   ```

1. In the function `main`, replace the line 

    `StartLabels("bucket","file");` 

   with

    `StartFaces("bucket","file");` 

   If you have already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace will be different\.

1. In the call to `StartFaces`, replace *bucket* and *file* with the Amazon S3 bucket name and file name of the video you want to analyze\.

1. In the function `main`, replace the line 

   `GetResultsLabels();`

   with

   `GetResultsFaces();`

   If you have already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace will be different\.

1. Run the code\. Information about the faces detected in the video is shown\.