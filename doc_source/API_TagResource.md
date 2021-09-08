# TagResource<a name="API_TagResource"></a>

 Adds one or more key\-value tags to an Amazon Rekognition collection, stream processor, or Custom Labels model\. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)\. 

This operation requires permissions to perform the `rekognition:TagResource` action\. 

## Request Syntax<a name="API_TagResource_RequestSyntax"></a>

```
{
   "ResourceArn": "string",
   "Tags": { 
      "string" : "string" 
   }
}
```

## Request Parameters<a name="API_TagResource_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ ResourceArn ](#API_TagResource_RequestSyntax) **   <a name="rekognition-TagResource-request-ResourceArn"></a>
 Amazon Resource Name \(ARN\) of the model, collection, or stream processor that you want to assign the tags to\.   
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Required: Yes

 ** [ Tags ](#API_TagResource_RequestSyntax) **   <a name="rekognition-TagResource-request-Tags"></a>
 The key\-value tags to assign to the resource\.   
Type: String to string map  
Map Entries: Minimum number of 0 items\. Maximum number of 200 items\.  
Key Length Constraints: Minimum length of 1\. Maximum length of 128\.  
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`   
Value Length Constraints: Minimum length of 0\. Maximum length of 256\.  
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`   
Required: Yes

## Response Elements<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body\.

## Errors<a name="API_TagResource_Errors"></a>

 ** AccessDeniedException **   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 ** InternalServerError **   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

 ** InvalidParameterException **   
Input parameter violated a constraint\. Validate your parameter before calling the API operation again\.  
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **   
The number of requests exceeded your throughput limit\. If you want to increase this limit, contact Amazon Rekognition\.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The resource specified in the request cannot be found\.  
HTTP Status Code: 400

 ** ServiceQuotaExceededException **   
  
The size of the resource exceeds the allowed limit\. For more information, see [Guidelines and quotas in Amazon Rekognition](limits.md)\.   
HTTP Status Code: 400

 ** ThrottlingException **   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/TagResource) 
+  [ AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/TagResource) 
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/TagResource) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/TagResource) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/TagResource) 
+  [ AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/TagResource) 
+  [ AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/TagResource) 
+  [ AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/TagResource) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/TagResource) 