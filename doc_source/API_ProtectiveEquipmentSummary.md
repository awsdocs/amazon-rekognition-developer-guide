# ProtectiveEquipmentSummary<a name="API_ProtectiveEquipmentSummary"></a>

Summary information for required items of personal protective equipment \(PPE\) detected on persons by a call to [DetectProtectiveEquipment](API_DetectProtectiveEquipment.md)\. You specify the required type of PPE in the `SummarizationAttributes` \([ProtectiveEquipmentSummarizationAttributes](API_ProtectiveEquipmentSummarizationAttributes.md)\) input parameter\. The summary includes which persons were detected wearing the required personal protective equipment \(`PersonsWithRequiredEquipment`\), which persons were detected as not wearing the required PPE \(`PersonsWithoutRequiredEquipment`\), and the persons in which a determination could not be made \(`PersonsIndeterminate`\)\.

To get a total for each category, use the size of the field array\. For example, to find out how many people were detected as wearing the specified PPE, use the size of the `PersonsWithRequiredEquipment` array\. If you want to find out more about a person, such as the location \([BoundingBox](API_BoundingBox.md)\) of the person on the image, use the person ID in each array element\. Each person ID matches the ID field of a [ProtectiveEquipmentPerson](API_ProtectiveEquipmentPerson.md) object returned in the `Persons` array by `DetectProtectiveEquipment`\.

## Contents<a name="API_ProtectiveEquipmentSummary_Contents"></a>

 **PersonsIndeterminate**   <a name="rekognition-Type-ProtectiveEquipmentSummary-PersonsIndeterminate"></a>
An array of IDs for persons where it was not possible to determine if they are wearing personal protective equipment\.   
Type: Array of integers  
Valid Range: Minimum value of 0\.  
Required: No

 **PersonsWithoutRequiredEquipment**   <a name="rekognition-Type-ProtectiveEquipmentSummary-PersonsWithoutRequiredEquipment"></a>
An array of IDs for persons who are not wearing all of the types of PPE specified in the `RequiredEquipmentTypes` field of the detected personal protective equipment\.   
Type: Array of integers  
Valid Range: Minimum value of 0\.  
Required: No

 **PersonsWithRequiredEquipment**   <a name="rekognition-Type-ProtectiveEquipmentSummary-PersonsWithRequiredEquipment"></a>
An array of IDs for persons who are wearing detected personal protective equipment\.   
Type: Array of integers  
Valid Range: Minimum value of 0\.  
Required: No

## See Also<a name="API_ProtectiveEquipmentSummary_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ProtectiveEquipmentSummary) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ProtectiveEquipmentSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ProtectiveEquipmentSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ProtectiveEquipmentSummary) 