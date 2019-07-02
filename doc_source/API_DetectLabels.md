# DetectLabels<a name="API_DetectLabels"></a>

Detects instances of real\-world entities within an image \(JPEG or PNG\) provided as input\. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; and concepts like landscape, evening, and nature\. 

For an example, see [Analyzing Images Stored in an Amazon S3 Bucket](images-s3.md)\.

**Note**  
 `DetectLabels` does not support the detection of activities\. However, activity detection is supported for label detection in videos\. For more information, see [StartLabelDetection](API_StartLabelDetection.md)\.

You pass the input image as base64\-encoded image bytes or as a reference to an image in an Amazon S3 bucket\. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported\. The image must be either a PNG or JPEG formatted file\. 

 For each object, scene, and concept the API returns one or more labels\. Each label provides the object name, and the level of confidence that the image contains the object\. For example, suppose the input image has a lighthouse, the sea, and a rock\. The response includes all three labels, one for each object\. 

 `{Name: lighthouse, Confidence: 98.4629}` 

 `{Name: rock,Confidence: 79.2097}` 

 ` {Name: sea,Confidence: 75.061}` 

In the preceding example, the operation returns one label for each of the three objects\. The operation can also return multiple labels for the same object in the image\. For example, if the input image shows a flower \(for example, a tulip\), the operation might return the following three labels\. 

 `{Name: flower,Confidence: 99.0562}` 

 `{Name: plant,Confidence: 99.0562}` 

 `{Name: tulip,Confidence: 99.0562}` 

In this example, the detection algorithm more precisely identifies the flower as a tulip\.

In response, the API returns an array of labels\. In addition, the response also includes the orientation correction\. Optionally, you can specify `MinConfidence` to control the confidence threshold for the labels returned\. The default is 55%\. You can also add the `MaxLabels` parameter to limit the number of labels returned\. 

**Note**  
If the object detected is a person, the operation doesn't provide the same facial details that the [DetectFaces](API_DetectFaces.md) operation provides\.

 `DetectLabels` returns bounding boxes for instances of common object labels in an array of [Instance](API_Instance.md) objects\. An `Instance` object contains a [BoundingBox](API_BoundingBox.md) object, for the location of the label on the image\. It also includes the confidence by which the bounding box was detected\.

 `DetectLabels` also returns a hierarchical taxonomy of detected labels\. For example, a detected car might be assigned the label *car*\. The label *car* has two parent labels: *Vehicle* \(its parent\) and *Transportation* \(its grandparent\)\. The response returns the entire list of ancestors for a label\. Each ancestor is a unique label in the response\. In the previous example, *Car*, *Vehicle*, and *Transportation* are returned as unique labels in the response\. 

This is a stateless API operation\. That is, the operation does not persist any data\.

This operation requires permissions to perform the `rekognition:DetectLabels` action\. 

## Request Syntax<a name="API_DetectLabels_RequestSyntax"></a>

```
{
   "[Image](#rekognition-DetectLabels-request-Image)": { 
      "[Bytes](API_Image.md#rekognition-Type-Image-Bytes)": blob,
      "[S3Object](API_Image.md#rekognition-Type-Image-S3Object)": { 
         "[Bucket](API_S3Object.md#rekognition-Type-S3Object-Bucket)": "string",
         "[Name](API_S3Object.md#rekognition-Type-S3Object-Name)": "string",
         "[Version](API_S3Object.md#rekognition-Type-S3Object-Version)": "string"
      }
   },
   "[MaxLabels](#rekognition-DetectLabels-request-MaxLabels)": number,
   "[MinConfidence](#rekognition-DetectLabels-request-MinConfidence)": number
}
```

## Request Parameters<a name="API_DetectLabels_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [Image](#API_DetectLabels_RequestSyntax) **   <a name="rekognition-DetectLabels-request-Image"></a>
The input image as base64\-encoded bytes or an S3 object\. If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported\. Images stored in an S3 Bucket do not need to be base64\-encoded\.  
If you are using an AWS SDK to call Amazon Rekognition, you might not need to base64\-encode image bytes passed using the `Bytes` field\. For more information, see [Images](images-information.md)\.  
Type: [Image](API_Image.md) object  
Required: Yes

 ** [MaxLabels](#API_DetectLabels_RequestSyntax) **   <a name="rekognition-DetectLabels-request-MaxLabels"></a>
Maximum number of labels you want the service to return in the response\. The service returns the specified number of highest confidence labels\.   
Type: Integer  
Valid Range: Minimum value of 0\.  
Required: No

 ** [MinConfidence](#API_DetectLabels_RequestSyntax) **   <a name="rekognition-DetectLabels-request-MinConfidence"></a>
Specifies the minimum confidence level for the labels to return\. Amazon Rekognition doesn't return any labels with confidence lower than this specified value\.  
If `MinConfidence` is not specified, the operation returns labels with a confidence values greater than or equal to 55 percent\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

## Response Syntax<a name="API_DetectLabels_ResponseSyntax"></a>

```
{
   "[LabelModelVersion](#rekognition-DetectLabels-response-LabelModelVersion)": "string",
   "[Labels](#rekognition-DetectLabels-response-Labels)": [ 
      { 
         "[Confidence](API_Label.md#rekognition-Type-Label-Confidence)": number,
         "[Instances](API_Label.md#rekognition-Type-Label-Instances)": [ 
            { 
               "[BoundingBox](API_Instance.md#rekognition-Type-Instance-BoundingBox)": { 
                  "[Height](API_BoundingBox.md#rekognition-Type-BoundingBox-Height)": number,
                  "[Left](API_BoundingBox.md#rekognition-Type-BoundingBox-Left)": number,
                  "[Top](API_BoundingBox.md#rekognition-Type-BoundingBox-Top)": number,
                  "[Width](API_BoundingBox.md#rekognition-Type-BoundingBox-Width)": number
               },
               "[Confidence](API_Instance.md#rekognition-Type-Instance-Confidence)": number
            }
         ],
         "[Name](API_Label.md#rekognition-Type-Label-Name)": "string",
         "[Parents](API_Label.md#rekognition-Type-Label-Parents)": [ 
            { 
               "[Name](API_Parent.md#rekognition-Type-Parent-Name)": "string"
            }
         ]
      }
   ],
   "[OrientationCorrection](#rekognition-DetectLabels-response-OrientationCorrection)": "string"
}
```

## Response Elements<a name="API_DetectLabels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [LabelModelVersion](#API_DetectLabels_ResponseSyntax) **   <a name="rekognition-DetectLabels-response-LabelModelVersion"></a>
Version number of the label detection model that was used to detect labels\.  
Type: String

 ** [Labels](#API_DetectLabels_ResponseSyntax) **   <a name="rekognition-DetectLabels-response-Labels"></a>
An array of labels for the real\-world objects detected\.   
Type: Array of [Label](API_Label.md) objects

 ** [OrientationCorrection](#API_DetectLabels_ResponseSyntax) **   <a name="rekognition-DetectLabels-response-OrientationCorrection"></a>
The value of `OrientationCorrection` is always null\.  
If the input image is in \.jpeg format, it might contain exchangeable image file format \(Exif\) metadata that includes the image's orientation\. Amazon Rekognition uses this orientation information to perform image correction\. The bounding box coordinates are translated to represent object locations after the orientation information in the Exif metadata is used to correct the image orientation\. Images in \.png format don't contain Exif metadata\.  
Amazon Rekognition doesn’t perform image correction for images in \.png format and \.jpeg images without orientation information in the image Exif metadata\. The bounding box coordinates aren't translated and represent the object locations before the image is rotated\.   
Type: String  
Valid Values:` ROTATE_0 | ROTATE_90 | ROTATE_180 | ROTATE_270` 

## Errors<a name="API_DetectLabels_Errors"></a>

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

## See Also<a name="API_DetectLabels_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DetectLabels) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DetectLabels) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DetectLabels) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DetectLabels) 
+  [AWS SDK for Go \- Pilot](https://docs.aws.amazon.com/goto/SdkForGoPilot/rekognition-2016-06-27/DetectLabels) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/DetectLabels) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DetectLabels) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DetectLabels) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DetectLabels) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/DetectLabels) 