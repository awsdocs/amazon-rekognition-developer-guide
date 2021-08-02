# UntagResource<a name="API_UntagResource"></a>

 Removes one or more tags from an Amazon Rekognition collection, stream processor, or Custom Labels model\. 

This operation requires permissions to perform the `rekognition:UntagResource` action\. 

## Request Syntax<a name="API_UntagResource_RequestSyntax"></a>

```
{
   "ResourceArn": "string",
   "TagKeys": [ "string" ]
}
```

## Request Parameters<a name="API_UntagResource_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ResourceArn](#API_UntagResource_RequestSyntax) **   <a name="rekognition-UntagResource-request-ResourceArn"></a>
 Amazon Resource Name \(ARN\) of the model, collection, or stream processor that you want to remove the tags from\.   
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="rekognition-UntagResource-request-TagKeys"></a>
 A list of the tags that you want to remove\.   
Type: Array of strings  
Array Members: Minimum number of 0 items\. Maximum number of 200 items\.  
Length Constraints: Minimum length of 1\. Maximum length of 128\.  
Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`   
Required: Yes

## Response Elements<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body\.

## Errors<a name="API_UntagResource_Errors"></a>

 **AccessDeniedException**   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 **InternalServerError**   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

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

## See Also<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/UntagResource) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/UntagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/UntagResource) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/UntagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/UntagResource) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/UntagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/UntagResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/UntagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/UntagResource) 