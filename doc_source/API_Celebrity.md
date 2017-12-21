# Celebrity<a name="API_Celebrity"></a>

Provides information about a celebrity recognized by the [RecognizeCelebrities](API_RecognizeCelebrities.md) operation\.

## Contents<a name="API_Celebrity_Contents"></a>

 **Face**   
Provides information about the celebrity's face, such as its location on the image\.  
Type: [ComparedFace](API_ComparedFace.md) object  
Required: No

 **Id**   
A unique identifier for the celebrity\.   
Type: String  
Pattern: `[0-9A-Za-z]*`   
Required: No

 **MatchConfidence**   
The confidence, in percentage, that Rekognition has that the recognized face is the celebrity\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 **Name**   
The name of the celebrity\.  
Type: String  
Required: No

 **Urls**   
An array of URLs pointing to additional information about the celebrity\. If there is no additional information about the celebrity, this list is empty\.  
Type: Array of strings  
Required: No

## See Also<a name="API_Celebrity_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/Celebrity) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/Celebrity) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/Celebrity) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/Celebrity) 