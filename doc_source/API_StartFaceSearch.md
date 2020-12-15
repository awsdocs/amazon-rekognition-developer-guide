# StartFaceSearch<a name="API_StartFaceSearch"></a>

Starts the asynchronous search for faces in a collection that match the faces of persons detected in a stored video\.

The video must be stored in an Amazon S3 bucket\. Use [Video](API_Video.md) to specify the bucket name and the filename of the video\. `StartFaceSearch` returns a job identifier \(`JobId`\) which you use to get the search results once the search has completed\. When searching is finished, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in `NotificationChannel`\. To get the search results, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`\. If so, call [GetFaceSearch](API_GetFaceSearch.md) and pass the job identifier \(`JobId`\) from the initial call to `StartFaceSearch`\. For more information, see [ Searching stored videos for faces](procedure-person-search-videos.md)\.

## Request Syntax<a name="API_StartFaceSearch_RequestSyntax"></a>

```
{
   "ClientRequestToken": "string",
   "CollectionId": "string",
   "FaceMatchThreshold": number,
   "JobTag": "string",
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

## Request Parameters<a name="API_StartFaceSearch_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ClientRequestToken](#API_StartFaceSearch_RequestSyntax) **   <a name="rekognition-StartFaceSearch-request-ClientRequestToken"></a>
Idempotent token used to identify the start request\. If you use the same token with multiple `StartFaceSearch` requests, the same `JobId` is returned\. Use `ClientRequestToken` to prevent the same job from being accidently started more than once\.   
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$`   
Required: No

 ** [CollectionId](#API_StartFaceSearch_RequestSyntax) **   <a name="rekognition-StartFaceSearch-request-CollectionId"></a>
ID of the collection that contains the faces you want to search for\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

 ** [FaceMatchThreshold](#API_StartFaceSearch_RequestSyntax) **   <a name="rekognition-StartFaceSearch-request-FaceMatchThreshold"></a>
The minimum confidence in the person match to return\. For example, don't return any matches where confidence in matches is less than 70%\. The default value is 80%\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 ** [JobTag](#API_StartFaceSearch_RequestSyntax) **   <a name="rekognition-StartFaceSearch-request-JobTag"></a>
An identifier you specify that's returned in the completion notification that's published to your Amazon Simple Notification Service topic\. For example, you can use `JobTag` to group related jobs and identify them in the completion notification\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 256\.  
Pattern: `[a-zA-Z0-9_.\-:]+`   
Required: No

 ** [NotificationChannel](#API_StartFaceSearch_RequestSyntax) **   <a name="rekognition-StartFaceSearch-request-NotificationChannel"></a>
The ARN of the Amazon SNS topic to which you want Amazon Rekognition Video to publish the completion status of the search\.   
Type: [NotificationChannel](API_NotificationChannel.md) object  
Required: No

 ** [Video](#API_StartFaceSearch_RequestSyntax) **   <a name="rekognition-StartFaceSearch-request-Video"></a>
The video you want to search\. The video must be stored in an Amazon S3 bucket\.   
Type: [Video](API_Video.md) object  
Required: Yes

## Response Syntax<a name="API_StartFaceSearch_ResponseSyntax"></a>

```
{
   "JobId": "string"
}
```

## Response Elements<a name="API_StartFaceSearch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [JobId](#API_StartFaceSearch_ResponseSyntax) **   <a name="rekognition-StartFaceSearch-response-JobId"></a>
The identifier for the search job\. Use `JobId` to identify the job in a subsequent call to `GetFaceSearch`\.   
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$` 

## Errors<a name="API_StartFaceSearch_Errors"></a>

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

 **ResourceNotFoundException**   
The collection specified in the request cannot be found\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

 **VideoTooLargeException**   
The file size or duration of the supplied media is too large\. The maximum file size is 10GB\. The maximum duration is 6 hours\.   
HTTP Status Code: 400

## See Also<a name="API_StartFaceSearch_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/StartFaceSearch) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/StartFaceSearch) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StartFaceSearch) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/StartFaceSearch) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/StartFaceSearch) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/StartFaceSearch) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/StartFaceSearch) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/StartFaceSearch) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StartFaceSearch) 