# DeleteCollection<a name="API_DeleteCollection"></a>

Deletes the specified collection\. Note that this operation removes all faces in the collection\. For an example, see [Deleting a Collection](delete-collection-procedure.md)\.

This operation requires permissions to perform the `rekognition:DeleteCollection` action\.

## Request Syntax<a name="API_DeleteCollection_RequestSyntax"></a>

```
{
   "[CollectionId](#rekognition-DeleteCollection-request-CollectionId)": "string"
}
```

## Request Parameters<a name="API_DeleteCollection_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [CollectionId](#API_DeleteCollection_RequestSyntax) **   <a name="rekognition-DeleteCollection-request-CollectionId"></a>
ID of the collection to delete\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

## Response Syntax<a name="API_DeleteCollection_ResponseSyntax"></a>

```
{
   "[StatusCode](#rekognition-DeleteCollection-response-StatusCode)": number
}
```

## Response Elements<a name="API_DeleteCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [StatusCode](#API_DeleteCollection_ResponseSyntax) **   <a name="rekognition-DeleteCollection-response-StatusCode"></a>
HTTP status code that indicates the result of the operation\.  
Type: Integer  
Valid Range: Minimum value of 0\.

## Errors<a name="API_DeleteCollection_Errors"></a>

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
The collection specified in the request cannot be found\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_DeleteCollection_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DeleteCollection) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DeleteCollection) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DeleteCollection) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DeleteCollection) 
+  [AWS SDK for Go \- Pilot](https://docs.aws.amazon.com/goto/SdkForGoPilot/rekognition-2016-06-27/DeleteCollection) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/DeleteCollection) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DeleteCollection) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DeleteCollection) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DeleteCollection) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/DeleteCollection) 