# ListDatasetEntries<a name="API_ListDatasetEntries"></a>

 Lists the entries \(images\) within a dataset\. An entry is a JSON Line that contains the information for a single image, including the image location, assigned labels, and object location bounding boxes\. For more information, see [Creating a manifest file](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-manifest-files.html)\.

JSON Lines in the response include information about non\-terminal errors found in the dataset\. Non terminal errors are reported in `errors` lists within each JSON Line\. The same information is reported in the training and testing validation result manifests that Amazon Rekognition Custom Labels creates during model training\. 

You can filter the response in variety of ways, such as choosing which labels to return and returning JSON Lines created after a specific date\. 

This operation requires permissions to perform the `rekognition:ListDatasetEntries` action\.

## Request Syntax<a name="API_ListDatasetEntries_RequestSyntax"></a>

```
{
   "ContainsLabels": [ "string" ],
   "DatasetArn": "string",
   "HasErrors": boolean,
   "Labeled": boolean,
   "MaxResults": number,
   "NextToken": "string",
   "SourceRefContains": "string"
}
```

## Request Parameters<a name="API_ListDatasetEntries_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ ContainsLabels ](#API_ListDatasetEntries_RequestSyntax) **   <a name="rekognition-ListDatasetEntries-request-ContainsLabels"></a>
Specifies a label filter for the response\. The response includes an entry only if one or more of the labels in `ContainsLabels` exist in the entry\.   
Type: Array of strings  
Array Members: Minimum number of 1 item\. Maximum number of 10 items\.  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `.{1,}`   
Required: No

 ** [ DatasetArn ](#API_ListDatasetEntries_RequestSyntax) **   <a name="rekognition-ListDatasetEntries-request-DatasetArn"></a>
 The Amazon Resource Name \(ARN\) for the dataset that you want to use\.   
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/dataset\/(train|test)\/[0-9]+$)`   
Required: Yes

 ** [ HasErrors ](#API_ListDatasetEntries_RequestSyntax) **   <a name="rekognition-ListDatasetEntries-request-HasErrors"></a>
Specifies an error filter for the response\. Specify `True` to only include entries that have errors\.   
Type: Boolean  
Required: No

 ** [ Labeled ](#API_ListDatasetEntries_RequestSyntax) **   <a name="rekognition-ListDatasetEntries-request-Labeled"></a>
 Specify `true` to get only the JSON Lines where the image is labeled\. Specify `false` to get only the JSON Lines where the image isn't labeled\. If you don't specify `Labeled`, `ListDatasetEntries` returns JSON Lines for labeled and unlabeled images\.   
Type: Boolean  
Required: No

 ** [ MaxResults ](#API_ListDatasetEntries_RequestSyntax) **   <a name="rekognition-ListDatasetEntries-request-MaxResults"></a>
The maximum number of results to return per paginated call\. The largest value you can specify is 100\. If you specify a value greater than 100, a ValidationException error occurs\. The default value is 100\.   
Type: Integer  
Valid Range: Minimum value of 1\. Maximum value of 100\.  
Required: No

 ** [ NextToken ](#API_ListDatasetEntries_RequestSyntax) **   <a name="rekognition-ListDatasetEntries-request-NextToken"></a>
If the previous response was incomplete \(because there is more results to retrieve\), Amazon Rekognition Custom Labels returns a pagination token in the response\. You can use this pagination token to retrieve the next set of results\.   
Type: String  
Length Constraints: Maximum length of 1024\.  
Required: No

 ** [ SourceRefContains ](#API_ListDatasetEntries_RequestSyntax) **   <a name="rekognition-ListDatasetEntries-request-SourceRefContains"></a>
If specified, `ListDatasetEntries` only returns JSON Lines where the value of `SourceRefContains` is part of the `source-ref` field\. The `source-ref` field contains the Amazon S3 location of the image\. You can use `SouceRefContains` for tasks such as getting the JSON Line for a single image, or gettting JSON Lines for all images within a specific folder\.  
For more information, see [ Creating a manifest file\.](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-manifest-files.html)   
For more information, see Creating a manifest file in the *Amazon Rekognition Custom Labels Developer Guide*\.   
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 2048\.  
Pattern: `.*\S.*`   
Required: No

## Response Syntax<a name="API_ListDatasetEntries_ResponseSyntax"></a>

```
{
   "DatasetEntries": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements<a name="API_ListDatasetEntries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [ DatasetEntries ](#API_ListDatasetEntries_ResponseSyntax) **   <a name="rekognition-ListDatasetEntries-response-DatasetEntries"></a>
 A list of entries \(images\) in the dataset\.   
Type: Array of strings  
Length Constraints: Minimum length of 1\. Maximum length of 100000\.  
Pattern: `^\{.*\}$` 

 ** [ NextToken ](#API_ListDatasetEntries_ResponseSyntax) **   <a name="rekognition-ListDatasetEntries-response-NextToken"></a>
If the previous response was incomplete \(because there is more results to retrieve\), Amazon Rekognition Custom Labels returns a pagination token in the response\. You can use this pagination token to retrieve the next set of results\.   
Type: String  
Length Constraints: Maximum length of 1024\.

## Errors<a name="API_ListDatasetEntries_Errors"></a>

 ** AccessDeniedException **   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 ** InternalServerError **   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

 ** InvalidPaginationTokenException **   
Pagination token in the request is not valid\.  
HTTP Status Code: 400

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

 ** ResourceNotReadyException **   
The requested resource isn't ready\. For example, this exception occurs when you call `DetectCustomLabels` with a model version that isn't deployed\.   
HTTP Status Code: 400

 ** ThrottlingException **   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_ListDatasetEntries_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/ListDatasetEntries) 
+  [ AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/ListDatasetEntries) 
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ListDatasetEntries) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ListDatasetEntries) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ListDatasetEntries) 
+  [ AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/ListDatasetEntries) 
+  [ AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/ListDatasetEntries) 
+  [ AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/ListDatasetEntries) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ListDatasetEntries) 