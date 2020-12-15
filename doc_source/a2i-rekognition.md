# Reviewing inappropriate content with Amazon Augmented AI<a name="a2i-rekognition"></a>

Amazon Augmented AI \(Amazon A2I\) enables you to build the workflows that are required for human review of machine learning predictions\.

Amazon Rekognition is directly integrated with Amazon A2I so that you can easily implement human review for the use case of detecting unsafe images\. Amazon A2I provides a human review workflow for image moderation\. This enables you to easily review predictions from Amazon Rekognition\. You can define confidence thresholds for your use case and adjust them over time\. With Amazon A2I, you can use a pool of reviewers within your own organization or Amazon Mechanical Turk\. You can also use workforce vendors that are prescreened by AWS for quality and adherence to security procedures\.

The following steps walk you through how to set up Amazon A2I with Amazon Rekognition\. First, you create a flow definition with Amazon A2I that has the conditions that trigger human review\. Then, you pass the flow definition's Amazon Resource Name \(ARN\) to the Amazon Rekognition `DetectModerationLabel` operation\. In the `DetectModerationLabel` response, you can see if human review is required\. The results of human review are available in an Amazon S3 bucket that is set by the flow definition\.

**Running DetectModerationLabels with Amazon A2I**
**Note**  
Create all of your Amazon A2I resources and Amazon Rekognition resources in the same region\.

1. Complete the prerequisites that are listed in [Getting Started with Amazon Augmented AI](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-getting-started.html) in the *SageMaker Documentation*\.

   Additionally, remember to set up your IAM permissions as in the page [ Permissions and Security in Amazon Augmented AI](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-permissions-security.html) in the *SageMaker Documentation*\.

1. Follow the instructions for [Creating a Human Review Workflow](https://docs.aws.amazon.com/sagemaker/latest/dg/create-human-review-console.html) in the *SageMaker Documentation*\.

   A human review workflow manages the processing of an image\. It holds the conditions that trigger a human review, the work team that the image is sent to, the UI template that the work team uses, and the Amazon S3 bucket that the work team's results are sent to\.

   Within your `CreateFlowDefinition` call, you need to set the `HumanLoopRequestSource` to "AWS/Rekognition/DetectModerationLabels/Image/V3"\. After that, you need to decide how you want to set up your conditions that trigger human review\.

   With Amazon Textract you have two options for `ConditionType`: `ModerationLabelConfidenceCheck`, and `Sampling`\.

   `ModerationLabelConfidenceCheck` creates a human loop when confidence of a moderation label is within a range\. Finally, `Sampling` sends a random percent of the documents processed for human review\. Each `ConditionType` uses a different set of `ConditionParameters` to set what results in human review\.

   `ModerationLabelCondifenceCheck` has the `ConditionParameters` `ModerationLableName` which sets the key that needs to be reviewed by humans\. Additionally, it has confidence, which set the percentage range for sending to human review with LessThan, GreaterThan, and Equals\. `Sampling` has `RandomSamplingPercentage` which sets a percent of documents that will be sent to human review\.

   The following code example is a partial call of `CreateFlowDefinition`\. It sends an image for human review if it's rated less than 98% on the label "Suggestive", and more than 95% on the label "Female Swimwear or Underwear"\. This means that if the image isn't considered suggestive but does have a woman in underwear or swimwear, you can double check the image by using human review\.

   ```
       def create_flow_definition():
       '''
       Creates a Flow Definition resource
   
       Returns:
       struct: FlowDefinitionArn
       '''
       humanLoopActivationConditions = json.dumps(
           {
               "Conditions": [
                   {
                     "And": [
                       {
                           "ConditionType": "ModerationLabelConfidenceCheck",
                           "ConditionParameters": {
                               "ModerationLabelName": "Suggestive",
                               "ConfidenceLessThan": 98
                           }
                       },
                       {
                           "ConditionType": "ModerationLabelConfidenceCheck",
                           "ConditionParameters": {
                               "ModerationLabelName": "Female Swimwear Or Underwear",
                               "ConfidenceGreaterThan": 95
                           }
                       }
                     ]
                  }
               ]
           }
       )
   ```

   `CreateFlowDefinition` returns a `FlowDefinitionArn`, which you use in the next step when you call `DetectModerationLabels`\.

   For more information see [CreateFlowDefinition](https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateFlowDefinition.html) in the * SageMaker API Reference*\.

1. Set the `HumanLoopConfig` parameter when you call `DetectModerationLabels`, as in [Detecting inappropriate images](procedure-moderate-images.md)\. 

   1. Within the `HumanLoopConfig` parameter, set the `FlowDefinitionArn` to the ARN of the flow definition that you created in step 2\.

   1. Set your `HumanLoopName`\. This should be unique within a Region and must be lowercase\.

   1. \(Optional\) You can use `DataAttributes` to set whether or not the image you passed to Amazon Rekognition is free of personally identifiable information\. You must set this parameter in order to send information to Amazon Mechanical Turk\.

   The following is an example of what a call to `DetectModerationLabels` looks like with the `HumanLoopConfig` set in Python\.

   ```
            client.detect_moderation_labels(Image={'S3Object':{'Bucket':Bucket,'Name':photo}},
            HumanLoopConfig={'FlowDefinitionArn':string,'HumanLoopName':string})
   ```

1. Run `DetectModerationLabels`\.

   When you run `DetectModerationLabels` with `HumanLoopConfig` enabled, Amazon Rekognition calls the SageMaker API operation `StartHumanLoop`\. This command takes the response from `DetectModerationLabels` and checks it against the flow definition's conditions in the example\. If it meets the conditions for review, it returns a `HumanLoopArn`\. This means that the members of the work team that you set in your flow definiton now can review the image\. Calling the Amazon Augmented AI runtime operation `DescribeHumanLoop` provides information about the outcome of the loop\. For more information, see [ DescribeHumanLoop](https://docs.aws.amazon.com/augmented-ai/2019-11-07/APIReference/API_DescribeHumanLoop.html) in the *Amazon Augmented AI API Reference documentation*\.

   After the image has been reviewed, you can see the results in the bucket that is specified in your flow definition's output path\. Amazon A2I will also notify you with Amazon CloudWatch Events when the review is complete\. To see what events to look for, see [CloudWatch Events](https://docs.aws.amazon.com/sagemaker/latest/dg/augmented-ai-cloudwatch-events.html) in the *SageMaker Documentation*\.

   For more information, see [Getting Started with Amazon Augmented AI](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-getting-started.html) in the *SageMaker Documentation*\.