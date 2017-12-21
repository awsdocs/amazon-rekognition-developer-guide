# Creating a Collection<a name="create-collection-procedure"></a>

You can use the [CreateCollection](API_CreateCollection.md) operation to create a collection\.

The following procedures show how you can use the operation with the AWS CLI, the AWS SDK for Java\. 

For more information, see [Managing Collections](managing-collections.md)\. 

**To create a collection \(AWS CLI\)**

1. On the command line, type the following command\. Replace `collectionname` with the name of the collection you want to create\.

   ```
   aws rekognition create-collection \
       --collection-id "collectionname" \
       --region us-west-2 \
       --profile adminuser
   ```

1. To run the command, choose **Enter**\. The JSON output for the `CreateCollection` API operation is displayed\.

**To create a collection \(AWS SDK for Java\)**

+ To create a collection, use the following AWS SDK for Java example code\.

  ```
  package com.amazonaws.samples;
  import com.amazonaws.AmazonClientException;
  import com.amazonaws.auth.AWSCredentials;
  import com.amazonaws.auth.AWSStaticCredentialsProvider;
  import com.amazonaws.auth.profile.ProfileCredentialsProvider;
  import com.amazonaws.regions.Regions;
  import com.amazonaws.services.rekognition.AmazonRekognition;
  import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
  import com.amazonaws.services.rekognition.model.CreateCollectionRequest;
  import com.amazonaws.services.rekognition.model.CreateCollectionResult;
  
  public class CreateCollection {
  
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
  
        
        String collectionId = "exampleCollection";
              System.out.println("Creating collection: " +
           collectionId );
              
          CreateCollectionRequest request = new CreateCollectionRequest()
                      .withCollectionId(collectionId);
             
        CreateCollectionResult createCollectionResult = amazonRekognition.createCollection(request); 
        System.out.println("CollectionArn : " +
           createCollectionResult.getCollectionArn());
        System.out.println("Status code : " +
           createCollectionResult.getStatusCode().toString());
  
     }
  
  }
  ```