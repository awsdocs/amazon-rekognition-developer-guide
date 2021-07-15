# DetectModerationLabels<a name="API_DetectModerationLabels"></a>

Detects unsafe content in a specified JPEG or PNG format image\. Use `DetectModerationLabels` to moderate images depending on your requirements\. For example, you might want to filter images that contain nudity, but not images containing suggestive content\.

To filter images, use the labels returned by `DetectModerationLabels` to determine which types of content are appropriate\.

For information about moderation labels, see [Content moderation](moderation.md)\. For a list of moderation labels in Amazon Rekognition, see [Using the image and video moderation APIs](https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html#moderation-api)\.

You pass the input image either as base64\-encoded image bytes or as a reference to an image in an Amazon S3 bucket\. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported\. The image must be either a PNG or JPEG formatted file\. 

## Request Syntax<a name="API_DetectModerationLabels_RequestSyntax"></a>

```
{
   "HumanLoopConfig": { 
      "DataAttributes": { 
         "ContentClassifiers": [ "string" ]
      },
      "FlowDefinitionArn": "string",
      "HumanLoopName": "string"
   },
   "Image": { 
      "Bytes": blob,
      "S3Object": { 
         "Bucket": "string",
         "Name": "string",
         "Version": "string"
      }
   },
   "MinConfidence": number
}
```

## Request Parameters<a name="API_DetectModerationLabels_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [HumanLoopConfig](#API_DetectModerationLabels_RequestSyntax) **   <a name="rekognition-DetectModerationLabels-request-HumanLoopConfig"></a>
Sets up the configuration for human evaluation, including the FlowDefinition the image will be sent to\.  
Type: [HumanLoopConfig](API_HumanLoopConfig.md) object  
Required: No

 ** [Image](#API_DetectModerationLabels_RequestSyntax) **   <a name="rekognition-DetectModerationLabels-request-Image"></a>
The input image as base64\-encoded bytes or an S3 object\. If you use the AWS CLI to call Amazon Rekognition operations, passing base64\-encoded image bytes is not supported\.   
If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64\-encode image bytes passed using the `Bytes` field\. For more information, see [Images](images-information.md)\.  
Type: [Image](API_Image.md) object  
Required: Yes

 ** [MinConfidence](#API_DetectModerationLabels_RequestSyntax) **   <a name="rekognition-DetectModerationLabels-request-MinConfidence"></a>
Specifies the minimum confidence level for the labels to return\. Amazon Rekognition doesn't return any labels with a confidence level lower than this specified value\.  
If you don't specify `MinConfidence`, the operation returns labels with confidence values greater than or equal to 50 percent\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

## Response Syntax<a name="API_DetectModerationLabels_ResponseSyntax"></a>

```
{
   "HumanLoopActivationOutput": { 
      "HumanLoopActivationConditionsEvaluationResults": "string",
      "HumanLoopActivationReasons": [ "string" ],
      "HumanLoopArn": "string"
   },
   "ModerationLabels": [ 
      { 
         "Confidence": number,
         "Name": "string",
         "ParentName": "string"
      }
   ],
   "ModerationModelVersion": "string"
}
```

## Response Elements<a name="API_DetectModerationLabels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [HumanLoopActivationOutput](#API_DetectModerationLabels_ResponseSyntax) **   <a name="rekognition-DetectModerationLabels-response-HumanLoopActivationOutput"></a>
Shows the results of the human in the loop evaluation\.  
Type: [HumanLoopActivationOutput](API_HumanLoopActivationOutput.md) object

 ** [ModerationLabels](#API_DetectModerationLabels_ResponseSyntax) **   <a name="rekognition-DetectModerationLabels-response-ModerationLabels"></a>
Array of detected Moderation labels and the time, in milliseconds from the start of the video, they were detected\.  
Type: Array of [ModerationLabel](API_ModerationLabel.md) objects

 ** [ModerationModelVersion](#API_DetectModerationLabels_ResponseSyntax) **   <a name="rekognition-DetectModerationLabels-response-ModerationModelVersion"></a>
Version number of the moderation detection model that was used to detect unsafe content\.  
Type: String

## Errors<a name="API_DetectModerationLabels_Errors"></a>

 **AccessDeniedException**   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 **HumanLoopQuotaExceededException**   
The number of in\-progress human reviews you have has exceeded the number allowed\.  
HTTP Status Code: 400

 **ImageTooLargeException**   
The input image size exceeds the allowed limit\. If you are calling [DetectProtectiveEquipment](API_DetectProtectiveEquipment.md), the image size or resolution exceeds the allowed limit\. For more information, see [Guidelines and quotas in Amazon Rekognition](limits.md)\.   
HTTP Status Code: 400

 **InternalServerError**   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

 **InvalidImageFormatException**   
The provided image format is not supported\.   
HTTP Status Code: 400

 **InvalidParameterException**   
Input parameter violated a constraint\. Validate your parameter before calling the API operation again\.  
HTTP Status Code: 400

 **InvalidS3ObjectException**   
Amazon Rekognition is unable to access the S3 object specified in the request\.  
HTTP Status Code: 400

 **ProvisionedThroughputExceededException**   
The number of requests exceeded your throughput limit\. If you want to increase this limit, contact Amazon Rekognition\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_DetectModerationLabels_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DetectModerationLabels) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DetectModerationLabels) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DetectModerationLabels) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DetectModerationLabels) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DetectModerationLabels) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DetectModerationLabels) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DetectModerationLabels) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DetectModerationLabels) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DetectModerationLabels) 