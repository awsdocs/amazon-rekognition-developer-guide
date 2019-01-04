# CreateCollection<a name="API_CreateCollection"></a>

Creates a collection in an AWS Region\. You can add faces to the collection using the [IndexFaces](API_IndexFaces.md) operation\. 

For example, you might create collections, one for each of your application users\. A user can then index faces using the `IndexFaces` operation and persist results in a specific collection\. Then, a user can search the collection for faces in the user\-specific container\. 

When you create a collection, it is associated with the latest version of the face model version\.

**Note**  
Collection names are case\-sensitive\.

This operation requires permissions to perform the `rekognition:CreateCollection` action\.

## Request Syntax<a name="API_CreateCollection_RequestSyntax"></a>

```
{
   "[CollectionId](#rekognition-CreateCollection-request-CollectionId)": "string"
}
```

## Request Parameters<a name="API_CreateCollection_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [CollectionId](#API_CreateCollection_RequestSyntax) **   <a name="rekognition-CreateCollection-request-CollectionId"></a>
ID for the collection that you are creating\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

## Response Syntax<a name="API_CreateCollection_ResponseSyntax"></a>

```
{
   "[CollectionArn](#rekognition-CreateCollection-response-CollectionArn)": "string",
   "[FaceModelVersion](#rekognition-CreateCollection-response-FaceModelVersion)": "string",
   "[StatusCode](#rekognition-CreateCollection-response-StatusCode)": number
}
```

## Response Elements<a name="API_CreateCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [CollectionArn](#API_CreateCollection_ResponseSyntax) **   <a name="rekognition-CreateCollection-response-CollectionArn"></a>
Amazon Resource Name \(ARN\) of the collection\. You can use this to manage permissions on your resources\.   
Type: String

 ** [FaceModelVersion](#API_CreateCollection_ResponseSyntax) **   <a name="rekognition-CreateCollection-response-FaceModelVersion"></a>
Version number of the face detection model associated with the collection you are creating\.  
Type: String

 ** [StatusCode](#API_CreateCollection_ResponseSyntax) **   <a name="rekognition-CreateCollection-response-StatusCode"></a>
HTTP status code indicating the result of the operation\.  
Type: Integer  
Valid Range: Minimum value of 0\.

## Errors<a name="API_CreateCollection_Errors"></a>

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

 **ResourceAlreadyExistsException**   
A collection with the specified ID already exists\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_CreateCollection_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/CreateCollection) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/CreateCollection) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CreateCollection) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/CreateCollection) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/CreateCollection) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/CreateCollection) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/CreateCollection) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/CreateCollection) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/CreateCollection) 