# DeleteProject<a name="API_DeleteProject"></a>

Deletes an Amazon Rekognition Custom Labels project\. To delete a project you must first delete all models associated with the project\. To delete a model, see [ DeleteProjectVersion ](API_DeleteProjectVersion.md)\.

This operation requires permissions to perform the `rekognition:DeleteProject` action\. 

## Request Syntax<a name="API_DeleteProject_RequestSyntax"></a>

```
{
   "ProjectArn": "string"
}
```

## Request Parameters<a name="API_DeleteProject_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ ProjectArn ](#API_DeleteProject_RequestSyntax) **   <a name="rekognition-DeleteProject-request-ProjectArn"></a>
The Amazon Resource Name \(ARN\) of the project that you want to delete\.  
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`   
Required: Yes

## Response Syntax<a name="API_DeleteProject_ResponseSyntax"></a>

```
{
   "Status": "string"
}
```

## Response Elements<a name="API_DeleteProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [ Status ](#API_DeleteProject_ResponseSyntax) **   <a name="rekognition-DeleteProject-response-Status"></a>
The current status of the delete project operation\.  
Type: String  
Valid Values:` CREATING | CREATED | DELETING` 

## Errors<a name="API_DeleteProject_Errors"></a>

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

 ** ResourceInUseException **   
The specified resource is already being used\.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The resource specified in the request cannot be found\.  
HTTP Status Code: 400

 ** ThrottlingException **   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_DeleteProject_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DeleteProject) 
+  [ AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DeleteProject) 
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DeleteProject) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DeleteProject) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DeleteProject) 
+  [ AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DeleteProject) 
+  [ AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DeleteProject) 
+  [ AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DeleteProject) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DeleteProject) 