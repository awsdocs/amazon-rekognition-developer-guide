# PersonDetail<a name="API_PersonDetail"></a>

Details about a person detected in a video analysis request\.

## Contents<a name="API_PersonDetail_Contents"></a>

 **BoundingBox**   <a name="rekognition-Type-PersonDetail-BoundingBox"></a>
Bounding box around the detected person\.  
Type: [BoundingBox](API_BoundingBox.md) object  
Required: No

 **Face**   <a name="rekognition-Type-PersonDetail-Face"></a>
Face details for the detected person\.  
Type: [FaceDetail](API_FaceDetail.md) object  
Required: No

 **Index**   <a name="rekognition-Type-PersonDetail-Index"></a>
Identifier for the person detected person within a video\. Use to keep track of the person throughout the video\. The identifier is not stored by Amazon Rekognition\.  
Type: Long  
Required: No

## See Also<a name="API_PersonDetail_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/PersonDetail) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/PersonDetail) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/PersonDetail) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/PersonDetail) 