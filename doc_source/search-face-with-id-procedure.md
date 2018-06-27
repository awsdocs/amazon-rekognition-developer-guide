# Searching for a Face Using Its Face ID<a name="search-face-with-id-procedure"></a>

You can use the [SearchFaces](API_SearchFaces.md) operation to search for faces in a collection that match a supplied face ID\.

The face ID is returned in the [IndexFaces](API_IndexFaces.md) operation response when the face is detected and added to a collection\. For more information, see [Managing Faces in a Collection](collections.md#collections-index-faces)\.

**To search for a face in a collection using its face ID \(SDK\)**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` permissions\. For more information, see [Step 1: Set Up an AWS Account and Create an IAM User](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Use the following examples to call the `SearchFaces` operation\.

------
#### [ Java ]

   This example displays information about faces that match a face identified by its ID\.

   Change the value of `collectionID` to the collection that contains the required face\. Change the value of `faceId` to the identifier of the face you want to find\.

   ```
   
   package aws.example.rekognition.image;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.fasterxml.jackson.databind.ObjectMapper;
   import com.amazonaws.services.rekognition.model.FaceMatch;
   import com.amazonaws.services.rekognition.model.SearchFacesRequest;
   import com.amazonaws.services.rekognition.model.SearchFacesResult;
   import java.util.List;
   
   
     public class SearchFaceMatchingIdCollection {
         public static final String collectionId = "MyCollection";
         public static final String faceId = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx";
         
       public static void main(String[] args) throws Exception {
           
           AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
         
           ObjectMapper objectMapper = new ObjectMapper();
         // Search collection for faces matching the face id.
         
         SearchFacesRequest searchFacesRequest = new SearchFacesRequest()
                 .withCollectionId(collectionId)
                 .withFaceId(faceId)
                 .withFaceMatchThreshold(70F)
                 .withMaxFaces(2);
              
          SearchFacesResult searchFacesByIdResult = 
                  rekognitionClient.searchFaces(searchFacesRequest);
   
          System.out.println("Face matching faceId " + faceId);
         List < FaceMatch > faceImageMatches = searchFacesByIdResult.getFaceMatches();
         for (FaceMatch face: faceImageMatches) {
            System.out.println(objectMapper.writerWithDefaultPrettyPrinter()
                    .writeValueAsString(face));
            
            System.out.println();
         }
       }
   
   }
   ```

   Run the example code\. Information about matching faces is displayed\.

------
#### [ AWS CLI ]

   This AWS CLI command displays the JSON output for the `search-faces` CLI operation\. Replace the value of `face-id` with the face identifier that you want to search for, and replace the value of `collection-id` with the collection you want to search in\.

   ```
   aws rekognition search-faces \
       --face-id face-id \
       --collection-id "collection-id"
   ```

------
#### [ Python ]

   This example displays information about faces that match a face identified by its ID\.

   Change the value of `collectionID` to the collection that contains the required face\. Change the value of `faceId` to the identifier of the face you want to find\.

   ```
   import boto3
   
   if __name__ == "__main__":
   
       bucket='bucket'
       collectionId='MyCollection'
       threshold = 50
       maxFaces=2
       faceId='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
   
       client=boto3.client('rekognition')
   
     
       response=client.search_faces(CollectionId=collectionId,
                                   FaceId=faceId,
                                   FaceMatchThreshold=threshold,
                                   MaxFaces=maxFaces)
   
                           
       faceMatches=response['FaceMatches']
       print 'Matching faces'
       for match in faceMatches:
               print 'FaceId:' + match['Face']['FaceId']
               print 'Similarity: ' + "{:.2f}".format(match['Similarity']) + "%"
               print
   ```

------
#### [ \.NET ]

   This example displays information about faces that match a face identified by its ID\.

   Change the value of `collectionID` to the collection that contains the required face\. Change the value of `faceId` to the identifier of the face that you want to find\.

   ```
   using System;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   public class SearchFacesMatchingId
   {
       public static void Example()
       {
           String collectionId = "MyCollection";
           String faceId = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx";
   
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           // Search collection for faces matching the face id.
   
           SearchFacesRequest searchFacesRequest = new SearchFacesRequest()
           {
               CollectionId = collectionId,
               FaceId = faceId,
               FaceMatchThreshold = 70F,
               MaxFaces = 2
           };
   
           SearchFacesResponse searchFacesResponse = rekognitionClient.SearchFaces(searchFacesRequest);
   
           Console.WriteLine("Face matching faceId " + faceId);
   
           Console.WriteLine("Matche(s): ");
           foreach (FaceMatch face in searchFacesResponse.FaceMatches)
               Console.WriteLine("FaceId: " + face.Face.FaceId + ", Similarity: " + face.Similarity);
       }
   }
   ```

   Run the example code\. Information about matching faces is displayed\.

------

## SearchFaces Operation Request<a name="searchfaces-operation-request"></a>

Given a face ID \(each face stored in the face collection has a face ID\), `SearchFaces` searches the specified face collection for similar faces\. The response doesn't include the face you are searching for\. It includes only similar faces\. By default, `SearchFaces` returns faces for which the algorithm detects similarity of greater than 80%\. The similarity indicates how closely the face matches with the input face\. Optionally, you can use `FaceMatchThreshold` to specify a different value\. 

```
{
    "CollectionId": "MyCollection",
    "FaceId": "0b683aed-a0f1-48b2-9b5e-139e9cc2a757",
    "MaxFaces": 2,
    "FaceMatchThreshold": 70
}
```

## SearchFaces Operation Response<a name="searchfaces-operation-response"></a>

The operation returns an array of face matches that were found and the face ID you provided as input\.

```
{
    "SearchedFaceId": "7ecf8c19-5274-5917-9c91-1db9ae0449e2",
    "FaceMatches": [ list of face matches found ]
}
```

For each face match that was found, the response includes similarity and face metadata, as shown in the following example response: 

```
{
   ...
    "FaceMatches": [
        {
            "Similarity": 100.0,
            "Face": {
                "BoundingBox": {
                    "Width": 0.6154,
                    "Top": 0.2442,
                    "Left": 0.1765,
                    "Height": 0.4692
                },
                "FaceId": "84de1c86-5059-53f2-a432-34ebb704615d",
                "Confidence": 99.9997,
                "ImageId": "d38ebf91-1a11-58fc-ba42-f978b3f32f60"
            }
        },
        {
            "Similarity": 84.6859,
            "Face": {
                "BoundingBox": {
                    "Width": 0.2044,
                    "Top": 0.2254,
                    "Left": 0.4622,
                    "Height": 0.3119
                },
                "FaceId": "6fc892c7-5739-50da-a0d7-80cc92c0ba54",
                "Confidence": 99.9981,
                "ImageId": "5d913eaf-cf7f-5e09-8c8f-cb1bdea8e6aa"
            }
        }
    ]
}
```