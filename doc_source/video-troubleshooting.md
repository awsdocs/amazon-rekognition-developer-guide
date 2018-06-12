# Troubleshooting Amazon Rekognition Video<a name="video-troubleshooting"></a>

The following covers troubleshooting information for working with Amazon Rekognition Video and stored videos\.

## I never receive the completion status that's sent to the Amazon SNS topic<a name="video-no-sns-topic"></a>

 Amazon Rekognition Video publishes status information to an Amazon SNS topic when video analysis completes\. Typically, you get the completion status message by subscribing to the topic with an Amazon SQS queue or Lambda function\. To help your investigation, subscribe to the Amazon SNS topic by email so you receive the messages that are sent to your Amazon SNS topic in your email inbox\. For more information, see [Subscribe to a Topic](http://docs.aws.amazon.com/sns/latest/dg/SubscribeTopic.html)\.

If you don't receive the message in your application, consider the following:
+ Verify that the analysis has completed\. Check the `JobStatus` value in the Get operation response \(`GetLabelDetection`, for example\)\. If the value is `IN_PROGRESS`, the analysis isn't complete, and the completion status hasn't yet been published to the Amazon SNS topic\.
+ Verify that you have an IAM service role that gives Amazon Rekognition Video permissions to publish to your Amazon SNS topics\. For more information, see [Configuring Amazon Rekognition Video](api-video-roles.md)\. 
+ Confirm that the IAM service role that you're using can publish to the Amazon SNS topic by using role credentials\. Use the following steps:
  + Get the user Amazon Resource Name \(ARN\):

    ```
    aws sts get-caller-identity --profile RekognitionUser 
    ```
  + Add the user ARN to the role trust relationship by using the [AWS Management Console](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html)\. For example:

    ```
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Service": "rekognition.amazonaws.com",
            "AWS": "arn:User ARN"
          },
          "Action": "sts:AssumeRole",
          "Condition": {}
        }
      ]
    }
    ```
  + Assume the role: `aws sts assume-role --role-arn arn:Role ARN --role-session-name SessionName --profile RekognitionUser`
  + Publish to the Amazon SNS topic: `aws sns publish --topic-arn arn:Topic ARN --message "Hello World!" --region us-east-1 --profile RekognitionUser`

  If the AWS CLI command works, you receive the message \(in your email inbox, if you've subscribed to the topic by email\)\. If you don't receive the message:
  + Check that you've configured Amazon Rekognition Video\. For more information, see [Configuring Amazon Rekognition Video](api-video-roles.md)\.
  + Check the other tips for this troubleshooting question\.
+ Check that you're using the correct Amazon SNS topic:
  + If you use an IAM service role to give Amazon Rekognition Video access to a single Amazon SNS topic, check that you've given permissions to the correct Amazon SNS topic\. For more information, see [Giving Access to an Existing Amazon SNS Topic](api-video-roles.md#api-video-roles-single-topics)\.
  + If you use an IAM service role to give Amazon Rekognition Video access to multiple SNS topics, verify that you're using the correct topic and that the topic name is prepended with *AmazonRekognition*\. For more information, see [Giving Access to Multiple Amazon SNS Topics](api-video-roles.md#api-video-roles-all-topics)\. 
  + If you use an AWS Lambda function, confirm that your Lambda function is subscribed to the correct Amazon SNS topic\. For more information, see [ Invoking Lambda Functions Using Amazon SNS Notifications](http://docs.aws.amazon.com/sns/latest/dg/sns-lambda.html)\.
+ If you subscribe an Amazon SQS queue to your Amazon SNS topic, confirm that your Amazon SNS topic has permissions to send messages to the Amazon SQS queue\. For more information, see [Give permission to the Amazon SNS topic to send messages to the Amazon SQS queue](http://docs.aws.amazon.com/sns/latest/dg/SendMessageToSQS.html#SendMessageToSQS.sqs.permissions)\.