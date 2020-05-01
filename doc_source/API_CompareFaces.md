# CompareFaces<a name="API_CompareFaces"></a>

Compares a face in the *source* input image with each of the 100 largest faces detected in the *target* input image\. 

**Note**  
 If the source image contains multiple faces, the service detects the largest face and compares it with each face detected in the target image\. 

You pass the input and target images either as base64\-encoded image bytes or as references to images in an Amazon S3 bucket\. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes isn't supported\. The image must be formatted as a PNG or JPEG file\. 

In response, the operation returns an array of face matches ordered by similarity score in descending order\. For each face match, the response provides a bounding box of the face, facial landmarks, pose details \(pitch, role, and yaw\), quality \(brightness and sharpness\), and confidence value \(indicating the level of confidence that the bounding box contains a face\)\. The response also provides a similarity score, which indicates how closely the faces match\. 

**Note**  
By default, only faces with a similarity score of greater than or equal to 80% are returned in the response\. You can change this value by specifying the `SimilarityThreshold` parameter\.

 `CompareFaces` also returns an array of faces that don't match the source image\. For each face, it returns a bounding box, confidence value, landmarks, pose details, and quality\. The response also returns information about the face in the source image, including the bounding box of the face and confidence value\.

The `QualityFilter` input parameter allows you to filter out detected faces that don’t meet a required quality bar\. The quality bar is based on a variety of common use cases\. Use `QualityFilter` to set the quality bar by specifying `LOW`, `MEDIUM`, or `HIGH`\. If you do not want to filter detected faces, specify `NONE`\. The default value is `NONE`\. 

**Note**  
To use quality filtering, you need a collection associated with version 3 of the face model or higher\. To get the version of the face model associated with a collection, call [DescribeCollection](API_DescribeCollection.md)\. 

If the image doesn't contain Exif metadata, `CompareFaces` returns orientation information for the source and target images\. Use these values to display the images with the correct image orientation\.

If no faces are detected in the source or target images, `CompareFaces` returns an `InvalidParameterException` error\. 

**Note**  
 This is a stateless API operation\. That is, data returned by this operation doesn't persist\.

For an example, see [Comparing Faces in Images](faces-comparefaces.md)\.

This operation requires permissions to perform the `rekognition:CompareFaces` action\.

## Request Syntax<a name="API_CompareFaces_RequestSyntax"></a>

```
{
   "[QualityFilter](#rekognition-CompareFaces-request-QualityFilter)": "string",
   "[SimilarityThreshold](#rekognition-CompareFaces-request-SimilarityThreshold)": number,
   "[SourceImage](#rekognition-CompareFaces-request-SourceImage)": { 
      "[Bytes](API_Image.md#rekognition-Type-Image-Bytes)": blob,
      "[S3Object](API_Image.md#rekognition-Type-Image-S3Object)": { 
         "[Bucket](API_S3Object.md#rekognition-Type-S3Object-Bucket)": "string",
         "[Name](API_S3Object.md#rekognition-Type-S3Object-Name)": "string",
         "[Version](API_S3Object.md#rekognition-Type-S3Object-Version)": "string"
      }
   },
   "[TargetImage](#rekognition-CompareFaces-request-TargetImage)": { 
      "[Bytes](API_Image.md#rekognition-Type-Image-Bytes)": blob,
      "[S3Object](API_Image.md#rekognition-Type-Image-S3Object)": { 
         "[Bucket](API_S3Object.md#rekognition-Type-S3Object-Bucket)": "string",
         "[Name](API_S3Object.md#rekognition-Type-S3Object-Name)": "string",
         "[Version](API_S3Object.md#rekognition-Type-S3Object-Version)": "string"
      }
   }
}
```

## Request Parameters<a name="API_CompareFaces_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [QualityFilter](#API_CompareFaces_RequestSyntax) **   <a name="rekognition-CompareFaces-request-QualityFilter"></a>
A filter that specifies a quality bar for how much filtering is done to identify faces\. Filtered faces aren't compared\. If you specify `AUTO`, Amazon Rekognition chooses the quality bar\. If you specify `LOW`, `MEDIUM`, or `HIGH`, filtering removes all faces that don’t meet the chosen quality bar\. The quality bar is based on a variety of common use cases\. Low\-quality detections can occur for a number of reasons\. Some examples are an object that's misidentified as a face, a face that's too blurry, or a face with a pose that's too extreme to use\. If you specify `NONE`, no filtering is performed\. The default value is `NONE`\.   
To use quality filtering, the collection you are using must be associated with version 3 of the face model or higher\.  
Type: String  
Valid Values:` NONE | AUTO | LOW | MEDIUM | HIGH`   
Required: No

 ** [SimilarityThreshold](#API_CompareFaces_RequestSyntax) **   <a name="rekognition-CompareFaces-request-SimilarityThreshold"></a>
The minimum level of confidence in the face matches that a match must meet to be included in the `FaceMatches` array\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 ** [SourceImage](#API_CompareFaces_RequestSyntax) **   <a name="rekognition-CompareFaces-request-SourceImage"></a>
The input image as base64\-encoded bytes or an S3 object\. If you use the AWS CLI to call Amazon Rekognition operations, passing base64\-encoded image bytes is not supported\.   
If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64\-encode image bytes passed using the `Bytes` field\. For more information, see [Images](images-information.md)\.  
Type: [Image](API_Image.md) object  
Required: Yes

 ** [TargetImage](#API_CompareFaces_RequestSyntax) **   <a name="rekognition-CompareFaces-request-TargetImage"></a>
The target image as base64\-encoded bytes or an S3 object\. If you use the AWS CLI to call Amazon Rekognition operations, passing base64\-encoded image bytes is not supported\.   
If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64\-encode image bytes passed using the `Bytes` field\. For more information, see [Images](images-information.md)\.  
Type: [Image](API_Image.md) object  
Required: Yes

## Response Syntax<a name="API_CompareFaces_ResponseSyntax"></a>

```
{
   "[FaceMatches](#rekognition-CompareFaces-response-FaceMatches)": [ 
      { 
         "[Face](API_CompareFacesMatch.md#rekognition-Type-CompareFacesMatch-Face)": { 
            "[BoundingBox](API_ComparedFace.md#rekognition-Type-ComparedFace-BoundingBox)": { 
               "[Height](API_BoundingBox.md#rekognition-Type-BoundingBox-Height)": number,
               "[Left](API_BoundingBox.md#rekognition-Type-BoundingBox-Left)": number,
               "[Top](API_BoundingBox.md#rekognition-Type-BoundingBox-Top)": number,
               "[Width](API_BoundingBox.md#rekognition-Type-BoundingBox-Width)": number
            },
            "[Confidence](API_ComparedFace.md#rekognition-Type-ComparedFace-Confidence)": number,
            "[Landmarks](API_ComparedFace.md#rekognition-Type-ComparedFace-Landmarks)": [ 
               { 
                  "[Type](API_Landmark.md#rekognition-Type-Landmark-Type)": "string",
                  "[X](API_Landmark.md#rekognition-Type-Landmark-X)": number,
                  "[Y](API_Landmark.md#rekognition-Type-Landmark-Y)": number
               }
            ],
            "[Pose](API_ComparedFace.md#rekognition-Type-ComparedFace-Pose)": { 
               "[Pitch](API_Pose.md#rekognition-Type-Pose-Pitch)": number,
               "[Roll](API_Pose.md#rekognition-Type-Pose-Roll)": number,
               "[Yaw](API_Pose.md#rekognition-Type-Pose-Yaw)": number
            },
            "[Quality](API_ComparedFace.md#rekognition-Type-ComparedFace-Quality)": { 
               "[Brightness](API_ImageQuality.md#rekognition-Type-ImageQuality-Brightness)": number,
               "[Sharpness](API_ImageQuality.md#rekognition-Type-ImageQuality-Sharpness)": number
            }
         },
         "[Similarity](API_CompareFacesMatch.md#rekognition-Type-CompareFacesMatch-Similarity)": number
      }
   ],
   "[SourceImageFace](#rekognition-CompareFaces-response-SourceImageFace)": { 
      "[BoundingBox](API_ComparedSourceImageFace.md#rekognition-Type-ComparedSourceImageFace-BoundingBox)": { 
         "[Height](API_BoundingBox.md#rekognition-Type-BoundingBox-Height)": number,
         "[Left](API_BoundingBox.md#rekognition-Type-BoundingBox-Left)": number,
         "[Top](API_BoundingBox.md#rekognition-Type-BoundingBox-Top)": number,
         "[Width](API_BoundingBox.md#rekognition-Type-BoundingBox-Width)": number
      },
      "[Confidence](API_ComparedSourceImageFace.md#rekognition-Type-ComparedSourceImageFace-Confidence)": number
   },
   "[SourceImageOrientationCorrection](#rekognition-CompareFaces-response-SourceImageOrientationCorrection)": "string",
   "[TargetImageOrientationCorrection](#rekognition-CompareFaces-response-TargetImageOrientationCorrection)": "string",
   "[UnmatchedFaces](#rekognition-CompareFaces-response-UnmatchedFaces)": [ 
      { 
         "[BoundingBox](API_ComparedFace.md#rekognition-Type-ComparedFace-BoundingBox)": { 
            "[Height](API_BoundingBox.md#rekognition-Type-BoundingBox-Height)": number,
            "[Left](API_BoundingBox.md#rekognition-Type-BoundingBox-Left)": number,
            "[Top](API_BoundingBox.md#rekognition-Type-BoundingBox-Top)": number,
            "[Width](API_BoundingBox.md#rekognition-Type-BoundingBox-Width)": number
         },
         "[Confidence](API_ComparedFace.md#rekognition-Type-ComparedFace-Confidence)": number,
         "[Landmarks](API_ComparedFace.md#rekognition-Type-ComparedFace-Landmarks)": [ 
            { 
               "[Type](API_Landmark.md#rekognition-Type-Landmark-Type)": "string",
               "[X](API_Landmark.md#rekognition-Type-Landmark-X)": number,
               "[Y](API_Landmark.md#rekognition-Type-Landmark-Y)": number
            }
         ],
         "[Pose](API_ComparedFace.md#rekognition-Type-ComparedFace-Pose)": { 
            "[Pitch](API_Pose.md#rekognition-Type-Pose-Pitch)": number,
            "[Roll](API_Pose.md#rekognition-Type-Pose-Roll)": number,
            "[Yaw](API_Pose.md#rekognition-Type-Pose-Yaw)": number
         },
         "[Quality](API_ComparedFace.md#rekognition-Type-ComparedFace-Quality)": { 
            "[Brightness](API_ImageQuality.md#rekognition-Type-ImageQuality-Brightness)": number,
            "[Sharpness](API_ImageQuality.md#rekognition-Type-ImageQuality-Sharpness)": number
         }
      }
   ]
}
```

## Response Elements<a name="API_CompareFaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [FaceMatches](#API_CompareFaces_ResponseSyntax) **   <a name="rekognition-CompareFaces-response-FaceMatches"></a>
An array of faces in the target image that match the source image face\. Each `CompareFacesMatch` object provides the bounding box, the confidence level that the bounding box contains a face, and the similarity score for the face in the bounding box and the face in the source image\.  
Type: Array of [CompareFacesMatch](API_CompareFacesMatch.md) objects

 ** [SourceImageFace](#API_CompareFaces_ResponseSyntax) **   <a name="rekognition-CompareFaces-response-SourceImageFace"></a>
The face in the source image that was used for comparison\.  
Type: [ComparedSourceImageFace](API_ComparedSourceImageFace.md) object

 ** [SourceImageOrientationCorrection](#API_CompareFaces_ResponseSyntax) **   <a name="rekognition-CompareFaces-response-SourceImageOrientationCorrection"></a>
The value of `SourceImageOrientationCorrection` is always null\.  
If the input image is in \.jpeg format, it might contain exchangeable image file format \(Exif\) metadata that includes the image's orientation\. Amazon Rekognition uses this orientation information to perform image correction\. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation\. Images in \.png format don't contain Exif metadata\.  
Amazon Rekognition doesn’t perform image correction for images in \.png format and \.jpeg images without orientation information in the image Exif metadata\. The bounding box coordinates aren't translated and represent the object locations before the image is rotated\.   
Type: String  
Valid Values:` ROTATE_0 | ROTATE_90 | ROTATE_180 | ROTATE_270` 

 ** [TargetImageOrientationCorrection](#API_CompareFaces_ResponseSyntax) **   <a name="rekognition-CompareFaces-response-TargetImageOrientationCorrection"></a>
The value of `TargetImageOrientationCorrection` is always null\.  
If the input image is in \.jpeg format, it might contain exchangeable image file format \(Exif\) metadata that includes the image's orientation\. Amazon Rekognition uses this orientation information to perform image correction\. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation\. Images in \.png format don't contain Exif metadata\.  
Amazon Rekognition doesn’t perform image correction for images in \.png format and \.jpeg images without orientation information in the image Exif metadata\. The bounding box coordinates aren't translated and represent the object locations before the image is rotated\.   
Type: String  
Valid Values:` ROTATE_0 | ROTATE_90 | ROTATE_180 | ROTATE_270` 

 ** [UnmatchedFaces](#API_CompareFaces_ResponseSyntax) **   <a name="rekognition-CompareFaces-response-UnmatchedFaces"></a>
An array of faces in the target image that did not match the source image face\.  
Type: Array of [ComparedFace](API_ComparedFace.md) objects

## Errors<a name="API_CompareFaces_Errors"></a>

 **AccessDeniedException**   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 **ImageTooLargeException**   
The input image size exceeds the allowed limit\. For more information, see [Limits in Amazon Rekognition](limits.md)\.   
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

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_CompareFaces_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/CompareFaces) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/CompareFaces) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CompareFaces) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/CompareFaces) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/CompareFaces) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/CompareFaces) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/CompareFaces) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/CompareFaces) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CompareFaces) 