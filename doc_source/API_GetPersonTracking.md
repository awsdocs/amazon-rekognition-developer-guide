# GetPersonTracking<a name="API_GetPersonTracking"></a>

Gets the person tracking results of a Rekognition Video analysis started by [StartPersonTracking](API_StartPersonTracking.md)\.

The person detection operation is started by a call to `StartPersonTracking` which returns a job identifier \(`JobId`\)\. When the person detection operation finishes, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to `StartPersonTracking`\.

To get the results of the person tracking operation, first check that the status value published to the Amazon SNS topic is `SUCCEEDED`\. If so, call [GetPersonTracking](#API_GetPersonTracking) and pass the job identifier \(`JobId`\) from the initial call to `StartPersonTracking`\.

 `GetPersonTracking` returns an array, `Persons`, of tracked persons and the time\(s\) they were tracked in the video\. 

By default, the array is sorted by the time\(s\) a person is tracked in the video\. You can sort by tracked persons by specifying `INDEX` for the `SortBy` input parameter\.

Use the `MaxResults` parameter to limit the number of items returned\. If there are more results than specified in `MaxResults`, the value of `NextToken` in the operation response contains a pagination token for getting the next set of results\. To get the next page of results, call `GetPersonTracking` and populate the `NextToken` request parameter with the token value returned from the previous call to `GetPersonTracking`\.

## Request Syntax<a name="API_GetPersonTracking_RequestSyntax"></a>

```
{
   "JobId": "string",
   "MaxResults": number,
   "NextToken": "string",
   "SortBy": "string"
}
```

## Request Parameters<a name="API_GetPersonTracking_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** JobId **   
The identifier for a job that tracks persons in a video\. You get the `JobId` from a call to `StartPersonTracking`\.   
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 64\.  
Pattern: `^[a-zA-Z0-9-_]+$`   
Required: Yes

 ** MaxResults **   
Maximum number of tracked persons to return\. The default is 1000\.   
Type: Integer  
Valid Range: Minimum value of 1\.  
Required: No

 ** NextToken **   
If the previous response was incomplete \(because there are more persons to retrieve\), Rekognition Video returns a pagination token in the response\. You can use this pagination token to retrieve the next set of persons\.   
Type: String  
Length Constraints: Maximum length of 255\.  
Required: No

 ** SortBy **   
Sort to use for elements in the `Persons` array\. Use `TIMESTAMP` to sort array elements by the time persons are detected\. Use `INDEX` to sort by the tracked persons\. If you sort by `INDEX`, the array elements for each person are sorted by detection confidence\. The default sort is by `TIMESTAMP`\.  
Type: String  
Valid Values:` INDEX | TIMESTAMP`   
Required: No

## Response Syntax<a name="API_GetPersonTracking_ResponseSyntax"></a>

```
{
   "JobStatus": "string",
   "NextToken": "string",
   "Persons": [ 
      { 
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
      "DurationMillis": number,
      "Format": "string",
      "FrameHeight": number,
      "FrameRate": number,
      "FrameWidth": number
   }
}
```

## Response Elements<a name="API_GetPersonTracking_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** JobStatus **   
The current status of the person tracking job\.  
Type: String  
Valid Values:` IN_PROGRESS | SUCCEEDED | FAILED` 

 ** NextToken **   
If the response is truncated, Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of persons\.   
Type: String  
Length Constraints: Maximum length of 255\.

 ** Persons **   
An array of the persons detected in the video and the times they are tracked throughout the video\. An array element will exist for each time the person is tracked\.   
Type: Array of [PersonDetection](API_PersonDetection.md) objects

 ** StatusMessage **   
If the job fails, `StatusMessage` provides a descriptive error message\.  
Type: String

 ** VideoMetadata **   
Information about a video that Rekognition Video analyzed\. `Videometadata` is returned in every page of paginated responses from a Rekognition Video operation\.  
Type: [VideoMetadata](API_VideoMetadata.md) object

## Errors<a name="API_GetPersonTracking_Errors"></a>

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

## See Also<a name="API_GetPersonTracking_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS Command Line Interface](http://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/GetPersonTracking) 

+  [AWS SDK for \.NET](http://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/GetPersonTracking) 

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GetPersonTracking) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/GetPersonTracking) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/GetPersonTracking) 

+  [AWS SDK for JavaScript](http://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/GetPersonTracking) 

+  [AWS SDK for PHP V3](http://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/GetPersonTracking) 

+  [AWS SDK for Python](http://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/GetPersonTracking) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/GetPersonTracking) 