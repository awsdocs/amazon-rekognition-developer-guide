# GetCelebrityRecognition<a name="API_GetCelebrityRecognition"></a>

Gets the celebrity recognition results for a Amazon Rekognition Video analysis started by [ StartCelebrityRecognition ](API_StartCelebrityRecognition.md)\.

Celebrity recognition in a video is an asynchronous operation\. Analysis is started by a call to [ StartCelebrityRecognition ](API_StartCelebrityRecognition.md) which returns a job identifier \(`JobId`\)\. When the celebrity recognition operation finishes, Amazon Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartCelebrityRecognition`\. To get the results of the celebrity recognition analysis, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`\. If so, call `GetCelebrityDetection` and pass the job identifier \(`JobId`\) from the initial call to `StartCelebrityDetection`\. 

For more information, see [Working with stored videos](video.md)\.

 `GetCelebrityRecognition` returns detected celebrities and the time\(s\) they are detected in an array \(`Celebrities`\) of [ CelebrityRecognition ](API_CelebrityRecognition.md) objects\. Each `CelebrityRecognition` contains information about the celebrity in a [ CelebrityDetail ](API_CelebrityDetail.md) object and the time, `Timestamp`, the celebrity was detected\. 

**Note**  
 `GetCelebrityRecognition` only returns the default facial attributes \(`BoundingBox`, `Confidence`, `Landmarks`, `Pose`, and `Quality`\)\. The other facial attributes listed in the `Face` object of the following response syntax are not returned\. For more information, see [ FaceDetail ](API_FaceDetail.md)\. 

By default, the `Celebrities` array is sorted by time \(milliseconds from the start of the video\)\. You can also sort the array by celebrity by specifying the value `ID` in the `SortBy` input parameter\.

The `CelebrityDetail` object includes the celebrity identifer and additional information urls\. If you don't store the additional information urls, you can get them later by calling [ GetCelebrityInfo ](API_GetCelebrityInfo.md) with the celebrity identifer\.

No information is returned for faces not recognized as celebrities\.

Use MaxResults parameter to limit the number of labels returned\. If there are more results than specified in `MaxResults`, the value of `NextToken` in the operation response contains a pagination token for getting the next set of results\. To get the next page of results, call `GetCelebrityDetection` and populate the `NextToken` request parameter with the token value returned from the previous call to `GetCelebrityRecognition`\.

## Request Syntax<a name="API_GetCelebrityRecognition_RequestSyntax"></a>

```
{
   "JobId": "string",
   "MaxResults": number,
   "NextToken": "string",
   "SortBy": "string"
}
```

## Request Parameters<a name="API_GetCelebrityRecognition_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ JobId ](#API_GetCelebrityRecognition_RequestSyntax) **   <a name="rekognition-GetCelebrityRecognition-request-JobId"></a>
Job identifier for the required celebrity recognition analysis\. You can get the job identifer from a call to `StartCelebrityRecognition`\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$`   
Required: Yes

 ** [ MaxResults ](#API_GetCelebrityRecognition_RequestSyntax) **   <a name="rekognition-GetCelebrityRecognition-request-MaxResults"></a>
Maximum number of results to return per paginated call\. The largest value you can specify is 1000\. If you specify a value greater than 1000, a maximum of 1000 results is returned\. The default value is 1000\.  
Type: Integer  
Valid Range: Minimum value of 1\.  
Required: No

 ** [ NextToken ](#API_GetCelebrityRecognition_RequestSyntax) **   <a name="rekognition-GetCelebrityRecognition-request-NextToken"></a>
If the previous response was incomplete \(because there is more recognized celebrities to retrieve\), Amazon Rekognition Video returns a pagination token in the response\. You can use this pagination token to retrieve the next set of celebrities\.   
Type: String  
Length Constraints: Maximum length of 255\.  
Required: No

 ** [ SortBy ](#API_GetCelebrityRecognition_RequestSyntax) **   <a name="rekognition-GetCelebrityRecognition-request-SortBy"></a>
Sort to use for celebrities returned in `Celebrities` field\. Specify `ID` to sort by the celebrity identifier, specify `TIMESTAMP` to sort by the time the celebrity was recognized\.  
Type: String  
Valid Values:` ID | TIMESTAMP`   
Required: No

## Response Syntax<a name="API_GetCelebrityRecognition_ResponseSyntax"></a>

```
{
   "Celebrities": [ 
      { 
         "Celebrity": { 
            "BoundingBox": { 
               "Height": number,
               "Left": number,
               "Top": number,
               "Width": number
            },
            "Confidence": number,
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
            "Id": "string",
            "Name": "string",
            "Urls": [ "string" ]
         },
         "Timestamp": number
      }
   ],
   "JobStatus": "string",
   "NextToken": "string",
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

## Response Elements<a name="API_GetCelebrityRecognition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [ Celebrities ](#API_GetCelebrityRecognition_ResponseSyntax) **   <a name="rekognition-GetCelebrityRecognition-response-Celebrities"></a>
Array of celebrities recognized in the video\.  
Type: Array of [ CelebrityRecognition ](API_CelebrityRecognition.md) objects

 ** [ JobStatus ](#API_GetCelebrityRecognition_ResponseSyntax) **   <a name="rekognition-GetCelebrityRecognition-response-JobStatus"></a>
The current status of the celebrity recognition job\.  
Type: String  
Valid Values:` IN_PROGRESS | SUCCEEDED | FAILED` 

 ** [ NextToken ](#API_GetCelebrityRecognition_ResponseSyntax) **   <a name="rekognition-GetCelebrityRecognition-response-NextToken"></a>
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of celebrities\.  
Type: String  
Length Constraints: Maximum length of 255\.

 ** [ StatusMessage ](#API_GetCelebrityRecognition_ResponseSyntax) **   <a name="rekognition-GetCelebrityRecognition-response-StatusMessage"></a>
If the job fails, `StatusMessage` provides a descriptive error message\.  
Type: String

 ** [ VideoMetadata ](#API_GetCelebrityRecognition_ResponseSyntax) **   <a name="rekognition-GetCelebrityRecognition-response-VideoMetadata"></a>
Information about a video that Amazon Rekognition Video analyzed\. `Videometadata` is returned in every page of paginated responses from a Amazon Rekognition Video operation\.  
Type: [ VideoMetadata ](API_VideoMetadata.md) object

## Errors<a name="API_GetCelebrityRecognition_Errors"></a>

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

## See Also<a name="API_GetCelebrityRecognition_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [ AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [ AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [ AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [ AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/GetCelebrityRecognition) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/GetCelebrityRecognition) 