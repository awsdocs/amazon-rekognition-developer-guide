# ListFaces<a name="API_ListFaces"></a>

Returns metadata for faces in the specified collection\. This metadata includes information such as the bounding box coordinates, the confidence \(that the bounding box contains a face\), and face ID\. For an example, see [Listing faces in a collection](list-faces-in-collection-procedure.md)\. 

This operation requires permissions to perform the `rekognition:ListFaces` action\.

## Request Syntax<a name="API_ListFaces_RequestSyntax"></a>

```
{
   "CollectionId": "string",
   "MaxResults": number,
   "NextToken": "string"
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
   "FaceModelVersion": "string",
   "Faces": [ 
      { 
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
      }
   ],
   "NextToken": "string"
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

## See Also<a name="API_ListFaces_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/ListFaces) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/ListFaces) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ListFaces) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ListFaces) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/ListFaces) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/ListFaces) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/ListFaces) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/ListFaces) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ListFaces) 