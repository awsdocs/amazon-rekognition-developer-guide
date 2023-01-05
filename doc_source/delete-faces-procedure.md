# Deleting faces from a collection<a name="delete-faces-procedure"></a>

You can use the [DeleteFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteFaces.html) operation to delete faces from a collection\. For more information, see [Managing faces in a collection](collections.md#collections-index-faces)\. 



**To delete faces from a collection**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` permissions\. For more information, see [Step 1: Set up an AWS account and create an IAM user](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Use the following examples to call the `DeleteFaces` operation\.

------
#### [ Java ]

   This example deletes a single face from a collection\.

   Change the value of `collectionId` to the collection that contains the face that you want to delete\. Change the value of `faces` to the ID of the face that you want to delete\. To delete multiple faces, add the face IDs to the `faces` array\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   package aws.example.rekognition.image;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.DeleteFacesRequest;
   import com.amazonaws.services.rekognition.model.DeleteFacesResult;
   
   import java.util.List;
   
   
   public class DeleteFacesFromCollection {
      public static final String collectionId = "MyCollection";
      public static final String faces[] = {"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"};
   
      public static void main(String[] args) throws Exception {
         
         AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
        
         
         DeleteFacesRequest deleteFacesRequest = new DeleteFacesRequest()
                 .withCollectionId(collectionId)
                 .withFaceIds(faces);
        
         DeleteFacesResult deleteFacesResult=rekognitionClient.deleteFaces(deleteFacesRequest);
         
        
         List < String > faceRecords = deleteFacesResult.getDeletedFaces();
         System.out.println(Integer.toString(faceRecords.size()) + " face(s) deleted:");
         for (String face: faceRecords) {
            System.out.println("FaceID: " + face);
         }
      }
   }
   ```

------
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/DeleteFacesFromCollection.java)\.

   ```
       public static void deleteFacesCollection(RekognitionClient rekClient,
                                                String collectionId,
                                                String faceId) {
   
           try {
               DeleteFacesRequest deleteFacesRequest = DeleteFacesRequest.builder()
                   .collectionId(collectionId)
                   .faceIds(faceId)
                   .build();
   
               rekClient.deleteFaces(deleteFacesRequest);
               System.out.println("The face was deleted from the collection.");
   
           } catch(RekognitionException e) {
               System.out.println(e.getMessage());
               System.exit(1);
           }
       }
   ```

------
#### [ AWS CLI ]

   This AWS CLI command displays the JSON output for the `delete-faces` CLI operation\. Replace the value of `collection-id` with the name of the collection that contains the face you want to delete\. Replace the value of `face-ids` with an array of face IDs that you want to delete\.

   ```
   aws rekognition delete-faces --collection-id "collectionname" --face-ids '["faceid"]'
   ```

------
#### [ Python ]

   This example deletes a single face from a collection\.

   Change the value of `collectionId` to the collection that contains the face that you want to delete\. Change the value of `faces` to the ID of the face that you want to delete\. To delete multiple faces, add the face IDs to the `faces` array\.

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   
   def delete_faces_from_collection(collection_id, faces):
   
       client=boto3.client('rekognition')
   
       response=client.delete_faces(CollectionId=collection_id,
                                  FaceIds=faces)
       
       print(str(len(response['DeletedFaces'])) + ' faces deleted:') 							
       for faceId in response['DeletedFaces']:
            print (faceId)
       return len(response['DeletedFaces'])
   
   def main():
   
       collection_id='collection'
       faces=[]
       faces.append("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
   
       faces_count=delete_faces_from_collection(collection_id, faces)
       print("deleted faces count: " + str(faces_count))
   
   if __name__ == "__main__":
       main()
   ```

------
#### [ \.NET ]

   This example deletes a single face from a collection\.

   Change the value of `collectionId` to the collection that contains the face that you want to delete\. Change the value of `faces` to the ID of the face that you want to delete\. To delete multiple faces, add the face IDs to the `faces` list\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   using System;
   using System.Collections.Generic;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   public class DeleteFaces
   {
       public static void Example()
       {
           String collectionId = "MyCollection";
           List<String> faces = new List<String>() { "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" };
   
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           DeleteFacesRequest deleteFacesRequest = new DeleteFacesRequest()
           {
               CollectionId = collectionId,
               FaceIds = faces
           };
   
           DeleteFacesResponse deleteFacesResponse = rekognitionClient.DeleteFaces(deleteFacesRequest);
           foreach (String face in deleteFacesResponse.DeletedFaces)
               Console.WriteLine("FaceID: " + face);
       }
   }
   ```

------

## DeleteFaces operation request<a name="deletefaces-request"></a>

The input to `DeleteFaces` is the ID of the collection that contains the faces, and an array of face IDs for the faces to be deleted\. 

```
{
    "CollectionId": "MyCollection",
    "FaceIds": [
        "daf29cac-f910-41e9-851f-6eeb0e08f973"
    ]
}
```

## DeleteFaces operation response<a name="deletefaces-operation-response"></a>

The `DeleteFaces` response contains an array of face IDs for the faces that were deleted\.

```
{
    "DeletedFaces": [
        "daf29cac-f910-41e9-851f-6eeb0e08f973"
    ]
}
```