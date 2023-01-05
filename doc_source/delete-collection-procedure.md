# Deleting a collection<a name="delete-collection-procedure"></a>

You can use the [DeleteCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteCollection.html) operation to delete a collection\.

For more information, see [Managing collections](collections.md#managing-collections)\. 



**To delete a collection \(SDK\)**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` permissions\. For more information, see [Step 1: Set up an AWS account and create an IAM user](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Use the following examples to call the `DeleteCollection` operation\.

------
#### [ Java ]

   This example deletes a collection\.

   Change the value `collectionId` to the collection that you want to delete\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
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
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/DeleteCollection.java)\.

   ```
       public static void deleteMyCollection(RekognitionClient rekClient,String collectionId ) {
   
           try {
               DeleteCollectionRequest deleteCollectionRequest = DeleteCollectionRequest.builder()
                   .collectionId(collectionId)
                   .build();
   
               DeleteCollectionResponse deleteCollectionResponse = rekClient.deleteCollection(deleteCollectionRequest);
               System.out.println(collectionId + ": " + deleteCollectionResponse.statusCode().toString());
   
           } catch(RekognitionException e) {
               System.out.println(e.getMessage());
               System.exit(1);
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

   Change the value `collection_id` to the collection that you want to delete\.

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   from botocore.exceptions import ClientError
   from os import environ
   
   def delete_collection(collection_id):
   
   
       print('Attempting to delete collection ' + collection_id)
       client=boto3.client('rekognition')
       status_code=0
       try:
           response=client.delete_collection(CollectionId=collection_id)
           status_code=response['StatusCode']
           
       except ClientError as e:
           if e.response['Error']['Code'] == 'ResourceNotFoundException':
               print ('The collection ' + collection_id + ' was not found ')
           else:
               print ('Error other than Not Found occurred: ' + e.response['Error']['Message'])
           status_code=e.response['ResponseMetadata']['HTTPStatusCode']
       return(status_code)
   
   
   def main():
       collection_id='UnitTestCollection'
       status_code=delete_collection(collection_id)
       print('Status code: ' + str(status_code))
   
   if __name__ == "__main__":
       main()
   ```

------
#### [ \.NET ]

   This example deletes a collection\.

   Change the value `collectionId` to the collection that you want to delete\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
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
#### [ Node\.js ]

   ```
   import { DeleteCollectionCommand } from  "@aws-sdk/client-rekognition";
   import  { RekognitionClient } from "@aws-sdk/client-rekognition";
   
   // Set the AWS Region.
   const REGION = "region"; //e.g. "us-east-1"
   const rekogClient = new RekognitionClient({ region: REGION });
   
   // Name the collection
   const collection_name = "collectionName"
   
   const deleteCollection = async (collectionName) => {
       try {
          console.log(`Attempting to delete collection named - ${collectionName}`)
          var response = await rekogClient.send(new DeleteCollectionCommand({CollectionId: collectionName}))
          var status_code = response.StatusCode
          if (status_code = 200){
              console.log("Collection successfully deleted.")
          }
          return response; // For unit tests.
       } catch (err) {
         console.log("Error", err.stack);
       }
     };
   
   deleteCollection(collection_name)
   ```

------

## DeleteCollection operation request<a name="deletecollection-request"></a>

The input to `DeleteCollection` is the ID of the collection to be deleted, as shown in the following JSON example\. 

```
{
    "CollectionId": "MyCollection"
}
```

## DeleteCollection operation response<a name="deletecollection-operation-response"></a>

The `DeleteCollection` response contains an HTTP status code that indicates the success or failure of the operation\. `200` is returned if the collection is successfully deleted\.

```
{"StatusCode":200}
```