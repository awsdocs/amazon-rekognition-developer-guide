# DeleteFaces<a name="API_DeleteFaces"></a>

Deletes faces from a collection\. You specify a collection ID and an array of face IDs to remove from the collection\.

This operation requires permissions to perform the `rekognition:DeleteFaces` action\.

## Request Syntax<a name="API_DeleteFaces_RequestSyntax"></a>

```
{
   "[CollectionId](#rekognition-DeleteFaces-request-CollectionId)": "string",
   "[FaceIds](#rekognition-DeleteFaces-request-FaceIds)": [ "string" ]
}
```

## Request Parameters<a name="API_DeleteFaces_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [CollectionId](#API_DeleteFaces_RequestSyntax) **   <a name="rekognition-DeleteFaces-request-CollectionId"></a>
Collection from which to remove the specific faces\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

 ** [FaceIds](#API_DeleteFaces_RequestSyntax) **   <a name="rekognition-DeleteFaces-request-FaceIds"></a>
An array of face IDs to delete\.  
Type: Array of strings  
Array Members: Minimum number of 1 item\. Maximum number of 4096 items\.  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

## Response Syntax<a name="API_DeleteFaces_ResponseSyntax"></a>

```
{
   "[DeletedFaces](#rekognition-DeleteFaces-response-DeletedFaces)": [ "string" ]
}
```

## Response Elements<a name="API_DeleteFaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [DeletedFaces](#API_DeleteFaces_ResponseSyntax) **   <a name="rekognition-DeleteFaces-response-DeletedFaces"></a>
An array of strings \(face IDs\) of the faces that were deleted\.  
Type: Array of strings  
Array Members: Minimum number of 1 item\. Maximum number of 4096 items\.  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` 

## Errors<a name="API_DeleteFaces_Errors"></a>

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

## See Also<a name="API_DeleteFaces_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DeleteFaces) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DeleteFaces) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DeleteFaces) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DeleteFaces) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/DeleteFaces) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DeleteFaces) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DeleteFaces) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DeleteFaces) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DeleteFaces) 