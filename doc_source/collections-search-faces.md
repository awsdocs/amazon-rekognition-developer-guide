# Searching for Faces with Rekognition Image Collection<a name="collections-search-faces"></a>

After you create a face collection and store faces, you can search a face collection for face matches\. For more information about storing faces in a face collection, see [Managing Collections](managing-collections.md) and [Storing Faces in a Face Collection](collections-index-faces.md)\. With Amazon Rekognition, you can do the following:
+ **Search a face collection given an image \([SearchFacesByImage](API_SearchFacesByImage.md)\)** – For a given input image \(\.jpeg or \.png\), the operation first detects the face in the input image, and then searches the specified face collection for similar faces\. 
**Note**  
If the service detects multiple faces in the input image, it uses the largest face detected for searching the face collection\.

  The operation returns an array of face matches found, and information about the input face \(such as the bounding box, along with the confidence value that indicates the level of confidence that the bounding box contains a face\)\. 

  ```
  {
      "SearchedFaceBoundingBox": {
          "Width": 0.6154,
          "Top": 0.2442,
          "Left": 0.1765,
          "Height": 0.4692
      },
      "SearchedFaceConfidence": 99.9997,
      "FaceMatches": [ list of face matches found ]
  }
  ```
+ **Search a face collection given a face ID \([SearchFaces](API_SearchFaces.md)\) ** – Given a face ID \(each face stored in the face collection has a face ID\), `SearchFaces` searches the specified face collection for similar faces\. The response doesn't include the face you are searching for, it includes only similar faces\. 

  The operation returns an array of face matches found and the face ID you provided as input\.

  ```
  {
      "SearchedFaceId": "7ecf8c19-5274-5917-9c91-1db9ae0449e2",
      "FaceMatches": [ list of face matches found ]
  }
  ```

  For example, the `SearchFacesByImage` API performs a search using the largest face in the input image\. If you want to search for other faces in the input image, you might first index all faces using the `IndexFaces` API\. You get a face ID in response\. You can then use `SearchFaces` API to search for faces using the face IDs\.

   

By default, both of these operations return faces for which the algorithm detects similarity of greater than 80%\. The similarity indicates how closely the face matches with the input face\. Optionally, you can use `FaceMatchThreshold` to specify a different value\. For each face match found, the response includes similarity and face metadata as shown in the following example response: 

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

The `CompareFaces` operation and the two search faces operations differ as follows:
+ The `CompareFaces` operation compares a face in a source image with faces in the target image\. The scope of this comparison is limited to the faces detected in the target image\. For more information, see [Compare Faces in Images](faces.md#faces-comparefaces)\.
+ `SearchFaces` and `SearchFacesByImage` compare a face \(identified either by a `FaceId` or an input image\) with all faces in a given face collection\. Therefore, the scope of this search is much larger\. Also, because the facial feature information is persisted for faces already stored in the face collection, you can search for matching faces multiple times\.