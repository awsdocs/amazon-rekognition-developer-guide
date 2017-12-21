# DeleteFaces<a name="API_DeleteFaces"></a>

Deletes faces from a collection\. You specify a collection ID and an array of face IDs to remove from the collection\.

This operation requires permissions to perform the `rekognition:DeleteFaces` action\.

## Request Syntax<a name="API_DeleteFaces_RequestSyntax"></a>

```
{
   "CollectionId": "string",
   "FaceIds": [ "string" ]
}
```

## Request Parameters<a name="API_DeleteFaces_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** CollectionId **   
Collection from which to remove the specific faces\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

 ** FaceIds **   
An array of face IDs to delete\.  
Type: Array of strings  
Array Members: Minimum number of 1 item\. Maximum number of 4096 items\.  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

## Response Syntax<a name="API_DeleteFaces_ResponseSyntax"></a>

```
{
   "DeletedFaces": [ "string" ]
}
```

## Response Elements<a name="API_DeleteFaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** DeletedFaces **   
An array of strings \(face IDs\) of the faces that were deleted\.  
Type: Array of strings  
Array Members: Minimum number of 1 item\. Maximum number of 4096 items\.  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` 

## Errors<a name="API_DeleteFaces_Errors"></a>

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

## Example<a name="API_DeleteFaces_Examples"></a>

### Example Request<a name="API_DeleteFaces_Example_1"></a>

The following example shows a request that deletes a face from a collection named examplemyphotos\.

#### Sample Request<a name="API_DeleteFaces_Example_1_Request"></a>

```
POST https://rekognition.us-west-2.amazonaws.com/ HTTP/1.1
Host: rekognition.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 81
X-Amz-Target: RekognitionService.DeleteFaces
X-Amz-Date: 20170105T170305Z
User-Agent: aws-cli/1.11.25 Python/2.7.9 Windows/8 botocore/1.4.82
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=XXXXXXXX/20170105/us-west-2/rekognition/aws4_request,
  SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=XXXXXXXX

{
  "FaceIds":[
     "11111111-2222-3333-4444-555555555555"
  ],
  "CollectionId":"examplemyphotos"
}
```

#### Sample Response<a name="API_DeleteFaces_Example_1_Response"></a>

```
 HTTP/1.1 200 OK
 Content-Type: application/x-amz-json-1.1
 Date: Thu, 05 Jan 2017 17:03:06 GMT
 x-amzn-RequestId: d3c6f630-d368-11e6-96d5-039839f35287
 Content-Length: 57
 Connection: keep-alive

 {
    "DeletedFaces":[
       "11111111-2222-3333-4444-555555555555"
    ]
 }
```

## See Also<a name="API_DeleteFaces_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS Command Line Interface](http://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DeleteFaces) 

+  [AWS SDK for \.NET](http://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DeleteFaces) 

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DeleteFaces) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DeleteFaces) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/DeleteFaces) 

+  [AWS SDK for JavaScript](http://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DeleteFaces) 

+  [AWS SDK for PHP V3](http://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DeleteFaces) 

+  [AWS SDK for Python](http://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DeleteFaces) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/DeleteFaces) 