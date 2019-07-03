# Landmark<a name="API_Landmark"></a>

Indicates the location of the landmark on the face\.

## Contents<a name="API_Landmark_Contents"></a>

 **Type**   <a name="rekognition-Type-Landmark-Type"></a>
Type of landmark\.  
Type: String  
Valid Values:` eyeLeft | eyeRight | nose | mouthLeft | mouthRight | leftEyeBrowLeft | leftEyeBrowRight | leftEyeBrowUp | rightEyeBrowLeft | rightEyeBrowRight | rightEyeBrowUp | leftEyeLeft | leftEyeRight | leftEyeUp | leftEyeDown | rightEyeLeft | rightEyeRight | rightEyeUp | rightEyeDown | noseLeft | noseRight | mouthUp | mouthDown | leftPupil | rightPupil | upperJawlineLeft | midJawlineLeft | chinBottom | midJawlineRight | upperJawlineRight`   
Required: No

 **X**   <a name="rekognition-Type-Landmark-X"></a>
The x\-coordinate from the top left of the landmark expressed as the ratio of the width of the image\. For example, if the image is 700 x 200 and the x\-coordinate of the landmark is at 350 pixels, this value is 0\.5\.   
Type: Float  
Required: No

 **Y**   <a name="rekognition-Type-Landmark-Y"></a>
The y\-coordinate from the top left of the landmark expressed as the ratio of the height of the image\. For example, if the image is 700 x 200 and the y\-coordinate of the landmark is at 100 pixels, this value is 0\.5\.  
Type: Float  
Required: No

## See Also<a name="API_Landmark_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/Landmark) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/Landmark) 
+  [AWS SDK for Go \- Pilot](https://docs.aws.amazon.com/goto/SdkForGoPilot/rekognition-2016-06-27/Landmark) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/Landmark) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/Landmark) 