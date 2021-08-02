# ProjectVersionDescription<a name="API_ProjectVersionDescription"></a>

The description of a version of a model\.

## Contents<a name="API_ProjectVersionDescription_Contents"></a>

 **BillableTrainingTimeInSeconds**   <a name="rekognition-Type-ProjectVersionDescription-BillableTrainingTimeInSeconds"></a>
The duration, in seconds, that the model version has been billed for training\. This value is only returned if the model version has been successfully trained\.  
Type: Long  
Valid Range: Minimum value of 0\.  
Required: No

 **CreationTimestamp**   <a name="rekognition-Type-ProjectVersionDescription-CreationTimestamp"></a>
The Unix datetime for the date and time that training started\.  
Type: Timestamp  
Required: No

 **EvaluationResult**   <a name="rekognition-Type-ProjectVersionDescription-EvaluationResult"></a>
The training results\. `EvaluationResult` is only returned if training is successful\.  
Type: [EvaluationResult](API_EvaluationResult.md) object  
Required: No

 **KmsKeyId**   <a name="rekognition-Type-ProjectVersionDescription-KmsKeyId"></a>
The identifer for the AWS Key Management Service \(AWS KMS\) customer master key that was used to encrypt the model during training\.   
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 2048\.  
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`   
Required: No

 **ManifestSummary**   <a name="rekognition-Type-ProjectVersionDescription-ManifestSummary"></a>
The location of the summary manifest\. The summary manifest provides aggregate data validation results for the training and test datasets\.  
Type: [GroundTruthManifest](API_GroundTruthManifest.md) object  
Required: No

 **MinInferenceUnits**   <a name="rekognition-Type-ProjectVersionDescription-MinInferenceUnits"></a>
The minimum number of inference units used by the model\. For more information, see [StartProjectVersion](API_StartProjectVersion.md)\.  
Type: Integer  
Valid Range: Minimum value of 1\.  
Required: No

 **OutputConfig**   <a name="rekognition-Type-ProjectVersionDescription-OutputConfig"></a>
The location where training results are saved\.  
Type: [OutputConfig](API_OutputConfig.md) object  
Required: No

 **ProjectVersionArn**   <a name="rekognition-Type-ProjectVersionDescription-ProjectVersionArn"></a>
The Amazon Resource Name \(ARN\) of the model version\.   
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/version\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`   
Required: No

 **Status**   <a name="rekognition-Type-ProjectVersionDescription-Status"></a>
The current status of the model version\.  
Type: String  
Valid Values:` TRAINING_IN_PROGRESS | TRAINING_COMPLETED | TRAINING_FAILED | STARTING | RUNNING | FAILED | STOPPING | STOPPED | DELETING`   
Required: No

 **StatusMessage**   <a name="rekognition-Type-ProjectVersionDescription-StatusMessage"></a>
A descriptive message for an error or warning that occurred\.  
Type: String  
Required: No

 **TestingDataResult**   <a name="rekognition-Type-ProjectVersionDescription-TestingDataResult"></a>
Contains information about the testing results\.  
Type: [TestingDataResult](API_TestingDataResult.md) object  
Required: No

 **TrainingDataResult**   <a name="rekognition-Type-ProjectVersionDescription-TrainingDataResult"></a>
Contains information about the training results\.  
Type: [TrainingDataResult](API_TrainingDataResult.md) object  
Required: No

 **TrainingEndTimestamp**   <a name="rekognition-Type-ProjectVersionDescription-TrainingEndTimestamp"></a>
The Unix date and time that training of the model ended\.  
Type: Timestamp  
Required: No

## See Also<a name="API_ProjectVersionDescription_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ProjectVersionDescription) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ProjectVersionDescription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ProjectVersionDescription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ProjectVersionDescription) 