# StartTechnicalCueDetectionFilter<a name="API_StartTechnicalCueDetectionFilter"></a>

Filters for the technical segments returned by [GetSegmentDetection](API_GetSegmentDetection.md)\. For more information, see [StartSegmentDetectionFilters](API_StartSegmentDetectionFilters.md)\.

## Contents<a name="API_StartTechnicalCueDetectionFilter_Contents"></a>

 **MinSegmentConfidence**   <a name="rekognition-Type-StartTechnicalCueDetectionFilter-MinSegmentConfidence"></a>
Specifies the minimum confidence that Amazon Rekognition Video must have in order to return a detected segment\. Confidence represents how certain Amazon Rekognition is that a segment is correctly identified\. 0 is the lowest confidence\. 100 is the highest confidence\. Amazon Rekognition Video doesn't return any segments with a confidence level lower than this specified value\.  
If you don't specify `MinSegmentConfidence`, `GetSegmentDetection` returns segments with confidence values greater than or equal to 50 percent\.  
Type: Float  
Valid Range: Minimum value of 50\. Maximum value of 100\.  
Required: No

## See Also<a name="API_StartTechnicalCueDetectionFilter_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StartTechnicalCueDetectionFilter) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/StartTechnicalCueDetectionFilter) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/StartTechnicalCueDetectionFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StartTechnicalCueDetectionFilter) 