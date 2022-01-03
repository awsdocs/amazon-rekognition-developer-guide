# DescribeDataset<a name="API_DescribeDataset"></a>

 Describes an Amazon Rekognition Custom Labels dataset\. You can get information such as the current status of a dataset and statistics about the images and labels in a dataset\. 

This operation requires permissions to perform the `rekognition:DescribeDataset` action\.

## Request Syntax<a name="API_DescribeDataset_RequestSyntax"></a>

```
{
   "DatasetArn": "string"
}
```

## Request Parameters<a name="API_DescribeDataset_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ DatasetArn ](#API_DescribeDataset_RequestSyntax) **   <a name="rekognition-DescribeDataset-request-DatasetArn"></a>
 The Amazon Resource Name \(ARN\) of the dataset that you want to describe\.   
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/dataset\/(train|test)\/[0-9]+$)`   
Required: Yes

## Response Syntax<a name="API_DescribeDataset_ResponseSyntax"></a>

```
{
   "DatasetDescription": { 
      "CreationTimestamp": number,
      "DatasetStats": { 
         "ErrorEntries": number,
         "LabeledEntries": number,
         "TotalEntries": number,
         "TotalLabels": number
      },
      "LastUpdatedTimestamp": number,
      "Status": "string",
      "StatusMessage": "string",
      "StatusMessageCode": "string"
   }
}
```

## Response Elements<a name="API_DescribeDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [ DatasetDescription ](#API_DescribeDataset_ResponseSyntax) **   <a name="rekognition-DescribeDataset-response-DatasetDescription"></a>
 The description for the dataset\.   
Type: [ DatasetDescription ](API_DatasetDescription.md) object

## Errors<a name="API_DescribeDataset_Errors"></a>

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

 ** ThrottlingException **   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_DescribeDataset_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DescribeDataset) 
+  [ AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DescribeDataset) 
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DescribeDataset) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DescribeDataset) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DescribeDataset) 
+  [ AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DescribeDataset) 
+  [ AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DescribeDataset) 
+  [ AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DescribeDataset) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DescribeDataset) 