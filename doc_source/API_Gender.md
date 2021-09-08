# Gender<a name="API_Gender"></a>

The predicted gender of a detected face\. 

Amazon Rekognition makes gender binary \(male/female\) predictions based on the physical appearance of a face in a particular image\. This kind of prediction is not designed to categorize a person’s gender identity, and you shouldn't use Amazon Rekognition to make such a determination\. For example, a male actor wearing a long\-haired wig and earrings for a role might be predicted as female\.

Using Amazon Rekognition to make gender binary predictions is best suited for use cases where aggregate gender distribution statistics need to be analyzed without identifying specific users\. For example, the percentage of female users compared to male users on a social media platform\. 

We don't recommend using gender binary predictions to make decisions that impact  an individual's rights, privacy, or access to services\.

## Contents<a name="API_Gender_Contents"></a>

 ** Confidence **   <a name="rekognition-Type-Gender-Confidence"></a>
Level of confidence in the prediction\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 ** Value **   <a name="rekognition-Type-Gender-Value"></a>
The predicted gender of the face\.  
Type: String  
Valid Values:` Male | Female`   
Required: No

## See Also<a name="API_Gender_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/Gender) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/Gender) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/Gender) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/Gender) 