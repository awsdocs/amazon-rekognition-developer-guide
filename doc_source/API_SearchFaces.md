# SearchFaces<a name="API_SearchFaces"></a>

For a given input face ID, searches for matching faces in the collection the face belongs to\. You get a face ID when you add a face to the collection using the [ IndexFaces ](API_IndexFaces.md) operation\. The operation compares the features of the input face with faces in the specified collection\. 

**Note**  
You can also search faces without indexing faces by using the `SearchFacesByImage` operation\.

 The operation response returns an array of faces that match, ordered by similarity score with the highest similarity first\. More specifically, it is an array of metadata for each face match that is found\. Along with the metadata, the response also includes a `confidence` value for each face match, indicating the confidence that the specific face matches the input face\. 

For an example, see [Searching for a face using its face ID](search-face-with-id-procedure.md)\.

This operation requires permissions to perform the `rekognition:SearchFaces` action\.

## Request Syntax<a name="API_SearchFaces_RequestSyntax"></a>

```
{
   "CollectionId": "string",
   "FaceId": "string",
   "FaceMatchThreshold": number,
   "MaxFaces": number
}
```

## Request Parameters<a name="API_SearchFaces_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ CollectionId ](#API_SearchFaces_RequestSyntax) **   <a name="rekognition-SearchFaces-request-CollectionId"></a>
ID of the collection the face belongs to\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

 ** [ FaceId ](#API_SearchFaces_RequestSyntax) **   <a name="rekognition-SearchFaces-request-FaceId"></a>
ID of a face to find matches for in the collection\.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: Yes

 ** [ FaceMatchThreshold ](#API_SearchFaces_RequestSyntax) **   <a name="rekognition-SearchFaces-request-FaceMatchThreshold"></a>
Optional value specifying the minimum confidence in the face match to return\. For example, don't return any matches where confidence in matches is less than 70%\. The default value is 80%\.   
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 ** [ MaxFaces ](#API_SearchFaces_RequestSyntax) **   <a name="rekognition-SearchFaces-request-MaxFaces"></a>
Maximum number of faces to return\. The operation returns the maximum number of faces with the highest confidence in the match\.  
Type: Integer  
Valid Range: Minimum value of 1\. Maximum value of 4096\.  
Required: No

## Response Syntax<a name="API_SearchFaces_ResponseSyntax"></a>

```
{
   "FaceMatches": [ 
      { 
         "Face": { 
            "BoundingBox": { 
               "Height": number,
               "Left": number,
               "Top": number,
               "Width": number
            },
            "Confidence": number,
            "ExternalImageId": "string",
            "FaceId": "string",
            "ImageId": "string"
         },
         "Similarity": number
      }
   ],
   "FaceModelVersion": "string",
   "SearchedFaceId": "string"
}
```

## Response Elements<a name="API_SearchFaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [ FaceMatches ](#API_SearchFaces_ResponseSyntax) **   <a name="rekognition-SearchFaces-response-FaceMatches"></a>
An array of faces that matched the input face, along with the confidence in the match\.  
Type: Array of [ FaceMatch ](API_FaceMatch.md) objects

 ** [ FaceModelVersion ](#API_SearchFaces_ResponseSyntax) **   <a name="rekognition-SearchFaces-response-FaceModelVersion"></a>
Version number of the face detection model associated with the input collection \(`CollectionId`\)\.  
Type: String

 ** [ SearchedFaceId ](#API_SearchFaces_ResponseSyntax) **   <a name="rekognition-SearchFaces-response-SearchedFaceId"></a>
ID of the face that was searched for matches in a collection\.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` 

## Errors<a name="API_SearchFaces_Errors"></a>

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

## See Also<a name="API_SearchFaces_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/SearchFaces) 
+  [ AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/SearchFaces) 
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/SearchFaces) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/SearchFaces) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/SearchFaces) 
+  [ AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/SearchFaces) 
+  [ AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/SearchFaces) 
+  [ AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/SearchFaces) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/SearchFaces) 