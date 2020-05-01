# GetFaceDetection<a name="API_GetFaceDetection"></a>

Gets face detection results for a Amazon Rekognition Video analysis started by [StartFaceDetection](API_StartFaceDetection.md)\.

Face detection with Amazon Rekognition Video is an asynchronous operation\. You start face detection by calling [StartFaceDetection](API_StartFaceDetection.md) which returns a job identifier \(`JobId`\)\. When the face detection operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartFaceDetection`\. To get the results of the face detection operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`\. If so, call [GetFaceDetection](#API_GetFaceDetection) and pass the job identifier \(`JobId`\) from the initial call to `StartFaceDetection`\.

 `GetFaceDetection` returns an array of detected faces \(`Faces`\) sorted by the time the faces were detected\. 

Use MaxResults parameter to limit the number of labels returned\. If there are more results than specified in `MaxResults`, the value of `NextToken` in the operation response contains a pagination token for getting the next set of results\. To get the next page of results, call `GetFaceDetection` and populate the `NextToken` request parameter with the token value returned from the previous call to `GetFaceDetection`\.

## Request Syntax<a name="API_GetFaceDetection_RequestSyntax"></a>

```
{
   "[JobId](#rekognition-GetFaceDetection-request-JobId)": "string",
   "[MaxResults](#rekognition-GetFaceDetection-request-MaxResults)": number,
   "[NextToken](#rekognition-GetFaceDetection-request-NextToken)": "string"
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
   "[Faces](#rekognition-GetFaceDetection-response-Faces)": [ 
      { 
         "[Face](API_FaceDetection.md#rekognition-Type-FaceDetection-Face)": { 
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
         },
         "[Timestamp](API_FaceDetection.md#rekognition-Type-FaceDetection-Timestamp)": number
      }
   ],
   "[JobStatus](#rekognition-GetFaceDetection-response-JobStatus)": "string",
   "[NextToken](#rekognition-GetFaceDetection-response-NextToken)": "string",
   "[StatusMessage](#rekognition-GetFaceDetection-response-StatusMessage)": "string",
   "[VideoMetadata](#rekognition-GetFaceDetection-response-VideoMetadata)": { 
      "[Codec](API_VideoMetadata.md#rekognition-Type-VideoMetadata-Codec)": "string",
      "[DurationMillis](API_VideoMetadata.md#rekognition-Type-VideoMetadata-DurationMillis)": number,
      "[Format](API_VideoMetadata.md#rekognition-Type-VideoMetadata-Format)": "string",
      "[FrameHeight](API_VideoMetadata.md#rekognition-Type-VideoMetadata-FrameHeight)": number,
      "[FrameRate](API_VideoMetadata.md#rekognition-Type-VideoMetadata-FrameRate)": number,
      "[FrameWidth](API_VideoMetadata.md#rekognition-Type-VideoMetadata-FrameWidth)": number
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