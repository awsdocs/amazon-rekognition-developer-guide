# FaceSearchSettings<a name="API_FaceSearchSettings"></a>

Input face recognition parameters for an Amazon Rekognition stream processor\. `FaceRecognitionSettings` is a request parameter for [CreateStreamProcessor](API_CreateStreamProcessor.md)\.

## Contents<a name="API_FaceSearchSettings_Contents"></a>

 **CollectionId**   <a name="rekognition-Type-FaceSearchSettings-CollectionId"></a>
The ID of a collection that contains faces that you want to search for\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: No

 **FaceMatchThreshold**   <a name="rekognition-Type-FaceSearchSettings-FaceMatchThreshold"></a>
Minimum face match confidence score that must be met to return a result for a recognized face\. Default is 70\. 0 is the lowest confidence\. 100 is the highest confidence\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

## See Also<a name="API_FaceSearchSettings_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/FaceSearchSettings) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/FaceSearchSettings) 
+  [AWS SDK for Go \- Pilot](https://docs.aws.amazon.com/goto/SdkForGoPilot/rekognition-2016-06-27/FaceSearchSettings) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/FaceSearchSettings) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/FaceSearchSettings) 