# PersonDetection<a name="API_PersonDetection"></a>

Details and tracking information for a single time a person is tracked in a video\. Amazon Rekognition operations that track persons return an array of `PersonDetection` objects with elements for each time a person is tracked in a video\. 

For more information, see [GetPersonTracking](API_GetPersonTracking.md)\. 

## Contents<a name="API_PersonDetection_Contents"></a>

 **Person**   <a name="rekognition-Type-PersonDetection-Person"></a>
Details about a person tracked in a video\.  
Type: [PersonDetail](API_PersonDetail.md) object  
Required: No

 **Timestamp**   <a name="rekognition-Type-PersonDetection-Timestamp"></a>
The time, in milliseconds from the start of the video, that the person was tracked\.  
Type: Long  
Required: No

## See Also<a name="API_PersonDetection_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/PersonDetection) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/PersonDetection) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/PersonDetection) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/PersonDetection) 