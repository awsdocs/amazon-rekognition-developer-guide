# DatasetDescription<a name="API_DatasetDescription"></a>

 A description for a dataset\. For more information, see [ DescribeDataset ](API_DescribeDataset.md)\.

The status fields `Status`, `StatusMessage`, and `StatusMessageCode` reflect the last operation on the dataset\. 

## Contents<a name="API_DatasetDescription_Contents"></a>

 ** CreationTimestamp **   <a name="rekognition-Type-DatasetDescription-CreationTimestamp"></a>
 The Unix timestamp for the time and date that the dataset was created\.   
Type: Timestamp  
Required: No

 ** DatasetStats **   <a name="rekognition-Type-DatasetDescription-DatasetStats"></a>
 The status message code for the dataset\.   
Type: [ DatasetStats ](API_DatasetStats.md) object  
Required: No

 ** LastUpdatedTimestamp **   <a name="rekognition-Type-DatasetDescription-LastUpdatedTimestamp"></a>
 The Unix timestamp for the date and time that the dataset was last updated\.   
Type: Timestamp  
Required: No

 ** Status **   <a name="rekognition-Type-DatasetDescription-Status"></a>
 The status of the dataset\.   
Type: String  
Valid Values:` CREATE_IN_PROGRESS | CREATE_COMPLETE | CREATE_FAILED | UPDATE_IN_PROGRESS | UPDATE_COMPLETE | UPDATE_FAILED | DELETE_IN_PROGRESS`   
Required: No

 ** StatusMessage **   <a name="rekognition-Type-DatasetDescription-StatusMessage"></a>
 The status message for the dataset\.   
Type: String  
Required: No

 ** StatusMessageCode **   <a name="rekognition-Type-DatasetDescription-StatusMessageCode"></a>
 The status message code for the dataset operation\. If a service error occurs, try the API call again later\. If a client error occurs, check the input parameters to the dataset API call that failed\.   
Type: String  
Valid Values:` SUCCESS | SERVICE_ERROR | CLIENT_ERROR`   
Required: No

## See Also<a name="API_DatasetDescription_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DatasetDescription) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DatasetDescription) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DatasetDescription) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DatasetDescription) 