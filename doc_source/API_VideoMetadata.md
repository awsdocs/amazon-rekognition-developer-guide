# VideoMetadata<a name="API_VideoMetadata"></a>

Information about a video that Amazon Rekognition analyzed\. `Videometadata` is returned in every page of paginated responses from a Amazon Rekognition video operation\.

## Contents<a name="API_VideoMetadata_Contents"></a>

 **Codec**   <a name="rekognition-Type-VideoMetadata-Codec"></a>
Type of compression used in the analyzed video\.   
Type: String  
Required: No

 **DurationMillis**   <a name="rekognition-Type-VideoMetadata-DurationMillis"></a>
Length of the video in milliseconds\.  
Type: Long  
Valid Range: Minimum value of 0\.  
Required: No

 **Format**   <a name="rekognition-Type-VideoMetadata-Format"></a>
Format of the analyzed video\. Possible values are MP4, MOV and AVI\.   
Type: String  
Required: No

 **FrameHeight**   <a name="rekognition-Type-VideoMetadata-FrameHeight"></a>
Vertical pixel dimension of the video\.  
Type: Long  
Valid Range: Minimum value of 0\.  
Required: No

 **FrameRate**   <a name="rekognition-Type-VideoMetadata-FrameRate"></a>
Number of frames per second in the video\.  
Type: Float  
Required: No

 **FrameWidth**   <a name="rekognition-Type-VideoMetadata-FrameWidth"></a>
Horizontal pixel dimension of the video\.  
Type: Long  
Valid Range: Minimum value of 0\.  
Required: No

## See Also<a name="API_VideoMetadata_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/VideoMetadata) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/VideoMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/VideoMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/VideoMetadata) 