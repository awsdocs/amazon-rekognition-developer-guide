# Deleting a Collection<a name="delete-collection-procedure"></a>

You can use the [DeleteCollection](API_DeleteCollection.md) operation to delete a collection\.

For more information, see [Managing Collections](collections.md#managing-collections)\. 

**To delete a collection \(SDK\)**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` permissions\. For more information, see [Step 1: Set Up an AWS Account and Create an IAM User](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Use the following examples to call the `DeleteCollection` operation\.

------
#### [ Java ]

   This example deletes a collection\.

   Change the value `collectionId` to the collection that you want to delete\.

   ```
   
   package aws.example.rekognition.image;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.DeleteCollectionRequest;
   import com.amazonaws.services.rekognition.model.DeleteCollectionResult;
   
   
   public class DeleteCollection {
   
      public static void main(String[] args) throws Exception {
   
         AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
   
         String collectionId = "MyCollection";
   
         System.out.println("Deleting collections");
         
         DeleteCollectionRequest request = new DeleteCollectionRequest()
            .withCollectionId(collectionId);
         DeleteCollectionResult deleteCollectionResult = rekognitionClient.deleteCollection(request);        
     
         System.out.println(collectionId + ": " + deleteCollectionResult.getStatusCode()
            .toString());
   
      } 
   
   }
   ```

------
#### [ AWS CLI ]

   This AWS CLI command displays the JSON output for the `delete-collection` CLI operation\. Replace the value of `collection-id` with the name of the collection that you want to delete\.

   ```
   aws rekognition delete-collection \
       --collection-id "collectionname"
   ```

------
#### [ Python ]

   This example deletes a collection\.

   Change the value `collectionId` to the collection that you want to delete\.

   ```
   import boto3
   from botocore.exceptions import ClientError
   from os import environ
   
   if __name__ == "__main__":
   
       collectionId='MyCollection'
       print('Attempting to delete collection ' + collectionId)
       client=boto3.client('rekognition')
       statusCode=''
       try:
           response=client.delete_collection(CollectionId=collectionId)
           statusCode=response['StatusCode']
           
       except ClientError as e:
           if e.response['Error']['Code'] == 'ResourceNotFoundException':
               print ('The collection ' + collectionId + ' was not found ')
           else:
               print ('Error other than Not Found occurred: ' + e.response['Error']['Message'])
           statusCode=e.response['ResponseMetadata']['HTTPStatusCode']
       print('Operation returned Status Code: ' + str(statusCode))
       print('Done...')
   ```

------
#### [ \.NET ]

   This example deletes a collection\.

   Change the value `collectionId` to the collection that you want to delete\.

   ```
   using System;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   public class DeleteCollection
   {
       public static void Example()
       {
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           String collectionId = "MyCollection";
           Console.WriteLine("Deleting collection: " + collectionId);
   
           DeleteCollectionRequest deleteCollectionRequest = new DeleteCollectionRequest()
           {
               CollectionId = collectionId
           };
   
           DeleteCollectionResponse deleteCollectionResponse = rekognitionClient.DeleteCollection(deleteCollectionRequest);
           Console.WriteLine(collectionId + ": " + deleteCollectionResponse.StatusCode);
       }
   }
   ```

------

## DeleteCollection Operation Request<a name="deletecollection-request"></a>

The input to `DeleteCollection` is the ID of the collection to be deleted, as shown in the following JSON example\. 

```
{
    "CollectionId": "MyCollection"
}
```

## DeleteCollection Operation Response<a name="deletecollection-operation-response"></a>

The `DeleteCollection` response contains an HTTP status code that indicates the success or failure of the operation\. `200` is returned if the collection is successfully deleted\.

```
{"StatusCode":200}
```