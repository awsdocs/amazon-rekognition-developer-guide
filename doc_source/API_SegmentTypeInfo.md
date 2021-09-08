# SegmentTypeInfo<a name="API_SegmentTypeInfo"></a>

Information about the type of a segment requested in a call to [ StartSegmentDetection ](API_StartSegmentDetection.md)\. An array of `SegmentTypeInfo` objects is returned by the response from [ GetSegmentDetection ](API_GetSegmentDetection.md)\.

## Contents<a name="API_SegmentTypeInfo_Contents"></a>

 ** ModelVersion **   <a name="rekognition-Type-SegmentTypeInfo-ModelVersion"></a>
The version of the model used to detect segments\.  
Type: String  
Required: No

 ** Type **   <a name="rekognition-Type-SegmentTypeInfo-Type"></a>
The type of a segment \(technical cue or shot detection\)\.  
Type: String  
Valid Values:` TECHNICAL_CUE | SHOT`   
Required: No

## See Also<a name="API_SegmentTypeInfo_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/SegmentTypeInfo) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/SegmentTypeInfo) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/SegmentTypeInfo) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/SegmentTypeInfo) 