# DetectTextFilters<a name="API_DetectTextFilters"></a>

A set of optional parameters that you can use to set the criteria that the text must meet to be included in your response\. `WordFilter` looks at a word’s height, width, and minimum confidence\. `RegionOfInterest` lets you set a specific region of the image to look for text in\. 

## Contents<a name="API_DetectTextFilters_Contents"></a>

 **RegionsOfInterest**   <a name="rekognition-Type-DetectTextFilters-RegionsOfInterest"></a>
 A Filter focusing on a certain area of the image\. Uses a `BoundingBox` object to set the region of the image\.  
Type: Array of [RegionOfInterest](API_RegionOfInterest.md) objects  
Array Members: Minimum number of 0 items\. Maximum number of 10 items\.  
Required: No

 **WordFilter**   <a name="rekognition-Type-DetectTextFilters-WordFilter"></a>
A set of parameters that allow you to filter out certain results from your returned results\.  
Type: [DetectionFilter](API_DetectionFilter.md) object  
Required: No

## See Also<a name="API_DetectTextFilters_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DetectTextFilters) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DetectTextFilters) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/DetectTextFilters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DetectTextFilters) 