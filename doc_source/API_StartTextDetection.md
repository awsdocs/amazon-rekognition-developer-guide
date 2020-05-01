# StartTextDetection<a name="API_StartTextDetection"></a>

Starts asynchronous detection of text in a stored video\.

Amazon Rekognition Video can detect text in a video stored in an Amazon S3 bucket\. Use [Video](API_Video.md) to specify the bucket name and the filename of the video\. `StartTextDetection` returns a job identifier \(`JobId`\) which you use to get the results of the operation\. When text detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in `NotificationChannel`\.

To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`\. if so, call [GetTextDetection](API_GetTextDetection.md) and pass the job identifier \(`JobId`\) from the initial call to `StartTextDetection`\. 

## Request Syntax<a name="API_StartTextDetection_RequestSyntax"></a>

```
{
   "[ClientRequestToken](#rekognition-StartTextDetection-request-ClientRequestToken)": "string",
   "[Filters](#rekognition-StartTextDetection-request-Filters)": { 
      "[RegionsOfInterest](API_StartTextDetectionFilters.md#rekognition-Type-StartTextDetectionFilters-RegionsOfInterest)": [ 
         { 
            "[BoundingBox](API_RegionOfInterest.md#rekognition-Type-RegionOfInterest-BoundingBox)": { 
               "[Height](API_BoundingBox.md#rekognition-Type-BoundingBox-Height)": number,
               "[Left](API_BoundingBox.md#rekognition-Type-BoundingBox-Left)": number,
               "[Top](API_BoundingBox.md#rekognition-Type-BoundingBox-Top)": number,
               "[Width](API_BoundingBox.md#rekognition-Type-BoundingBox-Width)": number
            }
         }
      ],
      "[WordFilter](API_StartTextDetectionFilters.md#rekognition-Type-StartTextDetectionFilters-WordFilter)": { 
         "[MinBoundingBoxHeight](API_DetectionFilter.md#rekognition-Type-DetectionFilter-MinBoundingBoxHeight)": number,
         "[MinBoundingBoxWidth](API_DetectionFilter.md#rekognition-Type-DetectionFilter-MinBoundingBoxWidth)": number,
         "[MinConfidence](API_DetectionFilter.md#rekognition-Type-DetectionFilter-MinConfidence)": number
      }
   },
   "[JobTag](#rekognition-StartTextDetection-request-JobTag)": "string",
   "[NotificationChannel](#rekognition-StartTextDetection-request-NotificationChannel)": { 
      "[RoleArn](API_NotificationChannel.md#rekognition-Type-NotificationChannel-RoleArn)": "string",
      "[SNSTopicArn](API_NotificationChannel.md#rekognition-Type-NotificationChannel-SNSTopicArn)": "string"
   },
   "[Video](#rekognition-StartTextDetection-request-Video)": { 
      "[S3Object](API_Video.md#rekognition-Type-Video-S3Object)": { 
         "[Bucket](API_S3Object.md#rekognition-Type-S3Object-Bucket)": "string",
         "[Name](API_S3Object.md#rekognition-Type-S3Object-Name)": "string",
         "[Version](API_S3Object.md#rekognition-Type-S3Object-Version)": "string"
      }
   }
}
```

## Request Parameters<a name="API_StartTextDetection_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ClientRequestToken](#API_StartTextDetection_RequestSyntax) **   <a name="rekognition-StartTextDetection-request-ClientRequestToken"></a>
Idempotent token used to identify the start request\. If you use the same token with multiple `StartTextDetection` requests, the same `JobId` is returned\. Use `ClientRequestToken` to prevent the same job from being accidentaly started more than once\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$`   
Required: No

 ** [Filters](#API_StartTextDetection_RequestSyntax) **   <a name="rekognition-StartTextDetection-request-Filters"></a>
Optional parameters that let you set criteria the text must meet to be included in your response\.  
Type: [StartTextDetectionFilters](API_StartTextDetectionFilters.md) object  
Required: No

 ** [JobTag](#API_StartTextDetection_RequestSyntax) **   <a name="rekognition-StartTextDetection-request-JobTag"></a>
An identifier returned in the completion status published by your Amazon Simple Notification Service topic\. For example, you can use `JobTag` to group related jobs and identify them in the completion notification\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 256\.  
Pattern: `[a-zA-Z0-9_.\-:]+`   
Required: No

 ** [NotificationChannel](#API_StartTextDetection_RequestSyntax) **   <a name="rekognition-StartTextDetection-request-NotificationChannel"></a>
The Amazon Simple Notification Service topic to which Amazon Rekognition publishes the completion status of a video analysis operation\. For more information, see [Calling Amazon Rekognition Video Operations](api-video.md)\.  
Type: [NotificationChannel](API_NotificationChannel.md) object  
Required: No

 ** [Video](#API_StartTextDetection_RequestSyntax) **   <a name="rekognition-StartTextDetection-request-Video"></a>
Video file stored in an Amazon S3 bucket\. Amazon Rekognition video start operations such as [StartLabelDetection](API_StartLabelDetection.md) use `Video` to specify a video for analysis\. The supported file formats are \.mp4, \.mov and \.avi\.  
Type: [Video](API_Video.md) object  
Required: Yes

## Response Syntax<a name="API_StartTextDetection_ResponseSyntax"></a>

```
{
   "[JobId](#rekognition-StartTextDetection-response-JobId)": "string"
}
```

## Response Elements<a name="API_StartTextDetection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [JobId](#API_StartTextDetection_ResponseSyntax) **   <a name="rekognition-StartTextDetection-response-JobId"></a>
Identifier for the text detection job\. Use `JobId` to identify the job in a subsequent call to `GetTextDetection`\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$` 

## Errors<a name="API_StartTextDetection_Errors"></a>

 **AccessDeniedException**   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 **IdempotentParameterMismatchException**   
A `ClientRequestToken` input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation\.  
HTTP Status Code: 400

 **InternalServerError**   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

 **InvalidParameterException**   
Input parameter violated a constraint\. Validate your parameter before calling the API operation again\.  
HTTP Status Code: 400

 **InvalidS3ObjectException**   
Amazon Rekognition is unable to access the S3 object specified in the request\.  
HTTP Status Code: 400

 **LimitExceededException**   
An Amazon Rekognition service limit was exceeded\. For example, if you start too many Amazon Rekognition Video jobs concurrently, calls to start operations \(`StartLabelDetection`, for example\) will raise a `LimitExceededException` exception \(HTTP status code: 400\) until the number of concurrently running jobs is below the Amazon Rekognition service limit\.   
HTTP Status Code: 400

 **ProvisionedThroughputExceededException**   
The number of requests exceeded your throughput limit\. If you want to increase this limit, contact Amazon Rekognition\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

 **VideoTooLargeException**   
The file size or duration of the supplied media is too large\. The maximum file size is 10GB\. The maximum duration is 6 hours\.   
HTTP Status Code: 400

## See Also<a name="API_StartTextDetection_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/StartTextDetection) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/StartTextDetection) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StartTextDetection) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/StartTextDetection) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/StartTextDetection) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/StartTextDetection) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/StartTextDetection) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/StartTextDetection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StartTextDetection) 