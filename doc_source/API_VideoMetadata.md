# VideoMetadata<a name="API_VideoMetadata"></a>

Information about a video that Amazon Rekognition analyzed\. `Videometadata` is returned in every page of paginated responses from a Amazon Rekognition video operation\.

## Contents<a name="API_VideoMetadata_Contents"></a>

 **Codec**   
Type of compression used in the analyzed video\.   
Type: String  
Required: No

 **DurationMillis**   
Length of the video in milliseconds\.  
Type: Long  
Valid Range: Minimum value of 0\.  
Required: No

 **Format**   
Format of the analyzed video\. Possible values are MP4, MOV and AVI\.   
Type: String  
Required: No

 **FrameHeight**   
Vertical pixel dimension of the video\.  
Type: Long  
Valid Range: Minimum value of 0\.  
Required: No

 **FrameRate**   
Number of frames per second in the video\.  
Type: Float  
Required: No

 **FrameWidth**   
Horizontal pixel dimension of the video\.  
Type: Long  
Valid Range: Minimum value of 0\.  
Required: No

## See Also<a name="API_VideoMetadata_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/VideoMetadata) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/VideoMetadata) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/VideoMetadata) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/VideoMetadata) 