# DeleteDataset<a name="API_DeleteDataset"></a>

Deletes an existing Amazon Rekognition Custom Labels dataset\. Deleting a dataset might take while\. Use [ DescribeDataset ](API_DescribeDataset.md) to check the current status\. The dataset is still deleting if the value of `Status` is `DELETE_IN_PROGRESS`\. If you try to access the dataset after it is deleted, you get a `ResourceNotFoundException` exception\. 

You can't delete a dataset while it is creating \(`Status` = `CREATE_IN_PROGRESS`\) or if the dataset is updating \(`Status` = `UPDATE_IN_PROGRESS`\)\.

This operation requires permissions to perform the `rekognition:DeleteDataset` action\.

## Request Syntax<a name="API_DeleteDataset_RequestSyntax"></a>

```
{
   "DatasetArn": "string"
}
```

## Request Parameters<a name="API_DeleteDataset_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ DatasetArn ](#API_DeleteDataset_RequestSyntax) **   <a name="rekognition-DeleteDataset-request-DatasetArn"></a>
 The ARN of the Amazon Rekognition Custom Labels dataset that you want to delete\.   
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/dataset\/(train|test)\/[0-9]+$)`   
Required: Yes

## Response Elements<a name="API_DeleteDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body\.

## Errors<a name="API_DeleteDataset_Errors"></a>

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

## See Also<a name="API_DeleteDataset_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DeleteDataset) 
+  [ AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DeleteDataset) 
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DeleteDataset) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DeleteDataset) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DeleteDataset) 
+  [ AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DeleteDataset) 
+  [ AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DeleteDataset) 
+  [ AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DeleteDataset) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DeleteDataset) 