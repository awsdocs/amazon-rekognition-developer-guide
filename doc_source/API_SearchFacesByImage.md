# SearchFacesByImage<a name="API_SearchFacesByImage"></a>

For a given input image, first detects the largest face in the image, and then searches the specified collection for matching faces\. The operation compares the features of the input face with faces in the specified collection\. 

**Note**  
To search for all faces in an input image, you might first call the [IndexFaces](API_IndexFaces.md) operation, and then use the face IDs returned in subsequent calls to the [SearchFaces](API_SearchFaces.md) operation\.   
 You can also call the `DetectFaces` operation and use the bounding boxes in the response to make face crops, which then you can pass in to the `SearchFacesByImage` operation\. 

You pass the input image either as base64\-encoded image bytes or as a reference to an image in an Amazon S3 bucket\. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported\. The image must be either a PNG or JPEG formatted file\. 

 The response returns an array of faces that match, ordered by similarity score with the highest similarity first\. More specifically, it is an array of metadata for each face match found\. Along with the metadata, the response also includes a `similarity` indicating how similar the face is to the input face\. In the response, the operation also returns the bounding box \(and a confidence level that the bounding box contains a face\) of the face that Amazon Rekognition used for the input image\. 

For an example, see [Searching for a Face Using an Image](search-face-with-image-procedure.md)\.

The `QualityFilter` input parameter allows you to filter out detected faces that don’t meet a required quality bar\. The quality bar is based on a variety of common use cases\. Use `QualityFilter` to set the quality bar for filtering by specifying `LOW`, `MEDIUM`, or `HIGH`\. If you do not want to filter detected faces, specify `NONE`\. The default value is `NONE`\.

**Note**  
To use quality filtering, you need a collection associated with version 3 of the face model or higher\. To get the version of the face model associated with a collection, call [DescribeCollection](API_DescribeCollection.md)\. 

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
   "[MaxFaces](#rekognition-SearchFacesByImage-request-MaxFaces)": number,
   "[QualityFilter](#rekognition-SearchFacesByImage-request-QualityFilter)": "string"
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
\(Optional\) Specifies the minimum confidence in the face match to return\. For example, don't return any matches where confidence in matches is less than 70%\. The default value is 80%\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 ** [Image](#API_SearchFacesByImage_RequestSyntax) **   <a name="rekognition-SearchFacesByImage-request-Image"></a>
The input image as base64\-encoded bytes or an S3 object\. If you use the AWS CLI to call Amazon Rekognition operations, passing base64\-encoded image bytes is not supported\.   
If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64\-encode image bytes passed using the `Bytes` field\. For more information, see [Images](images-information.md)\.  
Type: [Image](API_Image.md) object  
Required: Yes

 ** [MaxFaces](#API_SearchFacesByImage_RequestSyntax) **   <a name="rekognition-SearchFacesByImage-request-MaxFaces"></a>
Maximum number of faces to return\. The operation returns the maximum number of faces with the highest confidence in the match\.  
Type: Integer  
Valid Range: Minimum value of 1\. Maximum value of 4096\.  
Required: No

 ** [QualityFilter](#API_SearchFacesByImage_RequestSyntax) **   <a name="rekognition-SearchFacesByImage-request-QualityFilter"></a>
A filter that specifies a quality bar for how much filtering is done to identify faces\. Filtered faces aren't searched for in the collection\. If you specify `AUTO`, Amazon Rekognition chooses the quality bar\. If you specify `LOW`, `MEDIUM`, or `HIGH`, filtering removes all faces that don’t meet the chosen quality bar\. The quality bar is based on a variety of common use cases\. Low\-quality detections can occur for a number of reasons\. Some examples are an object that's misidentified as a face, a face that's too blurry, or a face with a pose that's too extreme to use\. If you specify `NONE`, no filtering is performed\. The default value is `NONE`\.   
To use quality filtering, the collection you are using must be associated with version 3 of the face model or higher\.  
Type: String  
Valid Values:` NONE | AUTO | LOW | MEDIUM | HIGH`   
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

## See Also<a name="API_SearchFacesByImage_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/SearchFacesByImage) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/SearchFacesByImage) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/SearchFacesByImage) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/SearchFacesByImage) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/SearchFacesByImage) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/SearchFacesByImage) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/SearchFacesByImage) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/SearchFacesByImage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/SearchFacesByImage) 