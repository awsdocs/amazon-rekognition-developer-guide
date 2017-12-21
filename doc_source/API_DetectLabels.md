# DetectLabels<a name="API_DetectLabels"></a>

Detects instances of real\-world entities within an image \(JPEG or PNG\) provided as input\. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; and concepts like landscape, evening, and nature\. For an example, see [Analysing Images Stored in an Amazon S3 Bucket](images-s3.md)\.

**Note**  
 `DetectLabels` does not support the detection of activities\. However, activity detection is supported for label detection in videos\. For more information, see [StartLabelDetection](API_StartLabelDetection.md)\.

You pass the input image as base64\-encoded image bytes or as a reference to an image in an Amazon S3 bucket\. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported\. The image must be either a PNG or JPEG formatted file\. 

 For each object, scene, and concept the API returns one or more labels\. Each label provides the object name, and the level of confidence that the image contains the object\. For example, suppose the input image has a lighthouse, the sea, and a rock\. The response will include all three labels, one for each object\. 

 `{Name: lighthouse, Confidence: 98.4629}` 

 `{Name: rock,Confidence: 79.2097}` 

 ` {Name: sea,Confidence: 75.061}` 

 In the preceding example, the operation returns one label for each of the three objects\. The operation can also return multiple labels for the same object in the image\. For example, if the input image shows a flower \(for example, a tulip\), the operation might return the following three labels\. 

 `{Name: flower,Confidence: 99.0562}` 

 `{Name: plant,Confidence: 99.0562}` 

 `{Name: tulip,Confidence: 99.0562}` 

In this example, the detection algorithm more precisely identifies the flower as a tulip\.

In response, the API returns an array of labels\. In addition, the response also includes the orientation correction\. Optionally, you can specify `MinConfidence` to control the confidence threshold for the labels returned\. The default is 50%\. You can also add the `MaxLabels` parameter to limit the number of labels returned\. 

**Note**  
If the object detected is a person, the operation doesn't provide the same facial details that the [DetectFaces](API_DetectFaces.md) operation provides\.

This is a stateless API operation\. That is, the operation does not persist any data\.

This operation requires permissions to perform the `rekognition:DetectLabels` action\. 

## Request Syntax<a name="API_DetectLabels_RequestSyntax"></a>

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
   "MaxLabels": number,
   "MinConfidence": number
}
```

## Request Parameters<a name="API_DetectLabels_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** Image **   
The input image as base64\-encoded bytes or an S3 object\. If you use the AWS CLI to call Amazon Rekognition operations, passing base64\-encoded image bytes is not supported\.   
Type: [Image](API_Image.md) object  
Required: Yes

 ** MaxLabels **   
Maximum number of labels you want the service to return in the response\. The service returns the specified number of highest confidence labels\.   
Type: Integer  
Valid Range: Minimum value of 0\.  
Required: No

 ** MinConfidence **   
Specifies the minimum confidence level for the labels to return\. Amazon Rekognition doesn't return any labels with confidence lower than this specified value\.  
If `MinConfidence` is not specified, the operation returns labels with a confidence values greater than or equal to 50 percent\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

## Response Syntax<a name="API_DetectLabels_ResponseSyntax"></a>

```
{
   "Labels": [ 
      { 
         "Confidence": number,
         "Name": "string"
      }
   ],
   "OrientationCorrection": "string"
}
```

## Response Elements<a name="API_DetectLabels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** Labels **   
An array of labels for the real\-world objects detected\.   
Type: Array of [Label](API_Label.md) objects

 ** OrientationCorrection **   
 The orientation of the input image \(counter\-clockwise direction\)\. If your application displays the image, you can use this value to correct the orientation\. If Amazon Rekognition detects that the input image was rotated \(for example, by 90 degrees\), it first corrects the orientation before detecting the labels\.   
If the input image Exif metadata populates the orientation field, Amazon Rekognition does not perform orientation correction and the value of OrientationCorrection will be null\.
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

## Example<a name="API_DetectLabels_Examples"></a>

### Example Request<a name="API_DetectLabels_Example_1"></a>

The following example shows a request that detects labels in an image \(skateboard\.jpg\) stored in an Amazon S3 bucket \(example\-photos\)\.

#### Sample Request<a name="API_DetectLabels_Example_1_Request"></a>

```
POST https://rekognition.us-west-2.amazonaws.com/ HTTP/1.1
Host: rekognition.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 91
X-Amz-Target: RekognitionService.DetectLabels
X-Amz-Date: 20170104T233405Z
User-Agent: aws-cli/1.11.25 Python/2.7.9 Windows/8 botocore/1.4.82
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=XXXXXXXX/20170104/us-west-2/rekognition/aws4_request,
  SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=XXXXXXXX

{
   "Image":{
      "S3Object":{
         "Bucket":"example-photos",
         "Name":"skateboard.jpg"
      }
   }
}
```

#### Sample Response<a name="API_DetectLabels_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: Wed, 04 Jan 2017 23:34:28 GMT
x-amzn-RequestId: 54cd6508-d2d6-11e6-bbda-cfd624bc06b2
Content-Length: 1882
Connection: keep-alive

{
   "Labels":[
      {
         "Confidence":99.25072479248047,
         "Name":"People"
      },
      {
         "Confidence":99.25074005126953,
         "Name":"Person"
      },
      {
         "Confidence":99.2429428100586,
         "Name":"Human"
      },
      {
         "Confidence":99.23795318603516,
         "Name":"Skateboard"
      },
      {
         "Confidence":99.23795318603516,
         "Name":"Sport"
      },
      {
         "Confidence":97.44398498535156,
         "Name":"Parking"
      },
      {
         "Confidence":97.44398498535156,
         "Name":"Parking Lot"
      },
      {
         "Confidence":87.81458282470703,
         "Name":"Automobile"
      },
      {
         "Confidence":87.81458282470703,
         "Name":"Car"
      },
      {
         "Confidence":87.81458282470703,
         "Name":"Vehicle"
      },
      {
         "Confidence":82.21033477783203,
         "Name":"Sedan"
      },
      {
         "Confidence":78.62909698486328,
         "Name":"Boardwalk"
      },
      {
         "Confidence":78.62909698486328,
         "Name":"Path"
      },
      {
         "Confidence":78.62909698486328,
         "Name":"Pavement"
      },
      {
         "Confidence":78.62909698486328,
         "Name":"Sidewalk"
      },
      {
         "Confidence":78.62909698486328,
         "Name":"Walkway"
      },
      {
         "Confidence":76.63581085205078,
         "Name":"Intersection"
      },
      {
         "Confidence":76.63581085205078,
         "Name":"Road"
      },
      {
         "Confidence":71.48307800292969,
         "Name":"Coupe"
      },
      {
         "Confidence":71.48307800292969,
         "Name":"Sports Car"
      },
      {
         "Confidence":67.8428726196289,
         "Name":"Building"
      },
      {
         "Confidence":62.91515350341797,
         "Name":"City"
      },
      {
         "Confidence":62.91515350341797,
         "Name":"Downtown"
      },
      {
         "Confidence":62.91515350341797,
         "Name":"Urban"
      },
      {
         "Confidence":62.04115676879883,
         "Name":"Neighborhood"
      },
      {
         "Confidence":62.04115676879883,
         "Name":"Town"
      },
      {
         "Confidence":61.2546272277832,
         "Name":"Suv"
      },
      {
         "Confidence":56.249610900878906,
         "Name":"Street"
      },
      {
         "Confidence":53.987510681152344,
         "Name":"Metropolis"
      },
      {
         "Confidence":52.98323059082031,
         "Name":"Housing"
      },
      {
         "Confidence":52.358848571777344,
         "Name":"Office Building"
      },
      {
         "Confidence":51.10673904418945,
         "Name":"Engine"
      },
      {
         "Confidence":51.10673904418945,
         "Name":"Machine"
      },
      {
         "Confidence":51.10673904418945,
         "Name":"Motor"
      },
      {
         "Confidence":51.06093215942383,
         "Name":"Apartment Building"
      },
      {
         "Confidence":51.06093215942383,
         "Name":"High Rise"
      },
      {
         "Confidence":50.64869689941406,
         "Name":"Pedestrian"
      }
   ]
}
```

## See Also<a name="API_DetectLabels_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS Command Line Interface](http://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DetectLabels) 

+  [AWS SDK for \.NET](http://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DetectLabels) 

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DetectLabels) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DetectLabels) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/DetectLabels) 

+  [AWS SDK for JavaScript](http://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DetectLabels) 

+  [AWS SDK for PHP V3](http://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DetectLabels) 

+  [AWS SDK for Python](http://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DetectLabels) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/DetectLabels) 