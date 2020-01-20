# HumanLoopActivationOutput<a name="API_HumanLoopActivationOutput"></a>

Shows the results of the human in the loop evaluation\. If there is no HumanLoopArn, the input did not trigger human review\.

## Contents<a name="API_HumanLoopActivationOutput_Contents"></a>

 **HumanLoopActivationConditionsEvaluationResults**   <a name="rekognition-Type-HumanLoopActivationOutput-HumanLoopActivationConditionsEvaluationResults"></a>
Shows the result of condition evaluations, including those conditions which activated a human review\.  
Type: String  
Length Constraints: Maximum length of 10240\.  
Required: No

 **HumanLoopActivationReasons**   <a name="rekognition-Type-HumanLoopActivationOutput-HumanLoopActivationReasons"></a>
Shows if and why human review was needed\.  
Type: Array of strings  
Array Members: Minimum number of 1 item\.  
Required: No

 **HumanLoopArn**   <a name="rekognition-Type-HumanLoopActivationOutput-HumanLoopArn"></a>
The Amazon Resource Name \(ARN\) of the HumanLoop created\.  
Type: String  
Length Constraints: Maximum length of 256\.  
Required: No

## See Also<a name="API_HumanLoopActivationOutput_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/HumanLoopActivationOutput) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/HumanLoopActivationOutput) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/HumanLoopActivationOutput) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/HumanLoopActivationOutput) 