# AgeRange<a name="API_AgeRange"></a>

Structure containing the estimated age range, in years, for a face\.

Amazon Rekognition estimates an age range for faces detected in the input image\. Estimated age ranges can overlap\. A face of a 5\-year\-old might have an estimated range of 4\-6, while the face of a 6\-year\-old might have an estimated range of 4\-8\.

## Contents<a name="API_AgeRange_Contents"></a>

 **High**   <a name="rekognition-Type-AgeRange-High"></a>
The highest estimated age\.  
Type: Integer  
Valid Range: Minimum value of 0\.  
Required: No

 **Low**   <a name="rekognition-Type-AgeRange-Low"></a>
The lowest estimated age\.  
Type: Integer  
Valid Range: Minimum value of 0\.  
Required: No

## See Also<a name="API_AgeRange_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/AgeRange) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/AgeRange) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/AgeRange) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/AgeRange) 