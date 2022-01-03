# DistributeDatasetEntries<a name="API_DistributeDatasetEntries"></a>

Distributes the entries \(images\) in a training dataset across the training dataset and the test dataset for a project\. `DistributeDatasetEntries` moves 20% of the training dataset images to the test dataset\. An entry is a JSON Line that describes an image\. 

You supply the Amazon Resource Names \(ARN\) of a project's training dataset and test dataset\. The training dataset must contain the images that you want to split\. The test dataset must be empty\. The datasets must belong to the same project\. To create training and test datasets for a project, call [ CreateDataset ](API_CreateDataset.md)\.

Distributing a dataset takes a while to complete\. To check the status call `DescribeDataset`\. The operation is complete when the `Status` field for the training dataset and the test dataset is `UPDATE_COMPLETE`\. If the dataset split fails, the value of `Status` is `UPDATE_FAILED`\.

This operation requires permissions to perform the `rekognition:DistributeDatasetEntries` action\.

## Request Syntax<a name="API_DistributeDatasetEntries_RequestSyntax"></a>

```
{
   "Datasets": [ 
      { 
         "Arn": "string"
      }
   ]
}
```

## Request Parameters<a name="API_DistributeDatasetEntries_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ Datasets ](#API_DistributeDatasetEntries_RequestSyntax) **   <a name="rekognition-DistributeDatasetEntries-request-Datasets"></a>
The ARNS for the training dataset and test dataset that you want to use\. The datasets must belong to the same project\. The test dataset must be empty\.   
Type: Array of [ DistributeDataset ](API_DistributeDataset.md) objects  
Array Members: Fixed number of 2 items\.  
Required: Yes

## Response Elements<a name="API_DistributeDatasetEntries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body\.

## Errors<a name="API_DistributeDatasetEntries_Errors"></a>

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

 ** ResourceNotReadyException **   
The requested resource isn't ready\. For example, this exception occurs when you call `DetectCustomLabels` with a model version that isn't deployed\.   
HTTP Status Code: 400

 ** ThrottlingException **   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_DistributeDatasetEntries_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DistributeDatasetEntries) 
+  [ AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DistributeDatasetEntries) 
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DistributeDatasetEntries) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DistributeDatasetEntries) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DistributeDatasetEntries) 
+  [ AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DistributeDatasetEntries) 
+  [ AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DistributeDatasetEntries) 
+  [ AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DistributeDatasetEntries) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DistributeDatasetEntries) 