# GetCelebrityRecognition<a name="API_GetCelebrityRecognition"></a>

Gets the celebrity recognition results for a Rekognition Video analysis started by [StartCelebrityRecognition](API_StartCelebrityRecognition.md)\.

Celebrity recognition in a video is an asynchronous operation\. Analysis is started by a call to [StartCelebrityRecognition](API_StartCelebrityRecognition.md) which returns a job identifier \(`JobId`\)\. When the celebrity recognition operation finishes, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartCelebrityRecognition`\. To get the results of the celebrity recognition analysis, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`\. If so, call `GetCelebrityDetection` and pass the job identifier \(`JobId`\) from the initial call to `StartCelebrityDetection`\. For more information, see [Working with Stored Videos](video.md)\.

 `GetCelebrityRecognition` returns detected celebrities and the time\(s\) they are detected in an array \(`Celebrities`\) of [CelebrityRecognition](API_CelebrityRecognition.md) objects\. Each `CelebrityRecognition` contains information about the celebrity in a [CelebrityDetail](API_CelebrityDetail.md) object and the time, `Timestamp`, the celebrity was detected\. 

**Note**  
 `GetCelebrityRecognition` only returns the default facial attributes \(`BoundingBox`, `Confidence`, `Landmarks`, `Pose`, and `Quality`\)\. The other facial attributes listed in the `Face` object of the following response syntax are not returned\. For more information, see [FaceDetail](API_FaceDetail.md)\. 

By default, the `Celebrities` array is sorted by time \(milliseconds from the start of the video\)\. You can also sort the array by celebrity by specifying the value `ID` in the `SortBy` input parameter\.

The `CelebrityDetail` object includes the celebrity identifer and additional information urls\. If you don't store the additional information urls, you can get them later by calling [GetCelebrityInfo](API_GetCelebrityInfo.md) with the celebrity identifer\.

No information is returned for faces not recognized as celebrities\.

Use MaxResults parameter to limit the number of labels returned\. If there are more results than specified in `MaxResults`, the value of `NextToken` in the operation response contains a pagination token for getting the next set of results\. To get the next page of results, call `GetCelebrityDetection` and populate the `NextToken` request parameter with the token value returned from the previous call to `GetCelebrityRecognition`\.

## Request Syntax<a name="API_GetCelebrityRecognition_RequestSyntax"></a>

```
{
   "[JobId](#rekognition-GetCelebrityRecognition-request-JobId)": "string",
   "[MaxResults](#rekognition-GetCelebrityRecognition-request-MaxResults)": number,
   "[NextToken](#rekognition-GetCelebrityRecognition-request-NextToken)": "string",
   "[SortBy](#rekognition-GetCelebrityRecognition-request-SortBy)": "string"
}
```

## Request Parameters<a name="API_GetCelebrityRecognition_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [JobId](#API_GetCelebrityRecognition_RequestSyntax) **   <a name="rekognition-GetCelebrityRecognition-request-JobId"></a>
Job identifier for the required celebrity recognition analysis\. You can get the job identifer from a call to `StartCelebrityRecognition`\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$`   
Required: Yes

 ** [MaxResults](#API_GetCelebrityRecognition_RequestSyntax) **   <a name="rekognition-GetCelebrityRecognition-request-MaxResults"></a>
Maximum number of results to return per paginated call\. The largest value you can specify is 1000\. If you specify a value greater than 1000, a maximum of 1000 results is returned\. The default value is 1000\.  
Type: Integer  
Valid Range: Minimum value of 1\.  
Required: No

 ** [NextToken](#API_GetCelebrityRecognition_RequestSyntax) **   <a name="rekognition-GetCelebrityRecognition-request-NextToken"></a>
If the previous response was incomplete \(because there is more recognized celebrities to retrieve\), Rekognition Video returns a pagination token in the response\. You can use this pagination token to retrieve the next set of celebrities\.   
Type: String  
Length Constraints: Maximum length of 255\.  
Required: No

 ** [SortBy](#API_GetCelebrityRecognition_RequestSyntax) **   <a name="rekognition-GetCelebrityRecognition-request-SortBy"></a>
Sort to use for celebrities returned in `Celebrities` field\. Specify `ID` to sort by the celebrity identifier, specify `TIMESTAMP` to sort by the time the celebrity was recognized\.  
Type: String  
Valid Values:` ID | TIMESTAMP`   
Required: No

## Response Syntax<a name="API_GetCelebrityRecognition_ResponseSyntax"></a>

```
{
   "[Celebrities](#rekognition-GetCelebrityRecognition-response-Celebrities)": [ 
      { 
         "[Celebrity](API_CelebrityRecognition.md#rekognition-Type-CelebrityRecognition-Celebrity)": { 
            "[BoundingBox](API_CelebrityDetail.md#rekognition-Type-CelebrityDetail-BoundingBox)": { 
               "[Height](API_BoundingBox.md#rekognition-Type-BoundingBox-Height)": number,
               "[Left](API_BoundingBox.md#rekognition-Type-BoundingBox-Left)": number,
               "[Top](API_BoundingBox.md#rekognition-Type-BoundingBox-Top)": number,
               "[Width](API_BoundingBox.md#rekognition-Type-BoundingBox-Width)": number
            },
            "[Confidence](API_CelebrityDetail.md#rekognition-Type-CelebrityDetail-Confidence)": number,
            "[Face](API_CelebrityDetail.md#rekognition-Type-CelebrityDetail-Face)": { 
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
            "[Id](API_CelebrityDetail.md#rekognition-Type-CelebrityDetail-Id)": "string",
            "[Name](API_CelebrityDetail.md#rekognition-Type-CelebrityDetail-Name)": "string",
            "[Urls](API_CelebrityDetail.md#rekognition-Type-CelebrityDetail-Urls)": [ "string" ]
         },
         "[Timestamp](API_CelebrityRecognition.md#rekognition-Type-CelebrityRecognition-Timestamp)": number
      }
   ],
   "[JobStatus](#rekognition-GetCelebrityRecognition-response-JobStatus)": "string",
   "[NextToken](#rekognition-GetCelebrityRecognition-response-NextToken)": "string",
   "[StatusMessage](#rekognition-GetCelebrityRecognition-response-StatusMessage)": "string",
   "[VideoMetadata](#rekognition-GetCelebrityRecognition-response-VideoMetadata)": { 
      "[Codec](API_VideoMetadata.md#rekognition-Type-VideoMetadata-Codec)": "string",
      "[DurationMillis](API_VideoMetadata.md#rekognition-Type-VideoMetadata-DurationMillis)": number,
      "[Format](API_VideoMetadata.md#rekognition-Type-VideoMetadata-Format)": "string",
      "[FrameHeight](API_VideoMetadata.md#rekognition-Type-VideoMetadata-FrameHeight)": number,
      "[FrameRate](API_VideoMetadata.md#rekognition-Type-VideoMetadata-FrameRate)": number,
      "[FrameWidth](API_VideoMetadata.md#rekognition-Type-VideoMetadata-FrameWidth)": number
   }
}
```

## Response Elements<a name="API_GetCelebrityRecognition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [Celebrities](#API_GetCelebrityRecognition_ResponseSyntax) **   <a name="rekognition-GetCelebrityRecognition-response-Celebrities"></a>
Array of celebrities recognized in the video\.  
Type: Array of [CelebrityRecognition](API_CelebrityRecognition.md) objects

 ** [JobStatus](#API_GetCelebrityRecognition_ResponseSyntax) **   <a name="rekognition-GetCelebrityRecognition-response-JobStatus"></a>
The current status of the celebrity recognition job\.  
Type: String  
Valid Values:` IN_PROGRESS | SUCCEEDED | FAILED` 

 ** [NextToken](#API_GetCelebrityRecognition_ResponseSyntax) **   <a name="rekognition-GetCelebrityRecognition-response-NextToken"></a>
If the response is truncated, Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of celebrities\.  
Type: String  
Length Constraints: Maximum length of 255\.

 ** [StatusMessage](#API_GetCelebrityRecognition_ResponseSyntax) **   <a name="rekognition-GetCelebrityRecognition-response-StatusMessage"></a>
If the job fails, `StatusMessage` provides a descriptive error message\.  
Type: String

 ** [VideoMetadata](#API_GetCelebrityRecognition_ResponseSyntax) **   <a name="rekognition-GetCelebrityRecognition-response-VideoMetadata"></a>
Information about a video that Rekognition Video analyzed\. `Videometadata` is returned in every page of paginated responses from a Rekognition Video operation\.  
Type: [VideoMetadata](API_VideoMetadata.md) object

## Errors<a name="API_GetCelebrityRecognition_Errors"></a>

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

## See Also<a name="API_GetCelebrityRecognition_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/GetCelebrityRecognition) 