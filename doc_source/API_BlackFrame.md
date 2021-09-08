# BlackFrame<a name="API_BlackFrame"></a>

 A filter that allows you to control the black frame detection by specifying the black levels and pixel coverage of black pixels in a frame\. As videos can come from multiple sources, formats, and time periods, they may contain different standards and varying noise levels for black frames that need to be accounted for\. For more information, see [ StartSegmentDetection ](API_StartSegmentDetection.md)\. 

## Contents<a name="API_BlackFrame_Contents"></a>

 ** MaxPixelThreshold **   <a name="rekognition-Type-BlackFrame-MaxPixelThreshold"></a>
 A threshold used to determine the maximum luminance value for a pixel to be considered black\. In a full color range video, luminance values range from 0\-255\. A pixel value of 0 is pure black, and the most strict filter\. The maximum black pixel value is computed as follows: max\_black\_pixel\_value = minimum\_luminance \+ MaxPixelThreshold \*luminance\_range\.   
For example, for a full range video with BlackPixelThreshold = 0\.1, max\_black\_pixel\_value is 0 \+ 0\.1 \* \(255\-0\) = 25\.5\.  
The default value of MaxPixelThreshold is 0\.2, which maps to a max\_black\_pixel\_value of 51 for a full range video\. You can lower this threshold to be more strict on black levels\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 1\.  
Required: No

 ** MinCoveragePercentage **   <a name="rekognition-Type-BlackFrame-MinCoveragePercentage"></a>
 The minimum percentage of pixels in a frame that need to have a luminance below the max\_black\_pixel\_value for a frame to be considered a black frame\. Luminance is calculated using the BT\.709 matrix\.   
The default value is 99, which means at least 99% of all pixels in the frame are black pixels as per the `MaxPixelThreshold` set\. You can reduce this value to allow more noise on the black frame\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

## See Also<a name="API_BlackFrame_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/BlackFrame) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/BlackFrame) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/BlackFrame) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/BlackFrame) 