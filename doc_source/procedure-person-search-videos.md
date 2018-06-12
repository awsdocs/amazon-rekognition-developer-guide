# Searching Stored Videos for Faces \(SDK for Java\)<a name="procedure-person-search-videos"></a>

The following procedure shows how to search a collection for faces that match the faces of persons detected in a video\. The procedure also shows how to get the tracking data for persons matched in the video\. The video must be stored in an Amazon S3 bucket\. The procedure expands on the code in [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md) which uses an Amazon Simple Queue Service queue to get the completion status of a video analysis request\. 

## Prerequisites<a name="moderate-images-prerequisites"></a>

To run these procedures, you need to have the AWS CLI and AWS SDK for Java installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. 

**To search a video**

1. [Create a collection](create-collection-procedure.md)\.

1. [Index a face into the collection](add-faces-to-collection-procedure.md)\.

1. Perform [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md)\.

1. Add the following code to the project created in step 3\.

   ```
        //Face collection search in video ==================================================================
        private static void StartFaceSearchCollection(String bucket, String video) throws Exception{
            
            
            StartFaceSearchRequest req = new StartFaceSearchRequest()
                    .withCollectionId("CollectionId")
                    .withVideo(new Video()
                            .withS3Object(new S3Object()
                                .withBucket(bucket)
                                .withName(video)))
                    .withNotificationChannel(channel);
      
                                              
             
            StartFaceSearchResult startPersonCollectionSearchResult = rek.startFaceSearch(req);
             startJobId=startPersonCollectionSearchResult.getJobId();
             
         } 
         
         private static void GetResultsFaceSearchCollection() throws Exception{
         
             GetFaceSearchResult faceSearchResult=null;
             int maxResults=10;
             String paginationToken=null;
             
             do {
                 
                 if (faceSearchResult !=null){
                     paginationToken = faceSearchResult.getNextToken();
                 }
             
             
                 faceSearchResult  = rek.getFaceSearch(
                         new GetFaceSearchRequest()
                             .withJobId(startJobId)
                             .withMaxResults(maxResults)
                             .withNextToken(paginationToken)
                             .withSortBy(FaceSearchSortBy.TIMESTAMP)
                         );
                 
       
                 VideoMetadata videoMetaData=faceSearchResult.getVideoMetadata();
                     
                 System.out.println("Format: " + videoMetaData.getFormat());
                 System.out.println("Codec: " + videoMetaData.getCodec());
                 System.out.println("Duration: " + videoMetaData.getDurationMillis());
                 System.out.println("FrameRate: " + videoMetaData.getFrameRate());
                 System.out.println();      
                     
                 
                 //Show search results
                 List<PersonMatch> matches= 
                         faceSearchResult.getPersons();
                 
                 for (PersonMatch match: matches) { 
                     long seconds=match.getTimestamp()/1000;
                     System.out.print("Sec: " + Long.toString(seconds));
                     System.out.println("Person number: " + match.getPerson().getIndex());
                     List <FaceMatch> faceMatches = match.getFaceMatches();
                     System.out.println("Matches in collection...");
                     for (FaceMatch faceMatch: faceMatches){
                         Face face=faceMatch.getFace();
                         System.out.println("Face Id: "+ face.getFaceId());
                         System.out.println("Similarity: " + faceMatch.getSimilarity().toString());
                         System.out.println();
                     }
                      System.out.println();           
                 } 
                 
                 System.out.println(); 
                 
             } while (faceSearchResult !=null && faceSearchResult.getNextToken() != null);
         
         }
   ```

1. In the function `main`, replace the line 

    `StartLabels("bucket","file");` 

   with

    `StartFaceSearchCollection("bucket","file");` 

   If you have already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace will be different\. 

1. In the call to `StartFaceSearchCollection`, replace *bucket* and *file* with the Amazon S3 bucket name and the file name of the video you want to search\.

1. In the function `main`, replace the line 

   `GetResultsLabels();`

   with

   `GetResultsFaceSearchCollection();`

   If you have already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace will be different\.

1. In the function `StartFaceSearchCollection`, change the value of `CollectionId` to the name of the collection you created in step 1\.

1. Run the code\. A list of persons in the video whose faces match those in the input collection is displayed\. The tracking data for each matched person is also displayed\.