# DatasetMetadata<a name="API_DatasetMetadata"></a>

 Summary information for an Amazon Rekognition Custom Labels dataset\. For more information, see [ ProjectDescription ](API_ProjectDescription.md)\. 

## Contents<a name="API_DatasetMetadata_Contents"></a>

 ** CreationTimestamp **   <a name="rekognition-Type-DatasetMetadata-CreationTimestamp"></a>
 The Unix timestamp for the date and time that the dataset was created\.   
Type: Timestamp  
Required: No

 ** DatasetArn **   <a name="rekognition-Type-DatasetMetadata-DatasetArn"></a>
 The Amazon Resource Name \(ARN\) for the dataset\.   
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/dataset\/(train|test)\/[0-9]+$)`   
Required: No

 ** DatasetType **   <a name="rekognition-Type-DatasetMetadata-DatasetType"></a>
 The type of the dataset\.   
Type: String  
Valid Values:` TRAIN | TEST`   
Required: No

 ** Status **   <a name="rekognition-Type-DatasetMetadata-Status"></a>
 The status for the dataset\.   
Type: String  
Valid Values:` CREATE_IN_PROGRESS | CREATE_COMPLETE | CREATE_FAILED | UPDATE_IN_PROGRESS | UPDATE_COMPLETE | UPDATE_FAILED | DELETE_IN_PROGRESS`   
Required: No

 ** StatusMessage **   <a name="rekognition-Type-DatasetMetadata-StatusMessage"></a>
 The status message for the dataset\.   
Type: String  
Required: No

 ** StatusMessageCode **   <a name="rekognition-Type-DatasetMetadata-StatusMessageCode"></a>
 The status message code for the dataset operation\. If a service error occurs, try the API call again later\. If a client error occurs, check the input parameters to the dataset API call that failed\.   
Type: String  
Valid Values:` SUCCESS | SERVICE_ERROR | CLIENT_ERROR`   
Required: No

## See Also<a name="API_DatasetMetadata_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DatasetMetadata) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DatasetMetadata) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DatasetMetadata) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DatasetMetadata) 