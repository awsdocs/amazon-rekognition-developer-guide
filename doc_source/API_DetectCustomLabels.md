# DetectCustomLabels<a name="API_DetectCustomLabels"></a>

Detects custom labels in a supplied image by using an Amazon Rekognition Custom Labels model\. 

You specify which version of a model version to use by using the `ProjectVersionArn` input parameter\. 

You pass the input image as base64\-encoded image bytes or as a reference to an image in an Amazon S3 bucket\. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported\. The image must be either a PNG or JPEG formatted file\. 

 For each object that the model version detects on an image, the API returns a \(`CustomLabel`\) object in an array \(`CustomLabels`\)\. Each `CustomLabel` object provides the label name \(`Name`\), the level of confidence that the image contains the object \(`Confidence`\), and object location information, if it exists, for the label on the image \(`Geometry`\)\. 

To filter labels that are returned, specify a value for `MinConfidence`\. `DetectCustomLabelsLabels` only returns labels with a confidence that's higher than the specified value\. The value of `MinConfidence` maps to the assumed threshold values created during training\. For more information, see [ Assumed Threshold](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tr-metrics-use.html#tr-assumed-threshold)\. Amazon Rekognition Custom Labels expresses an assumed threshold as a floating point value between 0\-1\. The range of `MinConfidence` normalizes the assumed threshold to a percentage value \(0\-100\)\. Confidence responses from `DetectCustomLabels` are also returned as a percentage\. You can use `MinConfidence` to change the precision and recall or your model\. For more information, see [ Analyzing an image](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/detecting-custom-labels.html)\. 

If you don't specify a value for `MinConfidence`, `DetectCustomLabels` returns labels based on the assumed threshold of each label\.

This is a stateless API operation\. That is, the operation does not persist any data\.

This operation requires permissions to perform the `rekognition:DetectCustomLabels` action\. 

For more information, see [ Analyzing an image](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/detecting-custom-labels.html)\. 

## Request Syntax<a name="API_DetectCustomLabels_RequestSyntax"></a>

```
{
   "Image": { 
      "Bytes": blob,
      "S3Object": { 
         "Bucket": "string",
         "Name": "string",
         "Version": "string"
      }
   },
   "MaxResults": number,
   "MinConfidence": number,
   "ProjectVersionArn": "string"
}
```

## Request Parameters<a name="API_DetectCustomLabels_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [Image](#API_DetectCustomLabels_RequestSyntax) **   <a name="rekognition-DetectCustomLabels-request-Image"></a>
Provides the input image either as bytes or an S3 object\.  
You pass image bytes to an Amazon Rekognition API operation by using the `Bytes` property\. For example, you would use the `Bytes` property to pass an image loaded from a local file system\. Image bytes passed by using the `Bytes` property must be base64\-encoded\. Your code may not need to encode image bytes if you are using an AWS SDK to call Amazon Rekognition API operations\.   
For more information, see [Analyzing an image loaded from a local file system](images-bytes.md)\.  
 You pass images stored in an S3 bucket to an Amazon Rekognition API operation by using the `S3Object` property\. Images stored in an S3 bucket do not need to be base64\-encoded\.  
The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations\.  
If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes using the Bytes property is not supported\. You must first upload the image to an Amazon S3 bucket and then call the operation using the S3Object property\.  
For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object\. For more information, see [Amazon Rekognition resource\-based policies](security_iam_service-with-iam.md#security_iam_service-with-iam-resource-based-policies)\.   
Type: [Image](API_Image.md) object  
Required: Yes

 ** [MaxResults](#API_DetectCustomLabels_RequestSyntax) **   <a name="rekognition-DetectCustomLabels-request-MaxResults"></a>
Maximum number of results you want the service to return in the response\. The service returns the specified number of highest confidence labels ranked from highest confidence to lowest\.  
Type: Integer  
Valid Range: Minimum value of 0\.  
Required: No

 ** [MinConfidence](#API_DetectCustomLabels_RequestSyntax) **   <a name="rekognition-DetectCustomLabels-request-MinConfidence"></a>
Specifies the minimum confidence level for the labels to return\. `DetectCustomLabels` doesn't return any labels with a confidence value that's lower than this specified value\. If you specify a value of 0, `DetectCustomLabels` returns all labels, regardless of the assumed threshold applied to each label\. If you don't specify a value for `MinConfidence`, `DetectCustomLabels` returns labels based on the assumed threshold of each label\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 ** [ProjectVersionArn](#API_DetectCustomLabels_RequestSyntax) **   <a name="rekognition-DetectCustomLabels-request-ProjectVersionArn"></a>
The ARN of the model version that you want to use\.  
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/version\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`   
Required: Yes

## Response Syntax<a name="API_DetectCustomLabels_ResponseSyntax"></a>

```
{
   "CustomLabels": [ 
      { 
         "Confidence": number,
         "Geometry": { 
            "BoundingBox": { 
               "Height": number,
               "Left": number,
               "Top": number,
               "Width": number
            },
            "Polygon": [ 
               { 
                  "X": number,
                  "Y": number
               }
            ]
         },
         "Name": "string"
      }
   ]
}
```

## Response Elements<a name="API_DetectCustomLabels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [CustomLabels](#API_DetectCustomLabels_ResponseSyntax) **   <a name="rekognition-DetectCustomLabels-response-CustomLabels"></a>
An array of custom labels detected in the input image\.  
Type: Array of [CustomLabel](API_CustomLabel.md) objects

## Errors<a name="API_DetectCustomLabels_Errors"></a>

 **AccessDeniedException**   
You are not authorized to perform the action\.  
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

 **LimitExceededException**   
An Amazon Rekognition service limit was exceeded\. For example, if you start too many Amazon Rekognition Video jobs concurrently, calls to start operations \(`StartLabelDetection`, for example\) will raise a `LimitExceededException` exception \(HTTP status code: 400\) until the number of concurrently running jobs is below the Amazon Rekognition service limit\.   
HTTP Status Code: 400

 **ProvisionedThroughputExceededException**   
The number of requests exceeded your throughput limit\. If you want to increase this limit, contact Amazon Rekognition\.  
HTTP Status Code: 400

 **ResourceNotFoundException**   
The resource specified in the request cannot be found\.  
HTTP Status Code: 400

 **ResourceNotReadyException**   
The requested resource isn't ready\. For example, this exception occurs when you call `DetectCustomLabels` with a model version that isn't deployed\.   
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_DetectCustomLabels_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DetectCustomLabels) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DetectCustomLabels) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DetectCustomLabels) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DetectCustomLabels) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DetectCustomLabels) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DetectCustomLabels) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DetectCustomLabels) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DetectCustomLabels) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DetectCustomLabels) 