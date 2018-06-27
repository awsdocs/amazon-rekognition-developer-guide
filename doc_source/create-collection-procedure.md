# Creating a Collection<a name="create-collection-procedure"></a>

You can use the [CreateCollection](API_CreateCollection.md) operation to create a collection\.

For more information, see [Managing Collections](collections.md#managing-collections)\. 

**To create a collection \(SDK\)**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` permissions\. For more information, see [Step 1: Set Up an AWS Account and Create an IAM User](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Use the following examples to call the `CreateCollection` operation\.

------
#### [ Java ]

   The following example creates a collection and displays its Amazon Resource Name \(ARN\)\.

   Change the value of `collectionId` to the name of the collection you want to create\.

   ```
   
   package aws.example.rekognition.image;
   
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.CreateCollectionRequest;
   import com.amazonaws.services.rekognition.model.CreateCollectionResult;
   
   
   public class CreateCollection {
   
      public static void main(String[] args) throws Exception {
   
   
         AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
   
         
         String collectionId = "MyCollection";
               System.out.println("Creating collection: " +
            collectionId );
               
           CreateCollectionRequest request = new CreateCollectionRequest()
                       .withCollectionId(collectionId);
              
         CreateCollectionResult createCollectionResult = rekognitionClient.createCollection(request); 
         System.out.println("CollectionArn : " +
            createCollectionResult.getCollectionArn());
         System.out.println("Status code : " +
            createCollectionResult.getStatusCode().toString());
   
      } 
   
   }
   ```

------
#### [ AWS CLI ]

   This AWS CLI command displays the JSON output for the `create-collection` CLI operation\. 

   Replace the value of `collection-id` with the name of the collection you want to create\.

   ```
   aws rekognition create-collection \
       --collection-id "collectionname"
   ```

------
#### [ Python ]

   The following example creates a collection and displays its Amazon Resource Name \(ARN\)\. 

   Change the value of `collectionId` to the name of collection you want to create\.

   ```
   import boto3
   
   if __name__ == "__main__":
   
       maxResults=2
       collectionId='MyCollection'
   	
       client=boto3.client('rekognition')
   
       #Create a collection
       print('Creating collection:' + collectionId)
       response=client.create_collection(CollectionId=collectionId)
       print('Collection ARN: ' + response['CollectionArn'])
       print('Status code: ' + str(response['StatusCode']))
       print('Done...')
   ```

------
#### [ \.NET ]

   The following example creates a collection and displays its Amazon Resource Name \(ARN\)\.

   Change the value of `collectionId` to the name of collection you want to create\.

   ```
   using System;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   public class CreateCollection
   {
       public static void Example()
       {
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           String collectionId = "MyCollection";
           Console.WriteLine("Creating collection: " + collectionId);
   
           CreateCollectionRequest createCollectionRequest = new CreateCollectionRequest()
           {
               CollectionId = collectionId
           };
   
           CreateCollectionResponse createCollectionResponse = rekognitionClient.CreateCollection(createCollectionRequest);
           Console.WriteLine("CollectionArn : " + createCollectionResponse.CollectionArn);
           Console.WriteLine("Status code : " + createCollectionResponse.StatusCode);
   
       }
   }
   ```

------

## CreateCollection Operation Request<a name="createcollection-request"></a>

The input to `CreationCollection` is the name of the collection that you want to create\.

```
{
    "CollectionId": "MyCollection"
}
```

## CreateCollection Operation Response<a name="createcollection-operation-response"></a>

Amazon Rekognition creates the collection and returns the Amazon Resource Name \(ARN\) of the newly created collection\.

```
{
   "CollectionArn": "aws:rekognition:us-east-1:acct-id:collection/examplecollection",
   "StatusCode": 200
}
```