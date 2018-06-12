# IndexFaces<a name="API_IndexFaces"></a>

Detects faces in the input image and adds them to the specified collection\. 

Amazon Rekognition does not save the actual faces detected\. Instead, the underlying detection algorithm first detects the faces in the input image, and for each face extracts facial features into a feature vector, and stores it in the back\-end database\. Amazon Rekognition uses feature vectors when performing face match and search operations using the [SearchFaces](API_SearchFaces.md) and [SearchFacesByImage](API_SearchFacesByImage.md) operations\.

If you are using version 1\.0 of the face detection model, `IndexFaces` indexes the 15 largest faces in the input image\. Later versions of the face detection model index the 100 largest faces in the input image\. To determine which version of the model you are using, check the the value of `FaceModelVersion` in the response from `IndexFaces`\. For more information, see [Model Versioning](face-detection-model.md)\.

If you provide the optional `ExternalImageID` for the input image you provided, Amazon Rekognition associates this ID with all faces that it detects\. When you call the [ListFaces](API_ListFaces.md) operation, the response returns the external ID\. You can use this external image ID to create a client\-side index to associate the faces with each image\. You can then use the index to find all faces in an image\. 

In response, the operation returns an array of metadata for all detected faces\. This includes, the bounding box of the detected face, confidence value \(indicating the bounding box contains a face\), a face ID assigned by the service for each face that is detected and stored, and an image ID assigned by the service for the input image\. If you request all facial attributes \(using the `detectionAttributes` parameter, Amazon Rekognition returns detailed facial attributes such as facial landmarks \(for example, location of eye and mount\) and other facial attributes such gender\. If you provide the same image, specify the same collection, and use the same external ID in the `IndexFaces` operation, Amazon Rekognition doesn't save duplicate face metadata\. 

The input image is passed either as base64\-encoded image bytes or as a reference to an image in an Amazon S3 bucket\. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported\. The image must be either a PNG or JPEG formatted file\. 

This operation requires permissions to perform the `rekognition:IndexFaces` action\.

## Request Syntax<a name="API_IndexFaces_RequestSyntax"></a>

```
{
   "[CollectionId](#rekognition-IndexFaces-request-CollectionId)": "string",
   "[DetectionAttributes](#rekognition-IndexFaces-request-DetectionAttributes)": [ "string" ],
   "[ExternalImageId](#rekognition-IndexFaces-request-ExternalImageId)": "string",
   "[Image](#rekognition-IndexFaces-request-Image)": { 
      "[Bytes](API_Image.md#rekognition-Type-Image-Bytes)": blob,
      "[S3Object](API_Image.md#rekognition-Type-Image-S3Object)": { 
         "[Bucket](API_S3Object.md#rekognition-Type-S3Object-Bucket)": "string",
         "[Name](API_S3Object.md#rekognition-Type-S3Object-Name)": "string",
         "[Version](API_S3Object.md#rekognition-Type-S3Object-Version)": "string"
      }
   }
}
```

## Request Parameters<a name="API_IndexFaces_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [CollectionId](#API_IndexFaces_RequestSyntax) **   <a name="rekognition-IndexFaces-request-CollectionId"></a>
The ID of an existing collection to which you want to add the faces that are detected in the input images\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

 ** [DetectionAttributes](#API_IndexFaces_RequestSyntax) **   <a name="rekognition-IndexFaces-request-DetectionAttributes"></a>
An array of facial attributes that you want to be returned\. This can be the default list of attributes or all attributes\. If you don't specify a value for `Attributes` or if you specify `["DEFAULT"]`, the API returns the following subset of facial attributes: `BoundingBox`, `Confidence`, `Pose`, `Quality` and `Landmarks`\. If you provide `["ALL"]`, all facial attributes are returned but the operation will take longer to complete\.  
If you provide both, `["ALL", "DEFAULT"]`, the service uses a logical AND operator to determine which attributes to return \(in this case, all attributes\)\.   
Type: Array of strings  
Valid Values:` DEFAULT | ALL`   
Required: No

 ** [ExternalImageId](#API_IndexFaces_RequestSyntax) **   <a name="rekognition-IndexFaces-request-ExternalImageId"></a>
ID you want to assign to all the faces detected in the image\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-:]+`   
Required: No

 ** [Image](#API_IndexFaces_RequestSyntax) **   <a name="rekognition-IndexFaces-request-Image"></a>
The input image as base64\-encoded bytes or an S3 object\. If you use the AWS CLI to call Amazon Rekognition operations, passing base64\-encoded image bytes is not supported\.   
Type: [Image](API_Image.md) object  
Required: Yes

## Response Syntax<a name="API_IndexFaces_ResponseSyntax"></a>

```
{
   "[FaceModelVersion](#rekognition-IndexFaces-response-FaceModelVersion)": "string",
   "[FaceRecords](#rekognition-IndexFaces-response-FaceRecords)": [ 
      { 
         "[Face](API_FaceRecord.md#rekognition-Type-FaceRecord-Face)": { 
            "[BoundingBox](API_Face.md#rekognition-Type-Face-BoundingBox)": { 
               "[Height](API_BoundingBox.md#rekognition-Type-BoundingBox-Height)": number,
               "[Left](API_BoundingBox.md#rekognition-Type-BoundingBox-Left)": number,
               "[Top](API_BoundingBox.md#rekognition-Type-BoundingBox-Top)": number,
               "[Width](API_BoundingBox.md#rekognition-Type-BoundingBox-Width)": number
            },
            "[Confidence](API_Face.md#rekognition-Type-Face-Confidence)": number,
            "[ExternalImageId](API_Face.md#rekognition-Type-Face-ExternalImageId)": "string",
            "[FaceId](API_Face.md#rekognition-Type-Face-FaceId)": "string",
            "[ImageId](API_Face.md#rekognition-Type-Face-ImageId)": "string"
         },
         "[FaceDetail](API_FaceRecord.md#rekognition-Type-FaceRecord-FaceDetail)": { 
            "[AgeRange](API_FaceDetail.md#rekognition-Type-FaceDetail-AgeRange)": { 
               "[High](API_AgeRange.md#rekognition-Type-AgeRange-High)": number,
               "[Low](API_AgeRange.md#rekognition-Type-AgeRange-Low)": number
            },
            "[Beard](API_FaceDetail.md#rekognition-Type-FaceDetail-Beard)": { 
               "[Confidence](API_Beard.md#rekognition-Type-Beard-Confidence)": number,
               "[Value](API_Beard.md#rekognition-Type-Beard-Value)": boolean
            },
            "[BoundingBox](API_FaceDetail.md#rekognition-Type-FaceDetail-BoundingBox)": { 
               "[Height](API_BoundingBox.md#rekognition-Type-BoundingBox-Height)": number,
               "[Left](API_BoundingBox.md#rekognition-Type-BoundingBox-Left)": number,
               "[Top](API_BoundingBox.md#rekognition-Type-BoundingBox-Top)": number,
               "[Width](API_BoundingBox.md#rekognition-Type-BoundingBox-Width)": number
            },
            "[Confidence](API_FaceDetail.md#rekognition-Type-FaceDetail-Confidence)": number,
            "[Emotions](API_FaceDetail.md#rekognition-Type-FaceDetail-Emotions)": [ 
               { 
                  "[Confidence](API_Emotion.md#rekognition-Type-Emotion-Confidence)": number,
                  "[Type](API_Emotion.md#rekognition-Type-Emotion-Type)": "string"
               }
            ],
            "[Eyeglasses](API_FaceDetail.md#rekognition-Type-FaceDetail-Eyeglasses)": { 
               "[Confidence](API_Eyeglasses.md#rekognition-Type-Eyeglasses-Confidence)": number,
               "[Value](API_Eyeglasses.md#rekognition-Type-Eyeglasses-Value)": boolean
            },
            "[EyesOpen](API_FaceDetail.md#rekognition-Type-FaceDetail-EyesOpen)": { 
               "[Confidence](API_EyeOpen.md#rekognition-Type-EyeOpen-Confidence)": number,
               "[Value](API_EyeOpen.md#rekognition-Type-EyeOpen-Value)": boolean
            },
            "[Gender](API_FaceDetail.md#rekognition-Type-FaceDetail-Gender)": { 
               "[Confidence](API_Gender.md#rekognition-Type-Gender-Confidence)": number,
               "[Value](API_Gender.md#rekognition-Type-Gender-Value)": "string"
            },
            "[Landmarks](API_FaceDetail.md#rekognition-Type-FaceDetail-Landmarks)": [ 
               { 
                  "[Type](API_Landmark.md#rekognition-Type-Landmark-Type)": "string",
                  "[X](API_Landmark.md#rekognition-Type-Landmark-X)": number,
                  "[Y](API_Landmark.md#rekognition-Type-Landmark-Y)": number
               }
            ],
            "[MouthOpen](API_FaceDetail.md#rekognition-Type-FaceDetail-MouthOpen)": { 
               "[Confidence](API_MouthOpen.md#rekognition-Type-MouthOpen-Confidence)": number,
               "[Value](API_MouthOpen.md#rekognition-Type-MouthOpen-Value)": boolean
            },
            "[Mustache](API_FaceDetail.md#rekognition-Type-FaceDetail-Mustache)": { 
               "[Confidence](API_Mustache.md#rekognition-Type-Mustache-Confidence)": number,
               "[Value](API_Mustache.md#rekognition-Type-Mustache-Value)": boolean
            },
            "[Pose](API_FaceDetail.md#rekognition-Type-FaceDetail-Pose)": { 
               "[Pitch](API_Pose.md#rekognition-Type-Pose-Pitch)": number,
               "[Roll](API_Pose.md#rekognition-Type-Pose-Roll)": number,
               "[Yaw](API_Pose.md#rekognition-Type-Pose-Yaw)": number
            },
            "[Quality](API_FaceDetail.md#rekognition-Type-FaceDetail-Quality)": { 
               "[Brightness](API_ImageQuality.md#rekognition-Type-ImageQuality-Brightness)": number,
               "[Sharpness](API_ImageQuality.md#rekognition-Type-ImageQuality-Sharpness)": number
            },
            "[Smile](API_FaceDetail.md#rekognition-Type-FaceDetail-Smile)": { 
               "[Confidence](API_Smile.md#rekognition-Type-Smile-Confidence)": number,
               "[Value](API_Smile.md#rekognition-Type-Smile-Value)": boolean
            },
            "[Sunglasses](API_FaceDetail.md#rekognition-Type-FaceDetail-Sunglasses)": { 
               "[Confidence](API_Sunglasses.md#rekognition-Type-Sunglasses-Confidence)": number,
               "[Value](API_Sunglasses.md#rekognition-Type-Sunglasses-Value)": boolean
            }
         }
      }
   ],
   "[OrientationCorrection](#rekognition-IndexFaces-response-OrientationCorrection)": "string"
}
```

## Response Elements<a name="API_IndexFaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [FaceModelVersion](#API_IndexFaces_ResponseSyntax) **   <a name="rekognition-IndexFaces-response-FaceModelVersion"></a>
Version number of the face detection model associated with the input collection \(`CollectionId`\)\.  
Type: String

 ** [FaceRecords](#API_IndexFaces_ResponseSyntax) **   <a name="rekognition-IndexFaces-response-FaceRecords"></a>
An array of faces detected and added to the collection\. For more information, see [Storing Faces in a Face Collection](collections-index-faces.md)\.   
Type: Array of [FaceRecord](API_FaceRecord.md) objects

 ** [OrientationCorrection](#API_IndexFaces_ResponseSyntax) **   <a name="rekognition-IndexFaces-response-OrientationCorrection"></a>
The orientation of the input image \(counterclockwise direction\)\. If your application displays the image, you can use this value to correct image orientation\. The bounding box coordinates returned in `FaceRecords` represent face locations before the image orientation is corrected\.   
If the input image is in jpeg format, it might contain exchangeable image \(Exif\) metadata\. If so, and the Exif metadata populates the orientation field, the value of `OrientationCorrection` is null and the bounding box coordinates in `FaceRecords` represent face locations after Exif metadata is used to correct the image orientation\. Images in \.png format don't contain Exif metadata\.
Type: String  
Valid Values:` ROTATE_0 | ROTATE_90 | ROTATE_180 | ROTATE_270` 

## Errors<a name="API_IndexFaces_Errors"></a>

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

 **ResourceNotFoundException**   
The collection specified in the request cannot be found\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## Example<a name="API_IndexFaces_Examples"></a>

### Example Request<a name="API_IndexFaces_Example_1"></a>

The following example shows a request that adds an image \(people\.jpg\) stored in an Amazon S3 bucket \(examplephotos\) to a collection \(examplemyphotos\)\.

#### Sample Request<a name="API_IndexFaces_Example_1_Request"></a>

```
POST https://rekognition.us-west-2.amazonaws.com/ HTTP/1.1
Host: rekognition.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 107
X-Amz-Target: RekognitionService.IndexFaces
X-Amz-Date: 20170105T162002Z
User-Agent: aws-cli/1.11.25 Python/2.7.9 Windows/8 botocore/1.4.82
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=XXXXXXXX/20170105/us-west-2/rekognition/aws4_request,
  SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=XXXXXXXX

{
   "Image":{
      "S3Object":{
         "Bucket":"example-photos",
         "Name":"people.jpg"
      }
   },
   "CollectionId":"examplemyphotos"
}
```

#### Sample Response<a name="API_IndexFaces_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1
Date: Thu, 05 Jan 2017 16:20:04 GMT
x-amzn-RequestId: cfe5d2f3-d362-11e6-988e-1194c13fd971
Content-Length: 1889
Connection: keep-alive

{
   "FaceModelVersion":"2.0",
   "FaceRecords":[
      {
         "Face":{
            "BoundingBox":{
               "Height":0.22206704318523407,
               "Left":0.503333330154419,
               "Top":0.21229049563407898,
               "Width":0.17666666209697723
            },
            "Confidence":99.9996566772461,
            "FaceId":"11111111-2222-3333-4444-555555555555",
            "ImageId":"11111111-2222-3333-4444-555555555555"
         },
         "FaceDetail":{
            "BoundingBox":{
               "Height":0.22206704318523407,
               "Left":0.503333330154419,
               "Top":0.21229049563407898,
               "Width":0.17666666209697723
            },
            "Confidence":99.9996566772461,
            "Landmarks":[
               {
                  "Type":"eyeLeft",
                  "X":0.5582929253578186,
                  "Y":0.327402263879776
               },
               {
                  "Type":"eyeRight",
                  "X":0.6097898483276367,
                  "Y":0.28622597455978394
               },
               {
                  "Type":"nose",
                  "X":0.6182368993759155,
                  "Y":0.34145522117614746
               },
               {
                  "Type":"mouthLeft",
                  "X":0.5820220708847046,
                  "Y":0.40035346150398254
               },
               {
                  "Type":"mouthRight",
                  "X":0.6310185194015503,
                  "Y":0.35822394490242004
               }
            ],
            "Pose":{
               "Pitch":-8.25561237335205,
               "Roll":-34.76542663574219,
               "Yaw":30.61958122253418
            },
            "Quality":{
               "Brightness":45.9112663269043,
               "Sharpness":50.0
            }
         }
      },
      {
         "Face":{
            "BoundingBox":{
               "Height":0.22067038714885712,
               "Left":0.402222216129303,
               "Top":0.3393854796886444,
               "Width":0.17555555701255798
            },
            "Confidence":99.9998779296875,
            "FaceId":"11111111-2222-3333-4444-555555555555",
            "ImageId":"11111111-2222-3333-4444-555555555555"
         },
         "FaceDetail":{
            "BoundingBox":{
               "Height":0.22067038714885712,
               "Left":0.402222216129303,
               "Top":0.3393854796886444,
               "Width":0.17555555701255798
            },
            "Confidence":99.9998779296875,
            "Landmarks":[
               {
                  "Type":"eyeLeft",
                  "X":0.46082764863967896,
                  "Y":0.4488079249858856
               },
               {
                  "Type":"eyeRight",
                  "X":0.509974479675293,
                  "Y":0.4110442101955414
               },
               {
                  "Type":"nose",
                  "X":0.5182068943977356,
                  "Y":0.4580079913139343
               },
               {
                  "Type":"mouthLeft",
                  "X":0.49137336015701294,
                  "Y":0.5153146386146545
               },
               {
                  "Type":"mouthRight",
                  "X":0.52939772605896,
                  "Y":0.4874058663845062
               }
            ],
            "Pose":{
               "Pitch":-12.197214126586914,
               "Roll":-33.81959533691406,
               "Yaw":32.57762908935547
            },
            "Quality":{
               "Brightness":32.43154525756836,
               "Sharpness":40.0
            }
         }
      }
   ],
   "OrientationCorrection":"ROTATE_0"
}
```

## See Also<a name="API_IndexFaces_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/IndexFaces) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/IndexFaces) 