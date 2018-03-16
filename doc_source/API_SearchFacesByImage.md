# SearchFacesByImage<a name="API_SearchFacesByImage"></a>

For a given input image, first detects the largest face in the image, and then searches the specified collection for matching faces\. The operation compares the features of the input face with faces in the specified collection\. 

**Note**  
 To search for all faces in an input image, you might first call the [IndexFaces](API_IndexFaces.md) operation, and then use the face IDs returned in subsequent calls to the [SearchFaces](API_SearchFaces.md) operation\.   
 You can also call the `DetectFaces` operation and use the bounding boxes in the response to make face crops, which then you can pass in to the `SearchFacesByImage` operation\. 

You pass the input image either as base64\-encoded image bytes or as a reference to an image in an Amazon S3 bucket\. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported\. The image must be either a PNG or JPEG formatted file\. 

 The response returns an array of faces that match, ordered by similarity score with the highest similarity first\. More specifically, it is an array of metadata for each face match found\. Along with the metadata, the response also includes a `similarity` indicating how similar the face is to the input face\. In the response, the operation also returns the bounding box \(and a confidence level that the bounding box contains a face\) of the face that Amazon Rekognition used for the input image\. 

For an example, see [Searching for a Face Using an Image](search-face-with-image-procedure.md)\.

This operation requires permissions to perform the `rekognition:SearchFacesByImage` action\.

## Request Syntax<a name="API_SearchFacesByImage_RequestSyntax"></a>

```
{
   "[CollectionId](#rekognition-SearchFacesByImage-request-CollectionId)": "string",
   "[FaceMatchThreshold](#rekognition-SearchFacesByImage-request-FaceMatchThreshold)": number,
   "[Image](#rekognition-SearchFacesByImage-request-Image)": { 
      "[Bytes](API_Image.md#rekognition-Type-Image-Bytes)": blob,
      "[S3Object](API_Image.md#rekognition-Type-Image-S3Object)": { 
         "[Bucket](API_S3Object.md#rekognition-Type-S3Object-Bucket)": "string",
         "[Name](API_S3Object.md#rekognition-Type-S3Object-Name)": "string",
         "[Version](API_S3Object.md#rekognition-Type-S3Object-Version)": "string"
      }
   },
   "[MaxFaces](#rekognition-SearchFacesByImage-request-MaxFaces)": number
}
```

## Request Parameters<a name="API_SearchFacesByImage_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [CollectionId](#API_SearchFacesByImage_RequestSyntax) **   <a name="rekognition-SearchFacesByImage-request-CollectionId"></a>
ID of the collection to search\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

 ** [FaceMatchThreshold](#API_SearchFacesByImage_RequestSyntax) **   <a name="rekognition-SearchFacesByImage-request-FaceMatchThreshold"></a>
\(Optional\) Specifies the minimum confidence in the face match to return\. For example, don't return any matches where confidence in matches is less than 70%\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 ** [Image](#API_SearchFacesByImage_RequestSyntax) **   <a name="rekognition-SearchFacesByImage-request-Image"></a>
The input image as base64\-encoded bytes or an S3 object\. If you use the AWS CLI to call Amazon Rekognition operations, passing base64\-encoded image bytes is not supported\.   
Type: [Image](API_Image.md) object  
Required: Yes

 ** [MaxFaces](#API_SearchFacesByImage_RequestSyntax) **   <a name="rekognition-SearchFacesByImage-request-MaxFaces"></a>
Maximum number of faces to return\. The operation returns the maximum number of faces with the highest confidence in the match\.  
Type: Integer  
Valid Range: Minimum value of 1\. Maximum value of 4096\.  
Required: No

## Response Syntax<a name="API_SearchFacesByImage_ResponseSyntax"></a>

```
{
   "[FaceMatches](#rekognition-SearchFacesByImage-response-FaceMatches)": [ 
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
   "[FaceModelVersion](#rekognition-SearchFacesByImage-response-FaceModelVersion)": "string",
   "[SearchedFaceBoundingBox](#rekognition-SearchFacesByImage-response-SearchedFaceBoundingBox)": { 
      "[Height](API_BoundingBox.md#rekognition-Type-BoundingBox-Height)": number,
      "[Left](API_BoundingBox.md#rekognition-Type-BoundingBox-Left)": number,
      "[Top](API_BoundingBox.md#rekognition-Type-BoundingBox-Top)": number,
      "[Width](API_BoundingBox.md#rekognition-Type-BoundingBox-Width)": number
   },
   "[SearchedFaceConfidence](#rekognition-SearchFacesByImage-response-SearchedFaceConfidence)": number
}
```

## Response Elements<a name="API_SearchFacesByImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [FaceMatches](#API_SearchFacesByImage_ResponseSyntax) **   <a name="rekognition-SearchFacesByImage-response-FaceMatches"></a>
An array of faces that match the input face, along with the confidence in the match\.  
Type: Array of [FaceMatch](API_FaceMatch.md) objects

 ** [FaceModelVersion](#API_SearchFacesByImage_ResponseSyntax) **   <a name="rekognition-SearchFacesByImage-response-FaceModelVersion"></a>
Version number of the face detection model associated with the input collection \(`CollectionId`\)\.  
Type: String

 ** [SearchedFaceBoundingBox](#API_SearchFacesByImage_ResponseSyntax) **   <a name="rekognition-SearchFacesByImage-response-SearchedFaceBoundingBox"></a>
The bounding box around the face in the input image that Amazon Rekognition used for the search\.  
Type: [BoundingBox](API_BoundingBox.md) object

 ** [SearchedFaceConfidence](#API_SearchFacesByImage_ResponseSyntax) **   <a name="rekognition-SearchFacesByImage-response-SearchedFaceConfidence"></a>
The level of confidence that the `searchedFaceBoundingBox`, contains a face\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.

## Errors<a name="API_SearchFacesByImage_Errors"></a>

 **AccessDeniedException**   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 **ImageTooLargeException**   
The input image size exceeds the allowed limit\. For more information, see [Limits in Amazon Rekognition](limits.md)\.   
HTTP Status Code: 400

 **InternalServerError**   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

 **InvalidImageFormatException**   
The provided image format is not supported\.   
HTTP Status Code: 400

 **InvalidParameterException**   
Input parameter violated a constraint\. Validate your parameter before calling the API operation again\.  
HTTP Status Code: 400

 **InvalidS3ObjectException**   
Amazon Rekognition is unable to access the S3 object specified in the request\.  
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

## Example<a name="API_SearchFacesByImage_Examples"></a>

### Example Request<a name="API_SearchFacesByImage_Example_1"></a>

The following example shows a request that determines the largest face in the supplied image \(people\.img\) and scans a collection \(examplemyphotos\) for matching faces\.

#### Sample Request<a name="API_SearchFacesByImage_Example_1_Request"></a>

```
POST https://rekognition.us-west-2.amazonaws.com/ HTTP/1.1
Host: rekognition.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 107
X-Amz-Target: RekognitionService.SearchFacesByImage
X-Amz-Date: 20170105T162552Z
User-Agent: aws-cli/1.11.25 Python/2.7.9 Windows/8 botocore/1.4.82
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=XXXXXXXX/us-west-2/rekognition/aws4_request,
  SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=XXXXXXXX

{
   "Image":{
      "S3Object":{
         "Bucket":"example-photos",
         "Name":"people.jpg"
      }
   },
   "CollectionId":"examplemyphotos"
}
```

#### Sample Response<a name="API_SearchFacesByImage_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: Thu, 05 Jan 2017 16:25:54 GMT
x-amzn-RequestId: a0c13bb0-d363-11e6-86be-1d11e90c3f85
Content-Length: 1460
Connection: keep-alive

{
   "FaceMatches":[
      {
         "Face":{
            "BoundingBox":{
               "Height":0.2220669984817505,
               "Left":0.5033329725265503,
               "Top":0.21229000389575958,
               "Width":0.1766670048236847
            },
            "Confidence":99.99970245361328,
            "FaceId":"11111111-2222-3333-4444-555555555555",
            "ImageId":"11111111-2222-3333-4444-555555555555"
         },
         "Similarity":100.0
      },
      {
         "Face":{
            "BoundingBox":{
               "Height":0.1622219979763031,
               "Left":0.18942700326442719,
               "Top":0.008888890035450459,
               "Width":0.21292200684547424
            },
            "Confidence":99.96389770507812,
            "ExternalImageId":"jadenoah2",
            "FaceId":"11111111-2222-3333-4444-555555555555",
            "ImageId":"11111111-2222-3333-4444-555555555555"
         },
         "Similarity":95.46002960205078
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
            "ExternalImageId":"jadegarrettelinoah",
            "FaceId":"11111111-2222-3333-4444-555555555555",
            "ImageId":"11111111-2222-3333-4444-555555555555"
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
            "ExternalImageId":"noahjade",
            "FaceId":"11111111-2222-3333-4444-555555555555",
            "ImageId":"11111111-2222-3333-4444-555555555555"
         },
         "Similarity":92.22525787353516
      }
   ],
   "FaceModelVersion":"2.0",
   "SearchedFaceBoundingBox":{
      "Height":0.22206704318523407,
      "Left":0.503333330154419,
      "Top":0.21229049563407898,
      "Width":0.17666666209697723
   },
   "SearchedFaceConfidence":99.9996566772461
}
```

## See Also<a name="API_SearchFacesByImage_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS Command Line Interface](http://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/SearchFacesByImage) 

+  [AWS SDK for \.NET](http://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/SearchFacesByImage) 

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/SearchFacesByImage) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/SearchFacesByImage) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/SearchFacesByImage) 

+  [AWS SDK for JavaScript](http://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/SearchFacesByImage) 

+  [AWS SDK for PHP V3](http://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/SearchFacesByImage) 

+  [AWS SDK for Python](http://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/SearchFacesByImage) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/SearchFacesByImage) 