# EvaluationResult<a name="API_EvaluationResult"></a>

The evaluation results for the training of a model\.

## Contents<a name="API_EvaluationResult_Contents"></a>

 **F1Score**   <a name="rekognition-Type-EvaluationResult-F1Score"></a>
The F1 score for the evaluation of all labels\. The F1 score metric evaluates the overall precision and recall performance of the model as a single value\. A higher value indicates better precision and recall performance\. A lower score indicates that precision, recall, or both are performing poorly\.   
Type: Float  
Required: No

 **Summary**   <a name="rekognition-Type-EvaluationResult-Summary"></a>
The S3 bucket that contains the training summary\.  
Type: [Summary](API_Summary.md) object  
Required: No

## See Also<a name="API_EvaluationResult_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/EvaluationResult) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/EvaluationResult) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/EvaluationResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/EvaluationResult) 