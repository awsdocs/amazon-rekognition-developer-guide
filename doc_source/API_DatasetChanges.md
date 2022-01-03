# DatasetChanges<a name="API_DatasetChanges"></a>

 Describes updates or additions to a dataset\. A Single update or addition is an entry \(JSON Line\) that provides information about a single image\. To update an existing entry, you match the `source-ref` field of the update entry with the `source-ref` filed of the entry that you want to update\. If the `source-ref` field doesn't match an existing entry, the entry is added to dataset as a new entry\. 

## Contents<a name="API_DatasetChanges_Contents"></a>

 ** GroundTruth **   <a name="rekognition-Type-DatasetChanges-GroundTruth"></a>
A Base64\-encoded binary data object containing one or JSON lines that either update the dataset or are additions to the dataset\. You change a dataset by calling [ UpdateDatasetEntries ](API_UpdateDatasetEntries.md)\. If you are using an AWS SDK to call `UpdateDatasetEntries`, you don't need to encode `Changes` as the SDK encodes the data for you\.   
For example JSON lines, see [Image\-Level labels in manifest files](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-manifest-file-classification.html) and [Object localization in manifest files](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-create-manifest-file-object-detection.html)\.  
Type: Base64\-encoded binary data object  
Length Constraints: Minimum length of 1\. Maximum length of 5242880\.  
Required: Yes

## See Also<a name="API_DatasetChanges_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DatasetChanges) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DatasetChanges) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DatasetChanges) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DatasetChanges) 