# Configuring Amazon Rekognition Video<a name="api-video-roles"></a>

To use the Amazon Rekognition Video API with stored videos, you have to configure the IAM user and an IAM service role to access your Amazon SNS topics\. You also have to subscribe an Amazon SQS queue to your Amazon SNS topics\. 

**Note**  
If you're using these instructions to set up the [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md) example, you don't need to do steps 3, 4, 5, and 6\. The example includes code to create and configure the Amazon SNS topic and Amazon SQS queue\.

The examples in this section create a new Amazon SNS topic by using the instructions that give Amazon Rekognition Video access to multiple topics\. If you want to use an existing Amazon SNS topic, use [Giving access to an existing Amazon SNS topic](#api-video-roles-single-topics) for step 3\.<a name="configure-rekvid-procedure"></a>

**To configure Amazon Rekognition Video**

1. Set up an AWS account to access Amazon Rekognition Video\. For more information, see [Step 1: Set up an AWS account and create an IAM user](setting-up.md)\.

   Ensure the user has at least the following permissions:
   + AmazonSQSFullAccess
   + AmazonRekognitionFullAccess
   + AmazonS3FullAccess
   + AmazonSNSFullAccess

1. Install and configure the required AWS SDK\. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\. 

1. [Create an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) by using the [Amazon SNS console](https://console.aws.amazon.com/sns/v2/home)\. Prepend the topic name with *AmazonRekognition*\. Note the topic Amazon Resource Name \(ARN\)\. Ensure the topic is in the same region as the AWS endpoint that you are using\.

1. [Create an Amazon SQS standard queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-create-queue.html) by using the [Amazon SQS console](https://console.aws.amazon.com/sqs/)\. Note the queue ARN\.

1. [Subscribe the queue to the topic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-subscribe-queue-sns-topic.html) you created in step 3\.

1. [Give permission to the Amazon SNS topic to send messages to the Amazon SQS queue](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToSQS.html#SendMessageToSQS.sqs.permissions)\.

1. Create an IAM service role to give Amazon Rekognition Video access to your Amazon SNS topics\. Note the Amazon Resource Name \(ARN\) of the service role\. For more information, see [Giving access to multiple Amazon SNS topics](#api-video-roles-all-topics)\.

1. To ensure your account is secure, you will want to limit the scope of Rekognition's access to just the resources you are using\. This can be done by attaching a Trust policy to your IAM service role\. For information on how to do this, see [Cross\-service confused deputy prevention](cross-service-confused-deputy-prevention.md)\.

1. [ Add the following inline policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#embed-inline-policy-console) to the IAM user that you created in step 1: 

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "MySid",
               "Effect": "Allow",
               "Action": "iam:PassRole",
               "Resource": "arn:Service role ARN from step 7"
           }
       ]
   }
   ```

   Give the inline policy a name of your choosing\.

1. If you use a customer managed AWS Key Management Service key to encrypt the videos in your Amazon S3 bucket, [add](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html#key-policy-modifying-how-to-console-policy-view) permissions to the key that allow the service role you created in step 7 to decrypt the videos\. At a minimum the service role needs permission for `kms:GenerateDataKey` and `kms:Decrypt` actions\. For example:

   ```
   {
       "Sid": "Decrypt only",
       "Effect": "Allow",
       "Principal": {
           "AWS": "arn:aws:iam::111122223333:user/user from step 1"
       },
       "Action": [
           "kms:Decrypt",
           "kms:GenerateDataKey"
       ],
       "Resource": "*"
   }
   ```

   For more information, see see [My Amazon S3 bucket has default encryption using a custom AWS KMS key\. How can I allow users to download from and upload to the bucket?](https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-access-default-encryption/) and [Protecting Data Using Server\-Side Encryption with KMS keys Stored in AWS Key Management Service \(SSE\-KMS\)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html)\. 

1. You can now run the examples in [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md) and [Analyzing a video with the AWS Command Line Interface](video-cli-commands.md)\.

## Giving access to multiple Amazon SNS topics<a name="api-video-roles-all-topics"></a>

You use an IAM service role to give Amazon Rekognition Video access to Amazon SNS topics that you create\. IAM provides the *Rekognition* use case for creating an Amazon Rekognition Video service role\.

You can give Amazon Rekognition Video access to multiple Amazon SNS topics by using the `AmazonRekognitionServiceRole` permissions policy and prepending the topic names with *AmazonRekognition*—for example, `AmazonRekognitionMyTopicName`\. 

**To give Amazon Rekognition Video access to multiple Amazon SNS topics**

1. [Create an IAM service role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html?icmpid=docs_iam_console)\. Use the following information to create the IAM service role:

   1. Choose **Rekognition** for the service name\.

   1. Choose **Rekognition** for the service role use case\. You should see the **AmazonRekognitionServiceRole** permissions policy listed\. **AmazonRekognitionServiceRole** gives Amazon Rekognition Video access to Amazon SNS topics that are prefixed with *AmazonRekognition*\.

   1. Give the service role a name of your choosing\.

1. Note the ARN of the service role\. You need it to start video analysis operations\.

## Giving access to an existing Amazon SNS topic<a name="api-video-roles-single-topics"></a>

You can create a permissions policy that allows Amazon Rekognition Video access to an existing Amazon SNS topic\.

**To give Amazon Rekognition Video access to an existing Amazon SNS topic**

1. [ Create a new permissions policy with the IAM JSON policy editor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor), and use the following policy\. Replace `topicarn` with the Amazon Resource Name \(ARN\) of the desired Amazon SNS topic\.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "sns:Publish"
               ],
               "Resource": "topicarn"
           }
       ]
   }
   ```

1. [Create an IAM service role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html?icmpid=docs_iam_console), or update an existing IAM service role\. Use the following information to create the IAM service role:

   1. Choose **Rekognition** for the service name\.

   1. Choose **Rekognition** for the service role use case\.

   1. Attach the permissions policy you created in step 1\.

1. Note the ARN of the service role\. You need it to start video analysis operations\.