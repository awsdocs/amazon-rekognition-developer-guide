# TrainingDataResult<a name="API_TrainingDataResult"></a>

Sagemaker Groundtruth format manifest files for the input, output and validation datasets that are used and created during testing\.

## Contents<a name="API_TrainingDataResult_Contents"></a>

 **Input**   <a name="rekognition-Type-TrainingDataResult-Input"></a>
The training assets that you supplied for training\.  
Type: [TrainingData](API_TrainingData.md) object  
Required: No

 **Output**   <a name="rekognition-Type-TrainingDataResult-Output"></a>
The images \(assets\) that were actually trained by Amazon Rekognition Custom Labels\.   
Type: [TrainingData](API_TrainingData.md) object  
Required: No

 **Validation**   <a name="rekognition-Type-TrainingDataResult-Validation"></a>
The location of the data validation manifest\. The data validation manifest is created for the training dataset during model training\.  
Type: [ValidationData](API_ValidationData.md) object  
Required: No

## See Also<a name="API_TrainingDataResult_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/TrainingDataResult) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/TrainingDataResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/TrainingDataResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/TrainingDataResult) 