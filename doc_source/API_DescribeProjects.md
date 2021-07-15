# DescribeProjects<a name="API_DescribeProjects"></a>

Lists and gets information about your Amazon Rekognition Custom Labels projects\.

This operation requires permissions to perform the `rekognition:DescribeProjects` action\.

## Request Syntax<a name="API_DescribeProjects_RequestSyntax"></a>

```
{
   "MaxResults": number,
   "NextToken": "string"
}
```

## Request Parameters<a name="API_DescribeProjects_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [MaxResults](#API_DescribeProjects_RequestSyntax) **   <a name="rekognition-DescribeProjects-request-MaxResults"></a>
The maximum number of results to return per paginated call\. The largest value you can specify is 100\. If you specify a value greater than 100, a ValidationException error occurs\. The default value is 100\.   
Type: Integer  
Valid Range: Minimum value of 1\. Maximum value of 100\.  
Required: No

 ** [NextToken](#API_DescribeProjects_RequestSyntax) **   <a name="rekognition-DescribeProjects-request-NextToken"></a>
If the previous response was incomplete \(because there is more results to retrieve\), Amazon Rekognition Custom Labels returns a pagination token in the response\. You can use this pagination token to retrieve the next set of results\.   
Type: String  
Length Constraints: Maximum length of 1024\.  
Required: No

## Response Syntax<a name="API_DescribeProjects_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ProjectDescriptions": [ 
      { 
         "CreationTimestamp": number,
         "ProjectArn": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements<a name="API_DescribeProjects_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [NextToken](#API_DescribeProjects_ResponseSyntax) **   <a name="rekognition-DescribeProjects-response-NextToken"></a>
If the previous response was incomplete \(because there is more results to retrieve\), Amazon Rekognition Custom Labels returns a pagination token in the response\. You can use this pagination token to retrieve the next set of results\.   
Type: String  
Length Constraints: Maximum length of 1024\.

 ** [ProjectDescriptions](#API_DescribeProjects_ResponseSyntax) **   <a name="rekognition-DescribeProjects-response-ProjectDescriptions"></a>
A list of project descriptions\. The list is sorted by the date and time the projects are created\.  
Type: Array of [ProjectDescription](API_ProjectDescription.md) objects

## Errors<a name="API_DescribeProjects_Errors"></a>

 **AccessDeniedException**   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 **InternalServerError**   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

 **InvalidPaginationTokenException**   
Pagination token in the request is not valid\.  
HTTP Status Code: 400

 **InvalidParameterException**   
Input parameter violated a constraint\. Validate your parameter before calling the API operation again\.  
HTTP Status Code: 400

 **ProvisionedThroughputExceededException**   
The number of requests exceeded your throughput limit\. If you want to increase this limit, contact Amazon Rekognition\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_DescribeProjects_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DescribeProjects) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DescribeProjects) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DescribeProjects) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DescribeProjects) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DescribeProjects) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DescribeProjects) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DescribeProjects) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DescribeProjects) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DescribeProjects) 