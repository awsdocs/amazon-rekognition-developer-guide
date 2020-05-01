# DetectionFilter<a name="API_DetectionFilter"></a>

A set of parameters that allow you to filter out certain results from your returned results\.

## Contents<a name="API_DetectionFilter_Contents"></a>

 **MinBoundingBoxHeight**   <a name="rekognition-Type-DetectionFilter-MinBoundingBoxHeight"></a>
Sets the minimum height of the word bounding box\. Words with bounding box heights lesser than this value will be excluded from the result\. Value is relative to the video frame height\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 1\.  
Required: No

 **MinBoundingBoxWidth**   <a name="rekognition-Type-DetectionFilter-MinBoundingBoxWidth"></a>
Sets the minimum width of the word bounding box\. Words with bounding boxes widths lesser than this value will be excluded from the result\. Value is relative to the video frame width\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 1\.  
Required: No

 **MinConfidence**   <a name="rekognition-Type-DetectionFilter-MinConfidence"></a>
Sets confidence of word detection\. Words with detection confidence below this will be excluded from the result\. Values should be between 0\.5 and 1 as Text in Video will not return any result below 0\.5\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

## See Also<a name="API_DetectionFilter_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DetectionFilter) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DetectionFilter) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/DetectionFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DetectionFilter) 