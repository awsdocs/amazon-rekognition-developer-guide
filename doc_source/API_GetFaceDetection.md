# GetFaceDetection<a name="API_GetFaceDetection"></a>

Gets face detection results for a Amazon Rekognition Video analysis started by [StartFaceDetection](API_StartFaceDetection.md)\.

Face detection with Amazon Rekognition Video is an asynchronous operation\. You start face detection by calling [StartFaceDetection](API_StartFaceDetection.md) which returns a job identifier \(`JobId`\)\. When the face detection operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartFaceDetection`\. To get the results of the face detection operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`\. If so, call [GetFaceDetection](#API_GetFaceDetection) and pass the job identifier \(`JobId`\) from the initial call to `StartFaceDetection`\.

 `GetFaceDetection` returns an array of detected faces \(`Faces`\) sorted by the time the faces were detected\. 

Use MaxResults parameter to limit the number of labels returned\. If there are more results than specified in `MaxResults`, the value of `NextToken` in the operation response contains a pagination token for getting the next set of results\. To get the next page of results, call `GetFaceDetection` and populate the `NextToken` request parameter with the token value returned from the previous call to `GetFaceDetection`\.

## Request Syntax<a name="API_GetFaceDetection_RequestSyntax"></a>

```
{
   "JobId": "string",
   "MaxResults": number,
   "NextToken": "string"
}
```

## Request Parameters<a name="API_GetFaceDetection_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [JobId](#API_GetFaceDetection_RequestSyntax) **   <a name="rekognition-GetFaceDetection-request-JobId"></a>
Unique identifier for the face detection job\. The `JobId` is returned from `StartFaceDetection`\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$`   
Required: Yes

 ** [MaxResults](#API_GetFaceDetection_RequestSyntax) **   <a name="rekognition-GetFaceDetection-request-MaxResults"></a>
Maximum number of results to return per paginated call\. The largest value you can specify is 1000\. If you specify a value greater than 1000, a maximum of 1000 results is returned\. The default value is 1000\.  
Type: Integer  
Valid Range: Minimum value of 1\.  
Required: No

 ** [NextToken](#API_GetFaceDetection_RequestSyntax) **   <a name="rekognition-GetFaceDetection-request-NextToken"></a>
If the previous response was incomplete \(because there are more faces to retrieve\), Amazon Rekognition Video returns a pagination token in the response\. You can use this pagination token to retrieve the next set of faces\.  
Type: String  
Length Constraints: Maximum length of 255\.  
Required: No

## Response Syntax<a name="API_GetFaceDetection_ResponseSyntax"></a>

```
{
   "Faces": [ 
      { 
         "Face": { 
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
         "Timestamp": number
      }
   ],
   "JobStatus": "string",
   "NextToken": "string",
   "StatusMessage": "string",
   "VideoMetadata": { 
      "Codec": "string",
      "DurationMillis": number,
      "Format": "string",
      "FrameHeight": number,
      "FrameRate": number,
      "FrameWidth": number
   }
}
```

## Response Elements<a name="API_GetFaceDetection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [Faces](#API_GetFaceDetection_ResponseSyntax) **   <a name="rekognition-GetFaceDetection-response-Faces"></a>
An array of faces detected in the video\. Each element contains a detected face's details and the time, in milliseconds from the start of the video, the face was detected\.   
Type: Array of [FaceDetection](API_FaceDetection.md) objects

 ** [JobStatus](#API_GetFaceDetection_ResponseSyntax) **   <a name="rekognition-GetFaceDetection-response-JobStatus"></a>
The current status of the face detection job\.  
Type: String  
Valid Values:` IN_PROGRESS | SUCCEEDED | FAILED` 

 ** [NextToken](#API_GetFaceDetection_ResponseSyntax) **   <a name="rekognition-GetFaceDetection-response-NextToken"></a>
If the response is truncated, Amazon Rekognition returns this token that you can use in the subsequent request to retrieve the next set of faces\.   
Type: String  
Length Constraints: Maximum length of 255\.

 ** [StatusMessage](#API_GetFaceDetection_ResponseSyntax) **   <a name="rekognition-GetFaceDetection-response-StatusMessage"></a>
If the job fails, `StatusMessage` provides a descriptive error message\.  
Type: String

 ** [VideoMetadata](#API_GetFaceDetection_ResponseSyntax) **   <a name="rekognition-GetFaceDetection-response-VideoMetadata"></a>
Information about a video that Amazon Rekognition Video analyzed\. `Videometadata` is returned in every page of paginated responses from a Amazon Rekognition video operation\.  
Type: [VideoMetadata](API_VideoMetadata.md) object

## Errors<a name="API_GetFaceDetection_Errors"></a>

 **AccessDeniedException**   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 **InternalServerError**   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

 **InvalidPaginationTokenException**   
Pagination token in the request is not valid\.  
HTTP Status Code: 400

 **InvalidParameterException**   
Input parameter violated a constraint\. Validate your parameter before calling the API operation again\.  
HTTP Status Code: 400

 **ProvisionedThroughputExceededException**   
The number of requests exceeded your throughput limit\. If you want to increase this limit, contact Amazon Rekognition\.  
HTTP Status Code: 400

 **ResourceNotFoundException**   
The collection specified in the request cannot be found\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_GetFaceDetection_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/GetFaceDetection) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/GetFaceDetection) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GetFaceDetection) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/GetFaceDetection) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/GetFaceDetection) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/GetFaceDetection) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/GetFaceDetection) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/GetFaceDetection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/GetFaceDetection) 