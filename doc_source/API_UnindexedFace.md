# UnindexedFace<a name="API_UnindexedFace"></a>

A face that [IndexFaces](API_IndexFaces.md) detected, but didn't index\. Use the `Reasons` response attribute to determine why a face wasn't indexed\.

## Contents<a name="API_UnindexedFace_Contents"></a>

 **FaceDetail**   <a name="rekognition-Type-UnindexedFace-FaceDetail"></a>
The structure that contains attributes of a face that `IndexFaces`detected, but didn't index\.   
Type: [FaceDetail](API_FaceDetail.md) object  
Required: No

 **Reasons**   <a name="rekognition-Type-UnindexedFace-Reasons"></a>
An array of reasons that specify why a face wasn't indexed\.   
+ EXTREME\_POSE \- The face is at a pose that can't be detected\. For example, the head is turned too far away from the camera\.
+ EXCEEDS\_MAX\_FACES \- The number of faces detected is already higher than that specified by the `MaxFaces` input parameter for `IndexFaces`\.
+ LOW\_BRIGHTNESS \- The image is too dark\.
+ LOW\_SHARPNESS \- The image is too blurry\.
+ LOW\_CONFIDENCE \- The face was detected with a low confidence\.
+ SMALL\_BOUNDING\_BOX \- The bounding box around the face is too small\.
Type: Array of strings  
Valid Values:` EXCEEDS_MAX_FACES | EXTREME_POSE | LOW_BRIGHTNESS | LOW_SHARPNESS | LOW_CONFIDENCE | SMALL_BOUNDING_BOX | LOW_FACE_QUALITY`   
Required: No

## See Also<a name="API_UnindexedFace_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/UnindexedFace) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/UnindexedFace) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/UnindexedFace) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/UnindexedFace) 