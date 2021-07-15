# StartTextDetectionFilters<a name="API_StartTextDetectionFilters"></a>

Set of optional parameters that let you set the criteria text must meet to be included in your response\. `WordFilter` looks at a word's height, width and minimum confidence\. `RegionOfInterest` lets you set a specific region of the screen to look for text in\.

## Contents<a name="API_StartTextDetectionFilters_Contents"></a>

 **RegionsOfInterest**   <a name="rekognition-Type-StartTextDetectionFilters-RegionsOfInterest"></a>
Filter focusing on a certain area of the frame\. Uses a `BoundingBox` object to set the region of the screen\.  
Type: Array of [RegionOfInterest](API_RegionOfInterest.md) objects  
Array Members: Minimum number of 0 items\. Maximum number of 10 items\.  
Required: No

 **WordFilter**   <a name="rekognition-Type-StartTextDetectionFilters-WordFilter"></a>
Filters focusing on qualities of the text, such as confidence or size\.  
Type: [DetectionFilter](API_DetectionFilter.md) object  
Required: No

## See Also<a name="API_StartTextDetectionFilters_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StartTextDetectionFilters) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/StartTextDetectionFilters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/StartTextDetectionFilters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StartTextDetectionFilters) 