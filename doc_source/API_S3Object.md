# S3Object<a name="API_S3Object"></a>

Provides the S3 bucket name and object name\.

The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations\.

For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object\. For more information, see [Amazon Rekognition Resource\-Based Policies](security_iam_service-with-iam.md#security_iam_service-with-iam-resource-based-policies)\. 

## Contents<a name="API_S3Object_Contents"></a>

 **Bucket**   <a name="rekognition-Type-S3Object-Bucket"></a>
Name of the S3 bucket\.  
Type: String  
Length Constraints: Minimum length of 3\. Maximum length of 255\.  
Pattern: `[0-9A-Za-z\.\-_]*`   
Required: No

 **Name**   <a name="rekognition-Type-S3Object-Name"></a>
S3 object key name\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 1024\.  
Required: No

 **Version**   <a name="rekognition-Type-S3Object-Version"></a>
If the bucket is versioning enabled, you can specify the object version\.   
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 1024\.  
Required: No

## See Also<a name="API_S3Object_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/S3Object) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/S3Object) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/S3Object) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/S3Object) 