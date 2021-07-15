# ListStreamProcessors<a name="API_ListStreamProcessors"></a>

Gets a list of stream processors that you have created with [CreateStreamProcessor](API_CreateStreamProcessor.md)\. 

## Request Syntax<a name="API_ListStreamProcessors_RequestSyntax"></a>

```
{
   "MaxResults": number,
   "NextToken": "string"
}
```

## Request Parameters<a name="API_ListStreamProcessors_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [MaxResults](#API_ListStreamProcessors_RequestSyntax) **   <a name="rekognition-ListStreamProcessors-request-MaxResults"></a>
Maximum number of stream processors you want Amazon Rekognition Video to return in the response\. The default is 1000\.   
Type: Integer  
Valid Range: Minimum value of 1\.  
Required: No

 ** [NextToken](#API_ListStreamProcessors_RequestSyntax) **   <a name="rekognition-ListStreamProcessors-request-NextToken"></a>
If the previous response was incomplete \(because there are more stream processors to retrieve\), Amazon Rekognition Video returns a pagination token in the response\. You can use this pagination token to retrieve the next set of stream processors\.   
Type: String  
Length Constraints: Maximum length of 255\.  
Required: No

## Response Syntax<a name="API_ListStreamProcessors_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "StreamProcessors": [ 
      { 
         "Name": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements<a name="API_ListStreamProcessors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [NextToken](#API_ListStreamProcessors_ResponseSyntax) **   <a name="rekognition-ListStreamProcessors-response-NextToken"></a>
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of stream processors\.   
Type: String  
Length Constraints: Maximum length of 255\.

 ** [StreamProcessors](#API_ListStreamProcessors_ResponseSyntax) **   <a name="rekognition-ListStreamProcessors-response-StreamProcessors"></a>
List of stream processors that you have created\.  
Type: Array of [StreamProcessor](API_StreamProcessor.md) objects

## Errors<a name="API_ListStreamProcessors_Errors"></a>

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

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_ListStreamProcessors_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/ListStreamProcessors) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/ListStreamProcessors) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ListStreamProcessors) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ListStreamProcessors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ListStreamProcessors) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/ListStreamProcessors) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/ListStreamProcessors) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/ListStreamProcessors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ListStreamProcessors) 