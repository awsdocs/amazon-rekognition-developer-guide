# DetectModerationLabels<a name="API_DetectModerationLabels"></a>

Detects explicit or suggestive adult content in a specified JPEG or PNG format image\. Use `DetectModerationLabels` to moderate images depending on your requirements\. For example, you might want to filter images that contain nudity, but not images containing suggestive content\.

To filter images, use the labels returned by `DetectModerationLabels` to determine which types of content are appropriate\. For information about moderation labels, see [Detecting Unsafe Content](moderation.md)\.

You pass the input image either as base64\-encoded image bytes or as a reference to an image in an Amazon S3 bucket\. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported\. The image must be either a PNG or JPEG formatted file\. 

## Request Syntax<a name="API_DetectModerationLabels_RequestSyntax"></a>

```
{
   "[Image](#rekognition-DetectModerationLabels-request-Image)": { 
      "[Bytes](API_Image.md#rekognition-Type-Image-Bytes)": blob,
      "[S3Object](API_Image.md#rekognition-Type-Image-S3Object)": { 
         "[Bucket](API_S3Object.md#rekognition-Type-S3Object-Bucket)": "string",
         "[Name](API_S3Object.md#rekognition-Type-S3Object-Name)": "string",
         "[Version](API_S3Object.md#rekognition-Type-S3Object-Version)": "string"
      }
   },
   "[MinConfidence](#rekognition-DetectModerationLabels-request-MinConfidence)": number
}
```

## Request Parameters<a name="API_DetectModerationLabels_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [Image](#API_DetectModerationLabels_RequestSyntax) **   <a name="rekognition-DetectModerationLabels-request-Image"></a>
The input image as base64\-encoded bytes or an S3 object\. If you use the AWS CLI to call Amazon Rekognition operations, passing base64\-encoded image bytes is not supported\.   
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
   "[ModerationLabels](#rekognition-DetectModerationLabels-response-ModerationLabels)": [ 
      { 
         "[Confidence](API_ModerationLabel.md#rekognition-Type-ModerationLabel-Confidence)": number,
         "[Name](API_ModerationLabel.md#rekognition-Type-ModerationLabel-Name)": "string",
         "[ParentName](API_ModerationLabel.md#rekognition-Type-ModerationLabel-ParentName)": "string"
      }
   ]
}
```

## Response Elements<a name="API_DetectModerationLabels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [ModerationLabels](#API_DetectModerationLabels_ResponseSyntax) **   <a name="rekognition-DetectModerationLabels-response-ModerationLabels"></a>
Array of detected Moderation labels and the time, in millseconds from the start of the video, they were detected\.  
Type: Array of [ModerationLabel](API_ModerationLabel.md) objects

## Errors<a name="API_DetectModerationLabels_Errors"></a>

 **AccessDeniedException**   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 **ImageTooLargeException**   
The input image size exceeds the allowed limit\. For more information, see [Limits in Amazon Rekognition](limits.md)\.   
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

## Examples<a name="API_DetectModerationLabels_Examples"></a>

### Example Request<a name="API_DetectModerationLabels_Example_1"></a>

The following example shows the request for a `DetectModerationLabels` API operation\.

#### Sample Request<a name="API_DetectModerationLabels_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: rekognition.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 77
X-Amz-Target: RekognitionService.DetectModerationLabels
X-Amz-Date: 20170424T195840Z
User-Agent: aws-cli/1.11.44 Python/2.7.6 Linux/4.2.0-42-generic botocore/1.5.7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=XXXXXXXXXXXXXXXXXXXXXXXXX/20170424/us-west-2/rekognition/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=XXXXXXXXXXXXXXXXXXXXXXXXX
{
   "Image":{
      "S3Object":{
         "Bucket":"example-photos",
         "Name":"input.jpg"
      }
   }
}
```

### Example Response<a name="API_DetectModerationLabels_Example_2"></a>

The following example shows the response of a call to `DetectmoderationLabels`\.

#### Sample Response<a name="API_DetectModerationLabels_Example_2_Response"></a>

```
{
    "ModerationLabels": [
        {
            "Confidence": 79.03318786621094,
            "ParentName": "",
            "Name": "Explicit Nudity"
        },
        {
            "Confidence": 79.03318786621094,
            "ParentName": "Explicit Nudity",
            "Name": "Graphic Male Nudity"
        },
        {
            "Confidence": 68.99967956542969,
            "ParentName": "Explicit Nudity",
            "Name": "Sexual Activity"
        }
    ]
}
```

## See Also<a name="API_DetectModerationLabels_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS Command Line Interface](http://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DetectModerationLabels) 

+  [AWS SDK for \.NET](http://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DetectModerationLabels) 

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DetectModerationLabels) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DetectModerationLabels) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/DetectModerationLabels) 

+  [AWS SDK for JavaScript](http://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DetectModerationLabels) 

+  [AWS SDK for PHP V3](http://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DetectModerationLabels) 

+  [AWS SDK for Python](http://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DetectModerationLabels) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/DetectModerationLabels) 