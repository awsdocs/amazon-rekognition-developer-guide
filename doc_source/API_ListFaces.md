# ListFaces<a name="API_ListFaces"></a>

Returns metadata for faces in the specified collection\. This metadata includes information such as the bounding box coordinates, the confidence \(that the bounding box contains a face\), and face ID\. For an example, see [Listing Faces in a Collection](list-faces-in-collection-procedure.md)\. 

This operation requires permissions to perform the `rekognition:ListFaces` action\.

## Request Syntax<a name="API_ListFaces_RequestSyntax"></a>

```
{
   "[CollectionId](#rekognition-ListFaces-request-CollectionId)": "string",
   "[MaxResults](#rekognition-ListFaces-request-MaxResults)": number,
   "[NextToken](#rekognition-ListFaces-request-NextToken)": "string"
}
```

## Request Parameters<a name="API_ListFaces_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [CollectionId](#API_ListFaces_RequestSyntax) **   <a name="rekognition-ListFaces-request-CollectionId"></a>
ID of the collection from which to list the faces\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

 ** [MaxResults](#API_ListFaces_RequestSyntax) **   <a name="rekognition-ListFaces-request-MaxResults"></a>
Maximum number of faces to return\.  
Type: Integer  
Valid Range: Minimum value of 0\. Maximum value of 4096\.  
Required: No

 ** [NextToken](#API_ListFaces_RequestSyntax) **   <a name="rekognition-ListFaces-request-NextToken"></a>
If the previous response was incomplete \(because there is more data to retrieve\), Amazon Rekognition returns a pagination token in the response\. You can use this pagination token to retrieve the next set of faces\.  
Type: String  
Length Constraints: Maximum length of 255\.  
Required: No

## Response Syntax<a name="API_ListFaces_ResponseSyntax"></a>

```
{
   "[FaceModelVersion](#rekognition-ListFaces-response-FaceModelVersion)": "string",
   "[Faces](#rekognition-ListFaces-response-Faces)": [ 
      { 
         "[BoundingBox](API_Face.md#rekognition-Type-Face-BoundingBox)": { 
            "[Height](API_BoundingBox.md#rekognition-Type-BoundingBox-Height)": number,
            "[Left](API_BoundingBox.md#rekognition-Type-BoundingBox-Left)": number,
            "[Top](API_BoundingBox.md#rekognition-Type-BoundingBox-Top)": number,
            "[Width](API_BoundingBox.md#rekognition-Type-BoundingBox-Width)": number
         },
         "[Confidence](API_Face.md#rekognition-Type-Face-Confidence)": number,
         "[ExternalImageId](API_Face.md#rekognition-Type-Face-ExternalImageId)": "string",
         "[FaceId](API_Face.md#rekognition-Type-Face-FaceId)": "string",
         "[ImageId](API_Face.md#rekognition-Type-Face-ImageId)": "string"
      }
   ],
   "[NextToken](#rekognition-ListFaces-response-NextToken)": "string"
}
```

## Response Elements<a name="API_ListFaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [FaceModelVersion](#API_ListFaces_ResponseSyntax) **   <a name="rekognition-ListFaces-response-FaceModelVersion"></a>
Version number of the face detection model associated with the input collection \(`CollectionId`\)\.  
Type: String

 ** [Faces](#API_ListFaces_ResponseSyntax) **   <a name="rekognition-ListFaces-response-Faces"></a>
An array of `Face` objects\.   
Type: Array of [Face](API_Face.md) objects

 ** [NextToken](#API_ListFaces_ResponseSyntax) **   <a name="rekognition-ListFaces-response-NextToken"></a>
If the response is truncated, Amazon Rekognition returns this token that you can use in the subsequent request to retrieve the next set of faces\.  
Type: String

## Errors<a name="API_ListFaces_Errors"></a>

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

## Example<a name="API_ListFaces_Examples"></a>

### Example Request<a name="API_ListFaces_Example_1"></a>

The following example shows a request that lists the faces in a collection \(examplemyphotos\)\.

#### Sample Request<a name="API_ListFaces_Example_1_Request"></a>

```
POST https://rekognition.us-west-2.amazonaws.com/ HTTP/1.1
Host: rekognition.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 28
X-Amz-Target: RekognitionService.ListFaces
X-Amz-Date: 20170104T232032Z
User-Agent: aws-cli/1.11.25 Python/2.7.9 Windows/8 botocore/1.4.82
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=XXXXXXXX/20170104/us-west-2/rekognition/aws4_request,
  SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=XXXXXXXX

{"CollectionId": "examplemyphotos"}
```

#### Sample Response<a name="API_ListFaces_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: Wed, 04 Jan 2017 23:20:33 GMT
x-amzn-RequestId: 63d76916-d2d4-11e6-aa8b-8bcb9b9028b4
Content-Length: 3440
Connection: keep-alive

{
   "FaceModelVersion":"2.0",
   "Faces":[
      {
         "BoundingBox":{
            "Height":0.14222200214862823,
            "Left":-0.06083089858293533,
            "Top":0.2477779984474182,
            "Width":0.18991099298000336
         },
         "Confidence":99.99889373779297,
         "ExternalImageId":"externalimageidONE",
         "FaceId":"11111111-2222-3333-4444-555555555555",
         "ImageId":"11111111-2222-3333-4444-555555555555"
      },
      {
         "BoundingBox":{
            "Height":0.1644439995288849,
            "Left":0.4376850128173828,
            "Top":0.22555600106716156,
            "Width":0.22106799483299255
         },
         "Confidence":99.2842025756836,
         "ExternalImageId":"externalimageidTWO",
         "FaceId":"11111111-2222-3333-4444-555555555555",
         "ImageId":"11111111-2222-3333-4444-555555555555"
      },
      {
         "BoundingBox":{
            "Height":0.1599999964237213,
            "Left":0.643172025680542,
            "Top":0.11999999731779099,
            "Width":0.20998500287532806
         },
         "Confidence":99.99870300292969,
         "ExternalImageId":"externalimageidTHREE",
         "FaceId":"11111111-2222-3333-4444-555555555555",
         "ImageId":"11111111-2222-3333-4444-555555555555"
      },
      {
         "BoundingBox":{
            "Height":0.10555599629878998,
            "Left":0.5014839768409729,
            "Top":0.22777800261974335,
            "Width":0.14243300259113312
         },
         "Confidence":99.9761962890625,
         "ExternalImageId":"externalimageidONE",
         "FaceId":"11111111-2222-3333-4444-555555555555",
         "ImageId":"11111111-2222-3333-4444-555555555555"
      },
      {
         "BoundingBox":{
            "Height":0.10888899862766266,
            "Left":0.8056380152702332,
            "Top":0.21555599570274353,
            "Width":0.1454010009765625
         },
         "Confidence":99.94869995117188,
         "ExternalImageId":"externalimageidONE",
         "FaceId":"11111111-2222-3333-4444-555555555555",
         "ImageId":"11111111-2222-3333-4444-555555555555"
      },
      {
         "BoundingBox":{
            "Height":0.12999999523162842,
            "Left":0.5430560111999512,
            "Top":0.2544440031051636,
            "Width":0.16249999403953552
         },
         "Confidence":99.97720336914062,
         "ExternalImageId":"externalimageidFOUR",
         "FaceId":"11111111-2222-3333-4444-555555555555",
         "ImageId":"11111111-2222-3333-4444-555555555555"
      },
      {
         "BoundingBox":{
            "Height":0.2055560052394867,
            "Left":0.12166199833154678,
            "Top":-0.06888890266418457,
            "Width":0.27448099851608276
         },
         "Confidence":100.0,
         "ExternalImageId":"externalimageidFIVE",
         "FaceId":"11111111-2222-3333-4444-555555555555",
         "ImageId":"11111111-2222-3333-4444-555555555555"
      },
      {
         "BoundingBox":{
            "Height":0.1622219979763031,
            "Left":0.18942700326442719,
            "Top":0.008888890035450459,
            "Width":0.21292200684547424
         },
         "Confidence":99.96389770507812,
         "ExternalImageId":"externalimageidSIX",
         "FaceId":"11111111-2222-3333-4444-555555555555",
         "ImageId":"11111111-2222-3333-4444-555555555555"
      },
      {
         "BoundingBox":{
            "Height":0.11222200095653534,
            "Left":0.04154299944639206,
            "Top":0.01888890005648136,
            "Width":0.149851992726326
         },
         "Confidence":99.99949645996094,
         "ExternalImageId":"externalimageidSEVEN",
         "FaceId":"11111111-2222-3333-4444-555555555555",
         "ImageId":"11111111-2222-3333-4444-555555555555"
      },
      {
         "BoundingBox":{
            "Height":0.04222220182418823,
            "Left":0.46696001291275024,
            "Top":0.8944439888000488,
            "Width":0.05580030009150505
         },
         "Confidence":90.60900115966797,
         "ExternalImageId":"externalimageidSIX",
         "FaceId":"11111111-2222-3333-4444-555555555555",
         "ImageId":"11111111-2222-3333-4444-555555555555"
      },
      {
         "BoundingBox":{
            "Height":0.3222219944000244,
            "Left":0.24332299828529358,
            "Top":0.22333300113677979,
            "Width":0.43026700615882874
         },
         "Confidence":99.97339630126953,
         "ExternalImageId":"externalimageidFIVE",
         "FaceId":"11111111-2222-3333-4444-555555555555",
         "ImageId":"11111111-2222-3333-4444-555555555555"
      },
      {
         "BoundingBox":{
            "Height":0.09666670113801956,
            "Left":0.04154299944639206,
            "Top":0.05444439873099327,
            "Width":0.12907999753952026
         },
         "Confidence":99.99909973144531,
         "ExternalImageId":"externalimageidONE",
         "FaceId":"11111111-2222-3333-4444-555555555555",
         "ImageId":"11111111-2222-3333-4444-555555555555"
      }
   ]
}
```

## See Also<a name="API_ListFaces_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS Command Line Interface](http://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/ListFaces) 

+  [AWS SDK for \.NET](http://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/ListFaces) 

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ListFaces) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ListFaces) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/ListFaces) 

+  [AWS SDK for JavaScript](http://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/ListFaces) 

+  [AWS SDK for PHP V3](http://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/ListFaces) 

+  [AWS SDK for Python](http://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/ListFaces) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/ListFaces) 