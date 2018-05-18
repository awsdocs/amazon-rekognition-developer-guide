# Searching for a Face Using its Face ID<a name="search-face-with-id-procedure"></a>

You can use the [SearchFaces](API_SearchFaces.md) operation to search for faces in a collection that match a supplied face ID\.

The following procedures show how you can use the operation with the AWS CLI, the AWS SDK for Java\. 

The face ID is returned in the [IndexFaces](API_IndexFaces.md) operation response when the face is detected and added to a collection\. For more information, see [Storing Faces in a Face Collection](collections-index-faces.md)\.

For more information, see [Managing Collections](managing-collections.md)\. 

**To search for a face in a collection using its face ID \(AWS CLI\)**

1. On the command line, type the following command\. Replace `faceid` with the face identifier you want to search for and replace `collection-id` with the collection you want to search in\.

   ```
   aws rekognition search-faces \
       --face-id face-id \
       --collection-id "collection-id" \
       --region us-east-1 \
       --profile adminuser
   ```

1. To run the command, choose **Enter**\. The JSON output for the `SearchFaces` operation is displayed\. 

**To search for a face in a collection using its face ID \(AWS SDK for Java\)**
+ To search for a face in a collection using its face ID, use the following AWS SDK for Java example code\.

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
  import com.amazonaws.services.rekognition.model.SearchFacesRequest;
  import com.amazonaws.services.rekognition.model.SearchFacesResult;
  import com.fasterxml.jackson.databind.ObjectMapper;
  
    public class SearchFaceMatchingId {
        public static final String collectionId = "collection-id";
        public static final String faceId = "face-id";
        
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
        // Search collection for faces matching the face id.
        
        SearchFacesRequest searchFacesRequest = new SearchFacesRequest()
                .withCollectionId(collectionId)
                .withFaceId(faceId)
                .withFaceMatchThreshold(70F)
                .withMaxFaces(2);
             
         SearchFacesResult searchFacesByImageResult = 
                 amazonRekognition.searchFaces(searchFacesRequest);
  
         System.out.println("Face matching faceId " + faceId);
        List < FaceMatch > faceImageMatches = searchFacesByImageResult.getFaceMatches();
        for (FaceMatch face: faceImageMatches) {
           System.out.println(objectMapper.writerWithDefaultPrettyPrinter()
                   .writeValueAsString(face));
           
           System.out.println();
        }
      }
  
  }
  ```