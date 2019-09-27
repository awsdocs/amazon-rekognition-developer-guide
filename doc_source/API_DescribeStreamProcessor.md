# DescribeStreamProcessor<a name="API_DescribeStreamProcessor"></a>

Provides information about a stream processor created by [CreateStreamProcessor](API_CreateStreamProcessor.md)\. You can get information about the input and output streams, the input parameters for the face recognition being performed, and the current status of the stream processor\.

## Request Syntax<a name="API_DescribeStreamProcessor_RequestSyntax"></a>

```
{
   "[Name](#rekognition-DescribeStreamProcessor-request-Name)": "string"
}
```

## Request Parameters<a name="API_DescribeStreamProcessor_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [Name](#API_DescribeStreamProcessor_RequestSyntax) **   <a name="rekognition-DescribeStreamProcessor-request-Name"></a>
Name of the stream processor for which you want information\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 128\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

## Response Syntax<a name="API_DescribeStreamProcessor_ResponseSyntax"></a>

```
{
   "[CreationTimestamp](#rekognition-DescribeStreamProcessor-response-CreationTimestamp)": number,
   "[Input](#rekognition-DescribeStreamProcessor-response-Input)": { 
      "[KinesisVideoStream](API_StreamProcessorInput.md#rekognition-Type-StreamProcessorInput-KinesisVideoStream)": { 
         "[Arn](API_KinesisVideoStream.md#rekognition-Type-KinesisVideoStream-Arn)": "string"
      }
   },
   "[LastUpdateTimestamp](#rekognition-DescribeStreamProcessor-response-LastUpdateTimestamp)": number,
   "[Name](#rekognition-DescribeStreamProcessor-response-Name)": "string",
   "[Output](#rekognition-DescribeStreamProcessor-response-Output)": { 
      "[KinesisDataStream](API_StreamProcessorOutput.md#rekognition-Type-StreamProcessorOutput-KinesisDataStream)": { 
         "[Arn](API_KinesisDataStream.md#rekognition-Type-KinesisDataStream-Arn)": "string"
      }
   },
   "[RoleArn](#rekognition-DescribeStreamProcessor-response-RoleArn)": "string",
   "[Settings](#rekognition-DescribeStreamProcessor-response-Settings)": { 
      "[FaceSearch](API_StreamProcessorSettings.md#rekognition-Type-StreamProcessorSettings-FaceSearch)": { 
         "[CollectionId](API_FaceSearchSettings.md#rekognition-Type-FaceSearchSettings-CollectionId)": "string",
         "[FaceMatchThreshold](API_FaceSearchSettings.md#rekognition-Type-FaceSearchSettings-FaceMatchThreshold)": number
      }
   },
   "[Status](#rekognition-DescribeStreamProcessor-response-Status)": "string",
   "[StatusMessage](#rekognition-DescribeStreamProcessor-response-StatusMessage)": "string",
   "[StreamProcessorArn](#rekognition-DescribeStreamProcessor-response-StreamProcessorArn)": "string"
}
```

## Response Elements<a name="API_DescribeStreamProcessor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [CreationTimestamp](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-CreationTimestamp"></a>
Date and time the stream processor was created  
Type: Timestamp

 ** [Input](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-Input"></a>
Kinesis video stream that provides the source streaming video\.  
Type: [StreamProcessorInput](API_StreamProcessorInput.md) object

 ** [LastUpdateTimestamp](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-LastUpdateTimestamp"></a>
The time, in Unix format, the stream processor was last updated\. For example, when the stream processor moves from a running state to a failed state, or when the user starts or stops the stream processor\.  
Type: Timestamp

 ** [Name](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-Name"></a>
Name of the stream processor\.   
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 128\.  
Pattern: `[a-zA-Z0-9_.\-]+` 

 ** [Output](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-Output"></a>
Kinesis data stream to which Amazon Rekognition Video puts the analysis results\.  
Type: [StreamProcessorOutput](API_StreamProcessorOutput.md) object

 ** [RoleArn](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-RoleArn"></a>
ARN of the IAM role that allows access to the stream processor\.  
Type: String  
Pattern: `arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+` 

 ** [Settings](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-Settings"></a>
Face recognition input parameters that are being used by the stream processor\. Includes the collection to use for face recognition and the face attributes to detect\.  
Type: [StreamProcessorSettings](API_StreamProcessorSettings.md) object

 ** [Status](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-Status"></a>
Current status of the stream processor\.  
Type: String  
Valid Values:` STOPPED | STARTING | RUNNING | FAILED | STOPPING` 

 ** [StatusMessage](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-StatusMessage"></a>
Detailed status message about the stream processor\.  
Type: String

 ** [StreamProcessorArn](#API_DescribeStreamProcessor_ResponseSyntax) **   <a name="rekognition-DescribeStreamProcessor-response-StreamProcessorArn"></a>
ARN of the stream processor\.  
Type: String  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:streamprocessor\/.+$)` 

## Errors<a name="API_DescribeStreamProcessor_Errors"></a>

 **AccessDeniedException**   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 **InternalServerError**   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

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

## See Also<a name="API_DescribeStreamProcessor_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DescribeStreamProcessor) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DescribeStreamProcessor) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DescribeStreamProcessor) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DescribeStreamProcessor) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/DescribeStreamProcessor) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DescribeStreamProcessor) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DescribeStreamProcessor) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DescribeStreamProcessor) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/DescribeStreamProcessor) 