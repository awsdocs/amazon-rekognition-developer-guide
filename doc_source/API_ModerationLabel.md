# ModerationLabel<a name="API_ModerationLabel"></a>

Provides information about a single type of unsafe content found in an image or video\. Each type of moderated content has a label within a hierarchical taxonomy\. For more information, see [Detecting Unsafe Content](moderation.md)\.

## Contents<a name="API_ModerationLabel_Contents"></a>

 **Confidence**   <a name="rekognition-Type-ModerationLabel-Confidence"></a>
Specifies the confidence that Amazon Rekognition has that the label has been correctly identified\.  
If you don't specify the `MinConfidence` parameter in the call to `DetectModerationLabels`, the operation returns labels with a confidence value greater than or equal to 50 percent\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 **Name**   <a name="rekognition-Type-ModerationLabel-Name"></a>
The label name for the type of unsafe content detected in the image\.  
Type: String  
Required: No

 **ParentName**   <a name="rekognition-Type-ModerationLabel-ParentName"></a>
The name for the parent label\. Labels at the top level of the hierarchy have the parent label `""`\.  
Type: String  
Required: No

## See Also<a name="API_ModerationLabel_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ModerationLabel) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ModerationLabel) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/ModerationLabel) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/ModerationLabel) 