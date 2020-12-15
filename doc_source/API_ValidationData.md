# ValidationData<a name="API_ValidationData"></a>

Contains the Amazon S3 bucket location of the validation data for a model training job\. 

The validation data includes error information for individual JSON Lines\. For more information, see *Debugging a Failed Model Training* in the Amazon Rekognition Custom Labels Developer Guide\. 

You get the `ValidationData` object for the training dataset \([TrainingDataResult](API_TrainingDataResult.md)\) and the test dataset \([TestingDataResult](API_TestingDataResult.md)\) by calling [DescribeProjectVersions](API_DescribeProjectVersions.md)\. 

The assets array contains a single [Asset](API_Asset.md) object\. The [GroundTruthManifest](API_GroundTruthManifest.md) field of the Asset object contains the S3 bucket location of the validation data\. 

## Contents<a name="API_ValidationData_Contents"></a>

 **Assets**   <a name="rekognition-Type-ValidationData-Assets"></a>
The assets that comprise the validation data\.   
Type: Array of [Asset](API_Asset.md) objects  
Required: No

## See Also<a name="API_ValidationData_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ValidationData) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ValidationData) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/ValidationData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ValidationData) 