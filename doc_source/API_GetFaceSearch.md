# GetFaceSearch<a name="API_GetFaceSearch"></a>

Gets the face search results for Amazon Rekognition Video face search started by [StartFaceSearch](API_StartFaceSearch.md)\. The search returns faces in a collection that match the faces of persons detected in a video\. It also includes the time\(s\) that faces are matched in the video\.

Face search in a video is an asynchronous operation\. You start face search by calling to [StartFaceSearch](API_StartFaceSearch.md) which returns a job identifier \(`JobId`\)\. When the search operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartFaceSearch`\. To get the search results, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`\. If so, call `GetFaceSearch` and pass the job identifier \(`JobId`\) from the initial call to `StartFaceSearch`\.

For more information, see [Searching Faces in a Collection](collections.md)\.

The search results are retured in an array, `Persons`, of [PersonMatch](API_PersonMatch.md) objects\. Each`PersonMatch` element contains details about the matching faces in the input collection, person information \(facial attributes, bounding boxes, and person identifer\) for the matched person, and the time the person was matched in the video\.

**Note**  
 `GetFaceSearch` only returns the default facial attributes \(`BoundingBox`, `Confidence`, `Landmarks`, `Pose`, and `Quality`\)\. The other facial attributes listed in the `Face` object of the following response syntax are not returned\. For more information, see [FaceDetail](API_FaceDetail.md)\. 

By default, the `Persons` array is sorted by the time, in milliseconds from the start of the video, persons are matched\. You can also sort by persons by specifying `INDEX` for the `SORTBY` input parameter\.

## Request Syntax<a name="API_GetFaceSearch_RequestSyntax"></a>

```
{
   "[JobId](#rekognition-GetFaceSearch-request-JobId)": "string",
   "[MaxResults](#rekognition-GetFaceSearch-request-MaxResults)": number,
   "[NextToken](#rekognition-GetFaceSearch-request-NextToken)": "string",
   "[SortBy](#rekognition-GetFaceSearch-request-SortBy)": "string"
}
```

## Request Parameters<a name="API_GetFaceSearch_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [JobId](#API_GetFaceSearch_RequestSyntax) **   <a name="rekognition-GetFaceSearch-request-JobId"></a>
The job identifer for the search request\. You get the job identifier from an initial call to `StartFaceSearch`\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$`   
Required: Yes

 ** [MaxResults](#API_GetFaceSearch_RequestSyntax) **   <a name="rekognition-GetFaceSearch-request-MaxResults"></a>
Maximum number of results to return per paginated call\. The largest value you can specify is 1000\. If you specify a value greater than 1000, a maximum of 1000 results is returned\. The default value is 1000\.  
Type: Integer  
Valid Range: Minimum value of 1\.  
Required: No

 ** [NextToken](#API_GetFaceSearch_RequestSyntax) **   <a name="rekognition-GetFaceSearch-request-NextToken"></a>
If the previous response was incomplete \(because there is more search results to retrieve\), Amazon Rekognition Video returns a pagination token in the response\. You can use this pagination token to retrieve the next set of search results\.   
Type: String  
Length Constraints: Maximum length of 255\.  
Required: No

 ** [SortBy](#API_GetFaceSearch_RequestSyntax) **   <a name="rekognition-GetFaceSearch-request-SortBy"></a>
Sort to use for grouping faces in the response\. Use `TIMESTAMP` to group faces by the time that they are recognized\. Use `INDEX` to sort by recognized faces\.   
Type: String  
Valid Values:` INDEX | TIMESTAMP`   
Required: No

## Response Syntax<a name="API_GetFaceSearch_ResponseSyntax"></a>

```
{
   "[JobStatus](#rekognition-GetFaceSearch-response-JobStatus)": "string",
   "[NextToken](#rekognition-GetFaceSearch-response-NextToken)": "string",
   "[Persons](#rekognition-GetFaceSearch-response-Persons)": [ 
      { 
         "[FaceMatches](API_PersonMatch.md#rekognition-Type-PersonMatch-FaceMatches)": [ 
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
         "[Person](API_PersonMatch.md#rekognition-Type-PersonMatch-Person)": { 
            "[BoundingBox](API_PersonDetail.md#rekognition-Type-PersonDetail-BoundingBox)": { 
               "[Height](API_BoundingBox.md#rekognition-Type-BoundingBox-Height)": number,
               "[Left](API_BoundingBox.md#rekognition-Type-BoundingBox-Left)": number,
               "[Top](API_BoundingBox.md#rekognition-Type-BoundingBox-Top)": number,
               "[Width](API_BoundingBox.md#rekognition-Type-BoundingBox-Width)": number
            },
            "[Face](API_PersonDetail.md#rekognition-Type-PersonDetail-Face)": { 
               "[AgeRange](API_FaceDetail.md#rekognition-Type-FaceDetail-AgeRange)": { 
                  "[High](API_AgeRange.md#rekognition-Type-AgeRange-High)": number,
                  "[Low](API_AgeRange.md#rekognition-Type-AgeRange-Low)": number
               },
               "[Beard](API_FaceDetail.md#rekognition-Type-FaceDetail-Beard)": { 
                  "[Confidence](API_Beard.md#rekognition-Type-Beard-Confidence)": number,
                  "[Value](API_Beard.md#rekognition-Type-Beard-Value)": boolean
               },
               "[BoundingBox](API_FaceDetail.md#rekognition-Type-FaceDetail-BoundingBox)": { 
                  "[Height](API_BoundingBox.md#rekognition-Type-BoundingBox-Height)": number,
                  "[Left](API_BoundingBox.md#rekognition-Type-BoundingBox-Left)": number,
                  "[Top](API_BoundingBox.md#rekognition-Type-BoundingBox-Top)": number,
                  "[Width](API_BoundingBox.md#rekognition-Type-BoundingBox-Width)": number
               },
               "[Confidence](API_FaceDetail.md#rekognition-Type-FaceDetail-Confidence)": number,
               "[Emotions](API_FaceDetail.md#rekognition-Type-FaceDetail-Emotions)": [ 
                  { 
                     "[Confidence](API_Emotion.md#rekognition-Type-Emotion-Confidence)": number,
                     "[Type](API_Emotion.md#rekognition-Type-Emotion-Type)": "string"
                  }
               ],
               "[Eyeglasses](API_FaceDetail.md#rekognition-Type-FaceDetail-Eyeglasses)": { 
                  "[Confidence](API_Eyeglasses.md#rekognition-Type-Eyeglasses-Confidence)": number,
                  "[Value](API_Eyeglasses.md#rekognition-Type-Eyeglasses-Value)": boolean
               },
               "[EyesOpen](API_FaceDetail.md#rekognition-Type-FaceDetail-EyesOpen)": { 
                  "[Confidence](API_EyeOpen.md#rekognition-Type-EyeOpen-Confidence)": number,
                  "[Value](API_EyeOpen.md#rekognition-Type-EyeOpen-Value)": boolean
               },
               "[Gender](API_FaceDetail.md#rekognition-Type-FaceDetail-Gender)": { 
                  "[Confidence](API_Gender.md#rekognition-Type-Gender-Confidence)": number,
                  "[Value](API_Gender.md#rekognition-Type-Gender-Value)": "string"
               },
               "[Landmarks](API_FaceDetail.md#rekognition-Type-FaceDetail-Landmarks)": [ 
                  { 
                     "[Type](API_Landmark.md#rekognition-Type-Landmark-Type)": "string",
                     "[X](API_Landmark.md#rekognition-Type-Landmark-X)": number,
                     "[Y](API_Landmark.md#rekognition-Type-Landmark-Y)": number
                  }
               ],
               "[MouthOpen](API_FaceDetail.md#rekognition-Type-FaceDetail-MouthOpen)": { 
                  "[Confidence](API_MouthOpen.md#rekognition-Type-MouthOpen-Confidence)": number,
                  "[Value](API_MouthOpen.md#rekognition-Type-MouthOpen-Value)": boolean
               },
               "[Mustache](API_FaceDetail.md#rekognition-Type-FaceDetail-Mustache)": { 
                  "[Confidence](API_Mustache.md#rekognition-Type-Mustache-Confidence)": number,
                  "[Value](API_Mustache.md#rekognition-Type-Mustache-Value)": boolean
               },
               "[Pose](API_FaceDetail.md#rekognition-Type-FaceDetail-Pose)": { 
                  "[Pitch](API_Pose.md#rekognition-Type-Pose-Pitch)": number,
                  "[Roll](API_Pose.md#rekognition-Type-Pose-Roll)": number,
                  "[Yaw](API_Pose.md#rekognition-Type-Pose-Yaw)": number
               },
               "[Quality](API_FaceDetail.md#rekognition-Type-FaceDetail-Quality)": { 
                  "[Brightness](API_ImageQuality.md#rekognition-Type-ImageQuality-Brightness)": number,
                  "[Sharpness](API_ImageQuality.md#rekognition-Type-ImageQuality-Sharpness)": number
               },
               "[Smile](API_FaceDetail.md#rekognition-Type-FaceDetail-Smile)": { 
                  "[Confidence](API_Smile.md#rekognition-Type-Smile-Confidence)": number,
                  "[Value](API_Smile.md#rekognition-Type-Smile-Value)": boolean
               },
               "[Sunglasses](API_FaceDetail.md#rekognition-Type-FaceDetail-Sunglasses)": { 
                  "[Confidence](API_Sunglasses.md#rekognition-Type-Sunglasses-Confidence)": number,
                  "[Value](API_Sunglasses.md#rekognition-Type-Sunglasses-Value)": boolean
               }
            },
            "[Index](API_PersonDetail.md#rekognition-Type-PersonDetail-Index)": number
         },
         "[Timestamp](API_PersonMatch.md#rekognition-Type-PersonMatch-Timestamp)": number
      }
   ],
   "[StatusMessage](#rekognition-GetFaceSearch-response-StatusMessage)": "string",
   "[VideoMetadata](#rekognition-GetFaceSearch-response-VideoMetadata)": { 
      "[Codec](API_VideoMetadata.md#rekognition-Type-VideoMetadata-Codec)": "string",
      "[DurationMillis](API_VideoMetadata.md#rekognition-Type-VideoMetadata-DurationMillis)": number,
      "[Format](API_VideoMetadata.md#rekognition-Type-VideoMetadata-Format)": "string",
      "[FrameHeight](API_VideoMetadata.md#rekognition-Type-VideoMetadata-FrameHeight)": number,
      "[FrameRate](API_VideoMetadata.md#rekognition-Type-VideoMetadata-FrameRate)": number,
      "[FrameWidth](API_VideoMetadata.md#rekognition-Type-VideoMetadata-FrameWidth)": number
   }
}
```

## Response Elements<a name="API_GetFaceSearch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [JobStatus](#API_GetFaceSearch_ResponseSyntax) **   <a name="rekognition-GetFaceSearch-response-JobStatus"></a>
The current status of the face search job\.  
Type: String  
Valid Values:` IN_PROGRESS | SUCCEEDED | FAILED` 

 ** [NextToken](#API_GetFaceSearch_ResponseSyntax) **   <a name="rekognition-GetFaceSearch-response-NextToken"></a>
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of search results\.   
Type: String  
Length Constraints: Maximum length of 255\.

 ** [Persons](#API_GetFaceSearch_ResponseSyntax) **   <a name="rekognition-GetFaceSearch-response-Persons"></a>
An array of persons, [PersonMatch](API_PersonMatch.md), in the video whose face\(s\) match the face\(s\) in an Amazon Rekognition collection\. It also includes time information for when persons are matched in the video\. You specify the input collection in an initial call to `StartFaceSearch`\. Each `Persons` element includes a time the person was matched, face match details \(`FaceMatches`\) for matching faces in the collection, and person information \(`Person`\) for the matched person\.   
Type: Array of [PersonMatch](API_PersonMatch.md) objects

 ** [StatusMessage](#API_GetFaceSearch_ResponseSyntax) **   <a name="rekognition-GetFaceSearch-response-StatusMessage"></a>
If the job fails, `StatusMessage` provides a descriptive error message\.  
Type: String

 ** [VideoMetadata](#API_GetFaceSearch_ResponseSyntax) **   <a name="rekognition-GetFaceSearch-response-VideoMetadata"></a>
Information about a video that Amazon Rekognition analyzed\. `Videometadata` is returned in every page of paginated responses from a Amazon Rekognition Video operation\.   
Type: [VideoMetadata](API_VideoMetadata.md) object

## Errors<a name="API_GetFaceSearch_Errors"></a>

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

## See Also<a name="API_GetFaceSearch_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/GetFaceSearch) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/GetFaceSearch) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GetFaceSearch) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/GetFaceSearch) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/GetFaceSearch) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/GetFaceSearch) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/GetFaceSearch) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/GetFaceSearch) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/GetFaceSearch) 