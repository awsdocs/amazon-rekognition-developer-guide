# IndexFaces<a name="API_IndexFaces"></a>

Detects faces in the input image and adds them to the specified collection\. 

Amazon Rekognition doesn't save the actual faces that are detected\. Instead, the underlying detection algorithm first detects the faces in the input image\. For each face, the algorithm extracts facial features into a feature vector, and stores it in the backend database\. Amazon Rekognition uses feature vectors when it performs face match and search operations using the [SearchFaces](API_SearchFaces.md) and [SearchFacesByImage](API_SearchFacesByImage.md) operations\.

For more information, see [Adding faces to a collection](add-faces-to-collection-procedure.md)\.

To get the number of faces in a collection, call [DescribeCollection](API_DescribeCollection.md)\. 

If you're using version 1\.0 of the face detection model, `IndexFaces` indexes the 15 largest faces in the input image\. Later versions of the face detection model index the 100 largest faces in the input image\. 

If you're using version 4 or later of the face model, image orientation information is not returned in the `OrientationCorrection` field\. 

To determine which version of the model you're using, call [DescribeCollection](API_DescribeCollection.md) and supply the collection ID\. You can also get the model version from the value of `FaceModelVersion` in the response from `IndexFaces` 

For more information, see [Model versioning](face-detection-model.md)\.

If you provide the optional `ExternalImageId` for the input image you provided, Amazon Rekognition associates this ID with all faces that it detects\. When you call the [ListFaces](API_ListFaces.md) operation, the response returns the external ID\. You can use this external image ID to create a client\-side index to associate the faces with each image\. You can then use the index to find all faces in an image\.

You can specify the maximum number of faces to index with the `MaxFaces` input parameter\. This is useful when you want to index the largest faces in an image and don't want to index smaller faces, such as those belonging to people standing in the background\.

The `QualityFilter` input parameter allows you to filter out detected faces that don’t meet a required quality bar\. The quality bar is based on a variety of common use cases\. By default, `IndexFaces` chooses the quality bar that's used to filter faces\. You can also explicitly choose the quality bar\. Use `QualityFilter`, to set the quality bar by specifying `LOW`, `MEDIUM`, or `HIGH`\. If you do not want to filter detected faces, specify `NONE`\. 

**Note**  
To use quality filtering, you need a collection associated with version 3 of the face model or higher\. To get the version of the face model associated with a collection, call [DescribeCollection](API_DescribeCollection.md)\. 

Information about faces detected in an image, but not indexed, is returned in an array of [UnindexedFace](API_UnindexedFace.md) objects, `UnindexedFaces`\. Faces aren't indexed for reasons such as:
+ The number of faces detected exceeds the value of the `MaxFaces` request parameter\.
+ The face is too small compared to the image dimensions\.
+ The face is too blurry\.
+ The image is too dark\.
+ The face has an extreme pose\.
+ The face doesn’t have enough detail to be suitable for face search\.

In response, the `IndexFaces` operation returns an array of metadata for all detected faces, `FaceRecords`\. This includes: 
+ The bounding box, `BoundingBox`, of the detected face\. 
+ A confidence value, `Confidence`, which indicates the confidence that the bounding box contains a face\.
+ A face ID, `FaceId`, assigned by the service for each face that's detected and stored\.
+ An image ID, `ImageId`, assigned by the service for the input image\.

If you request all facial attributes \(by using the `detectionAttributes` parameter\), Amazon Rekognition returns detailed facial attributes, such as facial landmarks \(for example, location of eye and mouth\) and other facial attributes\. If you provide the same image, specify the same collection, and use the same external ID in the `IndexFaces` operation, Amazon Rekognition doesn't save duplicate face metadata\.



The input image is passed either as base64\-encoded image bytes, or as a reference to an image in an Amazon S3 bucket\. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes isn't supported\. The image must be formatted as a PNG or JPEG file\. 

This operation requires permissions to perform the `rekognition:IndexFaces` action\.

## Request Syntax<a name="API_IndexFaces_RequestSyntax"></a>

```
{
   "CollectionId": "string",
   "DetectionAttributes": [ "string" ],
   "ExternalImageId": "string",
   "Image": { 
      "Bytes": blob,
      "S3Object": { 
         "Bucket": "string",
         "Name": "string",
         "Version": "string"
      }
   },
   "MaxFaces": number,
   "QualityFilter": "string"
}
```

## Request Parameters<a name="API_IndexFaces_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [CollectionId](#API_IndexFaces_RequestSyntax) **   <a name="rekognition-IndexFaces-request-CollectionId"></a>
The ID of an existing collection to which you want to add the faces that are detected in the input images\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

 ** [DetectionAttributes](#API_IndexFaces_RequestSyntax) **   <a name="rekognition-IndexFaces-request-DetectionAttributes"></a>
An array of facial attributes that you want to be returned\. This can be the default list of attributes or all attributes\. If you don't specify a value for `Attributes` or if you specify `["DEFAULT"]`, the API returns the following subset of facial attributes: `BoundingBox`, `Confidence`, `Pose`, `Quality`, and `Landmarks`\. If you provide `["ALL"]`, all facial attributes are returned, but the operation takes longer to complete\.  
If you provide both, `["ALL", "DEFAULT"]`, the service uses a logical AND operator to determine which attributes to return \(in this case, all attributes\)\.   
Type: Array of strings  
Valid Values:` DEFAULT | ALL`   
Required: No

 ** [ExternalImageId](#API_IndexFaces_RequestSyntax) **   <a name="rekognition-IndexFaces-request-ExternalImageId"></a>
The ID you want to assign to all the faces detected in the image\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-:]+`   
Required: No

 ** [Image](#API_IndexFaces_RequestSyntax) **   <a name="rekognition-IndexFaces-request-Image"></a>
The input image as base64\-encoded bytes or an S3 object\. If you use the AWS CLI to call Amazon Rekognition operations, passing base64\-encoded image bytes isn't supported\.   
If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64\-encode image bytes passed using the `Bytes` field\. For more information, see [Images](images-information.md)\.  
Type: [Image](API_Image.md) object  
Required: Yes

 ** [MaxFaces](#API_IndexFaces_RequestSyntax) **   <a name="rekognition-IndexFaces-request-MaxFaces"></a>
The maximum number of faces to index\. The value of `MaxFaces` must be greater than or equal to 1\. `IndexFaces` returns no more than 100 detected faces in an image, even if you specify a larger value for `MaxFaces`\.  
If `IndexFaces` detects more faces than the value of `MaxFaces`, the faces with the lowest quality are filtered out first\. If there are still more faces than the value of `MaxFaces`, the faces with the smallest bounding boxes are filtered out \(up to the number that's needed to satisfy the value of `MaxFaces`\)\. Information about the unindexed faces is available in the `UnindexedFaces` array\.   
The faces that are returned by `IndexFaces` are sorted by the largest face bounding box size to the smallest size, in descending order\.  
 `MaxFaces` can be used with a collection associated with any version of the face model\.  
Type: Integer  
Valid Range: Minimum value of 1\.  
Required: No

 ** [QualityFilter](#API_IndexFaces_RequestSyntax) **   <a name="rekognition-IndexFaces-request-QualityFilter"></a>
A filter that specifies a quality bar for how much filtering is done to identify faces\. Filtered faces aren't indexed\. If you specify `AUTO`, Amazon Rekognition chooses the quality bar\. If you specify `LOW`, `MEDIUM`, or `HIGH`, filtering removes all faces that don’t meet the chosen quality bar\. The default value is `AUTO`\. The quality bar is based on a variety of common use cases\. Low\-quality detections can occur for a number of reasons\. Some examples are an object that's misidentified as a face, a face that's too blurry, or a face with a pose that's too extreme to use\. If you specify `NONE`, no filtering is performed\.   
To use quality filtering, the collection you are using must be associated with version 3 of the face model or higher\.  
Type: String  
Valid Values:` NONE | AUTO | LOW | MEDIUM | HIGH`   
Required: No

## Response Syntax<a name="API_IndexFaces_ResponseSyntax"></a>

```
{
   "FaceModelVersion": "string",
   "FaceRecords": [ 
      { 
         "Face": { 
            "BoundingBox": { 
               "Height": number,
               "Left": number,
               "Top": number,
               "Width": number
            },
            "Confidence": number,
            "ExternalImageId": "string",
            "FaceId": "string",
            "ImageId": "string"
         },
         "FaceDetail": { 
            "AgeRange": { 
               "High": number,
               "Low": number
            },
            "Beard": { 
               "Confidence": number,
               "Value": boolean
            },
            "BoundingBox": { 
               "Height": number,
               "Left": number,
               "Top": number,
               "Width": number
            },
            "Confidence": number,
            "Emotions": [ 
               { 
                  "Confidence": number,
                  "Type": "string"
               }
            ],
            "Eyeglasses": { 
               "Confidence": number,
               "Value": boolean
            },
            "EyesOpen": { 
               "Confidence": number,
               "Value": boolean
            },
            "Gender": { 
               "Confidence": number,
               "Value": "string"
            },
            "Landmarks": [ 
               { 
                  "Type": "string",
                  "X": number,
                  "Y": number
               }
            ],
            "MouthOpen": { 
               "Confidence": number,
               "Value": boolean
            },
            "Mustache": { 
               "Confidence": number,
               "Value": boolean
            },
            "Pose": { 
               "Pitch": number,
               "Roll": number,
               "Yaw": number
            },
            "Quality": { 
               "Brightness": number,
               "Sharpness": number
            },
            "Smile": { 
               "Confidence": number,
               "Value": boolean
            },
            "Sunglasses": { 
               "Confidence": number,
               "Value": boolean
            }
         }
      }
   ],
   "OrientationCorrection": "string",
   "UnindexedFaces": [ 
      { 
         "FaceDetail": { 
            "AgeRange": { 
               "High": number,
               "Low": number
            },
            "Beard": { 
               "Confidence": number,
               "Value": boolean
            },
            "BoundingBox": { 
               "Height": number,
               "Left": number,
               "Top": number,
               "Width": number
            },
            "Confidence": number,
            "Emotions": [ 
               { 
                  "Confidence": number,
                  "Type": "string"
               }
            ],
            "Eyeglasses": { 
               "Confidence": number,
               "Value": boolean
            },
            "EyesOpen": { 
               "Confidence": number,
               "Value": boolean
            },
            "Gender": { 
               "Confidence": number,
               "Value": "string"
            },
            "Landmarks": [ 
               { 
                  "Type": "string",
                  "X": number,
                  "Y": number
               }
            ],
            "MouthOpen": { 
               "Confidence": number,
               "Value": boolean
            },
            "Mustache": { 
               "Confidence": number,
               "Value": boolean
            },
            "Pose": { 
               "Pitch": number,
               "Roll": number,
               "Yaw": number
            },
            "Quality": { 
               "Brightness": number,
               "Sharpness": number
            },
            "Smile": { 
               "Confidence": number,
               "Value": boolean
            },
            "Sunglasses": { 
               "Confidence": number,
               "Value": boolean
            }
         },
         "Reasons": [ "string" ]
      }
   ]
}
```

## Response Elements<a name="API_IndexFaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [FaceModelVersion](#API_IndexFaces_ResponseSyntax) **   <a name="rekognition-IndexFaces-response-FaceModelVersion"></a>
The version number of the face detection model that's associated with the input collection \(`CollectionId`\)\.  
Type: String

 ** [FaceRecords](#API_IndexFaces_ResponseSyntax) **   <a name="rekognition-IndexFaces-response-FaceRecords"></a>
An array of faces detected and added to the collection\. For more information, see [Managing faces in a collection](collections.md#collections-index-faces)\.   
Type: Array of [FaceRecord](API_FaceRecord.md) objects

 ** [OrientationCorrection](#API_IndexFaces_ResponseSyntax) **   <a name="rekognition-IndexFaces-response-OrientationCorrection"></a>
If your collection is associated with a face detection model that's later than version 3\.0, the value of `OrientationCorrection` is always null and no orientation information is returned\.  
If your collection is associated with a face detection model that's version 3\.0 or earlier, the following applies:  
+ If the input image is in \.jpeg format, it might contain exchangeable image file format \(Exif\) metadata that includes the image's orientation\. Amazon Rekognition uses this orientation information to perform image correction \- the bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation\. Images in \.png format don't contain Exif metadata\. The value of `OrientationCorrection` is null\.
+ If the image doesn't contain orientation information in its Exif metadata, Amazon Rekognition returns an estimated orientation \(ROTATE\_0, ROTATE\_90, ROTATE\_180, ROTATE\_270\)\. Amazon Rekognition doesn’t perform image correction for images\. The bounding box coordinates aren't translated and represent the object locations before the image is rotated\.
Bounding box information is returned in the `FaceRecords` array\. You can get the version of the face detection model by calling [DescribeCollection](API_DescribeCollection.md)\.   
Type: String  
Valid Values:` ROTATE_0 | ROTATE_90 | ROTATE_180 | ROTATE_270` 

 ** [UnindexedFaces](#API_IndexFaces_ResponseSyntax) **   <a name="rekognition-IndexFaces-response-UnindexedFaces"></a>
An array of faces that were detected in the image but weren't indexed\. They weren't indexed because the quality filter identified them as low quality, or the `MaxFaces` request parameter filtered them out\. To use the quality filter, you specify the `QualityFilter` request parameter\.  
Type: Array of [UnindexedFace](API_UnindexedFace.md) objects

## Errors<a name="API_IndexFaces_Errors"></a>

 **AccessDeniedException**   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 **ImageTooLargeException**   
The input image size exceeds the allowed limit\. If you are calling [DetectProtectiveEquipment](API_DetectProtectiveEquipment.md), the image size or resolution exceeds the allowed limit\. For more information, see [Guidelines and quotas in Amazon Rekognition](limits.md)\.   
HTTP Status Code: 400

 **InternalServerError**   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

 **InvalidImageFormatException**   
The provided image format is not supported\.   
HTTP Status Code: 400

 **InvalidParameterException**   
Input parameter violated a constraint\. Validate your parameter before calling the API operation again\.  
HTTP Status Code: 400

 **InvalidS3ObjectException**   
Amazon Rekognition is unable to access the S3 object specified in the request\.  
HTTP Status Code: 400

 **ProvisionedThroughputExceededException**   
The number of requests exceeded your throughput limit\. If you want to increase this limit, contact Amazon Rekognition\.  
HTTP Status Code: 400

 **ResourceNotFoundException**   
The resource specified in the request cannot be found\.  
HTTP Status Code: 400

 **ServiceQuotaExceededException**   
  
The size of the resource exceeds the allowed limit\. For more information, see [Guidelines and quotas in Amazon Rekognition](limits.md)\.   
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_IndexFaces_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/IndexFaces) 