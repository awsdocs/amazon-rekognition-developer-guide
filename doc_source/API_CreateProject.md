# CreateProject<a name="API_CreateProject"></a>

Creates a new Amazon Rekognition Custom Labels project\. A project is a group of resources \(datasets, model versions\) that you use to create and manage Amazon Rekognition Custom Labels models\. 

This operation requires permissions to perform the `rekognition:CreateProject` action\.

## Request Syntax<a name="API_CreateProject_RequestSyntax"></a>

```
{
   "ProjectName": "string"
}
```

## Request Parameters<a name="API_CreateProject_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ ProjectName ](#API_CreateProject_RequestSyntax) **   <a name="rekognition-CreateProject-request-ProjectName"></a>
The name of the project to create\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

## Response Syntax<a name="API_CreateProject_ResponseSyntax"></a>

```
{
   "ProjectArn": "string"
}
```

## Response Elements<a name="API_CreateProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [ ProjectArn ](#API_CreateProject_ResponseSyntax) **   <a name="rekognition-CreateProject-response-ProjectArn"></a>
The Amazon Resource Name \(ARN\) of the new project\. You can use the ARN to configure IAM access to the project\.   
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)` 

## Errors<a name="API_CreateProject_Errors"></a>

 ** AccessDeniedException **   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 ** InternalServerError **   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

 ** InvalidParameterException **   
Input parameter violated a constraint\. Validate your parameter before calling the API operation again\.  
HTTP Status Code: 400

 ** LimitExceededException **   
An Amazon Rekognition service limit was exceeded\. For example, if you start too many Amazon Rekognition Video jobs concurrently, calls to start operations \(`StartLabelDetection`, for example\) will raise a `LimitExceededException` exception \(HTTP status code: 400\) until the number of concurrently running jobs is below the Amazon Rekognition service limit\.   
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **   
The number of requests exceeded your throughput limit\. If you want to increase this limit, contact Amazon Rekognition\.  
HTTP Status Code: 400

 ** ResourceInUseException **   
The specified resource is already being used\.  
HTTP Status Code: 400

 ** ThrottlingException **   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_CreateProject_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/CreateProject) 
+  [ AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/CreateProject) 
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CreateProject) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/CreateProject) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/CreateProject) 
+  [ AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/CreateProject) 
+  [ AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/CreateProject) 
+  [ AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/CreateProject) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CreateProject) 