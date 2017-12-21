# Listing Faces in a Collection<a name="list-faces-in-collection-procedure"></a>

You can use the [IndexFaces](API_IndexFaces.md) operation to list the faces in a collection\.

The following procedures show how you can use the operation with the AWS CLI, the AWS SDK for Java\. 

For more information, see [Managing Collections](managing-collections.md)\. 

**To list faces in a collection \(AWS CLI\)**

1. Upload an image \(containing one or more faces\) to your S3 bucket\. 

   For instructions, see [Uploading Objects into Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. On the command line, type the following command\. Replace `collection-id` with the name of the collection you want to list\.

   ```
   aws rekognition list-faces \
         --collection-id "collection-id" \
         --region us-east-1
         --profile adminuser
   ```

1. To run the command, choose **Enter**\. The JSON output for the `ListFaces` operation is displayed\. 

   The command returns faces in the collection along with a `NextToken` in the response\. You can use this in your subsequent request \(by adding the `--next-token` parameter in the AWS CLI command\) to fetch next set of faces\.

**To list faces in a collection \(AWS SDK for Java\)**

+ To list faces in a collection, use the following AWS SDK for Java example code\.

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
  import com.amazonaws.services.rekognition.model.Face;
  import com.amazonaws.services.rekognition.model.ListFacesRequest;
  import com.amazonaws.services.rekognition.model.ListFacesResult;
  
  import com.fasterxml.jackson.databind.ObjectMapper;
  
  public class ListFaces {
      public static final String collectionId = "exampleCollection";
      public static final String bucket = "photo-label-detect";
  
  
     public static void main(String[] args) throws Exception {
        AWSCredentials credentials;
        try {
           credentials = new ProfileCredentialsProvider("AdminUser").getCredentials();
        } catch (Exception e) {
           throw new AmazonClientException(
              "Cannot load the credentials from the credential profiles file. " +
              "Please make sure that your credentials file is at the correct " +
              "location (/Users/userid/.aws/credentials), and is in valid format.",
              e);
        }
  
        ObjectMapper objectMapper = new ObjectMapper();
  
  
        AmazonRekognition amazonRekognition = AmazonRekognitionClientBuilder
           .standard()
           .withRegion(Regions.US_WEST_2)
           .withCredentials(new AWSStaticCredentialsProvider(credentials))
           .build();
  
  
   
        ListFacesResult listFacesResult = null;
        System.out.println("Faces in collection " + collectionId);
  
        String paginationToken = null;
        do {
           if (listFacesResult != null) {
              paginationToken = listFacesResult.getNextToken();
           }
           
           ListFacesRequest listFacesRequest = new ListFacesRequest()
                   .withCollectionId(collectionId)
                   .withMaxResults(1)
                   .withNextToken(paginationToken);
          
           listFacesResult =  amazonRekognition.listFaces(listFacesRequest);
           List < Face > faces = listFacesResult.getFaces();
           for (Face face: faces) {
              System.out.println(objectMapper.writerWithDefaultPrettyPrinter()
                 .writeValueAsString(face));
           }
        } while (listFacesResult != null && listFacesResult.getNextToken() !=
           null);
     }
  
  }
  ```