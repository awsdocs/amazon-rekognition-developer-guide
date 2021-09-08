# GetSegmentDetection<a name="API_GetSegmentDetection"></a>

Gets the segment detection results of a Amazon Rekognition Video analysis started by [ StartSegmentDetection ](API_StartSegmentDetection.md)\.

Segment detection with Amazon Rekognition Video is an asynchronous operation\. You start segment detection by calling [ StartSegmentDetection ](API_StartSegmentDetection.md) which returns a job identifier \(`JobId`\)\. When the segment detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartSegmentDetection`\. To get the results of the segment detection operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`\. if so, call `GetSegmentDetection` and pass the job identifier \(`JobId`\) from the initial call of `StartSegmentDetection`\.

 `GetSegmentDetection` returns detected segments in an array \(`Segments`\) of [ SegmentDetection ](API_SegmentDetection.md) objects\. `Segments` is sorted by the segment types specified in the `SegmentTypes` input parameter of `StartSegmentDetection`\. Each element of the array includes the detected segment, the precentage confidence in the acuracy of the detected segment, the type of the segment, and the frame in which the segment was detected\.

Use `SelectedSegmentTypes` to find out the type of segment detection requested in the call to `StartSegmentDetection`\.

Use the `MaxResults` parameter to limit the number of segment detections returned\. If there are more results than specified in `MaxResults`, the value of `NextToken` in the operation response contains a pagination token for getting the next set of results\. To get the next page of results, call `GetSegmentDetection` and populate the `NextToken` request parameter with the token value returned from the previous call to `GetSegmentDetection`\.

For more information, see [Detecting video segments in stored video](segments.md)\. 

## Request Syntax<a name="API_GetSegmentDetection_RequestSyntax"></a>

```
{
   "JobId": "string",
   "MaxResults": number,
   "NextToken": "string"
}
```

## Request Parameters<a name="API_GetSegmentDetection_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [ JobId ](#API_GetSegmentDetection_RequestSyntax) **   <a name="rekognition-GetSegmentDetection-request-JobId"></a>
Job identifier for the text detection operation for which you want results returned\. You get the job identifer from an initial call to `StartSegmentDetection`\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$`   
Required: Yes

 ** [ MaxResults ](#API_GetSegmentDetection_RequestSyntax) **   <a name="rekognition-GetSegmentDetection-request-MaxResults"></a>
Maximum number of results to return per paginated call\. The largest value you can specify is 1000\.  
Type: Integer  
Valid Range: Minimum value of 1\.  
Required: No

 ** [ NextToken ](#API_GetSegmentDetection_RequestSyntax) **   <a name="rekognition-GetSegmentDetection-request-NextToken"></a>
If the response is truncated, Amazon Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of text\.  
Type: String  
Length Constraints: Maximum length of 255\.  
Required: No

## Response Syntax<a name="API_GetSegmentDetection_ResponseSyntax"></a>

```
{
   "AudioMetadata": [ 
      { 
         "Codec": "string",
         "DurationMillis": number,
         "NumberOfChannels": number,
         "SampleRate": number
      }
   ],
   "JobStatus": "string",
   "NextToken": "string",
   "Segments": [ 
      { 
         "DurationFrames": number,
         "DurationMillis": number,
         "DurationSMPTE": "string",
         "EndFrameNumber": number,
         "EndTimecodeSMPTE": "string",
         "EndTimestampMillis": number,
         "ShotSegment": { 
            "Confidence": number,
            "Index": number
         },
         "StartFrameNumber": number,
         "StartTimecodeSMPTE": "string",
         "StartTimestampMillis": number,
         "TechnicalCueSegment": { 
            "Confidence": number,
            "Type": "string"
         },
         "Type": "string"
      }
   ],
   "SelectedSegmentTypes": [ 
      { 
         "ModelVersion": "string",
         "Type": "string"
      }
   ],
   "StatusMessage": "string",
   "VideoMetadata": [ 
      { 
         "Codec": "string",
         "ColorRange": "string",
         "DurationMillis": number,
         "Format": "string",
         "FrameHeight": number,
         "FrameRate": number,
         "FrameWidth": number
      }
   ]
}
```

## Response Elements<a name="API_GetSegmentDetection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [ AudioMetadata ](#API_GetSegmentDetection_ResponseSyntax) **   <a name="rekognition-GetSegmentDetection-response-AudioMetadata"></a>
An array of [ AudioMetadata ](API_AudioMetadata.md) objects\. There can be multiple audio streams\. Each `AudioMetadata` object contains metadata for a single audio stream\. Audio information in an `AudioMetadata` objects includes the audio codec, the number of audio channels, the duration of the audio stream, and the sample rate\. Audio metadata is returned in each page of information returned by `GetSegmentDetection`\.  
Type: Array of [ AudioMetadata ](API_AudioMetadata.md) objects

 ** [ JobStatus ](#API_GetSegmentDetection_ResponseSyntax) **   <a name="rekognition-GetSegmentDetection-response-JobStatus"></a>
Current status of the segment detection job\.  
Type: String  
Valid Values:` IN_PROGRESS | SUCCEEDED | FAILED` 

 ** [ NextToken ](#API_GetSegmentDetection_ResponseSyntax) **   <a name="rekognition-GetSegmentDetection-response-NextToken"></a>
If the previous response was incomplete \(because there are more labels to retrieve\), Amazon Rekognition Video returns a pagination token in the response\. You can use this pagination token to retrieve the next set of text\.  
Type: String  
Length Constraints: Maximum length of 255\.

 ** [ Segments ](#API_GetSegmentDetection_ResponseSyntax) **   <a name="rekognition-GetSegmentDetection-response-Segments"></a>
An array of segments detected in a video\. The array is sorted by the segment types \(TECHNICAL\_CUE or SHOT\) specified in the `SegmentTypes` input parameter of `StartSegmentDetection`\. Within each segment type the array is sorted by timestamp values\.  
Type: Array of [ SegmentDetection ](API_SegmentDetection.md) objects

 ** [ SelectedSegmentTypes ](#API_GetSegmentDetection_ResponseSyntax) **   <a name="rekognition-GetSegmentDetection-response-SelectedSegmentTypes"></a>
An array containing the segment types requested in the call to `StartSegmentDetection`\.   
Type: Array of [ SegmentTypeInfo ](API_SegmentTypeInfo.md) objects

 ** [ StatusMessage ](#API_GetSegmentDetection_ResponseSyntax) **   <a name="rekognition-GetSegmentDetection-response-StatusMessage"></a>
If the job fails, `StatusMessage` provides a descriptive error message\.  
Type: String

 ** [ VideoMetadata ](#API_GetSegmentDetection_ResponseSyntax) **   <a name="rekognition-GetSegmentDetection-response-VideoMetadata"></a>
Currently, Amazon Rekognition Video returns a single [ VideoMetadata ](API_VideoMetadata.md) object in the `VideoMetadata` array\. The object contains information about the video stream in the input file that Amazon Rekognition Video chose to analyze\. The `VideoMetadata` object includes the video codec, video format and other information\. Video metadata is returned in each page of information returned by `GetSegmentDetection`\.  
Type: Array of [ VideoMetadata ](API_VideoMetadata.md) objects

## Errors<a name="API_GetSegmentDetection_Errors"></a>

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

## See Also<a name="API_GetSegmentDetection_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/GetSegmentDetection) 
+  [ AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/GetSegmentDetection) 
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GetSegmentDetection) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/GetSegmentDetection) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/GetSegmentDetection) 
+  [ AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/GetSegmentDetection) 
+  [ AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/GetSegmentDetection) 
+  [ AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/GetSegmentDetection) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/GetSegmentDetection) 