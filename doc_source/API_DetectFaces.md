# DetectFaces<a name="API_DetectFaces"></a>

Detects faces within an image that is provided as input\.

 `DetectFaces` detects the 100 largest faces in the image\. For each face detected, the operation returns face details\. These details include a bounding box of the face, a confidence value \(that the bounding box contains a face\), and a fixed set of attributes such as facial landmarks \(for example, coordinates of eye and mouth\), presence of beard, sunglasses, and so on\. 

The face\-detection algorithm is most effective on frontal faces\. For non\-frontal or obscured faces, the algorithm might not detect the faces or might detect faces with lower confidence\. 

You pass the input image either as base64\-encoded image bytes or as a reference to an image in an Amazon S3 bucket\. If you use the to call Amazon Rekognition operations, passing image bytes is not supported\. The image must be either a PNG or JPEG formatted file\. 

**Note**  
This is a stateless API operation\. That is, the operation does not persist any data\.

This operation requires permissions to perform the `rekognition:DetectFaces` action\. 

## Request Syntax<a name="API_DetectFaces_RequestSyntax"></a>

```
{
   "[Attributes](#rekognition-DetectFaces-request-Attributes)": [ "string" ],
   "[Image](#rekognition-DetectFaces-request-Image)": { 
      "[Bytes](API_Image.md#rekognition-Type-Image-Bytes)": blob,
      "[S3Object](API_Image.md#rekognition-Type-Image-S3Object)": { 
         "[Bucket](API_S3Object.md#rekognition-Type-S3Object-Bucket)": "string",
         "[Name](API_S3Object.md#rekognition-Type-S3Object-Name)": "string",
         "[Version](API_S3Object.md#rekognition-Type-S3Object-Version)": "string"
      }
   }
}
```

## Request Parameters<a name="API_DetectFaces_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [Attributes](#API_DetectFaces_RequestSyntax) **   <a name="rekognition-DetectFaces-request-Attributes"></a>
An array of facial attributes you want to be returned\. This can be the default list of attributes or all attributes\. If you don't specify a value for `Attributes` or if you specify `["DEFAULT"]`, the API returns the following subset of facial attributes: `BoundingBox`, `Confidence`, `Pose`, `Quality`, and `Landmarks`\. If you provide `["ALL"]`, all facial attributes are returned, but the operation takes longer to complete\.  
If you provide both, `["ALL", "DEFAULT"]`, the service uses a logical AND operator to determine which attributes to return \(in this case, all attributes\)\.   
Type: Array of strings  
Valid Values:` DEFAULT | ALL`   
Required: No

 ** [Image](#API_DetectFaces_RequestSyntax) **   <a name="rekognition-DetectFaces-request-Image"></a>
The input image as base64\-encoded bytes or an S3 object\. If you use the AWS CLI to call Amazon Rekognition operations, passing base64\-encoded image bytes is not supported\.   
If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64\-encode image bytes passed using the `Bytes` field\. For more information, see [Images](images-information.md)\.  
Type: [Image](API_Image.md) object  
Required: Yes

## Response Syntax<a name="API_DetectFaces_ResponseSyntax"></a>

```
{
   "[FaceDetails](#rekognition-DetectFaces-response-FaceDetails)": [ 
      { 
         "[AgeRange](API_FaceDetail.md#rekognition-Type-FaceDetail-AgeRange)": { 
            "[High](API_AgeRange.md#rekognition-Type-AgeRange-High)": number,
            "[Low](API_AgeRange.md#rekognition-Type-AgeRange-Low)": number
         },
         "[Beard](API_FaceDetail.md#rekognition-Type-FaceDetail-Beard)": { 
            "[Confidence](API_Beard.md#rekognition-Type-Beard-Confidence)": number,
            "[Value](API_Beard.md#rekognition-Type-Beard-Value)": boolean
         },
         "[BoundingBox](API_FaceDetail.md#rekognition-Type-FaceDetail-BoundingBox)": { 
            "[Height](API_BoundingBox.md#rekognition-Type-BoundingBox-Height)": number,
            "[Left](API_BoundingBox.md#rekognition-Type-BoundingBox-Left)": number,
            "[Top](API_BoundingBox.md#rekognition-Type-BoundingBox-Top)": number,
            "[Width](API_BoundingBox.md#rekognition-Type-BoundingBox-Width)": number
         },
         "[Confidence](API_FaceDetail.md#rekognition-Type-FaceDetail-Confidence)": number,
         "[Emotions](API_FaceDetail.md#rekognition-Type-FaceDetail-Emotions)": [ 
            { 
               "[Confidence](API_Emotion.md#rekognition-Type-Emotion-Confidence)": number,
               "[Type](API_Emotion.md#rekognition-Type-Emotion-Type)": "string"
            }
         ],
         "[Eyeglasses](API_FaceDetail.md#rekognition-Type-FaceDetail-Eyeglasses)": { 
            "[Confidence](API_Eyeglasses.md#rekognition-Type-Eyeglasses-Confidence)": number,
            "[Value](API_Eyeglasses.md#rekognition-Type-Eyeglasses-Value)": boolean
         },
         "[EyesOpen](API_FaceDetail.md#rekognition-Type-FaceDetail-EyesOpen)": { 
            "[Confidence](API_EyeOpen.md#rekognition-Type-EyeOpen-Confidence)": number,
            "[Value](API_EyeOpen.md#rekognition-Type-EyeOpen-Value)": boolean
         },
         "[Gender](API_FaceDetail.md#rekognition-Type-FaceDetail-Gender)": { 
            "[Confidence](API_Gender.md#rekognition-Type-Gender-Confidence)": number,
            "[Value](API_Gender.md#rekognition-Type-Gender-Value)": "string"
         },
         "[Landmarks](API_FaceDetail.md#rekognition-Type-FaceDetail-Landmarks)": [ 
            { 
               "[Type](API_Landmark.md#rekognition-Type-Landmark-Type)": "string",
               "[X](API_Landmark.md#rekognition-Type-Landmark-X)": number,
               "[Y](API_Landmark.md#rekognition-Type-Landmark-Y)": number
            }
         ],
         "[MouthOpen](API_FaceDetail.md#rekognition-Type-FaceDetail-MouthOpen)": { 
            "[Confidence](API_MouthOpen.md#rekognition-Type-MouthOpen-Confidence)": number,
            "[Value](API_MouthOpen.md#rekognition-Type-MouthOpen-Value)": boolean
         },
         "[Mustache](API_FaceDetail.md#rekognition-Type-FaceDetail-Mustache)": { 
            "[Confidence](API_Mustache.md#rekognition-Type-Mustache-Confidence)": number,
            "[Value](API_Mustache.md#rekognition-Type-Mustache-Value)": boolean
         },
         "[Pose](API_FaceDetail.md#rekognition-Type-FaceDetail-Pose)": { 
            "[Pitch](API_Pose.md#rekognition-Type-Pose-Pitch)": number,
            "[Roll](API_Pose.md#rekognition-Type-Pose-Roll)": number,
            "[Yaw](API_Pose.md#rekognition-Type-Pose-Yaw)": number
         },
         "[Quality](API_FaceDetail.md#rekognition-Type-FaceDetail-Quality)": { 
            "[Brightness](API_ImageQuality.md#rekognition-Type-ImageQuality-Brightness)": number,
            "[Sharpness](API_ImageQuality.md#rekognition-Type-ImageQuality-Sharpness)": number
         },
         "[Smile](API_FaceDetail.md#rekognition-Type-FaceDetail-Smile)": { 
            "[Confidence](API_Smile.md#rekognition-Type-Smile-Confidence)": number,
            "[Value](API_Smile.md#rekognition-Type-Smile-Value)": boolean
         },
         "[Sunglasses](API_FaceDetail.md#rekognition-Type-FaceDetail-Sunglasses)": { 
            "[Confidence](API_Sunglasses.md#rekognition-Type-Sunglasses-Confidence)": number,
            "[Value](API_Sunglasses.md#rekognition-Type-Sunglasses-Value)": boolean
         }
      }
   ],
   "[OrientationCorrection](#rekognition-DetectFaces-response-OrientationCorrection)": "string"
}
```

## Response Elements<a name="API_DetectFaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [FaceDetails](#API_DetectFaces_ResponseSyntax) **   <a name="rekognition-DetectFaces-response-FaceDetails"></a>
Details of each face found in the image\.   
Type: Array of [FaceDetail](API_FaceDetail.md) objects

 ** [OrientationCorrection](#API_DetectFaces_ResponseSyntax) **   <a name="rekognition-DetectFaces-response-OrientationCorrection"></a>
The value of `OrientationCorrection` is always null\.  
If the input image is in \.jpeg format, it might contain exchangeable image file format \(Exif\) metadata that includes the image's orientation\. Amazon Rekognition uses this orientation information to perform image correction\. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation\. Images in \.png format don't contain Exif metadata\.  
Amazon Rekognition doesn’t perform image correction for images in \.png format and \.jpeg images without orientation information in the image Exif metadata\. The bounding box coordinates aren't translated and represent the object locations before the image is rotated\.   
Type: String  
Valid Values:` ROTATE_0 | ROTATE_90 | ROTATE_180 | ROTATE_270` 

## Errors<a name="API_DetectFaces_Errors"></a>

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

## See Also<a name="API_DetectFaces_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DetectFaces) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DetectFaces) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DetectFaces) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DetectFaces) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/DetectFaces) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DetectFaces) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DetectFaces) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DetectFaces) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/DetectFaces) 