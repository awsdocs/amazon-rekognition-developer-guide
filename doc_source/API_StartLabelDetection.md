# StartLabelDetection<a name="API_StartLabelDetection"></a>

Starts asynchronous detection of labels in a stored video\.

Rekognition Video can detect labels in a video\. Labels are instances of real\-world entities\. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; concepts like landscape, evening, and nature; and activities like a person getting out of a car or a person skiing\.

The video must be stored in an Amazon S3 bucket\. Use [Video](API_Video.md) to specify the bucket name and the filename of the video\. `StartLabelDetection` returns a job identifier \(`JobId`\) which you use to get the results of the operation\. When label detection is finished, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in `NotificationChannel`\.

To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`\. If so, call [GetLabelDetection](API_GetLabelDetection.md) and pass the job identifier \(`JobId`\) from the initial call to `StartLabelDetection`\.



## Request Syntax<a name="API_StartLabelDetection_RequestSyntax"></a>

```
{
   "ClientRequestToken": "string",
   "JobTag": "string",
   "MinConfidence": number,
   "NotificationChannel": { 
      "RoleArn": "string",
      "SNSTopicArn": "string"
   },
   "Video": { 
      "S3Object": { 
         "Bucket": "string",
         "Name": "string",
         "Version": "string"
      }
   }
}
```

## Request Parameters<a name="API_StartLabelDetection_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** ClientRequestToken **   
Idempotent token used to identify the start request\. If you use the same token with multiple `StartLabelDetection` requests, the same `JobId` is returned\. Use `ClientRequestToken` to prevent the same job from being accidently started more than once\.   
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$`   
Required: No

 ** JobTag **   
Unique identifier you specify to identify the job in the completion status published to the Amazon Simple Notification Service topic\.   
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 256\.  
Pattern: `[a-zA-Z0-9_.\-:]+`   
Required: No

 ** MinConfidence **   
Specifies the minimum confidence that Rekognition Video must have in order to return a detected label\. Confidence represents how certain Amazon Rekognition is that a label is correctly identified\.0 is the lowest confidence\. 100 is the highest confidence\. Rekognition Video doesn't return any labels with a confidence level lower than this specified value\.  
If you don't specify `MinConfidence`, the operation returns labels with confidence values greater than or equal to 50 percent\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 ** NotificationChannel **   
The Amazon SNS topic ARN you want Rekognition Video to publish the completion status of the label detection operation to\.   
Type: [NotificationChannel](API_NotificationChannel.md) object  
Required: No

 ** Video **   
The video in which you want to detect labels\. The video must be stored in an Amazon S3 bucket\.  
Type: [Video](API_Video.md) object  
Required: Yes

## Response Syntax<a name="API_StartLabelDetection_ResponseSyntax"></a>

```
{
   "JobId": "string"
}
```

## Response Elements<a name="API_StartLabelDetection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** JobId **   
The identifier for the label detection job\. Use `JobId` to identify the job in a subsequent call to `GetLabelDetection`\.   
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$` 

## Errors<a name="API_StartLabelDetection_Errors"></a>

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
  
HTTP Status Code: 400

 **ProvisionedThroughputExceededException**   
The number of requests exceeded your throughput limit\. If you want to increase this limit, contact Amazon Rekognition\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

 **VideoTooLargeException**   
The file size or duration of the supplied media is too large\. The maximum file size is 8GB\. The maximum duration is 2 hours\.   
HTTP Status Code: 400

## See Also<a name="API_StartLabelDetection_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS Command Line Interface](http://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/StartLabelDetection) 

+  [AWS SDK for \.NET](http://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/StartLabelDetection) 

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StartLabelDetection) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/StartLabelDetection) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/StartLabelDetection) 

+  [AWS SDK for JavaScript](http://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/StartLabelDetection) 

+  [AWS SDK for PHP V3](http://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/StartLabelDetection) 

+  [AWS SDK for Python](http://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/StartLabelDetection) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/StartLabelDetection) 