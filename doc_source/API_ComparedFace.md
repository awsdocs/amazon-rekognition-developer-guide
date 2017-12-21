# ComparedFace<a name="API_ComparedFace"></a>

Provides face metadata for target image faces that are analysed by `CompareFaces` and `RecognizeCelebrities`\.

## Contents<a name="API_ComparedFace_Contents"></a>

 **BoundingBox**   
Bounding box of the face\.  
Type: [BoundingBox](API_BoundingBox.md) object  
Required: No

 **Confidence**   
Level of confidence that what the bounding box contains is a face\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 **Landmarks**   
An array of facial landmarks\.  
Type: Array of [Landmark](API_Landmark.md) objects  
Required: No

 **Pose**   
Indicates the pose of the face as determined by its pitch, roll, and yaw\.  
Type: [Pose](API_Pose.md) object  
Required: No

 **Quality**   
Identifies face image brightness and sharpness\.   
Type: [ImageQuality](API_ImageQuality.md) object  
Required: No

## See Also<a name="API_ComparedFace_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ComparedFace) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ComparedFace) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/ComparedFace) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/ComparedFace) 