# Adding Faces to a Collection<a name="add-faces-to-collection-procedure"></a>

You can use the [IndexFaces](API_IndexFaces.md) operation to detect faces in an image and add them to a collection\. For each face detected, Amazon Rekognition extracts facial features and stores the feature information in a database\. In addition, the command stores metadata for each face that's detected in the specified face collection\. Amazon Rekognition doesn't store the actual image bytes\.

For information about providing suitable faces for indexing, see [Recommendations for Facial Recognition Input Images](recommendations-facial-input-images.md)\.

For each face, the `IndexFaces` operation persists the following information:
+ **Multidimensional facial features** – `IndexFaces` uses facial analysis to extract multidimensional information about the facial features and stores the information in the face collection\. You can't access this information directly\. However, Amazon Rekognition uses this information when it searches a face collection for face matches\.

   
+ **Metadata** – The metadata for each face includes a bounding box, confidence level \(that the bounding box contains a face\), IDs assigned by Amazon Rekognition \(face ID and image ID\), and an external image ID \(if you provided it\) in the request\. This information is returned to you in response to the `IndexFaces` API call\. For an example, see the `face` element in the following example response\.

  The service returns this metadata in response to the following API calls:

   
  +  `[ListFaces](API_ListFaces.md)` 
  + Search faces operations – The responses for [SearchFaces](API_SearchFaces.md) and [SearchFacesByImage](API_SearchFacesByImage.md) return the confidence in the match for each matching face, along with this metadata of the matched face\.

The number of faces indexed by `IndexFaces` depends on the version of the face detection model that's associated with the input collection\. For more information, see [Model Versioning](face-detection-model.md)\. 

Information about indexed faces is returned in an array of [FaceRecord](API_FaceRecord.md) objects\.

You might want to associate indexed faces with the image they were detected in\. For example, you might want to maintain a client\-side index of images and faces in the images\. To associate faces with an image, specify an image ID in the `ExternalImageId` request parameter\. The image ID can be the file name or another ID that you create\.

In addition to the preceding information that the API persists in the face collection, the API also returns face details that aren't persisted in the collection\. \(See the `faceDetail` element in the following example response\)\. 

**Note**  
`DetectFaces` returns the same information, so you don't need to call both `DetectFaces` and `IndexFaces` for the same image\. 

## Filtering Faces<a name="index-faces-filtering"></a>

The IndexFaces operation enables you to filter the faces that are indexed from an image\. With `IndexFaces` you can specify a maximum number of faces to index, or you can choose to only index faces detected with a high quality\. 

You can specify the maximum number of faces that are indexed by `IndexFaces` by using the `MaxFaces` input parameter\. This is useful when you want to index the largest faces in an image and don't want to index smaller faces, such as faces of people standing in the background\.

By default, `IndexFaces` filters out faces that are detected with low quality\. You can explicitly choose to filter out low quality faces by specifying `AUTO` for the value of the `QualityFilter` input parameter\. If you don't want to filter faces based on quality, specify `NONE` for `QualityFilter`\. `IndexFaces` filters low\-quality faces for the following reasons:
+ The face is too small compared to the image dimensions\.
+ The face is too blurry\.
+ The image is too dark\.
+ The face has an extreme pose\.

**Note**  
To use quality filtering, you need a collection that's associated with version 3 of the face model\. To get the version of the face model associated with a collection, call [DescribeCollection](API_DescribeCollection.md)\. 

Information about faces that aren't indexed by `IndexFaces` is returned in an array of [UnindexedFace](API_UnindexedFace.md) objects\. The `Reasons` array contains a list of reasons why a face isn't indexed\. For example, a value of `EXCEEDS_MAX_FACES` is a face that's not indexed because the number of faces specified by `MaxFaces` has already been detected\. 

For more information, see [Managing Faces in a Collection](collections.md#collections-index-faces)\. 

**To add faces to a collection \(SDK\)**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` and `AmazonS3ReadOnlyAccess` permissions\. For more information, see [Step 1: Set Up an AWS Account and Create an IAM User](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Upload an image \(containing one or more faces\) to your Amazon S3 bucket\. 

   For instructions, see [Uploading Objects into Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. Use the following examples to call the `IndexFaces` operation\.

------
#### [ Java ]

   This example displays the face identifiers for faces added to the collection\.

   Change the value of `collectionId` to the name of the collection that you want to add a face to\. Replace the values of `bucket` and `photo` with the names of the Amazon S3 bucket and image that you used in step 2\. The `.withMaxFaces(1)` parameter restricts the number of indexed faces to 1\. Remove or change its value to suit your needs\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   package aws.example.rekognition.image;
   
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.FaceRecord;
   import com.amazonaws.services.rekognition.model.Image;
   import com.amazonaws.services.rekognition.model.IndexFacesRequest;
   import com.amazonaws.services.rekognition.model.IndexFacesResult;
   import com.amazonaws.services.rekognition.model.QualityFilter;
   import com.amazonaws.services.rekognition.model.S3Object;
   import com.amazonaws.services.rekognition.model.UnindexedFace;
   import java.util.List;
   
   public class AddFacesToCollection {
       public static final String collectionId = "MyCollection";
       public static final String bucket = "bucket";
       public static final String photo = "input.jpg";
   
       public static void main(String[] args) throws Exception {
   
           AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
   
           Image image = new Image()
                   .withS3Object(new S3Object()
                   .withBucket(bucket)
                   .withName(photo));
           
           IndexFacesRequest indexFacesRequest = new IndexFacesRequest()
                   .withImage(image)
                   .withQualityFilter(QualityFilter.AUTO)
                   .withMaxFaces(1)
                   .withCollectionId(collectionId)
                   .withExternalImageId(photo)
                   .withDetectionAttributes("DEFAULT");
   
           IndexFacesResult indexFacesResult = rekognitionClient.indexFaces(indexFacesRequest);
           
           System.out.println("Results for " + photo);
           System.out.println("Faces indexed:");
           List<FaceRecord> faceRecords = indexFacesResult.getFaceRecords();
           for (FaceRecord faceRecord : faceRecords) {
               System.out.println("  Face ID: " + faceRecord.getFace().getFaceId());
               System.out.println("  Location:" + faceRecord.getFaceDetail().getBoundingBox().toString());
           }
           
           List<UnindexedFace> unindexedFaces = indexFacesResult.getUnindexedFaces();
           System.out.println("Faces not indexed:");
           for (UnindexedFace unindexedFace : unindexedFaces) {
               System.out.println("  Location:" + unindexedFace.getFaceDetail().getBoundingBox().toString());
               System.out.println("  Reasons:");
               for (String reason : unindexedFace.getReasons()) {
                   System.out.println("   " + reason);
               }
           }
       }
   }
   ```

------
#### [ AWS CLI ]

   This AWS CLI command displays the JSON output for the `index-faces` CLI operation\. 

   Replace the value of `collection-id` with the name of the collection you want the face to be stored in\. Replace the values of `Bucket` and `Name` with the Amazon S3 bucket and image file that you used in step 2\. The `max-faces` parameter restricts the number of indexed faces to 1\. Remove or change its value to suit your needs\.

   ```
   aws rekognition index-faces \
         --image '{"S3Object":{"Bucket":"bucket-name","Name":"file-name"}}' \
         --collection-id "collection-id" \
         --max-faces 1 \
         --quality-filter "AUTO" \
         --detection-attributes "ALL" \
         --external-image-id "example-image.jpg"
   ```

------
#### [ Python ]

   This example displays the face identifiers for faces added to the collection\.

   Change the value of `collectionId` to the name of the collection that you want to add a face to\. Replace the values of `bucket` and `photo` with the names of the Amazon S3 bucket and image that you used in step 2\. The `MaxFaces` input parameter restricts the number of indexed faces to 1\. Remove or change its value to suit your needs\.

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   
   if __name__ == "__main__":
   
       bucket='bucket'
       collectionId='MyCollection'
       photo='photo'
       
       client=boto3.client('rekognition')
   
       response=client.index_faces(CollectionId=collectionId,
                                   Image={'S3Object':{'Bucket':bucket,'Name':photo}},
                                   ExternalImageId=photo,
                                   MaxFaces=1,
                                   QualityFilter="AUTO",
                                   DetectionAttributes=['ALL'])
   
       print ('Results for ' + photo) 	
       print('Faces indexed:')						
       for faceRecord in response['FaceRecords']:
            print('  Face ID: ' + faceRecord['Face']['FaceId'])
            print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))
   
       print('Faces not indexed:')
       for unindexedFace in response['UnindexedFaces']:
           print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
           print(' Reasons:')
           for reason in unindexedFace['Reasons']:
               print('   ' + reason)
   ```

------
#### [ \.NET ]

   This example displays the face identifiers for faces added to the collection\.

   Change the value of `collectionId` to the name of the collection that you want to add a face to\. Replace the values of `bucket` and `photo` with the names of the Amazon S3 bucket and image that you used in step 2\. 

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   using System;
   using System.Collections.Generic;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   public class AddFaces
   {
       public static void Example()
       {
           String collectionId = "MyCollection";
           String bucket = "bucket";
           String photo = "input.jpg";
   
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           Image image = new Image()
           {
               S3Object = new S3Object()
               {
                   Bucket = bucket,
                   Name = photo
               }
           };
   
           IndexFacesRequest indexFacesRequest = new IndexFacesRequest()
           {
               Image = image,
               CollectionId = collectionId,
               ExternalImageId = photo,
               DetectionAttributes = new List<String>(){ "ALL" }
           };
   
           IndexFacesResponse indexFacesResponse = rekognitionClient.IndexFaces(indexFacesRequest);
   
           Console.WriteLine(photo + " added");
           foreach (FaceRecord faceRecord in indexFacesResponse.FaceRecords)
               Console.WriteLine("Face detected: Faceid is " +
                  faceRecord.Face.FaceId);
       }
   }
   ```

------

## IndexFaces Operation Request<a name="indexfaces-request"></a>

The input to `IndexFaces` is the image to be indexed and the collection to add the face or faces to\. 

```
{
    "CollectionId": "MyCollection",
    "Image": {
        "S3Object": {
            "Bucket": "bucket",
            "Name": "input.jpg"
        }
    },
    "ExternalImageId": "input.jpg",
    "DetectionAttributes": [
        "DEFAULT"
    ],
    "MaxFaces": 1,
    "QualityFilter": "AUTO"
}
```

## IndexFaces Operation Response<a name="indexfaces-operation-response"></a>

`IndexFaces` returns information about the faces that were detected in the image\. For example, the following JSON response includes the default detection attributes for faces detected in the input image\. The example also shows faces not indexed because the value of the `MaxFaces` input parameter has been exceeded — the `Reasons` array contains *EXCEEDS\_MAX\_FACES*\. If a face is not indexed for quality reasons, `Reasons` contains values such as *LOW\_SHARPNESS* or *LOW\_BRIGHTNESS*\. For more information, see [UnindexedFace](API_UnindexedFace.md)\.

```
{
    "FaceModelVersion": "3.0",
    "FaceRecords": [
        {
            "Face": {
                "BoundingBox": {
                    "Height": 0.3247932195663452,
                    "Left": 0.5055555701255798,
                    "Top": 0.2743072211742401,
                    "Width": 0.21444444358348846
                },
                "Confidence": 99.99998474121094,
                "ExternalImageId": "input.jpg",
                "FaceId": "b86e2392-9da1-459b-af68-49118dc16f87",
                "ImageId": "09f43d92-02b6-5cea-8fbd-9f187db2050d"
            },
            "FaceDetail": {
                "BoundingBox": {
                    "Height": 0.3247932195663452,
                    "Left": 0.5055555701255798,
                    "Top": 0.2743072211742401,
                    "Width": 0.21444444358348846
                },
                "Confidence": 99.99998474121094,
                "Landmarks": [
                    {
                        "Type": "eyeLeft",
                        "X": 0.5751981735229492,
                        "Y": 0.4010535478591919
                    },
                    {
                        "Type": "eyeRight",
                        "X": 0.6511467099189758,
                        "Y": 0.4017036259174347
                    },
                    {
                        "Type": "nose",
                        "X": 0.6314528584480286,
                        "Y": 0.4710812568664551
                    },
                    {
                        "Type": "mouthLeft",
                        "X": 0.5879443287849426,
                        "Y": 0.5171778798103333
                    },
                    {
                        "Type": "mouthRight",
                        "X": 0.6444502472877502,
                        "Y": 0.5164633989334106
                    }
                ],
                "Pose": {
                    "Pitch": -10.313642501831055,
                    "Roll": -1.0316886901855469,
                    "Yaw": 18.079818725585938
                },
                "Quality": {
                    "Brightness": 71.2919921875,
                    "Sharpness": 78.74752044677734
                }
            }
        }
    ],
    "OrientationCorrection": "",
    "UnindexedFaces": [
        {
            "FaceDetail": {
                "BoundingBox": {
                    "Height": 0.1329464465379715,
                    "Left": 0.5611110925674438,
                    "Top": 0.6832437515258789,
                    "Width": 0.08777777850627899
                },
                "Confidence": 92.37225341796875,
                "Landmarks": [
                    {
                        "Type": "eyeLeft",
                        "X": 0.5796897411346436,
                        "Y": 0.7452847957611084
                    },
                    {
                        "Type": "eyeRight",
                        "X": 0.6078574657440186,
                        "Y": 0.742687463760376
                    },
                    {
                        "Type": "nose",
                        "X": 0.597953200340271,
                        "Y": 0.7620673179626465
                    },
                    {
                        "Type": "mouthLeft",
                        "X": 0.5884202122688293,
                        "Y": 0.7920381426811218
                    },
                    {
                        "Type": "mouthRight",
                        "X": 0.60627681016922,
                        "Y": 0.7919750809669495
                    }
                ],
                "Pose": {
                    "Pitch": 15.658954620361328,
                    "Roll": -4.583454608917236,
                    "Yaw": 10.558992385864258
                },
                "Quality": {
                    "Brightness": 42.54612350463867,
                    "Sharpness": 86.93206024169922
                }
            },
            "Reasons": [
                "EXCEEDS_MAX_FACES"
            ]
        }
    ]
}
```

To get all facial information, specify 'ALL' for the `DetectionAttributes` request parameter\. For example, in the following example response, note the additional information in the `faceDetail` element, which isn't persisted on the server:
+ 25 facial landmarks \(compared to only five in the preceding example\)
+ Nine facial attributes \(eyeglasses, beard, and so on\) 
+ Emotions \(see the `emotion` element\)

The `face` element provides metadata that's persisted on the server\.

 `FaceModelVersion` is the version of the face model that's associated with the collection\. For more information, see [Model Versioning](face-detection-model.md)\.

`OrientationCorrection` is the estimated orientation of the image\. Orientation correction information is not returned if you are using a version of the face detection model that is greater than version 3\. For more information, see [Getting Image Orientation and Bounding Box Coordinates](images-orientation.md)\.

```
{
    "FaceModelVersion": "3.0",
    "FaceRecords": [
        {
            "Face": {
                "BoundingBox": {
                    "Height": 0.06333333253860474,
                    "Left": 0.17185185849666595,
                    "Top": 0.7366666793823242,
                    "Width": 0.11061728745698929
                },
                "Confidence": 99.99999237060547,
                "ExternalImageId": "input.jpg",
                "FaceId": "578e2e1b-d0b0-493c-aa39-ba476a421a34",
                "ImageId": "9ba38e68-35b6-5509-9d2e-fcffa75d1653"
            },
            "FaceDetail": {
                "AgeRange": {
                    "High": 25,
                    "Low": 15
                },
                "Beard": {
                    "Confidence": 99.98077392578125,
                    "Value": false
                },
                "BoundingBox": {
                    "Height": 0.06333333253860474,
                    "Left": 0.17185185849666595,
                    "Top": 0.7366666793823242,
                    "Width": 0.11061728745698929
                },
                "Confidence": 99.99999237060547,
                "Emotions": [
                    {
                        "Confidence": 95.40877532958984,
                        "Type": "HAPPY"
                    },
                    {
                        "Confidence": 6.6088080406188965,
                        "Type": "CALM"
                    },
                    {
                        "Confidence": 0.7385611534118652,
                        "Type": "SAD"
                    }
                ],
                "Eyeglasses": {
                    "Confidence": 99.96795654296875,
                    "Value": false
                },
                "EyesOpen": {
                    "Confidence": 64.0671157836914,
                    "Value": true
                },
                "Gender": {
                    "Confidence": 100,
                    "Value": "Female"
                },
                "Landmarks": [
                    {
                        "Type": "eyeLeft",
                        "X": 0.21361233294010162,
                        "Y": 0.757106363773346
                    },
                    {
                        "Type": "eyeRight",
                        "X": 0.2518567442893982,
                        "Y": 0.7599404454231262
                    },
                    {
                        "Type": "nose",
                        "X": 0.2262365221977234,
                        "Y": 0.7711842060089111
                    },
                    {
                        "Type": "mouthLeft",
                        "X": 0.2050037682056427,
                        "Y": 0.7801263332366943
                    },
                    {
                        "Type": "mouthRight",
                        "X": 0.2430567592382431,
                        "Y": 0.7836716771125793
                    },
                    {
                        "Type": "leftPupil",
                        "X": 0.2161938101053238,
                        "Y": 0.756662905216217
                    },
                    {
                        "Type": "rightPupil",
                        "X": 0.2523181438446045,
                        "Y": 0.7603650689125061
                    },
                    {
                        "Type": "leftEyeBrowLeft",
                        "X": 0.20066319406032562,
                        "Y": 0.7501518130302429
                    },
                    {
                        "Type": "leftEyeBrowUp",
                        "X": 0.2130996286869049,
                        "Y": 0.7480520606040955
                    },
                    {
                        "Type": "leftEyeBrowRight",
                        "X": 0.22584207355976105,
                        "Y": 0.7504606246948242
                    },
                    {
                        "Type": "rightEyeBrowLeft",
                        "X": 0.24509544670581818,
                        "Y": 0.7526801824569702
                    },
                    {
                        "Type": "rightEyeBrowUp",
                        "X": 0.2582615911960602,
                        "Y": 0.7516844868659973
                    },
                    {
                        "Type": "rightEyeBrowRight",
                        "X": 0.26881539821624756,
                        "Y": 0.7554477453231812
                    },
                    {
                        "Type": "leftEyeLeft",
                        "X": 0.20624476671218872,
                        "Y": 0.7568746209144592
                    },
                    {
                        "Type": "leftEyeRight",
                        "X": 0.22105035185813904,
                        "Y": 0.7582521438598633
                    },
                    {
                        "Type": "leftEyeUp",
                        "X": 0.21401576697826385,
                        "Y": 0.7553104162216187
                    },
                    {
                        "Type": "leftEyeDown",
                        "X": 0.21317370235919952,
                        "Y": 0.7584449648857117
                    },
                    {
                        "Type": "rightEyeLeft",
                        "X": 0.24393919110298157,
                        "Y": 0.7600628137588501
                    },
                    {
                        "Type": "rightEyeRight",
                        "X": 0.2598416209220886,
                        "Y": 0.7605880498886108
                    },
                    {
                        "Type": "rightEyeUp",
                        "X": 0.2519053518772125,
                        "Y": 0.7582084536552429
                    },
                    {
                        "Type": "rightEyeDown",
                        "X": 0.25177454948425293,
                        "Y": 0.7612871527671814
                    },
                    {
                        "Type": "noseLeft",
                        "X": 0.2185886949300766,
                        "Y": 0.774715781211853
                    },
                    {
                        "Type": "noseRight",
                        "X": 0.23328955471515656,
                        "Y": 0.7759330868721008
                    },
                    {
                        "Type": "mouthUp",
                        "X": 0.22446128726005554,
                        "Y": 0.7805567383766174
                    },
                    {
                        "Type": "mouthDown",
                        "X": 0.22087252140045166,
                        "Y": 0.7891407608985901
                    }
                ],
                "MouthOpen": {
                    "Confidence": 95.87068939208984,
                    "Value": false
                },
                "Mustache": {
                    "Confidence": 99.9828109741211,
                    "Value": false
                },
                "Pose": {
                    "Pitch": -0.9409101605415344,
                    "Roll": 7.233824253082275,
                    "Yaw": -2.3602254390716553
                },
                "Quality": {
                    "Brightness": 32.01998519897461,
                    "Sharpness": 93.67259216308594
                },
                "Smile": {
                    "Confidence": 86.7142105102539,
                    "Value": true
                },
                "Sunglasses": {
                    "Confidence": 97.38925170898438,
                    "Value": false
                }
            }
        }
    ],
    "OrientationCorrection": "ROTATE_0"
    "UnindexedFaces": []
}
```