# EquipmentDetection<a name="API_EquipmentDetection"></a>

Information about an item of Personal Protective Equipment \(PPE\) detected by [DetectProtectiveEquipment](API_DetectProtectiveEquipment.md)\. For more information, see [DetectProtectiveEquipment](API_DetectProtectiveEquipment.md)\.

## Contents<a name="API_EquipmentDetection_Contents"></a>

 **BoundingBox**   <a name="rekognition-Type-EquipmentDetection-BoundingBox"></a>
A bounding box surrounding the item of detected PPE\.  
Type: [BoundingBox](API_BoundingBox.md) object  
Required: No

 **Confidence**   <a name="rekognition-Type-EquipmentDetection-Confidence"></a>
The confidence that Amazon Rekognition has that the bounding box \(`BoundingBox`\) contains an item of PPE\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 **CoversBodyPart**   <a name="rekognition-Type-EquipmentDetection-CoversBodyPart"></a>
Information about the body part covered by the detected PPE\.  
Type: [CoversBodyPart](API_CoversBodyPart.md) object  
Required: No

 **Type**   <a name="rekognition-Type-EquipmentDetection-Type"></a>
The type of detected PPE\.  
Type: String  
Valid Values:` FACE_COVER | HAND_COVER | HEAD_COVER`   
Required: No

## See Also<a name="API_EquipmentDetection_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/EquipmentDetection) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/EquipmentDetection) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/EquipmentDetection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/EquipmentDetection) 