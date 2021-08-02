# CreateStreamProcessor<a name="API_CreateStreamProcessor"></a>

Creates an Amazon Rekognition stream processor that you can use to detect and recognize faces in a streaming video\.

Amazon Rekognition Video is a consumer of live video from Amazon Kinesis Video Streams\. Amazon Rekognition Video sends analysis results to Amazon Kinesis Data Streams\.

You provide as input a Kinesis video stream \(`Input`\) and a Kinesis data stream \(`Output`\) stream\. You also specify the face recognition criteria in `Settings`\. For example, the collection containing faces that you want to recognize\. Use `Name` to assign an identifier for the stream processor\. You use `Name` to manage the stream processor\. For example, you can start processing the source video by calling [StartStreamProcessor](API_StartStreamProcessor.md) with the `Name` field\. 

After you have finished analyzing a streaming video, use [StopStreamProcessor](API_StopStreamProcessor.md) to stop processing\. You can delete the stream processor by calling [DeleteStreamProcessor](API_DeleteStreamProcessor.md)\.

This operation requires permissions to perform the `rekognition:CreateStreamProcessor` action\. If you want to tag your stream processor, you also require permission to perform the `rekognition:TagResource` operation\.

## Request Syntax<a name="API_CreateStreamProcessor_RequestSyntax"></a>

```
{
   "Input": { 
      "KinesisVideoStream": { 
         "Arn": "string"
      }
   },
   "Name": "string",
   "Output": { 
      "KinesisDataStream": { 
         "Arn": "string"
      }
   },
   "RoleArn": "string",
   "Settings": { 
      "FaceSearch": { 
         "CollectionId": "string",
         "FaceMatchThreshold": number
      }
   },
   "Tags": { 
      "string" : "string" 
   }
}
```

## Request Parameters<a name="API_CreateStreamProcessor_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [Input](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-Input"></a>
Kinesis video stream stream that provides the source streaming video\. If you are using the AWS CLI, the parameter name is `StreamProcessorInput`\.  
Type: [StreamProcessorInput](API_StreamProcessorInput.md) object  
Required: Yes

 ** [Name](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-Name"></a>
An identifier you assign to the stream processor\. You can use `Name` to manage the stream processor\. For example, you can get the current status of the stream processor by calling [DescribeStreamProcessor](API_DescribeStreamProcessor.md)\. `Name` is idempotent\.   
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 128\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

 ** [Output](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-Output"></a>
Kinesis data stream stream to which Amazon Rekognition Video puts the analysis results\. If you are using the AWS CLI, the parameter name is `StreamProcessorOutput`\.  
Type: [StreamProcessorOutput](API_StreamProcessorOutput.md) object  
Required: Yes

 ** [RoleArn](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-RoleArn"></a>
ARN of the IAM role that allows access to the stream processor\.  
Type: String  
Pattern: `arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`   
Required: Yes

 ** [Settings](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-Settings"></a>
Face recognition input parameters to be used by the stream processor\. Includes the collection to use for face recognition and the face attributes to detect\.  
Type: [StreamProcessorSettings](API_StreamProcessorSettings.md) object  
Required: Yes

 ** [Tags](#API_CreateStreamProcessor_RequestSyntax) **   <a name="rekognition-CreateStreamProcessor-request-Tags"></a>
 A set of tags \(key\-value pairs\) that you want to attach to the stream processor\.   
Type: String to string map  
Map Entries: Minimum number of 0 items\. Maximum number of 200 items\.  
Key Length Constraints: Minimum length of 1\. Maximum length of 128\.  
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`   
Value Length Constraints: Minimum length of 0\. Maximum length of 256\.  
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`   
Required: No

## Response Syntax<a name="API_CreateStreamProcessor_ResponseSyntax"></a>

```
{
   "StreamProcessorArn": "string"
}
```

## Response Elements<a name="API_CreateStreamProcessor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [StreamProcessorArn](#API_CreateStreamProcessor_ResponseSyntax) **   <a name="rekognition-CreateStreamProcessor-response-StreamProcessorArn"></a>
ARN for the newly create stream processor\.  
Type: String  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:streamprocessor\/.+$)` 

## Errors<a name="API_CreateStreamProcessor_Errors"></a>

 **AccessDeniedException**   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 **InternalServerError**   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

 **InvalidParameterException**   
Input parameter violated a constraint\. Validate your parameter before calling the API operation again\.  
HTTP Status Code: 400

 **LimitExceededException**   
An Amazon Rekognition service limit was exceeded\. For example, if you start too many Amazon Rekognition Video jobs concurrently, calls to start operations \(`StartLabelDetection`, for example\) will raise a `LimitExceededException` exception \(HTTP status code: 400\) until the number of concurrently running jobs is below the Amazon Rekognition service limit\.   
HTTP Status Code: 400

 **ProvisionedThroughputExceededException**   
The number of requests exceeded your throughput limit\. If you want to increase this limit, contact Amazon Rekognition\.  
HTTP Status Code: 400

 **ResourceInUseException**   
The specified resource is already being used\.  
HTTP Status Code: 400

 **ServiceQuotaExceededException**   
  
The size of the resource exceeds the allowed limit\. For more information, see [Guidelines and quotas in Amazon Rekognition](limits.md)\.   
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_CreateStreamProcessor_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/CreateStreamProcessor) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/CreateStreamProcessor) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CreateStreamProcessor) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/CreateStreamProcessor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/CreateStreamProcessor) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/CreateStreamProcessor) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/CreateStreamProcessor) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/CreateStreamProcessor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CreateStreamProcessor) 