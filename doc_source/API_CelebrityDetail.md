# CelebrityDetail<a name="API_CelebrityDetail"></a>

Information about a recognized celebrity\.

## Contents<a name="API_CelebrityDetail_Contents"></a>

 **BoundingBox**   
Bounding box around the body of a celebrity\.  
Type: [BoundingBox](API_BoundingBox.md) object  
Required: No

 **Confidence**   
The confidence, in percentage, that Amazon Rekognition has that the recognized face is the celebrity\.   
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 **Face**   
Face details for the recognized celebrity\.  
Type: [FaceDetail](API_FaceDetail.md) object  
Required: No

 **Id**   
The unique identifier for the celebrity\.   
Type: String  
Pattern: `[0-9A-Za-z]*`   
Required: No

 **Name**   
The name of the celebrity\.  
Type: String  
Required: No

 **Urls**   
An array of URLs pointing to additional celebrity information\.   
Type: Array of strings  
Required: No

## See Also<a name="API_CelebrityDetail_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CelebrityDetail) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/CelebrityDetail) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/CelebrityDetail) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/CelebrityDetail) 