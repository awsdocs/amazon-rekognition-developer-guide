# FaceDetail<a name="API_FaceDetail"></a>

Structure containing attributes of the face that the algorithm detected\.

## Contents<a name="API_FaceDetail_Contents"></a>

 **AgeRange**   
The estimated age range, in years, for the face\. Low represents the lowest estimated age and High represents the highest estimated age\.  
Type: [AgeRange](API_AgeRange.md) object  
Required: No

 **Beard**   
Indicates whether or not the face has a beard, and the confidence level in the determination\.  
Type: [Beard](API_Beard.md) object  
Required: No

 **BoundingBox**   
Bounding box of the face\.  
Type: [BoundingBox](API_BoundingBox.md) object  
Required: No

 **Confidence**   
Confidence level that the bounding box contains a face \(and not a different object such as a tree\)\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 **Emotions**   
The emotions detected on the face, and the confidence level in the determination\. For example, HAPPY, SAD, and ANGRY\.   
Type: Array of [Emotion](API_Emotion.md) objects  
Required: No

 **Eyeglasses**   
Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination\.  
Type: [Eyeglasses](API_Eyeglasses.md) object  
Required: No

 **EyesOpen**   
Indicates whether or not the eyes on the face are open, and the confidence level in the determination\.  
Type: [EyeOpen](API_EyeOpen.md) object  
Required: No

 **Gender**   
Gender of the face and the confidence level in the determination\.  
Type: [Gender](API_Gender.md) object  
Required: No

 **Landmarks**   
Indicates the location of landmarks on the face\.  
Type: Array of [Landmark](API_Landmark.md) objects  
Required: No

 **MouthOpen**   
Indicates whether or not the mouth on the face is open, and the confidence level in the determination\.  
Type: [MouthOpen](API_MouthOpen.md) object  
Required: No

 **Mustache**   
Indicates whether or not the face has a mustache, and the confidence level in the determination\.  
Type: [Mustache](API_Mustache.md) object  
Required: No

 **Pose**   
Indicates the pose of the face as determined by its pitch, roll, and yaw\.  
Type: [Pose](API_Pose.md) object  
Required: No

 **Quality**   
Identifies image brightness and sharpness\.  
Type: [ImageQuality](API_ImageQuality.md) object  
Required: No

 **Smile**   
Indicates whether or not the face is smiling, and the confidence level in the determination\.  
Type: [Smile](API_Smile.md) object  
Required: No

 **Sunglasses**   
Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination\.  
Type: [Sunglasses](API_Sunglasses.md) object  
Required: No

## See Also<a name="API_FaceDetail_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/FaceDetail) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/FaceDetail) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/FaceDetail) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/FaceDetail) 