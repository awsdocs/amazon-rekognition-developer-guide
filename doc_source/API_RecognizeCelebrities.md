# RecognizeCelebrities<a name="API_RecognizeCelebrities"></a>

Returns an array of celebrities recognized in the input image\. For more information, see [Recognizing Celebrities](celebrities.md)\.

 `RecognizeCelebrities` returns the 100 largest faces in the image\. It lists recognized celebrities in the `CelebrityFaces` array and unrecognized faces in the `UnrecognizedFaces` array\. `RecognizeCelebrities` doesn't return celebrities whose faces are not amongst the largest 100 faces in the image\.

For each celebrity recognized, the `RecognizeCelebrities` returns a `Celebrity` object\. The `Celebrity` object contains the celebrity name, ID, URL links to additional information, match confidence, and a `ComparedFace` object that you can use to locate the celebrity's face on the image\.

Rekognition does not retain information about which images a celebrity has been recognized in\. Your application must store this information and use the `Celebrity` ID property as a unique identifier for the celebrity\. If you don't store the celebrity name or additional information URLs returned by `RecognizeCelebrities`, you will need the ID to identify the celebrity in a call to the [GetCelebrityInfo](API_GetCelebrityInfo.md) operation\.

You pass the imput image either as base64\-encoded image bytes or as a reference to an image in an Amazon S3 bucket\. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported\. The image must be either a PNG or JPEG formatted file\. 

For an example, see [Recognizing Celebrities in an Image](celebrities-procedure-image.md)\.

This operation requires permissions to perform the `rekognition:RecognizeCelebrities` operation\.

## Request Syntax<a name="API_RecognizeCelebrities_RequestSyntax"></a>

```
{
   "[Image](#rekognition-RecognizeCelebrities-request-Image)": { 
      "[Bytes](API_Image.md#rekognition-Type-Image-Bytes)": blob,
      "[S3Object](API_Image.md#rekognition-Type-Image-S3Object)": { 
         "[Bucket](API_S3Object.md#rekognition-Type-S3Object-Bucket)": "string",
         "[Name](API_S3Object.md#rekognition-Type-S3Object-Name)": "string",
         "[Version](API_S3Object.md#rekognition-Type-S3Object-Version)": "string"
      }
   }
}
```

## Request Parameters<a name="API_RecognizeCelebrities_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [Image](#API_RecognizeCelebrities_RequestSyntax) **   <a name="rekognition-RecognizeCelebrities-request-Image"></a>
The input image as base64\-encoded bytes or an S3 object\. If you use the AWS CLI to call Amazon Rekognition operations, passing base64\-encoded image bytes is not supported\.   
Type: [Image](API_Image.md) object  
Required: Yes

## Response Syntax<a name="API_RecognizeCelebrities_ResponseSyntax"></a>

```
{
   "[CelebrityFaces](#rekognition-RecognizeCelebrities-response-CelebrityFaces)": [ 
      { 
         "[Face](API_Celebrity.md#rekognition-Type-Celebrity-Face)": { 
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
         "[Id](API_Celebrity.md#rekognition-Type-Celebrity-Id)": "string",
         "[MatchConfidence](API_Celebrity.md#rekognition-Type-Celebrity-MatchConfidence)": number,
         "[Name](API_Celebrity.md#rekognition-Type-Celebrity-Name)": "string",
         "[Urls](API_Celebrity.md#rekognition-Type-Celebrity-Urls)": [ "string" ]
      }
   ],
   "[OrientationCorrection](#rekognition-RecognizeCelebrities-response-OrientationCorrection)": "string",
   "[UnrecognizedFaces](#rekognition-RecognizeCelebrities-response-UnrecognizedFaces)": [ 
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

## Response Elements<a name="API_RecognizeCelebrities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [CelebrityFaces](#API_RecognizeCelebrities_ResponseSyntax) **   <a name="rekognition-RecognizeCelebrities-response-CelebrityFaces"></a>
Details about each celebrity found in the image\. Amazon Rekognition can detect a maximum of 15 celebrities in an image\.  
Type: Array of [Celebrity](API_Celebrity.md) objects

 ** [OrientationCorrection](#API_RecognizeCelebrities_ResponseSyntax) **   <a name="rekognition-RecognizeCelebrities-response-OrientationCorrection"></a>
The orientation of the input image \(counterclockwise direction\)\. If your application displays the image, you can use this value to correct the orientation\. The bounding box coordinates returned in `CelebrityFaces` and `UnrecognizedFaces` represent face locations before the image orientation is corrected\.   
If the input image is in \.jpeg format, it might contain exchangeable image \(Exif\) metadata that includes the image's orientation\. If so, and the Exif metadata for the input image populates the orientation field, the value of `OrientationCorrection` is null and the `CelebrityFaces` and `UnrecognizedFaces` bounding box coordinates represent face locations after Exif metadata is used to correct the image orientation\. Images in \.png format don't contain Exif metadata\. 
Type: String  
Valid Values:` ROTATE_0 | ROTATE_90 | ROTATE_180 | ROTATE_270` 

 ** [UnrecognizedFaces](#API_RecognizeCelebrities_ResponseSyntax) **   <a name="rekognition-RecognizeCelebrities-response-UnrecognizedFaces"></a>
Details about each unrecognized face in the image\.  
Type: Array of [ComparedFace](API_ComparedFace.md) objects

## Errors<a name="API_RecognizeCelebrities_Errors"></a>

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

## Example<a name="API_RecognizeCelebrities_Examples"></a>

### Example Request<a name="API_RecognizeCelebrities_Example_1"></a>

The following example recognizes celebrities in an image \(image\.jpg\) stored in an Amazon S3 bucket \(photo\-collection\)\.

#### Sample Request<a name="API_RecognizeCelebrities_Example_1_Request"></a>

```
 POST https://rekognition.us-west-2.amazonaws.com/ HTTP/1.1
 Host: rekognition.us-west-2.amazonaws.com
 Accept-Encoding: identity
 Content-Length: 83
 X-Amz-Target: RekognitionService.RecognizeCelebrities
 X-Amz-Date: 20170414T195420Z
 User-Agent: aws-cli/1.11.47 Python/2.7.9 Windows/8 botocore/1.5.10
 Content-Type: application/x-amz-json-1.1
 Authorization: AWS4-HMAC-SHA256 Credential=XXXX/20170414/us-west-2/rekognition/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target,
    Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
{
    "Image": {
        "S3Object": {
            "Bucket": "photo-collection",
            "Name": "image.jpg"
        }
    }
}
```

#### Sample Response<a name="API_RecognizeCelebrities_Example_1_Response"></a>

```
{
   "CelebrityFaces": [{
       "Face": {
           "BoundingBox": {
               "Height": 0.617123007774353,
               "Left": 0.15641026198863983,
               "Top": 0.10864841192960739,
               "Width": 0.3641025722026825
           },
           "Confidence": 99.99589538574219,
           "Landmarks": [{
               "Type": "eyeLeft",
               "X": 0.2837241291999817,
               "Y": 0.3637104034423828
           }, {
               "Type": "eyeRight",
               "X": 0.4091649055480957,
               "Y": 0.37378931045532227
           }, {
               "Type": "nose",
               "X": 0.35267341136932373,
               "Y": 0.49657556414604187
           }, {
               "Type": "mouthLeft",
               "X": 0.2786353826522827,
               "Y": 0.5455248355865479
           }, {
               "Type": "mouthRight",
               "X": 0.39566439390182495,
               "Y": 0.5597742199897766
           }],
           "Pose": {
               "Pitch": -7.749263763427734,
               "Roll": 2.004552125930786,
               "Yaw": 9.012002944946289
           },
           "Quality": {
               "Brightness": 32.69192123413086,
               "Sharpness": 99.9305191040039
           }
       },
       "Id": "3Ir0du6",
       "MatchConfidence": 98.0,
       "Name": "Jeff Bezos",
       "Urls": ["www.imdb.com/name/nm1757263"]
   }],
   "OrientationCorrection": "ROTATE_0",
   "UnrecognizedFaces": [{
       "BoundingBox": {
           "Height": 0.5345501899719238,
           "Left": 0.48461538553237915,
           "Top": 0.16949152946472168,
           "Width": 0.3153846263885498
       },
       "Confidence": 99.92860412597656,
       "Landmarks": [{
           "Type": "eyeLeft",
           "X": 0.5863404870033264,
           "Y": 0.36940744519233704
       }, {
           "Type": "eyeRight",
           "X": 0.6999204754829407,
           "Y": 0.3769848346710205
       }, {
           "Type": "nose",
           "X": 0.6349524259567261,
           "Y": 0.4804527163505554
       }, {
           "Type": "mouthLeft",
           "X": 0.5872702598571777,
           "Y": 0.5535582304000854
       }, {
           "Type": "mouthRight",
           "X": 0.6952020525932312,
           "Y": 0.5600858926773071
       }],
       "Pose": {
           "Pitch": -7.386096477508545,
           "Roll": 2.304218292236328,
           "Yaw": -6.175624370574951
       },
       "Quality": {
           "Brightness": 37.16635513305664,
           "Sharpness": 99.884521484375
       }
   }]
}
```

## See Also<a name="API_RecognizeCelebrities_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/RecognizeCelebrities) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/RecognizeCelebrities) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/RecognizeCelebrities) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/RecognizeCelebrities) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/RecognizeCelebrities) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/RecognizeCelebrities) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/RecognizeCelebrities) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/RecognizeCelebrities) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/RecognizeCelebrities) 