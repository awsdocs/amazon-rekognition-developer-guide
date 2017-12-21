# Searching for a Face Using an Image<a name="search-face-with-image-procedure"></a>

You can use the [SearchFacesByImage](API_SearchFacesByImage.md) operation to search for faces in a collection that match the largest face in a supplied image\.

The following procedures show how you can use the operation with the AWS CLI, the AWS SDK for Java\. 

For more information, see [Searching for Faces with Rekognition Image Collection](collections-search-faces.md)\. 

**To search for a face in a collection using an image \(AWS CLI\)**

1. Upload an image \(containing one or more faces\) to your S3 bucket\. 

   For instructions, see [Uploading Objects into Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. On the command line, type the following command\. Replace `bucket-name` with the S3 bucket you are using\. Replace `example.jpg` with the image file name that contains the face you want to search for\. Replace `collection-id` with the collection you want to search in\.

   ```
   aws rekognition search-faces-by-image \
       --image '{"S3Object":{"Bucket":"bucket-name","Name":"Example.jpg"}}' \
       --collection-id "collection-id" \
       --region us-east-1 \
       --profile adminuser
   ```

1. To run the command, choose **Enter**\. The JSON output for the `SearchFacesByImage` operation is displayed\. 

**To search for a face in a collection using an image \(AWS SDK for Java\)**

1. Upload an image \(containing one or more faces\) to your S3 bucket\. 

   For instructions, see [Uploading Objects into Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. To search for a face in a collection using an image, use the following AWS SDK for Java example code\.

   ```
   package com.amazonaws.samples;
   
       import java.util.List;
       import com.amazonaws.AmazonClientException;
       import com.amazonaws.auth.AWSCredentials;
       import com.amazonaws.auth.AWSStaticCredentialsProvider;
       import com.amazonaws.auth.profile.ProfileCredentialsProvider;
       import com.amazonaws.regions.Regions;
       import com.amazonaws.services.rekognition.AmazonRekognition;
       import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
       import com.amazonaws.services.rekognition.model.FaceMatch;
       import com.amazonaws.services.rekognition.model.Image;
       import com.amazonaws.services.rekognition.model.S3Object;
       import com.amazonaws.services.rekognition.model.SearchFacesByImageRequest;
       import com.amazonaws.services.rekognition.model.SearchFacesByImageResult;
       import com.fasterxml.jackson.databind.ObjectMapper;
   
       public class SearchFacesMatchingImage {
           public static final String collectionId = "exampleCollection";
           public static final String bucket = "photo-label-detect";
           public static final String fileName = "filename.jpg";
             
           public static void main(String[] args) throws Exception {
               AWSCredentials credentials;
             try {
                credentials = new ProfileCredentialsProvider("AdminUser").getCredentials();
             } catch (Exception e) {
                throw new AmazonClientException(
                   "Cannot load the credentials from the credential profiles file. " +
                   "Please make sure that your credentials file is at the correct " +
                   "location (/Users/userid/.aws/credentials), and is in a valid format.",
                   e);
             }
             AmazonRekognition amazonRekognition = AmazonRekognitionClientBuilder
                .standard()
                .withRegion(Regions.US_WEST_2)
                .withCredentials(new AWSStaticCredentialsProvider(credentials))
                .build();
               
             ObjectMapper objectMapper = new ObjectMapper();
             
              // Get an image object from S3 bucket.
             Image image=new Image()
                     .withS3Object(new S3Object()
                             .withBucket(bucket)
                             .withName(fileName));
             
             // Search collection for faces similar to the largest face in the image.
             SearchFacesByImageRequest searchFacesByImageRequest = new SearchFacesByImageRequest()
                     .withCollectionId(collectionId)
                     .withImage(image)
                     .withFaceMatchThreshold(70F)
                     .withMaxFaces(2);
                  
              SearchFacesByImageResult searchFacesByImageResult = 
                      amazonRekognition.searchFacesByImage(searchFacesByImageRequest);
   
              System.out.println("Faces matching largest face in image from" + fileName);
             List < FaceMatch > faceImageMatches = searchFacesByImageResult.getFaceMatches();
             for (FaceMatch face: faceImageMatches) {
                 System.out.println(objectMapper.writerWithDefaultPrettyPrinter()
                         .writeValueAsString(face));
                System.out.println();
             }
          }
      }
   ```

   The code example stores three faces to an Amazon Rekognition face collection\. Then, it searches the face collection for face matches\. It shows usage of both `SearchFaces` and `SearchFacesByImage` API operations\. The code example specifies both the `FaceMatchThreshold` and `MaxFaces` parameters to limit the results returned in the response\.