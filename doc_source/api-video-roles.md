# Giving Rekognition Video Access to Your Amazon SNS Topics<a name="api-video-roles"></a>

You use an AWS Identity and Access Management \(IAM\) service role to give Rekognition Video access to Amazon SNS topics that you create\. IAM provides the *Rekognition* use case for creating a Rekognition Video service role\.

## Giving Access to Multiple Amazon SNS Topics<a name="api-video-roles-all-topics"></a>

You can give Rekognition Video access to multiple Amazon SNS topics by using the `AmazonRekognitionServiceRole` permissions policy and prepending the topic names with *AmazonRekognition*—for example, `AmazonRekognitionMyTopicName`\. 

**To give Rekognition Video access to multiple Amazon SNS topics**

1. [Create an IAM service role](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html?icmpid=docs_iam_console)\. Use the following information to create the IAM service role:

   1. Choose **Rekognition** for the service name\.

   1. Choose **Rekognition** for the service role use case\.

   1. Choose the **AmazonRekognitionServiceRole** permissions policy, which gives Rekognition Video access to Amazon SNS topics that are prefixed with *AmazonRekognition*\.

1. Note the ARN of the service role\. You need it to start video analysis operations\.

## Giving Access to an Existing Amazon SNS Topic<a name="api-video-roles-single-topics"></a>

You can create a permissions policy that allows Rekognition Video access to an existing Amazon SNS topic\.

**To give Rekognition Video access to an existing Amazon SNS topic**

1. [ Create a new permissions policy with the IAM JSON policy editor](http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor), and use the following policy\. Replace `topicarn` with the Amazon Resource Name \(ARN\) of the desired Amazon SNS topic\.

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

1. [Create an IAM service role](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html?icmpid=docs_iam_console), or update an existing IAM service role\. Use the following information to create the IAM service role:

   1. Choose **Rekognition** for the service name\.

   1. Choose **Rekognition** for the service role use case\.

   1. Attach the permissions policy you created in step 1\.

1. Note the ARN of the service role\. You need it to start video analysis operations\.