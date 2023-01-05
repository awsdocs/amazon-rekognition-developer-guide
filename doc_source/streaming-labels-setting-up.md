# Setting up your Amazon Rekognition Video and Amazon Kinesis resources<a name="streaming-labels-setting-up"></a>

 The following procedures describe the steps that you take to provision the Kinesis video stream and other resources that are used to detect labels in a streaming video\.

## Prerequisites<a name="streaming-video-prerequisites"></a>

To run this procedure, AWS SDK for Java must be installed\. For more information, see [Getting started with Amazon Rekognition](getting-started.md)\. The AWS account that you use requires access permissions to the Amazon Rekognition API\. For more information, see [Actions Defined by Amazon Rekognition](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonrekognition.html#amazonrekognition-actions-as-permissions) in the *IAM User Guide*\. 

**To detect labels in a video stream \(AWS SDK\)**

1. Create an Amazon S3 bucket\. Note the bucket name and any key prefixes that you want to use\. You use this information later\.

1. Create an Amazon SNS topic\. You can use it to receive notifications when an object of interest is first detected in the video stream\. Note the Amazon Resource Name \(ARN\) for the topic\. For more information, see [Creating an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html) in the Amazon SNS developer guide\.

1. Subscribe an endpoint to the Amazon SNS topic\. For more information, see [Subscribing to an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html) in the Amazon SNS developer guide\.

1. [Create a Kinesis video stream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-createstream.html) and note the Amazon Resource Name \(ARN\) of the stream\.

1. If you didn't already, create an IAM service role to give Amazon Rekognition Video access to your Kinesis video streams, your S3 bucket, and your Amazon SNS topic\. For more information, see [Giving access for label detection stream processors](#streaming-labels-giving-access)\.

You can then [create the label detection stream processor](streaming-labels-detection.md#streaming-video-create-labels-stream-processor) and [start the stream processor](streaming-labels-detection.md#streaming-video-start-labels-stream-processor) using the stream processor name that you chose\.

**Note**  
Start the stream processor only after you verified that you can ingest media into the Kinesis video stream\. 

## Camera orientation and setup<a name="streaming-labels-camera-setup"></a>

Amazon Rekognition Video Streaming Video Events can support all cameras that are supported by Kinesis Video Streams\. For best results, we recommend placing the camera between 0 to 45 degrees from the ground\. The camera needs to be in its canonical upright position\. For example, if there is a person in the frame, the person should be oriented vertically, and the head of the person should be higher in the frame than the feet\.

## Giving access for label detection stream processors<a name="streaming-labels-giving-access"></a>

You use an AWS Identity and Access Management \(IAM\) service role to give Amazon Rekognition Video read access to Kinesis video streams\. To do this, use IAM roles to give Amazon Rekognition Video access to your Amazon S3 bucket and to an Amazon SNS topic\.

You can create a permissions policy that allows Amazon Rekognition Video access to an existing Amazon SNS topic, Amazon S3 bucket, and Kinesis video stream\. For a step\-by\-step procedure using the AWS CLI, see [AWS CLI commands to set up a label detection IAM role](#streaming-labels-giving-access-cli)\. 

**To give Amazon Rekognition Video access to resources for label detection**

1. [ Create a new permissions policy with the IAM JSON policy editor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor), and use the following policy\. Replace `kvs-stream-name` with the name of the Kinesis video stream, `topicarn` with the Amazon Resource Name \(ARN\) of the Amazon SNS topic that you want to use, and `bucket-name` with the name of the Amazon S3 bucket\.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "KinesisVideoPermissions",
               "Effect": "Allow",
               "Action": [
                   "kinesisvideo:GetDataEndpoint",
                   "kinesisvideo:GetMedia"
               ],
               "Resource": [
                   "arn:aws:kinesisvideo:::stream/kvs-stream-name/*"
               ]
           },
           {
               "Sid": "SNSPermissions",
               "Effect": "Allow",
               "Action": [
                   "sns:Publish"
               ],
               "Resource": [
                   "arn:aws:sns:::sns-topic-name"
               ]
           },
           {
               "Sid": "S3Permissions",
               "Effect": "Allow",
               "Action": [
                   "s3:PutObject"
               ],
               "Resource": [
                   "arn:aws:s3:::bucket-name/*"
               ]
           }
       ]
   }
   ```

1. [Create an IAM service role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html?icmpid=docs_iam_console), or update an existing IAM service role\. Use the following information to create the IAM service role:

   1. Choose **Rekognition** for the service name\.

   1. Choose **Rekognition** for the service role use case\.

   1. Attach the permissions policy that you created in step 1\.

1. Note the ARN of the service role\. You need it to create the stream processor before you perform video analysis operations\.

1. \(Optional\) If you use your own AWS KMS key to encrypt data sent to your S3 bucket, you must add the following statement with the IAM role\. \(This is the IAM role that you created for the key policy, which corresponds to the customer managed key that you want to use\.\)

   ```
       
               {
                          "Sid": "Allow use of the key by label detection Role",
                          "Effect": "Allow",
                          "Principal": {
                              "AWS": "arn:aws:iam:::role/REPLACE_WITH_LABEL_DETECTION_ROLE_CREATED"
                          },
                          "Action": [
                              "kms:Decrypt",
                              "kms:GenerateDataKey*"
                          ],
                          "Resource": "*"
               }
   ```

## AWS CLI commands to set up a label detection IAM role<a name="streaming-labels-giving-access-cli"></a>

If you didn't already, set up and configure the AWS CLI with your credentials\.

Enter the following commands into the AWS CLI to set up an IAM role with the necessary permissions for label detection\.

1. `export IAM_ROLE_NAME=labels-test-role`

1. `export AWS_REGION=us-east-1`

1. Create a trust relationship policy file \(for example, assume\-role\-rekognition\.json\) with the following content\.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "",
         "Effect": "Allow",
         "Principal": {
           "Service": "rekognition.amazonaws.com"
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   ```

1. `aws iam create-role --role-name $IAM_ROLE_NAME --assume-role-policy-document file://path-to-assume-role-rekognition.json --region $AWS_REGION`

1. `aws iam attach-role-policy --role-name $IAM_ROLE_NAME --policy-arn "arn:aws:iam::aws:policy/service-role/AmazonRekognitionServiceRole" --region $AWS_REGION`

1. If the name of your SNS topic that you want to receive notifications with doesn't start with the "AmazonRekognition" prefix, add the following policy:

   `aws iam attach-role-policy --role-name $IAM_ROLE_NAME --policy-arn "arn:aws:iam::aws:policy/AmazonSNSFullAccess" --region $AWS_REGION`

1. If you use your own AWS KMS key to encrypt data sent to your Amazon S3 bucket, update the key policy of the customer managed key that you want to use\.

   1. Create a file kms\_key\_policy\.json that contains the following content:

      ```
      {
      "Sid": "Allow use of the key by label detection Role",
      "Effect": "Allow",
      "Principal": {
      "AWS": "arn:aws:iam:::role/REPLACE_WITH_IAM_ROLE_NAME_CREATED"
      },
      "Action": [
      "kms:Encrypt",
      "kms:GenerateDataKey*"
      ],
      "Resource": "*"
      }
      ```

   1. `export KMS_KEY_ID=labels-kms-key-id`\. Replace KMS\_KEY\_ID with the KMS key ID that you created\.

   1. `aws kms put-key-policy --policy-name default --key-id $KMS_KEY_ID --policy file://path-to-kms-key-policy.json`