# DescribeCollection<a name="API_DescribeCollection"></a>

Describes the specified collection\. You can use `DescribeCollection` to get information, such as the number of faces indexed into a collection and the version of the model used by the collection for face detection\.

For more information, see [Describing a Collection](describe-collection-procedure.md)\.

## Request Syntax<a name="API_DescribeCollection_RequestSyntax"></a>

```
{
   "[CollectionId](#rekognition-DescribeCollection-request-CollectionId)": "string"
}
```

## Request Parameters<a name="API_DescribeCollection_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [CollectionId](#API_DescribeCollection_RequestSyntax) **   <a name="rekognition-DescribeCollection-request-CollectionId"></a>
The ID of the collection to describe\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

## Response Syntax<a name="API_DescribeCollection_ResponseSyntax"></a>

```
{
   "[CollectionARN](#rekognition-DescribeCollection-response-CollectionARN)": "string",
   "[CreationTimestamp](#rekognition-DescribeCollection-response-CreationTimestamp)": number,
   "[FaceCount](#rekognition-DescribeCollection-response-FaceCount)": number,
   "[FaceModelVersion](#rekognition-DescribeCollection-response-FaceModelVersion)": "string"
}
```

## Response Elements<a name="API_DescribeCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [CollectionARN](#API_DescribeCollection_ResponseSyntax) **   <a name="rekognition-DescribeCollection-response-CollectionARN"></a>
The Amazon Resource Name \(ARN\) of the collection\.  
Type: String

 ** [CreationTimestamp](#API_DescribeCollection_ResponseSyntax) **   <a name="rekognition-DescribeCollection-response-CreationTimestamp"></a>
The number of milliseconds since the Unix epoch time until the creation of the collection\. The Unix epoch time is 00:00:00 Coordinated Universal Time \(UTC\), Thursday, 1 January 1970\.  
Type: Timestamp

 ** [FaceCount](#API_DescribeCollection_ResponseSyntax) **   <a name="rekognition-DescribeCollection-response-FaceCount"></a>
The number of faces that are indexed into the collection\. To index faces into a collection, use [IndexFaces](API_IndexFaces.md)\.  
Type: Long  
Valid Range: Minimum value of 0\.

 ** [FaceModelVersion](#API_DescribeCollection_ResponseSyntax) **   <a name="rekognition-DescribeCollection-response-FaceModelVersion"></a>
The version of the face model that's used by the collection for face detection\.  
For more information, see [Model Versioning](face-detection-model.md)\.  
Type: String

## Errors<a name="API_DescribeCollection_Errors"></a>

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

 **ResourceNotFoundException**   
The collection specified in the request cannot be found\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_DescribeCollection_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DescribeCollection) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DescribeCollection) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DescribeCollection) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DescribeCollection) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/DescribeCollection) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DescribeCollection) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DescribeCollection) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DescribeCollection) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/DescribeCollection) 