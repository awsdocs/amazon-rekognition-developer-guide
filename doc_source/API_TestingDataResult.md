# TestingDataResult<a name="API_TestingDataResult"></a>

Sagemaker Groundtruth format manifest files for the input, output and validation datasets that are used and created during testing\.

## Contents<a name="API_TestingDataResult_Contents"></a>

 **Input**   <a name="rekognition-Type-TestingDataResult-Input"></a>
The testing dataset that was supplied for training\.  
Type: [TestingData](API_TestingData.md) object  
Required: No

 **Output**   <a name="rekognition-Type-TestingDataResult-Output"></a>
The subset of the dataset that was actually tested\. Some images \(assets\) might not be tested due to file formatting and other issues\.   
Type: [TestingData](API_TestingData.md) object  
Required: No

 **Validation**   <a name="rekognition-Type-TestingDataResult-Validation"></a>
The location of the data validation manifest\. The data validation manifest is created for the test dataset during model training\.  
Type: [ValidationData](API_ValidationData.md) object  
Required: No

## See Also<a name="API_TestingDataResult_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/TestingDataResult) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/TestingDataResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/TestingDataResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/TestingDataResult) 