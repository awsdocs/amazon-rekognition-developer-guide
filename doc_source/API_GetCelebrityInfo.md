# GetCelebrityInfo<a name="API_GetCelebrityInfo"></a>

Gets the name and additional information about a celebrity based on his or her Rekognition ID\. The additional information is returned as an array of URLs\. If there is no additional information about the celebrity, this list is empty\. For more information, see [Getting Information about a Celebrity](get-celebrity-info-procedure.md)\.

This operation requires permissions to perform the `rekognition:GetCelebrityInfo` action\. 

## Request Syntax<a name="API_GetCelebrityInfo_RequestSyntax"></a>

```
{
   "[Id](#rekognition-GetCelebrityInfo-request-Id)": "string"
}
```

## Request Parameters<a name="API_GetCelebrityInfo_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [Id](#API_GetCelebrityInfo_RequestSyntax) **   <a name="rekognition-GetCelebrityInfo-request-Id"></a>
The ID for the celebrity\. You get the celebrity ID from a call to the [RecognizeCelebrities](API_RecognizeCelebrities.md) operation, which recognizes celebrities in an image\.   
Type: String  
Pattern: `[0-9A-Za-z]*`   
Required: Yes

## Response Syntax<a name="API_GetCelebrityInfo_ResponseSyntax"></a>

```
{
   "[Name](#rekognition-GetCelebrityInfo-response-Name)": "string",
   "[Urls](#rekognition-GetCelebrityInfo-response-Urls)": [ "string" ]
}
```

## Response Elements<a name="API_GetCelebrityInfo_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [Name](#API_GetCelebrityInfo_ResponseSyntax) **   <a name="rekognition-GetCelebrityInfo-response-Name"></a>
The name of the celebrity\.  
Type: String

 ** [Urls](#API_GetCelebrityInfo_ResponseSyntax) **   <a name="rekognition-GetCelebrityInfo-response-Urls"></a>
An array of URLs pointing to additional celebrity information\.   
Type: Array of strings

## Errors<a name="API_GetCelebrityInfo_Errors"></a>

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

## Example<a name="API_GetCelebrityInfo_Examples"></a>

### Example Request<a name="API_GetCelebrityInfo_Example_1"></a>

The following example shows a request that gets information about a celebrity\.

#### Sample Request<a name="API_GetCelebrityInfo_Example_1_Request"></a>

```
POST https://rekognition.us-west-2.amazonaws.com/ HTTP/1.1
Host: rekognition.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 18
X-Amz-Target: RekognitionService.GetCelebrityInfo
X-Amz-Date: 20170414T184757Z
User-Agent: aws-cli/1.11.47 Python/2.7.9 Windows/8 botocore/1.5.10
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=XXXXX/us-west-2/rekognition/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target,
   Signature=XXXXXXXXXXXXXXXXXXX

{"Id": "3Ir0du6"}
```

#### Sample Response<a name="API_GetCelebrityInfo_Example_1_Response"></a>

```
{
   "Name": "Jeff Bezos",
   "Urls": ["www.imdb.com/name/nm1757263"]
}
```

## See Also<a name="API_GetCelebrityInfo_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS Command Line Interface](http://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/GetCelebrityInfo) 

+  [AWS SDK for \.NET](http://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/GetCelebrityInfo) 

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GetCelebrityInfo) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/GetCelebrityInfo) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/GetCelebrityInfo) 

+  [AWS SDK for JavaScript](http://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/GetCelebrityInfo) 

+  [AWS SDK for PHP V3](http://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/GetCelebrityInfo) 

+  [AWS SDK for Python](http://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/GetCelebrityInfo) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/GetCelebrityInfo) 