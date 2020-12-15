# GetTextDetection<a name="API_GetTextDetection"></a>

Gets the text detection results of a Amazon Rekognition Video analysis started by [StartTextDetection](API_StartTextDetection.md)\.

Text detection with Amazon Rekognition Video is an asynchronous operation\. You start text detection by calling [StartTextDetection](API_StartTextDetection.md) which returns a job identifier \(`JobId`\) When the text detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartTextDetection`\. To get the results of the text detection operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`\. if so, call `GetTextDetection` and pass the job identifier \(`JobId`\) from the initial call of `StartLabelDetection`\.

 `GetTextDetection` returns an array of detected text \(`TextDetections`\) sorted by the time the text was detected, up to 50 words per frame of video\.

Each element of the array includes the detected text, the precentage confidence in the acuracy of the detected text, the time the text was detected, bounding box information for where the text was located, and unique identifiers for words and their lines\.

Use MaxResults parameter to limit the number of text detections returned\. If there are more results than specified in `MaxResults`, the value of `NextToken` in the operation response contains a pagination token for getting the next set of results\. To get the next page of results, call `GetTextDetection` and populate the `NextToken` request parameter with the token value returned from the previous call to `GetTextDetection`\.

## Request Syntax<a name="API_GetTextDetection_RequestSyntax"></a>

```
{
   "JobId": "string",
   "MaxResults": number,
   "NextToken": "string"
}
```

## Request Parameters<a name="API_GetTextDetection_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [JobId](#API_GetTextDetection_RequestSyntax) **   <a name="rekognition-GetTextDetection-request-JobId"></a>
Job identifier for the text detection operation for which you want results returned\. You get the job identifer from an initial call to `StartTextDetection`\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$`   
Required: Yes

 ** [MaxResults](#API_GetTextDetection_RequestSyntax) **   <a name="rekognition-GetTextDetection-request-MaxResults"></a>
Maximum number of results to return per paginated call\. The largest value you can specify is 1000\.  
Type: Integer  
Valid Range: Minimum value of 1\.  
Required: No

 ** [NextToken](#API_GetTextDetection_RequestSyntax) **   <a name="rekognition-GetTextDetection-request-NextToken"></a>
If the previous response was incomplete \(because there are more labels to retrieve\), Amazon Rekognition Video returns a pagination token in the response\. You can use this pagination token to retrieve the next set of text\.  
Type: String  
Length Constraints: Maximum length of 255\.  
Required: No

## Response Syntax<a name="API_GetTextDetection_ResponseSyntax"></a>

```
{
   "JobStatus": "string",
   "NextToken": "string",
   "StatusMessage": "string",
   "TextDetections": [ 
      { 
         "TextDetection": { 
            "Confidence": number,
            "DetectedText": "string",
            "Geometry": { 
               "BoundingBox": { 
                  "Height": number,
                  "Left": number,
                  "Top": number,
                  "Width": number
               },
               "Polygon": [ 
                  { 
                     "X": number,
                     "Y": number
                  }
               ]
            },
            "Id": number,
            "ParentId": number,
            "Type": "string"
         },
         "Timestamp": number
      }
   ],
   "TextModelVersion": "string",
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

## Response Elements<a name="API_GetTextDetection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [JobStatus](#API_GetTextDetection_ResponseSyntax) **   <a name="rekognition-GetTextDetection-response-JobStatus"></a>
Current status of the text detection job\.  
Type: String  
Valid Values:` IN_PROGRESS | SUCCEEDED | FAILED` 

 ** [NextToken](#API_GetTextDetection_ResponseSyntax) **   <a name="rekognition-GetTextDetection-response-NextToken"></a>
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of text\.  
Type: String  
Length Constraints: Maximum length of 255\.

 ** [StatusMessage](#API_GetTextDetection_ResponseSyntax) **   <a name="rekognition-GetTextDetection-response-StatusMessage"></a>
If the job fails, `StatusMessage` provides a descriptive error message\.  
Type: String

 ** [TextDetections](#API_GetTextDetection_ResponseSyntax) **   <a name="rekognition-GetTextDetection-response-TextDetections"></a>
An array of text detected in the video\. Each element contains the detected text, the time in milliseconds from the start of the video that the text was detected, and where it was detected on the screen\.  
Type: Array of [TextDetectionResult](API_TextDetectionResult.md) objects

 ** [TextModelVersion](#API_GetTextDetection_ResponseSyntax) **   <a name="rekognition-GetTextDetection-response-TextModelVersion"></a>
Version number of the text detection model that was used to detect text\.  
Type: String

 ** [VideoMetadata](#API_GetTextDetection_ResponseSyntax) **   <a name="rekognition-GetTextDetection-response-VideoMetadata"></a>
Information about a video that Amazon Rekognition analyzed\. `Videometadata` is returned in every page of paginated responses from a Amazon Rekognition video operation\.  
Type: [VideoMetadata](API_VideoMetadata.md) object

## Errors<a name="API_GetTextDetection_Errors"></a>

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

## See Also<a name="API_GetTextDetection_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/GetTextDetection) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/GetTextDetection) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GetTextDetection) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/GetTextDetection) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/GetTextDetection) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/GetTextDetection) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/GetTextDetection) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/GetTextDetection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/GetTextDetection) 