# ProjectDescription<a name="API_ProjectDescription"></a>

A description of a Amazon Rekognition Custom Labels project\.

## Contents<a name="API_ProjectDescription_Contents"></a>

 ** CreationTimestamp **   <a name="rekognition-Type-ProjectDescription-CreationTimestamp"></a>
The Unix timestamp for the date and time that the project was created\.  
Type: Timestamp  
Required: No

 ** ProjectArn **   <a name="rekognition-Type-ProjectDescription-ProjectArn"></a>
The Amazon Resource Name \(ARN\) of the project\.  
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`   
Required: No

 ** Status **   <a name="rekognition-Type-ProjectDescription-Status"></a>
The current status of the project\.  
Type: String  
Valid Values:` CREATING | CREATED | DELETING`   
Required: No

## See Also<a name="API_ProjectDescription_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ProjectDescription) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ProjectDescription) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ProjectDescription) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ProjectDescription) 