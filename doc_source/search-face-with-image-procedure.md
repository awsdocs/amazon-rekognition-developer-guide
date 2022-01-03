# Searching for a face using an image<a name="search-face-with-image-procedure"></a>

You can use the [ SearchFacesByImage ](API_SearchFacesByImage.md) operation to search for faces in a collection that match the largest face in a supplied image\.

For more information, see [Searching for faces within a collection](collections.md#collections-search-faces)\. 



**To search for a face in a collection using an image \(SDK\)**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` and `AmazonS3ReadOnlyAccess` permissions\. For more information, see [Step 1: Set up an AWS account and create an IAM user](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Upload an image \(that contains one or more faces\) to your S3 bucket\. 

   For instructions, see [Uploading Objects into Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service User Guide*\.

1. Use the following examples to call the `SearchFacesByImage` operation\.

------
#### [ Java ]

   This example displays information about faces that match the largest face in an image\. The code example specifies both the `FaceMatchThreshold` and `MaxFaces` parameters to limit the results that are returned in the response\.

   In the following example, change the following: change the value of `collectionId` to the collection you want to search, change the value of `bucket` to the bucket containing the input image, and change the value of `photo` to the input image\. 

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   package aws.example.rekognition.image;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.FaceMatch;
   import com.amazonaws.services.rekognition.model.Image;
   import com.amazonaws.services.rekognition.model.S3Object;
   import com.amazonaws.services.rekognition.model.SearchFacesByImageRequest;
   import com.amazonaws.services.rekognition.model.SearchFacesByImageResult;
   import java.util.List;
   import com.fasterxml.jackson.databind.ObjectMapper;
   
   
   public class SearchFaceMatchingImageCollection {
       public static final String collectionId = "MyCollection";
       public static final String bucket = "bucket";
       public static final String photo = "input.jpg";
         
       public static void main(String[] args) throws Exception {
   
          AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
           
         ObjectMapper objectMapper = new ObjectMapper();
         
          // Get an image object from S3 bucket.
         Image image=new Image()
                 .withS3Object(new S3Object()
                         .withBucket(bucket)
                         .withName(photo));
         
         // Search collection for faces similar to the largest face in the image.
         SearchFacesByImageRequest searchFacesByImageRequest = new SearchFacesByImageRequest()
                 .withCollectionId(collectionId)
                 .withImage(image)
                 .withFaceMatchThreshold(70F)
                 .withMaxFaces(2);
              
          SearchFacesByImageResult searchFacesByImageResult = 
                  rekognitionClient.searchFacesByImage(searchFacesByImageRequest);
   
          System.out.println("Faces matching largest face in image from" + photo);
         List < FaceMatch > faceImageMatches = searchFacesByImageResult.getFaceMatches();
         for (FaceMatch face: faceImageMatches) {
             System.out.println(objectMapper.writerWithDefaultPrettyPrinter()
                     .writeValueAsString(face));
            System.out.println();
         }
      }
   }
   ```

------
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/SearchFaceMatchingImageCollection.java)\.

   ```
       public static void searchFaceInCollection(RekognitionClient rekClient,String collectionId, String sourceImage) {
   
           try {
               InputStream sourceStream = new FileInputStream(new File(sourceImage));
               SdkBytes sourceBytes = SdkBytes.fromInputStream(sourceStream);
   
               Image souImage = Image.builder()
                       .bytes(sourceBytes)
                       .build();
   
               SearchFacesByImageRequest facesByImageRequest = SearchFacesByImageRequest.builder()
                       .image(souImage)
                       .maxFaces(10)
                       .faceMatchThreshold(70F)
                       .collectionId(collectionId)
                       .build();
   
               SearchFacesByImageResponse imageResponse = rekClient.searchFacesByImage(facesByImageRequest) ;
   
               // Display the results.
               System.out.println("Faces matching in the collection");
               List<FaceMatch> faceImageMatches = imageResponse.faceMatches();
               for (FaceMatch face: faceImageMatches) {
                   System.out.println("The similarity level is  "+face.similarity());
                   System.out.println();
               }
           } catch (RekognitionException | FileNotFoundException e) {
               System.out.println(e.getMessage());
               System.exit(1);
           }
       }
   ```

------
#### [ AWS CLI ]

   This AWS CLI command displays the JSON output for the `search-faces-by-image` CLI operation\. Replace the value of `Bucket` with the S3 bucket that you used in step 2\. Replace the value of `Name` with the image file name that you used in step 2\. Replace the value of `collection-id` with the collection you want to search in\.

   ```
   aws rekognition search-faces-by-image \
       --image '{"S3Object":{"Bucket":"bucket-name","Name":"Example.jpg"}}' \
       --collection-id "collection-id"
   ```

------
#### [ Python ]

   This example displays information about faces that match the largest face in an image\. The code example specifies both the `FaceMatchThreshold` and `MaxFaces` parameters to limit the results that are returned in the response\.

   In the following example, change the following: change the value of `collectionId` to the collection you want to search, and replace the values of `bucket` and `photo` with the names of the Amazon S3 bucket and image that you used in Step 2\. 

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   
   if __name__ == "__main__":
   
       bucket='bucket'
       collectionId='MyCollection'
       fileName='input.jpg'
       threshold = 70
       maxFaces=2
   
       client=boto3.client('rekognition')
   
     
       response=client.search_faces_by_image(CollectionId=collectionId,
                                   Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                                   FaceMatchThreshold=threshold,
                                   MaxFaces=maxFaces)
   
                                   
       faceMatches=response['FaceMatches']
       print ('Matching faces')
       for match in faceMatches:
               print ('FaceId:' + match['Face']['FaceId'])
               print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
               print
   ```

------
#### [ \.NET ]

   This example displays information about faces that match the largest face in an image\. The code example specifies both the `FaceMatchThreshold` and `MaxFaces` parameters to limit the results that are returned in the response\.

   In the following example, change the following: change the value of `collectionId` to the collection you want to search, and replace the values of `bucket` and `photo` with the names of the Amazon S3 bucket and image that you used in step 2\. 

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   using System;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   public class SearchFacesMatchingImage
   {
       public static void Example()
       {
           String collectionId = "MyCollection";
           String bucket = "bucket";
           String photo = "input.jpg";
   
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           // Get an image object from S3 bucket.
           Image image = new Image()
           {
               S3Object = new S3Object()
               {
                   Bucket = bucket,
                   Name = photo
               }
           };
   
           SearchFacesByImageRequest searchFacesByImageRequest = new SearchFacesByImageRequest()
           {
               CollectionId = collectionId,
               Image = image,
               FaceMatchThreshold = 70F,
               MaxFaces = 2
           };
   
           SearchFacesByImageResponse searchFacesByImageResponse = rekognitionClient.SearchFacesByImage(searchFacesByImageRequest);
   
           Console.WriteLine("Faces matching largest face in image from " + photo);
           foreach (FaceMatch face in searchFacesByImageResponse.FaceMatches)
               Console.WriteLine("FaceId: " + face.Face.FaceId + ", Similarity: " + face.Similarity);
       }
   }
   ```

------

## SearchFacesByImage operation request<a name="searchfacesbyimage-operation-request"></a>

The input parameters to `SearchFacesImageByImage` are the collection to search in and the source image location\. In this example, the source image is stored in an Amazon S3 bucket \(`S3Object`\)\. Also specified are the maximum number of faces to return \(`Maxfaces`\) and the minimum confidence that must be matched for a face to be returned \(`FaceMatchThreshold`\)\.

```
{
    "CollectionId": "MyCollection",
    "Image": {
        "S3Object": {
            "Bucket": "bucket",
            "Name": "input.jpg"
        }
    },
    "MaxFaces": 2,
    "FaceMatchThreshold": 70
}
```

## SearchFacesByImage operation response<a name="searchfacesbyimage-operation-response"></a>

Given an input image \(\.jpeg or \.png\), the operation first detects the face in the input image, and then searches the specified face collection for similar faces\. 

**Note**  
If the service detects multiple faces in the input image, it uses the largest face that's detected for searching the face collection\.

The operation returns an array of face matches that were found, and information about the input face\. This includes information such as the bounding box, along with the confidence value, which indicates the level of confidence that the bounding box contains a face\. 

By default, `SearchFacesByImage` returns faces for which the algorithm detects similarity of greater than 80%\. The similarity indicates how closely the face matches with the input face\. Optionally, you can use `FaceMatchThreshold` to specify a different value\. For each face match found, the response includes similarity and face metadata, as shown in the following example response: 

```
{
    "FaceMatches": [
        {
            "Face": {
                "BoundingBox": {
                    "Height": 0.06333330273628235,
                    "Left": 0.1718519926071167,
                    "Top": 0.7366669774055481,
                    "Width": 0.11061699688434601
                },
                "Confidence": 100,
                "ExternalImageId": "input.jpg",
                "FaceId": "578e2e1b-d0b0-493c-aa39-ba476a421a34",
                "ImageId": "9ba38e68-35b6-5509-9d2e-fcffa75d1653"
            },
            "Similarity": 99.9764175415039
        }
    ],
    "FaceModelVersion": "3.0",
    "SearchedFaceBoundingBox": {
        "Height": 0.06333333253860474,
        "Left": 0.17185185849666595,
        "Top": 0.7366666793823242,
        "Width": 0.11061728745698929
    },
    "SearchedFaceConfidence": 99.99999237060547
}
```