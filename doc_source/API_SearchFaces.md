# SearchFaces<a name="API_SearchFaces"></a>

For a given input face ID, searches for matching faces in the collection the face belongs to\. You get a face ID when you add a face to the collection using the [IndexFaces](API_IndexFaces.md) operation\. The operation compares the features of the input face with faces in the specified collection\. 

**Note**  
You can also search faces without indexing faces by using the `SearchFacesByImage` operation\.

 The operation response returns an array of faces that match, ordered by similarity score with the highest similarity first\. More specifically, it is an array of metadata for each face match that is found\. Along with the metadata, the response also includes a `confidence` value for each face match, indicating the confidence that the specific face matches the input face\. 

For an example, see [Searching for a Face Using Its Face ID](search-face-with-id-procedure.md)\.

This operation requires permissions to perform the `rekognition:SearchFaces` action\.

## Request Syntax<a name="API_SearchFaces_RequestSyntax"></a>

```
{
   "[CollectionId](#rekognition-SearchFaces-request-CollectionId)": "string",
   "[FaceId](#rekognition-SearchFaces-request-FaceId)": "string",
   "[FaceMatchThreshold](#rekognition-SearchFaces-request-FaceMatchThreshold)": number,
   "[MaxFaces](#rekognition-SearchFaces-request-MaxFaces)": number
}
```

## Request Parameters<a name="API_SearchFaces_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [CollectionId](#API_SearchFaces_RequestSyntax) **   <a name="rekognition-SearchFaces-request-CollectionId"></a>
ID of the collection the face belongs to\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

 ** [FaceId](#API_SearchFaces_RequestSyntax) **   <a name="rekognition-SearchFaces-request-FaceId"></a>
ID of a face to find matches for in the collection\.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

 ** [FaceMatchThreshold](#API_SearchFaces_RequestSyntax) **   <a name="rekognition-SearchFaces-request-FaceMatchThreshold"></a>
Optional value specifying the minimum confidence in the face match to return\. For example, don't return any matches where confidence in matches is less than 70%\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 ** [MaxFaces](#API_SearchFaces_RequestSyntax) **   <a name="rekognition-SearchFaces-request-MaxFaces"></a>
Maximum number of faces to return\. The operation returns the maximum number of faces with the highest confidence in the match\.  
Type: Integer  
Valid Range: Minimum value of 1\. Maximum value of 4096\.  
Required: No

## Response Syntax<a name="API_SearchFaces_ResponseSyntax"></a>

```
{
   "[FaceMatches](#rekognition-SearchFaces-response-FaceMatches)": [ 
      { 
         "[Face](API_FaceMatch.md#rekognition-Type-FaceMatch-Face)": { 
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
         },
         "[Similarity](API_FaceMatch.md#rekognition-Type-FaceMatch-Similarity)": number
      }
   ],
   "[FaceModelVersion](#rekognition-SearchFaces-response-FaceModelVersion)": "string",
   "[SearchedFaceId](#rekognition-SearchFaces-response-SearchedFaceId)": "string"
}
```

## Response Elements<a name="API_SearchFaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [FaceMatches](#API_SearchFaces_ResponseSyntax) **   <a name="rekognition-SearchFaces-response-FaceMatches"></a>
An array of faces that matched the input face, along with the confidence in the match\.  
Type: Array of [FaceMatch](API_FaceMatch.md) objects

 ** [FaceModelVersion](#API_SearchFaces_ResponseSyntax) **   <a name="rekognition-SearchFaces-response-FaceModelVersion"></a>
Version number of the face detection model associated with the input collection \(`CollectionId`\)\.  
Type: String

 ** [SearchedFaceId](#API_SearchFaces_ResponseSyntax) **   <a name="rekognition-SearchFaces-response-SearchedFaceId"></a>
ID of the face that was searched for matches in a collection\.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` 

## Errors<a name="API_SearchFaces_Errors"></a>

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

## Example<a name="API_SearchFaces_Examples"></a>

### Example Request<a name="API_SearchFaces_Example_1"></a>

The following example shows a request that searches for occurrences of a face within the collection \(examplemyphotos\) the face belongs to\.

#### Sample Request<a name="API_SearchFaces_Example_1_Request"></a>

```
POST https://rekognition.us-west-2.amazonaws.com/ HTTP/1.1
Host: rekognition.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 78
X-Amz-Target: RekognitionService.SearchFaces
X-Amz-Date: 20170105T163206Z
User-Agent: aws-cli/1.11.25 Python/2.7.9 Windows/8 botocore/1.4.82
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=XXXXXXXX/20170105/us-west-2/rekognition/aws4_request,
  SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=XXXXXXXX

{
   "FaceId":"11111111-2222-3333-4444-555555555555",
   "CollectionId":"examplemyphotos"
}
```

#### Sample Response<a name="API_SearchFaces_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: Thu, 05 Jan 2017 16:32:08 GMT
x-amzn-RequestId: 80269055-d364-11e6-9e9d-9b236fb2a3ad
Content-Length: 1057
Connection: keep-alive

{
   "FaceMatches":[
      {
         "Face":{
            "BoundingBox":{
               "Height":0.1622219979763031,
               "Left":0.18942700326442719,
               "Top":0.008888890035450459,
               "Width":0.21292200684547424
            },
            "Confidence":99.96389770507812,
            "ExternalImageId":"externalimageidONE",
            "FaceId":"11111111-2222-3333-4444-555555555555",
            "ImageId":"11111111-2222-3333-4444-555555555555"
         },
         "Similarity":95.46002197265625
      },
      {
         "Face":{
            "BoundingBox":{
               "Height":0.09666670113801956,
               "Left":0.04154299944639206,
               "Top":0.05444439873099327,
               "Width":0.12907999753952026
            },
            "Confidence":99.99909973144531,
            "ExternalImageId":"externalimageidTWO",
            "FaceId":"22222222-2222-3333-4444-555555555555",
            "ImageId":"22222222-2222-3333-4444-555555555555"
         },
         "Similarity":92.89849090576172
      },
      {
         "Face":{
            "BoundingBox":{
               "Height":0.11222200095653534,
               "Left":0.04154299944639206,
               "Top":0.01888890005648136,
               "Width":0.149851992726326
            },
            "Confidence":99.99949645996094,
            "ExternalImageId":"externalimageidTHREE",
            "FaceId":"11111111-2222-3333-4444-555555555555",
            "ImageId":"11111111-2222-3333-4444-555555555555"
         },
         "Similarity":92.22525024414062
      }
   ],
   "FaceModelVersion":"2.0",
   "SearchedFaceId":"11111111-2222-3333-4444-555555555555"
}
```

## See Also<a name="API_SearchFaces_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/SearchFaces) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/SearchFaces) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/SearchFaces) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/SearchFaces) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/SearchFaces) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/SearchFaces) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/SearchFaces) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/SearchFaces) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/SearchFaces) 