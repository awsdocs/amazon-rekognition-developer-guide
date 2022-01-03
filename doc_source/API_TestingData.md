# TestingData<a name="API_TestingData"></a>

The dataset used for testing\. Optionally, if `AutoCreate` is set, Amazon Rekognition Custom Labels uses the training dataset to create a test dataset with a temporary split of the training dataset\. 

## Contents<a name="API_TestingData_Contents"></a>

 ** Assets **   <a name="rekognition-Type-TestingData-Assets"></a>
The assets used for testing\.  
Type: Array of [ Asset ](API_Asset.md) objects  
Required: No

 ** AutoCreate **   <a name="rekognition-Type-TestingData-AutoCreate"></a>
If specified, Amazon Rekognition Custom Labels temporarily splits the training dataset \(80%\) to create a test dataset \(20%\) for the training job\. After training completes, the test dataset is not stored and the training dataset reverts to its previous size\.  
Type: Boolean  
Required: No

## See Also<a name="API_TestingData_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/TestingData) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/TestingData) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/TestingData) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/TestingData) 