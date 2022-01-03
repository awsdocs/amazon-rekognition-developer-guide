# DistributeDataset<a name="API_DistributeDataset"></a>

 A training dataset or a test dataset used in a dataset distribution operation\. For more information, see [ DistributeDatasetEntries ](API_DistributeDatasetEntries.md)\. 

## Contents<a name="API_DistributeDataset_Contents"></a>

 ** Arn **   <a name="rekognition-Type-DistributeDataset-Arn"></a>
The Amazon Resource Name \(ARN\) of the dataset that you want to use\.   
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/dataset\/(train|test)\/[0-9]+$)`   
Required: Yes

## See Also<a name="API_DistributeDataset_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DistributeDataset) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DistributeDataset) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DistributeDataset) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DistributeDataset) 