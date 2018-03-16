# DetectFaces<a name="API_DetectFaces"></a>

Detects faces within an image that is provided as input\.

 `DetectFaces` detects the 100 largest faces in the image\. For each face detected, the operation returns face details including a bounding box of the face, a confidence value \(that the bounding box contains a face\), and a fixed set of attributes such as facial landmarks \(for example, coordinates of eye and mouth\), gender, presence of beard, sunglasses, etc\. 

The face\-detection algorithm is most effective on frontal faces\. For non\-frontal or obscured faces, the algorithm may not detect the faces or might detect faces with lower confidence\. 

You pass the input image either as base64\-encoded image bytes or as a reference to an image in an Amazon S3 bucket\. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported\. The image must be either a PNG or JPEG formatted file\. 

**Note**  
This is a stateless API operation\. That is, the operation does not persist any data\.

For an example, see [Detecting Faces in an Image \(SDK\)](procedure-detecting-faces-in-images.md)\.

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
An array of facial attributes you want to be returned\. This can be the default list of attributes or all attributes\. If you don't specify a value for `Attributes` or if you specify `["DEFAULT"]`, the API returns the following subset of facial attributes: `BoundingBox`, `Confidence`, `Pose`, `Quality` and `Landmarks`\. If you provide `["ALL"]`, all facial attributes are returned but the operation will take longer to complete\.  
If you provide both, `["ALL", "DEFAULT"]`, the service uses a logical AND operator to determine which attributes to return \(in this case, all attributes\)\.   
Type: Array of strings  
Valid Values:` DEFAULT | ALL`   
Required: No

 ** [Image](#API_DetectFaces_RequestSyntax) **   <a name="rekognition-DetectFaces-request-Image"></a>
The input image as base64\-encoded bytes or an S3 object\. If you use the AWS CLI to call Amazon Rekognition operations, passing base64\-encoded image bytes is not supported\.   
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
 The orientation of the input image \(counter\-clockwise direction\)\. If your application displays the image, you can use this value to correct image orientation\. The bounding box coordinates returned in `FaceDetails` represent face locations before the image orientation is corrected\.   
If the input image is in \.jpeg format, it might contain exchangeable image \(Exif\) metadata that includes the image's orientation\. If so, and the Exif metadata for the input image populates the orientation field, the value of `OrientationCorrection` is null and the `FaceDetails` bounding box coordinates represent face locations after Exif metadata is used to correct the image orientation\. Images in \.png format don't contain Exif metadata\.
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

## Example<a name="API_DetectFaces_Examples"></a>

### Example Request<a name="API_DetectFaces_Example_1"></a>

The following example shows a request that detects faces in an image \(crowd\.jpg\) stored in an Amazon S3 bucket \(example\-photos\)\.

#### Sample Request<a name="API_DetectFaces_Example_1_Request"></a>

```
POST https://rekognition.us-west-2.amazonaws.com/ HTTP/1.1
Host: rekognition.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 77
X-Amz-Target: RekognitionService.DetectFaces
X-Amz-Date: 20170104T233701Z
User-Agent: aws-cli/1.11.25 Python/2.7.9 Windows/8 botocore/1.4.82
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=XXXXXXXX/20170104/us-west-2/rekognition/aws4_request,
  SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=XXXXXXXX
{
   "Image":{
      "S3Object":{
         "Bucket":"example-photos",
         "Name":"crowd.jpg"
      }
   }
}
```

#### Sample Response<a name="API_DetectFaces_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: Wed, 04 Jan 2017 23:37:03 GMT
x-amzn-RequestId: b1827570-d2d6-11e6-a51e-73b99a9bb0b9
Content-Length: 1355
Connection: keep-alive

{
   "FaceDetails":[
      {
         "BoundingBox":{
            "Height":0.18000000715255737,
            "Left":0.5555555820465088,
            "Top":0.33666667342185974,
            "Width":0.23999999463558197
         },
         "Confidence":100.0,
         "Landmarks":[
            {
               "Type":"eyeLeft",
               "X":0.6394737362861633,
               "Y":0.40819624066352844
            },
            {
               "Type":"eyeRight",
               "X":0.7266660928726196,
               "Y":0.41039225459098816
            },
            {
               "Type":"nose",
               "X":0.6912462115287781,
               "Y":0.44240960478782654
            },
            {
               "Type":"mouthLeft",
               "X":0.6306198239326477,
               "Y":0.46700039505958557
            },
            {
               "Type":"mouthRight",
               "X":0.7215608954429626,
               "Y":0.47114261984825134
            }
         ],
         "Pose":{
            "Pitch":4.050806522369385,
            "Roll":0.9950747489929199,
            "Yaw":13.693790435791016
         },
         "Quality":{
            "Brightness":37.60169982910156,
            "Sharpness":80.0
         }
      },
      {
         "BoundingBox":{
            "Height":0.16555555164813995,
            "Left":0.3096296191215515,
            "Top":0.7066666483879089,
            "Width":0.22074073553085327
         },
         "Confidence":99.99998474121094,
         "Landmarks":[
            {
               "Type":"eyeLeft",
               "X":0.3767718970775604,
               "Y":0.7863991856575012
            },
            {
               "Type":"eyeRight",
               "X":0.4517287313938141,
               "Y":0.7715709209442139
            },
            {
               "Type":"nose",
               "X":0.42001065611839294,
               "Y":0.8192070126533508
            },
            {
               "Type":"mouthLeft",
               "X":0.3915625810623169,
               "Y":0.8374140858650208
            },
            {
               "Type":"mouthRight",
               "X":0.46825936436653137,
               "Y":0.823401689529419
            }
         ],
         "Pose":{
            "Pitch":-16.320178985595703,
            "Roll":-15.097439765930176,
            "Yaw":-5.771541118621826
         },
         "Quality":{
            "Brightness":31.440860748291016,
            "Sharpness":60.000003814697266
         }
      }
   ],
   "OrientationCorrection":"ROTATE_0"
}
```

## See Also<a name="API_DetectFaces_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS Command Line Interface](http://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DetectFaces) 

+  [AWS SDK for \.NET](http://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DetectFaces) 

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DetectFaces) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DetectFaces) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/DetectFaces) 

+  [AWS SDK for JavaScript](http://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DetectFaces) 

+  [AWS SDK for PHP V3](http://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DetectFaces) 

+  [AWS SDK for Python](http://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DetectFaces) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/DetectFaces) 