# ProtectiveEquipmentPerson<a name="API_ProtectiveEquipmentPerson"></a>

A person detected by a call to [ DetectProtectiveEquipment ](API_DetectProtectiveEquipment.md)\. The API returns all persons detected in the input image in an array of `ProtectiveEquipmentPerson` objects\.

## Contents<a name="API_ProtectiveEquipmentPerson_Contents"></a>

 ** BodyParts **   <a name="rekognition-Type-ProtectiveEquipmentPerson-BodyParts"></a>
An array of body parts detected on a person's body \(including body parts without PPE\)\.   
Type: Array of [ ProtectiveEquipmentBodyPart ](API_ProtectiveEquipmentBodyPart.md) objects  
Required: No

 ** BoundingBox **   <a name="rekognition-Type-ProtectiveEquipmentPerson-BoundingBox"></a>
A bounding box around the detected person\.  
Type: [ BoundingBox ](API_BoundingBox.md) object  
Required: No

 ** Confidence **   <a name="rekognition-Type-ProtectiveEquipmentPerson-Confidence"></a>
The confidence that Amazon Rekognition has that the bounding box contains a person\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 ** Id **   <a name="rekognition-Type-ProtectiveEquipmentPerson-Id"></a>
The identifier for the detected person\. The identifier is only unique for a single call to `DetectProtectiveEquipment`\.  
Type: Integer  
Valid Range: Minimum value of 0\.  
Required: No

## See Also<a name="API_ProtectiveEquipmentPerson_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ProtectiveEquipmentPerson) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ProtectiveEquipmentPerson) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ProtectiveEquipmentPerson) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ProtectiveEquipmentPerson) 