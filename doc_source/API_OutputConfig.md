# OutputConfig<a name="API_OutputConfig"></a>

The S3 bucket and folder location where training output is placed\.

## Contents<a name="API_OutputConfig_Contents"></a>

 **S3Bucket**   <a name="rekognition-Type-OutputConfig-S3Bucket"></a>
The S3 bucket where training output is placed\.  
Type: String  
Length Constraints: Minimum length of 3\. Maximum length of 255\.  
Pattern: `[0-9A-Za-z\.\-_]*`   
Required: No

 **S3KeyPrefix**   <a name="rekognition-Type-OutputConfig-S3KeyPrefix"></a>
The prefix applied to the training output files\.   
Type: String  
Length Constraints: Maximum length of 1024\.  
Required: No

## See Also<a name="API_OutputConfig_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/OutputConfig) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/OutputConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/OutputConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/OutputConfig) 