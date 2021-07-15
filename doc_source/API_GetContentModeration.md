# GetContentModeration<a name="API_GetContentModeration"></a>

Gets the inappropriate, unwanted, or offensive content analysis results for a Amazon Rekognition Video analysis started by [StartContentModeration](API_StartContentModeration.md)\. For a list of moderation labels in Amazon Rekognition, see [Using the image and video moderation APIs](https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html#moderation-api)\.

Amazon Rekognition Video inappropriate or offensive content detection in a stored video is an asynchronous operation\. You start analysis by calling [StartContentModeration](API_StartContentModeration.md) which returns a job identifier \(`JobId`\)\. When analysis finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartContentModeration`\. To get the results of the content analysis, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`\. If so, call `GetContentModeration` and pass the job identifier \(`JobId`\) from the initial call to `StartContentModeration`\. 

For more information, see [Working with stored videos](video.md)\. 

 `GetContentModeration` returns detected inappropriate, unwanted, or offensive content moderation labels, and the time they are detected, in an array, `ModerationLabels`, of [ContentModerationDetection](API_ContentModerationDetection.md) objects\. 

By default, the moderated labels are returned sorted by time, in milliseconds from the start of the video\. You can also sort them by moderated label by specifying `NAME` for the `SortBy` input parameter\. 

Since video analysis can return a large number of results, use the `MaxResults` parameter to limit the number of labels returned in a single call to `GetContentModeration`\. If there are more results than specified in `MaxResults`, the value of `NextToken` in the operation response contains a pagination token for getting the next set of results\. To get the next page of results, call `GetContentModeration` and populate the `NextToken` request parameter with the value of `NextToken` returned from the previous call to `GetContentModeration`\.

For more information, see [Content moderation](moderation.md)\.

## Request Syntax<a name="API_GetContentModeration_RequestSyntax"></a>

```
{
   "JobId": "string",
   "MaxResults": number,
   "NextToken": "string",
   "SortBy": "string"
}
```

## Request Parameters<a name="API_GetContentModeration_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [JobId](#API_GetContentModeration_RequestSyntax) **   <a name="rekognition-GetContentModeration-request-JobId"></a>
The identifier for the inappropriate, unwanted, or offensive content moderation job\. Use `JobId` to identify the job in a subsequent call to `GetContentModeration`\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$`   
Required: Yes

 ** [MaxResults](#API_GetContentModeration_RequestSyntax) **   <a name="rekognition-GetContentModeration-request-MaxResults"></a>
Maximum number of results to return per paginated call\. The largest value you can specify is 1000\. If you specify a value greater than 1000, a maximum of 1000 results is returned\. The default value is 1000\.  
Type: Integer  
Valid Range: Minimum value of 1\.  
Required: No

 ** [NextToken](#API_GetContentModeration_RequestSyntax) **   <a name="rekognition-GetContentModeration-request-NextToken"></a>
If the previous response was incomplete \(because there is more data to retrieve\), Amazon Rekognition returns a pagination token in the response\. You can use this pagination token to retrieve the next set of content moderation labels\.  
Type: String  
Length Constraints: Maximum length of 255\.  
Required: No

 ** [SortBy](#API_GetContentModeration_RequestSyntax) **   <a name="rekognition-GetContentModeration-request-SortBy"></a>
Sort to use for elements in the `ModerationLabelDetections` array\. Use `TIMESTAMP` to sort array elements by the time labels are detected\. Use `NAME` to alphabetically group elements for a label together\. Within each label group, the array element are sorted by detection confidence\. The default sort is by `TIMESTAMP`\.  
Type: String  
Valid Values:` NAME | TIMESTAMP`   
Required: No

## Response Syntax<a name="API_GetContentModeration_ResponseSyntax"></a>

```
{
   "JobStatus": "string",
   "ModerationLabels": [ 
      { 
         "ModerationLabel": { 
            "Confidence": number,
            "Name": "string",
            "ParentName": "string"
         },
         "Timestamp": number
      }
   ],
   "ModerationModelVersion": "string",
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

## Response Elements<a name="API_GetContentModeration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [JobStatus](#API_GetContentModeration_ResponseSyntax) **   <a name="rekognition-GetContentModeration-response-JobStatus"></a>
The current status of the content moderation analysis job\.  
Type: String  
Valid Values:` IN_PROGRESS | SUCCEEDED | FAILED` 

 ** [ModerationLabels](#API_GetContentModeration_ResponseSyntax) **   <a name="rekognition-GetContentModeration-response-ModerationLabels"></a>
The detected inappropriate, unwanted, or offensive content moderation labels and the time\(s\) they were detected\.  
Type: Array of [ContentModerationDetection](API_ContentModerationDetection.md) objects

 ** [ModerationModelVersion](#API_GetContentModeration_ResponseSyntax) **   <a name="rekognition-GetContentModeration-response-ModerationModelVersion"></a>
Version number of the moderation detection model that was used to detect inappropriate, unwanted, or offensive content\.  
Type: String

 ** [NextToken](#API_GetContentModeration_ResponseSyntax) **   <a name="rekognition-GetContentModeration-response-NextToken"></a>
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of content moderation labels\.   
Type: String  
Length Constraints: Maximum length of 255\.

 ** [StatusMessage](#API_GetContentModeration_ResponseSyntax) **   <a name="rekognition-GetContentModeration-response-StatusMessage"></a>
If the job fails, `StatusMessage` provides a descriptive error message\.  
Type: String

 ** [VideoMetadata](#API_GetContentModeration_ResponseSyntax) **   <a name="rekognition-GetContentModeration-response-VideoMetadata"></a>
Information about a video that Amazon Rekognition analyzed\. `Videometadata` is returned in every page of paginated responses from `GetContentModeration`\.   
Type: [VideoMetadata](API_VideoMetadata.md) object

## Errors<a name="API_GetContentModeration_Errors"></a>

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
The resource specified in the request cannot be found\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_GetContentModeration_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/GetContentModeration) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/GetContentModeration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GetContentModeration) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/GetContentModeration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/GetContentModeration) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/GetContentModeration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/GetContentModeration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/GetContentModeration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/GetContentModeration) 