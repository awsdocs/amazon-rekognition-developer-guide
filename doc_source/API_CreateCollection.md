# CreateCollection<a name="API_CreateCollection"></a>

Creates a collection in an AWS Region\. You can add faces to the collection using the [IndexFaces](API_IndexFaces.md) operation\. 

For example, you might create collections, one for each of your application users\. A user can then index faces using the `IndexFaces` operation and persist results in a specific collection\. Then, a user can search the collection for faces in the user\-specific container\. 

**Note**  
Collection names are case\-sensitive\.

This operation requires permissions to perform the `rekognition:CreateCollection` action\.

## Request Syntax<a name="API_CreateCollection_RequestSyntax"></a>

```
{
   "CollectionId": "string"
}
```

## Request Parameters<a name="API_CreateCollection_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** CollectionId **   
ID for the collection that you are creating\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

## Response Syntax<a name="API_CreateCollection_ResponseSyntax"></a>

```
{
   "CollectionArn": "string",
   "FaceModelVersion": "string",
   "StatusCode": number
}
```

## Response Elements<a name="API_CreateCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** CollectionArn **   
Amazon Resource Name \(ARN\) of the collection\. You can use this to manage permissions on your resources\.   
Type: String

 ** FaceModelVersion **   
Version number of the face detection model associated with the collection you are creating\.  
Type: String

 ** StatusCode **   
HTTP status code indicating the result of the operation\.  
Type: Integer  
Valid Range: Minimum value of 0\.

## Errors<a name="API_CreateCollection_Errors"></a>

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

 **ResourceAlreadyExistsException**   
A collection with the specified ID already exists\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## Example<a name="API_CreateCollection_Examples"></a>

### Example Request<a name="API_CreateCollection_Example_1"></a>

The following example shows a request that creates a collection named mycollection\.

#### Sample Request<a name="API_CreateCollection_Example_1_Request"></a>

```
POST https://rekognition.us-west-2.amazonaws.com/ HTTP/1.1
Host: rekognition.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 32
X-Amz-Target: RekognitionService.CreateCollection
X-Amz-Date: 20170105T155520Z
User-Agent: aws-cli/1.11.25 Python/2.7.9 Windows/8 botocore/1.4.82
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=XXXXXXXXXXXXXXXXXX/20170105/us-west-2/rekognition/aws4_request,
  SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

{"CollectionId": "mycollection"}
```

#### Sample Response<a name="API_CreateCollection_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: Thu, 05 Jan 2017 15:55:22 GMT
x-amzn-RequestId: 5d4c8b73-d35f-11e6-96d5-039839f35287
Content-Length: 99
Connection: keep-alive
{
   "CollectionArn":"aws:rekognition:us-west-2:11111111111:collection/mycollection",
   "FaceModelVersion":"2.0",
   "StatusCode":200
}
```

## See Also<a name="API_CreateCollection_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS Command Line Interface](http://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/CreateCollection) 

+  [AWS SDK for \.NET](http://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/CreateCollection) 

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CreateCollection) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/CreateCollection) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/CreateCollection) 

+  [AWS SDK for JavaScript](http://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/CreateCollection) 

+  [AWS SDK for PHP V3](http://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/CreateCollection) 

+  [AWS SDK for Python](http://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/CreateCollection) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/CreateCollection) 