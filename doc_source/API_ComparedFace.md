# ComparedFace<a name="API_ComparedFace"></a>

Provides face metadata for target image faces that are analysed by `CompareFaces` and `RecognizeCelebrities`\.

## Contents<a name="API_ComparedFace_Contents"></a>

 **BoundingBox**   <a name="rekognition-Type-ComparedFace-BoundingBox"></a>
Bounding box of the face\.  
Type: [BoundingBox](API_BoundingBox.md) object  
Required: No

 **Confidence**   <a name="rekognition-Type-ComparedFace-Confidence"></a>
Level of confidence that what the bounding box contains is a face\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 **Landmarks**   <a name="rekognition-Type-ComparedFace-Landmarks"></a>
An array of facial landmarks\.  
Type: Array of [Landmark](API_Landmark.md) objects  
Required: No

 **Pose**   <a name="rekognition-Type-ComparedFace-Pose"></a>
Indicates the pose of the face as determined by its pitch, roll, and yaw\.  
Type: [Pose](API_Pose.md) object  
Required: No

 **Quality**   <a name="rekognition-Type-ComparedFace-Quality"></a>
Identifies face image brightness and sharpness\.   
Type: [ImageQuality](API_ImageQuality.md) object  
Required: No

## See Also<a name="API_ComparedFace_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ComparedFace) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ComparedFace) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/ComparedFace) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/ComparedFace) 