# GetFaceSearch<a name="API_GetFaceSearch"></a>

Gets the face search results for Amazon Rekognition Video face search started by [ StartFaceSearch ](API_StartFaceSearch.md)\. The search returns faces in a collection that match the faces of persons detected in a video\. It also includes the time\(s\) that faces are matched in the video\.

Face search in a video is an asynchronous operation\. You start face search by calling to [ StartFaceSearch ](API_StartFaceSearch.md) which returns a job identifier \(`JobId`\)\. When the search operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartFaceSearch`\. To get the search results, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`\. If so, call `GetFaceSearch` and pass the job identifier \(`JobId`\) from the initial call to `StartFaceSearch`\.

For more information, see [Searching faces in a collection](collections.md)\.

The search results are retured in an array, `Persons`, of [ PersonMatch ](API_PersonMatch.md) objects\. Each`PersonMatch` element contains details about the matching faces in the input collection, person information \(facial attributes, bounding boxes, and person identifer\) for the matched person, and the time the person was matched in the video\.

**Note**  
 `GetFaceSearch` only returns the default facial attributes \(`BoundingBox`, `Confidence`, `Landmarks`, `Pose`, and `Quality`\)\. The other facial attributes listed in the `Face` object of the following response syntax are not returned\. For more information, see [ FaceDetail ](API_FaceDetail.md)\. 

By default, the `Persons` array is sorted by the time, in milliseconds from the start of the video, persons are matched\. You can also sort by persons by specifying `INDEX` for the `SORTBY` input parameter\.

## Request Syntax<a name="API_GetFaceSearch_RequestSyntax"></a>

```
{
   "JobId": "string",
   "MaxResults": number,
   "NextToken": "string",
   "SortBy": "string"
}
```

## Request Parameters<a name="API_GetFaceSearch_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ JobId ](#API_GetFaceSearch_RequestSyntax) **   <a name="rekognition-GetFaceSearch-request-JobId"></a>
The job identifer for the search request\. You get the job identifier from an initial call to `StartFaceSearch`\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$`   
Required: Yes

 ** [ MaxResults ](#API_GetFaceSearch_RequestSyntax) **   <a name="rekognition-GetFaceSearch-request-MaxResults"></a>
Maximum number of results to return per paginated call\. The largest value you can specify is 1000\. If you specify a value greater than 1000, a maximum of 1000 results is returned\. The default value is 1000\.  
Type: Integer  
Valid Range: Minimum value of 1\.  
Required: No

 ** [ NextToken ](#API_GetFaceSearch_RequestSyntax) **   <a name="rekognition-GetFaceSearch-request-NextToken"></a>
If the previous response was incomplete \(because there is more search results to retrieve\), Amazon Rekognition Video returns a pagination token in the response\. You can use this pagination token to retrieve the next set of search results\.   
Type: String  
Length Constraints: Maximum length of 255\.  
Required: No

 ** [ SortBy ](#API_GetFaceSearch_RequestSyntax) **   <a name="rekognition-GetFaceSearch-request-SortBy"></a>
Sort to use for grouping faces in the response\. Use `TIMESTAMP` to group faces by the time that they are recognized\. Use `INDEX` to sort by recognized faces\.   
Type: String  
Valid Values:` INDEX | TIMESTAMP`   
Required: No

## Response Syntax<a name="API_GetFaceSearch_ResponseSyntax"></a>

```
{
   "JobStatus": "string",
   "NextToken": "string",
   "Persons": [ 
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
         "Person": { 
            "BoundingBox": { 
               "Height": number,
               "Left": number,
               "Top": number,
               "Width": number
            },
            "Face": { 
               "AgeRange": { 
                  "High": number,
                  "Low": number
               },
               "Beard": { 
                  "Confidence": number,
                  "Value": boolean
               },
               "BoundingBox": { 
                  "Height": number,
                  "Left": number,
                  "Top": number,
                  "Width": number
               },
               "Confidence": number,
               "Emotions": [ 
                  { 
                     "Confidence": number,
                     "Type": "string"
                  }
               ],
               "Eyeglasses": { 
                  "Confidence": number,
                  "Value": boolean
               },
               "EyesOpen": { 
                  "Confidence": number,
                  "Value": boolean
               },
               "Gender": { 
                  "Confidence": number,
                  "Value": "string"
               },
               "Landmarks": [ 
                  { 
                     "Type": "string",
                     "X": number,
                     "Y": number
                  }
               ],
               "MouthOpen": { 
                  "Confidence": number,
                  "Value": boolean
               },
               "Mustache": { 
                  "Confidence": number,
                  "Value": boolean
               },
               "Pose": { 
                  "Pitch": number,
                  "Roll": number,
                  "Yaw": number
               },
               "Quality": { 
                  "Brightness": number,
                  "Sharpness": number
               },
               "Smile": { 
                  "Confidence": number,
                  "Value": boolean
               },
               "Sunglasses": { 
                  "Confidence": number,
                  "Value": boolean
               }
            },
            "Index": number
         },
         "Timestamp": number
      }
   ],
   "StatusMessage": "string",
   "VideoMetadata": { 
      "Codec": "string",
      "ColorRange": "string",
      "DurationMillis": number,
      "Format": "string",
      "FrameHeight": number,
      "FrameRate": number,
      "FrameWidth": number
   }
}
```

## Response Elements<a name="API_GetFaceSearch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [ JobStatus ](#API_GetFaceSearch_ResponseSyntax) **   <a name="rekognition-GetFaceSearch-response-JobStatus"></a>
The current status of the face search job\.  
Type: String  
Valid Values:` IN_PROGRESS | SUCCEEDED | FAILED` 

 ** [ NextToken ](#API_GetFaceSearch_ResponseSyntax) **   <a name="rekognition-GetFaceSearch-response-NextToken"></a>
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of search results\.   
Type: String  
Length Constraints: Maximum length of 255\.

 ** [ Persons ](#API_GetFaceSearch_ResponseSyntax) **   <a name="rekognition-GetFaceSearch-response-Persons"></a>
An array of persons, [ PersonMatch ](API_PersonMatch.md), in the video whose face\(s\) match the face\(s\) in an Amazon Rekognition collection\. It also includes time information for when persons are matched in the video\. You specify the input collection in an initial call to `StartFaceSearch`\. Each `Persons` element includes a time the person was matched, face match details \(`FaceMatches`\) for matching faces in the collection, and person information \(`Person`\) for the matched person\.   
Type: Array of [ PersonMatch ](API_PersonMatch.md) objects

 ** [ StatusMessage ](#API_GetFaceSearch_ResponseSyntax) **   <a name="rekognition-GetFaceSearch-response-StatusMessage"></a>
If the job fails, `StatusMessage` provides a descriptive error message\.  
Type: String

 ** [ VideoMetadata ](#API_GetFaceSearch_ResponseSyntax) **   <a name="rekognition-GetFaceSearch-response-VideoMetadata"></a>
Information about a video that Amazon Rekognition analyzed\. `Videometadata` is returned in every page of paginated responses from a Amazon Rekognition Video operation\.   
Type: [ VideoMetadata ](API_VideoMetadata.md) object

## Errors<a name="API_GetFaceSearch_Errors"></a>

 ** AccessDeniedException **   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 ** InternalServerError **   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

 ** InvalidPaginationTokenException **   
Pagination token in the request is not valid\.  
HTTP Status Code: 400

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

## See Also<a name="API_GetFaceSearch_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/GetFaceSearch) 
+  [ AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/GetFaceSearch) 
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GetFaceSearch) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/GetFaceSearch) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/GetFaceSearch) 
+  [ AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/GetFaceSearch) 
+  [ AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/GetFaceSearch) 
+  [ AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/GetFaceSearch) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/GetFaceSearch) 