# ProtectiveEquipmentBodyPart<a name="API_ProtectiveEquipmentBodyPart"></a>

Information about a body part detected by [DetectProtectiveEquipment](API_DetectProtectiveEquipment.md) that contains PPE\. An array of `ProtectiveEquipmentBodyPart` objects is returned for each person detected by `DetectProtectiveEquipment`\. 

## Contents<a name="API_ProtectiveEquipmentBodyPart_Contents"></a>

 **Confidence**   <a name="rekognition-Type-ProtectiveEquipmentBodyPart-Confidence"></a>
The confidence that Amazon Rekognition has in the detection accuracy of the detected body part\.   
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 **EquipmentDetections**   <a name="rekognition-Type-ProtectiveEquipmentBodyPart-EquipmentDetections"></a>
An array of Personal Protective Equipment items detected around a body part\.  
Type: Array of [EquipmentDetection](API_EquipmentDetection.md) objects  
Required: No

 **Name**   <a name="rekognition-Type-ProtectiveEquipmentBodyPart-Name"></a>
The detected body part\.  
Type: String  
Valid Values:` FACE | HEAD | LEFT_HAND | RIGHT_HAND`   
Required: No

## See Also<a name="API_ProtectiveEquipmentBodyPart_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ProtectiveEquipmentBodyPart) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ProtectiveEquipmentBodyPart) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ProtectiveEquipmentBodyPart) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ProtectiveEquipmentBodyPart) 