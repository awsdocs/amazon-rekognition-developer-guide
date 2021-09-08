# GetCelebrityInfo<a name="API_GetCelebrityInfo"></a>

Gets the name and additional information about a celebrity based on their Amazon Rekognition ID\. The additional information is returned as an array of URLs\. If there is no additional information about the celebrity, this list is empty\.

For more information, see [Getting information about a celebrity](get-celebrity-info-procedure.md)\.

This operation requires permissions to perform the `rekognition:GetCelebrityInfo` action\. 

## Request Syntax<a name="API_GetCelebrityInfo_RequestSyntax"></a>

```
{
   "Id": "string"
}
```

## Request Parameters<a name="API_GetCelebrityInfo_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ Id ](#API_GetCelebrityInfo_RequestSyntax) **   <a name="rekognition-GetCelebrityInfo-request-Id"></a>
The ID for the celebrity\. You get the celebrity ID from a call to the [ RecognizeCelebrities ](API_RecognizeCelebrities.md) operation, which recognizes celebrities in an image\.   
Type: String  
Pattern: `[0-9A-Za-z]*`   
Required: Yes

## Response Syntax<a name="API_GetCelebrityInfo_ResponseSyntax"></a>

```
{
   "KnownGender": { 
      "Type": "string"
   },
   "Name": "string",
   "Urls": [ "string" ]
}
```

## Response Elements<a name="API_GetCelebrityInfo_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [ KnownGender ](#API_GetCelebrityInfo_ResponseSyntax) **   <a name="rekognition-GetCelebrityInfo-response-KnownGender"></a>
Retrieves the known gender for the celebrity\.  
Type: [ KnownGender ](API_KnownGender.md) object

 ** [ Name ](#API_GetCelebrityInfo_ResponseSyntax) **   <a name="rekognition-GetCelebrityInfo-response-Name"></a>
The name of the celebrity\.  
Type: String

 ** [ Urls ](#API_GetCelebrityInfo_ResponseSyntax) **   <a name="rekognition-GetCelebrityInfo-response-Urls"></a>
An array of URLs pointing to additional celebrity information\.   
Type: Array of strings  
Array Members: Minimum number of 0 items\. Maximum number of 255 items\.

## Errors<a name="API_GetCelebrityInfo_Errors"></a>

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

## See Also<a name="API_GetCelebrityInfo_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/GetCelebrityInfo) 
+  [ AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/GetCelebrityInfo) 
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GetCelebrityInfo) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/GetCelebrityInfo) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/GetCelebrityInfo) 
+  [ AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/GetCelebrityInfo) 
+  [ AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/GetCelebrityInfo) 
+  [ AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/GetCelebrityInfo) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/GetCelebrityInfo) 