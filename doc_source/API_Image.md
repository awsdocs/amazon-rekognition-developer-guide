# Image<a name="API_Image"></a>

Provides the input image either as bytes or an S3 object\.

You pass image bytes to an Amazon Rekognition API operation by using the `Bytes` property\. For example, you would use the `Bytes` property to pass an image loaded from a local file system\. Image bytes passed by using the `Bytes` property must be base64\-encoded\. Your code may not need to encode image bytes if you are using an AWS SDK to call Amazon Rekognition API operations\. 

For more information, see [Analyzing an Image Loaded from a Local File System](images-bytes.md)\.

 You pass images stored in an S3 bucket to an Amazon Rekognition API operation by using the `S3Object` property\. Images stored in an S3 bucket do not need to be base64\-encoded\.

The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition operations\.

If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes using the Bytes property is not supported\. You must first upload the image to an Amazon S3 bucket and then call the operation using the S3Object property\.

For Amazon Rekognition to process an S3 object, the user must have permission to access the S3 object\. For more information, see [Resource\-Based Policies](access-control-overview.md#manage-access-resource-policies)\. 

## Contents<a name="API_Image_Contents"></a>

 **Bytes**   <a name="rekognition-Type-Image-Bytes"></a>
Blob of image bytes up to 5 MBs\.  
Type: Base64\-encoded binary data object  
Length Constraints: Minimum length of 1\. Maximum length of 5242880\.  
Required: No

 **S3Object**   <a name="rekognition-Type-Image-S3Object"></a>
Identifies an S3 object as the image source\.  
Type: [S3Object](API_S3Object.md) object  
Required: No

## See Also<a name="API_Image_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/Image) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/Image) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/Image) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/Image) 