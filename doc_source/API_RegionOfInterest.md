# RegionOfInterest<a name="API_RegionOfInterest"></a>

Specifies a location within the frame that Rekognition checks for text\. Uses a `BoundingBox` object to set a region of the screen\.

A word is included in the region if the word is more than half in that region\. If there is more than one region, the word will be compared with all regions of the screen\. Any word more than half in a region is kept in the results\.

## Contents<a name="API_RegionOfInterest_Contents"></a>

 **BoundingBox**   <a name="rekognition-Type-RegionOfInterest-BoundingBox"></a>
The box representing a region of interest on screen\.  
Type: [BoundingBox](API_BoundingBox.md) object  
Required: No

## See Also<a name="API_RegionOfInterest_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/RegionOfInterest) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/RegionOfInterest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/RegionOfInterest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/RegionOfInterest) 