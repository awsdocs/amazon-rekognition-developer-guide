# Listing Collections<a name="list-collection-procedure"></a>

You can use the [ListCollections](API_ListCollections.md) operation to list the available collections\.

The following procedures show how you can use the operation with the AWS CLI, the AWS SDK for Java\. 

For more information, see [Managing Collections](managing-collections.md)\. 

**To list collections \(AWS CLI\)**

1. On the command line, type the following command\. The command returns a list of collections in the us\-west\-2 region\.

   ```
   aws rekognition list-collections \
       --region us-west-2 \
       --profile adminuser
   ```

1. To run the command, choose **Enter**\. The JSON output for the `ListCollections` API operation is displayed\. 

**To list collections \(AWS SDK for Java\)**

+ To list collections, use the following AWS SDK for Java example code\.

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
  import com.amazonaws.services.rekognition.model.ListCollectionsRequest;
  import com.amazonaws.services.rekognition.model.ListCollectionsResult;
  
  public class ListCollections {
  
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
  
  
        AmazonRekognition amazonRekognition = AmazonRekognitionClientBuilder
           .standard()
           .withRegion(Regions.US_WEST_2)
           .withCredentials(new AWSStaticCredentialsProvider(credentials))
           .build();
  
  
        System.out.println("Listing collections");
        int limit = 1;
        ListCollectionsResult listCollectionsResult = null;
        String paginationToken = null;
        do {
           if (listCollectionsResult != null) {
              paginationToken = listCollectionsResult.getNextToken();
           }
           ListCollectionsRequest listCollectionsRequest = new ListCollectionsRequest()
                   .withMaxResults(limit)
                   .withNextToken(paginationToken);
           listCollectionsResult=amazonRekognition.listCollections(listCollectionsRequest);
           
           List < String > collectionIds = listCollectionsResult.getCollectionIds();
           for (String resultId: collectionIds) {
              System.out.println(resultId);
           }
        } while (listCollectionsResult != null && listCollectionsResult.getNextToken() !=
           null);
       
     }
  
  
  }
  ```