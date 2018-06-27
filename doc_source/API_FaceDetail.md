# FaceDetail<a name="API_FaceDetail"></a>

Structure containing attributes of the face that the algorithm detected\.

A `FaceDetail` object contains either the default facial attributes or all facial attributes\. The default attributes are `BoundingBox`, `Confidence`, `Landmarks`, `Pose`, and `Quality`\.

 [GetFaceDetection](API_GetFaceDetection.md) is the only Amazon Rekognition Video stored video operation that can return a `FaceDetail` object with all attributes\. To specify which attributes to return, use the `FaceAttributes` input parameter for [StartFaceDetection](API_StartFaceDetection.md)\. The following Amazon Rekognition Video operations return only the default attributes\. The corresponding Start operations don't have a `FaceAttributes` input parameter\.
+ GetCelebrityRecognition
+ GetPersonTracking
+ GetFaceSearch

The Amazon Rekognition Image [DetectFaces](API_DetectFaces.md) and [IndexFaces](API_IndexFaces.md) operations can return all facial attributes\. To specify which attributes to return, use the `Attributes` input parameter for `DetectFaces`\. For `IndexFaces`, use the `DetectAttributes` input parameter\.

## Contents<a name="API_FaceDetail_Contents"></a>

 **AgeRange**   <a name="rekognition-Type-FaceDetail-AgeRange"></a>
The estimated age range, in years, for the face\. Low represents the lowest estimated age and High represents the highest estimated age\.  
Type: [AgeRange](API_AgeRange.md) object  
Required: No

 **Beard**   <a name="rekognition-Type-FaceDetail-Beard"></a>
Indicates whether or not the face has a beard, and the confidence level in the determination\.  
Type: [Beard](API_Beard.md) object  
Required: No

 **BoundingBox**   <a name="rekognition-Type-FaceDetail-BoundingBox"></a>
Bounding box of the face\. Default attribute\.  
Type: [BoundingBox](API_BoundingBox.md) object  
Required: No

 **Confidence**   <a name="rekognition-Type-FaceDetail-Confidence"></a>
Confidence level that the bounding box contains a face \(and not a different object such as a tree\)\. Default attribute\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 **Emotions**   <a name="rekognition-Type-FaceDetail-Emotions"></a>
The emotions detected on the face, and the confidence level in the determination\. For example, HAPPY, SAD, and ANGRY\.   
Type: Array of [Emotion](API_Emotion.md) objects  
Required: No

 **Eyeglasses**   <a name="rekognition-Type-FaceDetail-Eyeglasses"></a>
Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination\.  
Type: [Eyeglasses](API_Eyeglasses.md) object  
Required: No

 **EyesOpen**   <a name="rekognition-Type-FaceDetail-EyesOpen"></a>
Indicates whether or not the eyes on the face are open, and the confidence level in the determination\.  
Type: [EyeOpen](API_EyeOpen.md) object  
Required: No

 **Gender**   <a name="rekognition-Type-FaceDetail-Gender"></a>
Gender of the face and the confidence level in the determination\.  
Type: [Gender](API_Gender.md) object  
Required: No

 **Landmarks**   <a name="rekognition-Type-FaceDetail-Landmarks"></a>
Indicates the location of landmarks on the face\. Default attribute\.  
Type: Array of [Landmark](API_Landmark.md) objects  
Required: No

 **MouthOpen**   <a name="rekognition-Type-FaceDetail-MouthOpen"></a>
Indicates whether or not the mouth on the face is open, and the confidence level in the determination\.  
Type: [MouthOpen](API_MouthOpen.md) object  
Required: No

 **Mustache**   <a name="rekognition-Type-FaceDetail-Mustache"></a>
Indicates whether or not the face has a mustache, and the confidence level in the determination\.  
Type: [Mustache](API_Mustache.md) object  
Required: No

 **Pose**   <a name="rekognition-Type-FaceDetail-Pose"></a>
Indicates the pose of the face as determined by its pitch, roll, and yaw\. Default attribute\.  
Type: [Pose](API_Pose.md) object  
Required: No

 **Quality**   <a name="rekognition-Type-FaceDetail-Quality"></a>
Identifies image brightness and sharpness\. Default attribute\.  
Type: [ImageQuality](API_ImageQuality.md) object  
Required: No

 **Smile**   <a name="rekognition-Type-FaceDetail-Smile"></a>
Indicates whether or not the face is smiling, and the confidence level in the determination\.  
Type: [Smile](API_Smile.md) object  
Required: No

 **Sunglasses**   <a name="rekognition-Type-FaceDetail-Sunglasses"></a>
Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination\.  
Type: [Sunglasses](API_Sunglasses.md) object  
Required: No

## See Also<a name="API_FaceDetail_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/FaceDetail) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/FaceDetail) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/FaceDetail) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/FaceDetail) 