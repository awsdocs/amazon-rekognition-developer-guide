# ProtectiveEquipmentSummarizationAttributes<a name="API_ProtectiveEquipmentSummarizationAttributes"></a>

Specifies summary attributes to return from a call to [DetectProtectiveEquipment](API_DetectProtectiveEquipment.md)\. You can specify which types of PPE to summarize\. You can also specify a minimum confidence value for detections\. Summary information is returned in the `Summary` \([ProtectiveEquipmentSummary](API_ProtectiveEquipmentSummary.md)\) field of the response from `DetectProtectiveEquipment`\. The summary includes which persons in an image were detected wearing the requested types of person protective equipment \(PPE\), which persons were detected as not wearing PPE, and the persons in which a determination could not be made\. For more information, see [ProtectiveEquipmentSummary](API_ProtectiveEquipmentSummary.md)\.

## Contents<a name="API_ProtectiveEquipmentSummarizationAttributes_Contents"></a>

 **MinConfidence**   <a name="rekognition-Type-ProtectiveEquipmentSummarizationAttributes-MinConfidence"></a>
The minimum confidence level for which you want summary information\. The confidence level applies to person detection, body part detection, equipment detection, and body part coverage\. Amazon Rekognition doesn't return summary information with a confidence than this specified value\. There isn't a default value\.  
Specify a `MinConfidence` value that is between 50\-100% as `DetectProtectiveEquipment` returns predictions only where the detection confidence is between 50% \- 100%\. If you specify a value that is less than 50%, the results are the same specifying a value of 50%\.  
   
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: Yes

 **RequiredEquipmentTypes**   <a name="rekognition-Type-ProtectiveEquipmentSummarizationAttributes-RequiredEquipmentTypes"></a>
An array of personal protective equipment types for which you want summary information\. If a person is detected wearing a required requipment type, the person's ID is added to the `PersonsWithRequiredEquipment` array field returned in [ProtectiveEquipmentSummary](API_ProtectiveEquipmentSummary.md) by `DetectProtectiveEquipment`\.   
Type: Array of strings  
Valid Values:` FACE_COVER | HAND_COVER | HEAD_COVER`   
Required: Yes

## See Also<a name="API_ProtectiveEquipmentSummarizationAttributes_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ProtectiveEquipmentSummarizationAttributes) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ProtectiveEquipmentSummarizationAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ProtectiveEquipmentSummarizationAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ProtectiveEquipmentSummarizationAttributes) 