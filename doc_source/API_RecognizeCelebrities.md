# RecognizeCelebrities<a name="API_RecognizeCelebrities"></a>

Returns an array of celebrities recognized in the input image\. For more information, see [Recognizing celebrities](celebrities.md)\.

 `RecognizeCelebrities` returns the 64 largest faces in the image\. It lists the recognized celebrities in the `CelebrityFaces` array and any unrecognized faces in the `UnrecognizedFaces` array\. `RecognizeCelebrities` doesn't return celebrities whose faces aren't among the largest 64 faces in the image\.

For each celebrity recognized, `RecognizeCelebrities` returns a `Celebrity` object\. The `Celebrity` object contains the celebrity name, ID, URL links to additional information, match confidence, and a `ComparedFace` object that you can use to locate the celebrity's face on the image\.

Amazon Rekognition doesn't retain information about which images a celebrity has been recognized in\. Your application must store this information and use the `Celebrity` ID property as a unique identifier for the celebrity\. If you don't store the celebrity name or additional information URLs returned by `RecognizeCelebrities`, you will need the ID to identify the celebrity in a call to the [ GetCelebrityInfo ](API_GetCelebrityInfo.md) operation\.

You pass the input image either as base64\-encoded image bytes or as a reference to an image in an Amazon S3 bucket\. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported\. The image must be either a PNG or JPEG formatted file\. 

For an example, see [Recognizing celebrities in an image](celebrities-procedure-image.md)\.

This operation requires permissions to perform the `rekognition:RecognizeCelebrities` operation\.

## Request Syntax<a name="API_RecognizeCelebrities_RequestSyntax"></a>

```
{
   "Image": { 
      "Bytes": blob,
      "S3Object": { 
         "Bucket": "string",
         "Name": "string",
         "Version": "string"
      }
   }
}
```

## Request Parameters<a name="API_RecognizeCelebrities_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ Image ](#API_RecognizeCelebrities_RequestSyntax) **   <a name="rekognition-RecognizeCelebrities-request-Image"></a>
The input image as base64\-encoded bytes or an S3 object\. If you use the AWS CLI to call Amazon Rekognition operations, passing base64\-encoded image bytes is not supported\.   
If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64\-encode image bytes passed using the `Bytes` field\. For more information, see [Image specifications](images-information.md)\.  
Type: [ Image ](API_Image.md) object  
Required: Yes

## Response Syntax<a name="API_RecognizeCelebrities_ResponseSyntax"></a>

```
{
   "CelebrityFaces": [ 
      { 
         "Face": { 
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
            "Landmarks": [ 
               { 
                  "Type": "string",
                  "X": number,
                  "Y": number
               }
            ],
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
            }
         },
         "Id": "string",
         "KnownGender": { 
            "Type": "string"
         },
         "MatchConfidence": number,
         "Name": "string",
         "Urls": [ "string" ]
      }
   ],
   "OrientationCorrection": "string",
   "UnrecognizedFaces": [ 
      { 
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
         "Landmarks": [ 
            { 
               "Type": "string",
               "X": number,
               "Y": number
            }
         ],
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
         }
      }
   ]
}
```

## Response Elements<a name="API_RecognizeCelebrities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [ CelebrityFaces ](#API_RecognizeCelebrities_ResponseSyntax) **   <a name="rekognition-RecognizeCelebrities-response-CelebrityFaces"></a>
Details about each celebrity found in the image\. Amazon Rekognition can detect a maximum of 64 celebrities in an image\. Each celebrity object includes the following attributes: `Face`, `Confidence`, `Emotions`, `Landmarks`, `Pose`, `Quality`, `Smile`, `Id`, `KnownGender`, `MatchConfidence`, `Name`, `Urls`\.  
Type: Array of [ Celebrity ](API_Celebrity.md) objects

 ** [ OrientationCorrection ](#API_RecognizeCelebrities_ResponseSyntax) **   <a name="rekognition-RecognizeCelebrities-response-OrientationCorrection"></a>
Support for estimating image orientation using the the OrientationCorrection field has ceased as of August 2021\. Any returned values for this field included in an API response will always be NULL\.
The orientation of the input image \(counterclockwise direction\)\. If your application displays the image, you can use this value to correct the orientation\. The bounding box coordinates returned in `CelebrityFaces` and `UnrecognizedFaces` represent face locations before the image orientation is corrected\.   
If the input image is in \.jpeg format, it might contain exchangeable image \(Exif\) metadata that includes the image's orientation\. If so, and the Exif metadata for the input image populates the orientation field, the value of `OrientationCorrection` is null\. The `CelebrityFaces` and `UnrecognizedFaces` bounding box coordinates represent face locations after Exif metadata is used to correct the image orientation\. Images in \.png format don't contain Exif metadata\. 
Type: String  
Valid Values:` ROTATE_0 | ROTATE_90 | ROTATE_180 | ROTATE_270` 

 ** [ UnrecognizedFaces ](#API_RecognizeCelebrities_ResponseSyntax) **   <a name="rekognition-RecognizeCelebrities-response-UnrecognizedFaces"></a>
Details about each unrecognized face in the image\.  
Type: Array of [ ComparedFace ](API_ComparedFace.md) objects

## Errors<a name="API_RecognizeCelebrities_Errors"></a>

 ** AccessDeniedException **   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 ** ImageTooLargeException **   
The input image size exceeds the allowed limit\. If you are calling [ DetectProtectiveEquipment ](API_DetectProtectiveEquipment.md), the image size or resolution exceeds the allowed limit\. For more information, see [Guidelines and quotas in Amazon Rekognition](limits.md)\.   
HTTP Status Code: 400

 ** InternalServerError **   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

 ** InvalidImageFormatException **   
The provided image format is not supported\.   
HTTP Status Code: 400

 ** InvalidImageFormatException **   
The provided image format is not supported\.   
HTTP Status Code: 400

 ** InvalidParameterException **   
Input parameter violated a constraint\. Validate your parameter before calling the API operation again\.  
HTTP Status Code: 400

 ** InvalidS3ObjectException **   
Amazon Rekognition is unable to access the S3 object specified in the request\.  
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **   
The number of requests exceeded your throughput limit\. If you want to increase this limit, contact Amazon Rekognition\.  
HTTP Status Code: 400

 ** ThrottlingException **   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_RecognizeCelebrities_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/RecognizeCelebrities) 
+  [ AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/RecognizeCelebrities) 
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/RecognizeCelebrities) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/RecognizeCelebrities) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/RecognizeCelebrities) 
+  [ AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/RecognizeCelebrities) 
+  [ AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/RecognizeCelebrities) 
+  [ AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/RecognizeCelebrities) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/RecognizeCelebrities) 