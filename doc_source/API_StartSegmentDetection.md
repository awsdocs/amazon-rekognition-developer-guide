# StartSegmentDetection<a name="API_StartSegmentDetection"></a>

Starts asynchronous detection of segment detection in a stored video\.

Amazon Rekognition Video can detect segments in a video stored in an Amazon S3 bucket\. Use [Video](API_Video.md) to specify the bucket name and the filename of the video\. `StartSegmentDetection` returns a job identifier \(`JobId`\) which you use to get the results of the operation\. When segment detection is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in `NotificationChannel`\.

You can use the `Filters` \([StartSegmentDetectionFilters](API_StartSegmentDetectionFilters.md)\) input parameter to specify the minimum detection confidence returned in the response\. Within `Filters`, use `ShotFilter` \([StartShotDetectionFilter](API_StartShotDetectionFilter.md)\) to filter detected shots\. Use `TechnicalCueFilter` \([StartTechnicalCueDetectionFilter](API_StartTechnicalCueDetectionFilter.md)\) to filter technical cues\. 

To get the results of the segment detection operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`\. if so, call [GetSegmentDetection](API_GetSegmentDetection.md) and pass the job identifier \(`JobId`\) from the initial call to `StartSegmentDetection`\. 

For more information, see [Detecting video segments in stored video](segments.md)\. 

## Request Syntax<a name="API_StartSegmentDetection_RequestSyntax"></a>

```
{
   "ClientRequestToken": "string",
   "Filters": { 
      "ShotFilter": { 
         "MinSegmentConfidence": number
      },
      "TechnicalCueFilter": { 
         "MinSegmentConfidence": number
      }
   },
   "JobTag": "string",
   "NotificationChannel": { 
      "RoleArn": "string",
      "SNSTopicArn": "string"
   },
   "SegmentTypes": [ "string" ],
   "Video": { 
      "S3Object": { 
         "Bucket": "string",
         "Name": "string",
         "Version": "string"
      }
   }
}
```

## Request Parameters<a name="API_StartSegmentDetection_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ClientRequestToken](#API_StartSegmentDetection_RequestSyntax) **   <a name="rekognition-StartSegmentDetection-request-ClientRequestToken"></a>
Idempotent token used to identify the start request\. If you use the same token with multiple `StartSegmentDetection` requests, the same `JobId` is returned\. Use `ClientRequestToken` to prevent the same job from being accidently started more than once\.   
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$`   
Required: No

 ** [Filters](#API_StartSegmentDetection_RequestSyntax) **   <a name="rekognition-StartSegmentDetection-request-Filters"></a>
Filters for technical cue or shot detection\.  
Type: [StartSegmentDetectionFilters](API_StartSegmentDetectionFilters.md) object  
Required: No

 ** [JobTag](#API_StartSegmentDetection_RequestSyntax) **   <a name="rekognition-StartSegmentDetection-request-JobTag"></a>
An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic\. For example, you can use `JobTag` to group related jobs and identify them in the completion notification\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 256\.  
Pattern: `[a-zA-Z0-9_.\-:]+`   
Required: No

 ** [NotificationChannel](#API_StartSegmentDetection_RequestSyntax) **   <a name="rekognition-StartSegmentDetection-request-NotificationChannel"></a>
The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the completion status of the segment detection operation\.  
Type: [NotificationChannel](API_NotificationChannel.md) object  
Required: No

 ** [SegmentTypes](#API_StartSegmentDetection_RequestSyntax) **   <a name="rekognition-StartSegmentDetection-request-SegmentTypes"></a>
An array of segment types to detect in the video\. Valid values are TECHNICAL\_CUE and SHOT\.  
Type: Array of strings  
Array Members: Minimum number of 1 item\.  
Valid Values:` TECHNICAL_CUE | SHOT`   
Required: Yes

 ** [Video](#API_StartSegmentDetection_RequestSyntax) **   <a name="rekognition-StartSegmentDetection-request-Video"></a>
Video file stored in an Amazon S3 bucket\. Amazon Rekognition video start operations such as [StartLabelDetection](API_StartLabelDetection.md) use `Video` to specify a video for analysis\. The supported file formats are \.mp4, \.mov and \.avi\.  
Type: [Video](API_Video.md) object  
Required: Yes

## Response Syntax<a name="API_StartSegmentDetection_ResponseSyntax"></a>

```
{
   "JobId": "string"
}
```

## Response Elements<a name="API_StartSegmentDetection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [JobId](#API_StartSegmentDetection_ResponseSyntax) **   <a name="rekognition-StartSegmentDetection-response-JobId"></a>
Unique identifier for the segment detection job\. The `JobId` is returned from `StartSegmentDetection`\.   
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$` 

## Errors<a name="API_StartSegmentDetection_Errors"></a>

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

## See Also<a name="API_StartSegmentDetection_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/StartSegmentDetection) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/StartSegmentDetection) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StartSegmentDetection) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/StartSegmentDetection) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/StartSegmentDetection) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/StartSegmentDetection) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/StartSegmentDetection) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/StartSegmentDetection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StartSegmentDetection) 