# StartProjectVersion<a name="API_StartProjectVersion"></a>

Starts the running of the version of a model\. Starting a model takes a while to complete\. To check the current state of the model, use [ DescribeProjectVersions ](API_DescribeProjectVersions.md)\.

Once the model is running, you can detect custom labels in new images by calling [ DetectCustomLabels ](API_DetectCustomLabels.md)\.

**Note**  
You are charged for the amount of time that the model is running\. To stop a running model, call [ StopProjectVersion ](API_StopProjectVersion.md)\.

This operation requires permissions to perform the `rekognition:StartProjectVersion` action\.

## Request Syntax<a name="API_StartProjectVersion_RequestSyntax"></a>

```
{
   "MinInferenceUnits": number,
   "ProjectVersionArn": "string"
}
```

## Request Parameters<a name="API_StartProjectVersion_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ MinInferenceUnits ](#API_StartProjectVersion_RequestSyntax) **   <a name="rekognition-StartProjectVersion-request-MinInferenceUnits"></a>
The minimum number of inference units to use\. A single inference unit represents 1 hour of processing and can support up to 5 Transaction Pers Second \(TPS\)\. Use a higher number to increase the TPS throughput of your model\. You are charged for the number of inference units that you use\.   
Type: Integer  
Valid Range: Minimum value of 1\.  
Required: Yes

 ** [ ProjectVersionArn ](#API_StartProjectVersion_RequestSyntax) **   <a name="rekognition-StartProjectVersion-request-ProjectVersionArn"></a>
The Amazon Resource Name\(ARN\) of the model version that you want to start\.  
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/version\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`   
Required: Yes

## Response Syntax<a name="API_StartProjectVersion_ResponseSyntax"></a>

```
{
   "Status": "string"
}
```

## Response Elements<a name="API_StartProjectVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [ Status ](#API_StartProjectVersion_ResponseSyntax) **   <a name="rekognition-StartProjectVersion-response-Status"></a>
The current running status of the model\.   
Type: String  
Valid Values:` TRAINING_IN_PROGRESS | TRAINING_COMPLETED | TRAINING_FAILED | STARTING | RUNNING | FAILED | STOPPING | STOPPED | DELETING` 

## Errors<a name="API_StartProjectVersion_Errors"></a>

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

 ** ResourceNotFoundException **   
The resource specified in the request cannot be found\.  
HTTP Status Code: 400

 ** ThrottlingException **   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_StartProjectVersion_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/StartProjectVersion) 
+  [ AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/StartProjectVersion) 
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StartProjectVersion) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/StartProjectVersion) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/StartProjectVersion) 
+  [ AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/StartProjectVersion) 
+  [ AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/StartProjectVersion) 
+  [ AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/StartProjectVersion) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StartProjectVersion) 