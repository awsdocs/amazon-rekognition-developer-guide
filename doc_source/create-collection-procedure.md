# Creating a collection<a name="create-collection-procedure"></a>

You can use the [ CreateCollection ](API_CreateCollection.md) operation to create a collection\.

For more information, see [Managing collections](collections.md#managing-collections)\. 

**To create a collection \(SDK\)**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` permissions\. For more information, see [Step 1: Set up an AWS account and create an IAM user](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Use the following examples to call the `CreateCollection` operation\.

------
#### [ Java ]

   The following example creates a collection and displays its Amazon Resource Name \(ARN\)\.

   Change the value of `collectionId` to the name of the collection you want to create\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
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
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/CreateCollection.java)\.

   ```
       public static void createMyCollection(RekognitionClient rekClient,String collectionId ) {
   
           try {
               CreateCollectionRequest collectionRequest = CreateCollectionRequest.builder()
                       .collectionId(collectionId)
                       .build();
   
               CreateCollectionResponse collectionResponse = rekClient.createCollection(collectionRequest);
               System.out.println("CollectionArn : " +
                       collectionResponse.collectionArn());
               System.out.println("Status code : " +
                       collectionResponse.statusCode().toString());
   
           } catch(RekognitionException e) {
                   System.out.println(e.getMessage());
                   System.exit(1);
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

   Change the value of `collection_id` to the name of collection you want to create\.

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   
   def create_collection(collection_id):
   
       client=boto3.client('rekognition')
   
       #Create a collection
       print('Creating collection:' + collection_id)
       response=client.create_collection(CollectionId=collection_id)
       print('Collection ARN: ' + response['CollectionArn'])
       print('Status code: ' + str(response['StatusCode']))
       print('Done...')
       
   def main():
       collection_id='Collection'
       create_collection(collection_id)
   
   if __name__ == "__main__":
       main()
   ```

------
#### [ \.NET ]

   The following example creates a collection and displays its Amazon Resource Name \(ARN\)\.

   Change the value of `collectionId` to the name of collection you want to create\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
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

## CreateCollection operation request<a name="createcollection-request"></a>

The input to `CreationCollection` is the name of the collection that you want to create\.

```
{
    "CollectionId": "MyCollection"
}
```

## CreateCollection operation response<a name="createcollection-operation-response"></a>

Amazon Rekognition creates the collection and returns the Amazon Resource Name \(ARN\) of the newly created collection\.

```
{
   "CollectionArn": "aws:rekognition:us-east-1:acct-id:collection/examplecollection",
   "StatusCode": 200
}
```