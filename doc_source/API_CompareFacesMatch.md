# CompareFacesMatch<a name="API_CompareFacesMatch"></a>

Provides information about a face in a target image that matches the source image face analyzed by `CompareFaces`\. The `Face` property contains the bounding box of the face in the target image\. The `Similarity` property is the confidence that the source image face matches the face in the bounding box\.

## Contents<a name="API_CompareFacesMatch_Contents"></a>

 **Face**   <a name="rekognition-Type-CompareFacesMatch-Face"></a>
Provides face metadata \(bounding box and confidence that the bounding box actually contains a face\)\.  
Type: [ComparedFace](API_ComparedFace.md) object  
Required: No

 **Similarity**   <a name="rekognition-Type-CompareFacesMatch-Similarity"></a>
Level of confidence that the faces match\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

## See Also<a name="API_CompareFacesMatch_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CompareFacesMatch) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/CompareFacesMatch) 
+  [AWS SDK for Go \- Pilot](https://docs.aws.amazon.com/goto/SdkForGoPilot/rekognition-2016-06-27/CompareFacesMatch) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/CompareFacesMatch) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/CompareFacesMatch) 