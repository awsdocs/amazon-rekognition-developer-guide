# ListCollections<a name="API_ListCollections"></a>

Returns list of collection IDs in your account\. If the result is truncated, the response also provides a `NextToken` that you can use in the subsequent request to fetch the next set of collection IDs\.

For an example, see [Listing Collections](list-collection-procedure.md)\.

This operation requires permissions to perform the `rekognition:ListCollections` action\.

## Request Syntax<a name="API_ListCollections_RequestSyntax"></a>

```
{
   "[MaxResults](#rekognition-ListCollections-request-MaxResults)": number,
   "[NextToken](#rekognition-ListCollections-request-NextToken)": "string"
}
```

## Request Parameters<a name="API_ListCollections_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [MaxResults](#API_ListCollections_RequestSyntax) **   <a name="rekognition-ListCollections-request-MaxResults"></a>
Maximum number of collection IDs to return\.   
Type: Integer  
Valid Range: Minimum value of 0\. Maximum value of 4096\.  
Required: No

 ** [NextToken](#API_ListCollections_RequestSyntax) **   <a name="rekognition-ListCollections-request-NextToken"></a>
Pagination token from the previous response\.  
Type: String  
Length Constraints: Maximum length of 255\.  
Required: No

## Response Syntax<a name="API_ListCollections_ResponseSyntax"></a>

```
{
   "[CollectionIds](#rekognition-ListCollections-response-CollectionIds)": [ "string" ],
   "[FaceModelVersions](#rekognition-ListCollections-response-FaceModelVersions)": [ "string" ],
   "[NextToken](#rekognition-ListCollections-response-NextToken)": "string"
}
```

## Response Elements<a name="API_ListCollections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [CollectionIds](#API_ListCollections_ResponseSyntax) **   <a name="rekognition-ListCollections-response-CollectionIds"></a>
An array of collection IDs\.  
Type: Array of strings  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+` 

 ** [FaceModelVersions](#API_ListCollections_ResponseSyntax) **   <a name="rekognition-ListCollections-response-FaceModelVersions"></a>
Version numbers of the face detection models associated with the collections in the array `CollectionIds`\. For example, the value of `FaceModelVersions[2]` is the version number for the face detection model used by the collection in `CollectionId[2]`\.  
Type: Array of strings

 ** [NextToken](#API_ListCollections_ResponseSyntax) **   <a name="rekognition-ListCollections-response-NextToken"></a>
If the result is truncated, the response provides a `NextToken` that you can use in the subsequent request to fetch the next set of collection IDs\.  
Type: String  
Length Constraints: Maximum length of 255\.

## Errors<a name="API_ListCollections_Errors"></a>

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

 **ResourceNotFoundException**   
The collection specified in the request cannot be found\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## Example<a name="API_ListCollections_Examples"></a>

### Example Request<a name="API_ListCollections_Example_1"></a>

The following example shows a request that lists the available collections\.

#### Sample Request<a name="API_ListCollections_Example_1_Request"></a>

```
POST https://rekognition.us-west-2.amazonaws.com/ HTTP/1.1
Host: rekognition.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: RekognitionService.ListCollections
X-Amz-Date: 20170105T155800Z
User-Agent: aws-cli/1.11.25 Python/2.7.9 Windows/8 botocore/1.4.82
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=XXXXXXXX/20170105/us-west-2/rekognition/aws4_request,
  SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=XXXXXXXX

{}
```

#### Sample Response<a name="API_ListCollections_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: Thu, 05 Jan 2017 15:58:07 GMT
x-amzn-RequestId: bfe63e6c-d35f-11e6-840b-e97493937970
Content-Length: 45
Connection: keep-alive

{
   "CollectionIds":[
      "mycollection",
      "examplemyphotos"
   ],
   "FaceModelVersions":[
     "2.0",
     "2.0"
     ]
}
```

## See Also<a name="API_ListCollections_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS Command Line Interface](http://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/ListCollections) 

+  [AWS SDK for \.NET](http://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/ListCollections) 

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ListCollections) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ListCollections) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/ListCollections) 

+  [AWS SDK for JavaScript](http://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/ListCollections) 

+  [AWS SDK for PHP V3](http://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/ListCollections) 

+  [AWS SDK for Python](http://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/ListCollections) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/ListCollections) 