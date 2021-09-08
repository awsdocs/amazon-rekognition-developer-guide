# Listing faces in a collection<a name="list-faces-in-collection-procedure"></a>

You can use the [ ListFaces ](API_ListFaces.md) operation to list the faces in a collection\.

For more information, see [Managing faces in a collection](collections.md#collections-index-faces)\. 



**To list faces in a collection \(SDK\)**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` permissions\. For more information, see [Step 1: Set up an AWS account and create an IAM user](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Use the following examples to call the `ListFaces` operation\.

------
#### [ Java ]

   This example displays a list of faces in a collection\.

   Change the value of `collectionId` to the desired collection\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   package aws.example.rekognition.image;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.Face;
   import com.amazonaws.services.rekognition.model.ListFacesRequest;
   import com.amazonaws.services.rekognition.model.ListFacesResult;
   import java.util.List;
   import com.fasterxml.jackson.databind.ObjectMapper;
   
   
   
   public class ListFacesInCollection {
       public static final String collectionId = "MyCollection";
   
      public static void main(String[] args) throws Exception {
         
         AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
   
         ObjectMapper objectMapper = new ObjectMapper();
   
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
           
            listFacesResult =  rekognitionClient.listFaces(listFacesRequest);
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

------
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/ListFacesInCollection.java)\.

   ```
       public static void listFacesCollection(RekognitionClient rekClient, String collectionId ) {
   
           try {
               ListFacesRequest facesRequest = ListFacesRequest.builder()
                   .collectionId(collectionId)
                   .maxResults(10)
                   .build();
   
               ListFacesResponse facesResponse = rekClient.listFaces(facesRequest);
   
               // For each face in the collection, print out the confidence level and face id value.
               List<Face> faces = facesResponse.faces();
               for (Face face: faces) {
                   System.out.println("Confidence level there is a face: "+face.confidence());
                   System.out.println("The face Id value is "+face.faceId());
               }
   
           } catch (RekognitionException e) {
               System.out.println(e.getMessage());
               System.exit(1);
            }
         }
   ```

------
#### [ AWS CLI ]

   This AWS CLI command displays the JSON output for the `list-faces` CLI operation\. Replace the value of `collection-id` with the name of the collection you want to list\.

   ```
   aws rekognition list-faces \
         --collection-id "collection-id"
   ```

------
#### [ Python ]

   This example displays a list of faces in a collection\.

   Change the value of `collectionId` to the desired collection\.

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   
   def list_faces_in_collection(collection_id):
   
   
       maxResults=2
       faces_count=0
       tokens=True
   
       client=boto3.client('rekognition')
       response=client.list_faces(CollectionId=collection_id,
                                  MaxResults=maxResults)
   
       print('Faces in collection ' + collection_id)
   
    
       while tokens:
   
           faces=response['Faces']
   
           for face in faces:
               print (face)
               faces_count+=1
           if 'NextToken' in response:
               nextToken=response['NextToken']
               response=client.list_faces(CollectionId=collection_id,
                                          NextToken=nextToken,MaxResults=maxResults)
           else:
               tokens=False
       return faces_count   
   def main():
   
       collection_id='collection'
   
       faces_count=list_faces_in_collection(collection_id)
       print("faces count: " + str(faces_count))
   if __name__ == "__main__":
       main()
   ```

------
#### [ \.NET ]

   This example displays a list of faces in a collection\.

   Change the value of `collectionId` to the desired collection\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   using System;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   public class ListFaces
   {
       public static void Example()
       {
           String collectionId = "MyCollection";
   
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           ListFacesResponse listFacesResponse = null;
           Console.WriteLine("Faces in collection " + collectionId);
   
           String paginationToken = null;
           do
           {
               if (listFacesResponse != null)
                   paginationToken = listFacesResponse.NextToken;
   
               ListFacesRequest listFacesRequest = new ListFacesRequest()
               {
                   CollectionId = collectionId,
                   MaxResults = 1,
                   NextToken = paginationToken
               };
   
               listFacesResponse = rekognitionClient.ListFaces(listFacesRequest);
               foreach(Face face in listFacesResponse.Faces)
                   Console.WriteLine(face.FaceId);
           } while (listFacesResponse != null && !String.IsNullOrEmpty(listFacesResponse.NextToken));
       }
   }
   ```

------

## ListFaces operation request<a name="listfaces-request"></a>

The input to `ListFaces` is the ID of the collection that you want to list faces for\. `MaxResults` is the maximum number of faces to return\. 

```
{
    "CollectionId": "MyCollection",
    "MaxResults": 1
}
```

If the response has more faces than are requested by `MaxResults`, a token is returned that you can use to get the next set of results, in a subsequent call to `ListFaces`\. For example:

```
{
    "CollectionId": "MyCollection",
    "NextToken": "sm+5ythT3aeEVIR4WA....",
    "MaxResults": 1
}
```

## ListFaces operation response<a name="listfaces-response"></a>

The response from `ListFaces` is information about the face metadata that's stored in the specified collection\.
+ **FaceModelVersion** – The version of the face model that's associated with the collection\. For more information, see [Model versioning](face-detection-model.md)\.
+  **Faces** – Information about the faces in the collection\. This includes information about [ BoundingBox ](API_BoundingBox.md), confidence, image identifiers, and the face ID\. For more information, see [ Face ](API_Face.md)\. 
+  **NextToken** – The token that's used to get the next set of results\. 

```
{
    "FaceModelVersion": "3.0",
    "Faces": [
        {
            "BoundingBox": {
                "Height": 0.06333330273628235,
                "Left": 0.1718519926071167,
                "Top": 0.7366669774055481,
                "Width": 0.11061699688434601
            },
            "Confidence": 100,
            "ExternalImageId": "input.jpg",
            "FaceId": "0b683aed-a0f1-48b2-9b5e-139e9cc2a757",
            "ImageId": "9ba38e68-35b6-5509-9d2e-fcffa75d1653"
        }
    ],
    "NextToken": "sm+5ythT3aeEVIR4WA...."
}
```