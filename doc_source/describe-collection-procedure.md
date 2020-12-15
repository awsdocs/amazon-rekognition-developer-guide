# Describing a collection<a name="describe-collection-procedure"></a>

You can use the [DescribeCollection](API_DescribeCollection.md) operation to get the following information about a collection: 
+ The number of faces that are indexed into the collection\.
+ The version of the model that's used by the collection for face detection\. For more information, see [Model versioning](face-detection-model.md)\.
+ The Amazon Resource Name \(ARN\) of the collection\.
+ The creation date and time of the collection\.

**To describe a collection \(SDK\)**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` permissions\. For more information, see [Step 1: Set up an AWS account and create an IAM user](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Use the following examples to call the `DescribeCollection` operation\.

------
#### [ Java ]

   This example describes a collection\.

   Change the value `collectionId` to the ID of the desired collection\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   package com.amazonaws.samples;
   
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.DescribeCollectionRequest;
   import com.amazonaws.services.rekognition.model.DescribeCollectionResult;
   
   
   public class DescribeCollection {
   
      public static void main(String[] args) throws Exception {
   
         String collectionId = "CollectionID";
         
         AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
   
               
         System.out.println("Describing collection: " +
            collectionId );
            
               
           DescribeCollectionRequest request = new DescribeCollectionRequest()
                       .withCollectionId(collectionId);
              
         DescribeCollectionResult describeCollectionResult = rekognitionClient.describeCollection(request); 
         System.out.println("Collection Arn : " +
            describeCollectionResult.getCollectionARN());
         System.out.println("Face count : " +
            describeCollectionResult.getFaceCount().toString());
         System.out.println("Face model version : " +
            describeCollectionResult.getFaceModelVersion());
         System.out.println("Created : " +
            describeCollectionResult.getCreationTimestamp().toString());
   
      } 
   
   }
   ```

------
#### [ AWS CLI ]

   This AWS CLI command displays the JSON output for the `describe-collection` CLI operation\. Change the value of `collection-id` to the ID of the desired collection\.

   ```
   aws rekognition describe-collection --collection-id collectionname 
   ```

------
#### [ Python ]

   This example describes a collection\.

   Change the value `collection_id` to the ID of the desired collection\.

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   from botocore.exceptions import ClientError
   
   def describe_collection(collection_id):
   
       print('Attempting to describe collection ' + collection_id)
       client=boto3.client('rekognition')
   
       try:
           response=client.describe_collection(CollectionId=collection_id)
           print("Collection Arn: "  + response['CollectionARN'])
           print("Face Count: "  + str(response['FaceCount']))
           print("Face Model Version: "  + response['FaceModelVersion'])
           print("Timestamp: "  + str(response['CreationTimestamp']))
   
           
       except ClientError as e:
           if e.response['Error']['Code'] == 'ResourceNotFoundException':
               print ('The collection ' + collection_id + ' was not found ')
           else:
               print ('Error other than Not Found occurred: ' + e.response['Error']['Message'])
       print('Done...')
   
   
   def main():
       collection_id='MyCollection'
       describe_collection(collection_id)
   
   if __name__ == "__main__":
       main()
   ```

------
#### [ \.NET ]

   This example describes a collection\.

   Change the value `collectionId` to the ID of the desired collection\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   using System;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   public class DescribeCollection
   {
       public static void Example()
       {
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           String collectionId = "CollectionID";
           Console.WriteLine("Describing collection: " + collectionId);
   
           DescribeCollectionRequest describeCollectionRequest = new DescribeCollectionRequest()
           {
               CollectionId = collectionId
           };
   
           DescribeCollectionResponse describeCollectionResponse = rekognitionClient.DescribeCollection(describeCollectionRequest);
           Console.WriteLine("Collection ARN: " + describeCollectionResponse.CollectionARN);
           Console.WriteLine("Face count: " + describeCollectionResponse.FaceCount);
           Console.WriteLine("Face model version: " + describeCollectionResponse.FaceModelVersion);
           Console.WriteLine("Created: " + describeCollectionResponse.CreationTimestamp);
       }
   }
   ```

------

## DescribeCollection operation request<a name="describe-collection-request"></a>

The input to `DescribeCollection` is the ID of the desired collection, as shown in the following JSON example\. 

```
{
    "CollectionId": "MyCollection"
}
```

## DescribeCollection operation response<a name="describe-collection-operation-response"></a>

The response includes: 
+ The number of faces that are indexed into the collection, `FaceCount`\.
+ The version of the face model that's used to detect faces, `FaceModelVersion`\.
+ The collection Amazon Resource Name, `CollectionARN`\. 
+ The creation time and date of the collection, `CreationTimestamp`\. The value of `CreationTimestamp` is the number of milliseconds since the Unix epoch time until the creation of the collection\. The Unix epoch time is 00:00:00 Coordinated Universal Time \(UTC\), Thursday, 1 January 1970\. For more information, see [Unix Time](https://en.wikipedia.org/wiki/Unix_time)\.

```
{
    "CollectionARN": "arn:aws:rekognition:us-east-1:nnnnnnnnnnnn:collection/MyCollection",
    "CreationTimestamp": 1.533422155042E9,
    "FaceCount": 200,
    "FaceModelVersion": "1.0"
}
```