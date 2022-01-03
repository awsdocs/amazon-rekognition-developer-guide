# UpdateDatasetEntries<a name="API_UpdateDatasetEntries"></a>

Adds or updates one or more entries \(images\) in a dataset\. An entry is a JSON Line which contains the information for a single image, including the image location, assigned labels, and object location bounding boxes\. For more information, see [Image\-Level labels in manifest files ](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-manifest-file-classification.html) and [Object localization in manifest files](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-manifest-file-object-detection.html)\. 

If the `source-ref` field in the JSON line references an existing image, the existing image in the dataset is updated\. If `source-ref` field doesn't reference an existing image, the image is added as a new image to the dataset\. 

You specify the changes that you want to make in the `Changes` input parameter\. There isn't a limit to the number JSON Lines that you can change, but the size of `Changes` must be less than 5MB\.

 `UpdateDatasetEntries` returns immediatly, but the dataset update might take a while to complete\. Use [ DescribeDataset ](API_DescribeDataset.md) to check the current status\. The dataset updated successfully if the value of `Status` is `UPDATE_COMPLETE`\. 

To check if any non\-terminal errors occured, call [ ListDatasetEntries ](API_ListDatasetEntries.md) and check for the presence of `errors` lists in the JSON Lines\.

Dataset update fails if a terminal error occurs \(`Status` = `UPDATE_FAILED`\)\. Currently, you can't access the terminal error information from the Amazon Rekognition Custom Labels SDK\. 

This operation requires permissions to perform the `rekognition:UpdateDatasetEntries` action\.

## Request Syntax<a name="API_UpdateDatasetEntries_RequestSyntax"></a>

```
{
   "Changes": { 
      "GroundTruth": blob
   },
   "DatasetArn": "string"
}
```

## Request Parameters<a name="API_UpdateDatasetEntries_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ Changes ](#API_UpdateDatasetEntries_RequestSyntax) **   <a name="rekognition-UpdateDatasetEntries-request-Changes"></a>
 The changes that you want to make to the dataset\.   
Type: [ DatasetChanges ](API_DatasetChanges.md) object  
Required: Yes

 ** [ DatasetArn ](#API_UpdateDatasetEntries_RequestSyntax) **   <a name="rekognition-UpdateDatasetEntries-request-DatasetArn"></a>
 The Amazon Resource Name \(ARN\) of the dataset that you want to update\.   
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/dataset\/(train|test)\/[0-9]+$)`   
Required: Yes

## Response Elements<a name="API_UpdateDatasetEntries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body\.

## Errors<a name="API_UpdateDatasetEntries_Errors"></a>

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

## See Also<a name="API_UpdateDatasetEntries_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/UpdateDatasetEntries) 
+  [ AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/UpdateDatasetEntries) 
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/UpdateDatasetEntries) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/UpdateDatasetEntries) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/UpdateDatasetEntries) 
+  [ AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/UpdateDatasetEntries) 
+  [ AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/UpdateDatasetEntries) 
+  [ AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/UpdateDatasetEntries) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/UpdateDatasetEntries) 