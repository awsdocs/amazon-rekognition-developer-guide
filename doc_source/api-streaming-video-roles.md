# Giving Amazon Rekognition Video Access to Your Kinesis Streams<a name="api-streaming-video-roles"></a>

You use an AWS Identity and Access Management \(IAM\) service role to give Amazon Rekognition Video read access to Kinesis video streams and write access to Kinesis data streams\. 

## Giving Access to Your Kinesis Video Streams and Kinesis Data Streams<a name="api-streaming-video-roles-all-stream"></a>

 IAM provides the *Rekognition* service role use case that, when used with the `AmazonRekognitionServiceRole` permissions policy, can write to multiple Kinesis data streams and read from all your Kinesis video streams\. To give Amazon Rekognition Video write access to multiple Kinesis data streams, you can prepend the names of the Kinesis data streams with *AmazonRekognition*—for example, `AmazonRekognitionMyDataStreamName`\. 

**To give Amazon Rekognition Video access to your Kinesis video stream and Kinesis data stream**

1. [Create an IAM service role](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html?icmpid=docs_iam_console)\. Use the following information to create the IAM service role:

   1. Choose **Rekognition** for the service name\.

   1. Choose **Rekognition** for the service role use case\.

   1. Choose the **AmazonRekognitionServiceRole** permissions policy, which gives Amazon Rekognition Video write access to Kinesis data streams that are prefixed with *AmazonRekognition* and read access to all your Kinesis video streams\.

1. Note the Amazon Resource Name \(ARN\) of the service role\. You need it to start video analysis operations\.

## Giving Access to Individual Kinesis Streams<a name="api-streaming-video-roles-single-stream"></a>

You can create a permissions policy that allows Amazon Rekognition Video access to individual Kinesis video streams and Kinesis data streams\.

**To give Amazon Rekognition Video access to an individual Kinesis video stream and Kinesis data stream**

1. [ Create a new permissions policy with the IAM JSON policy editor](http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor), and use the following policy\. Replace `data-arn` with the ARN of the desired Kinesis data stream and `video-arn` with the ARN of the desired Kinesis video stream\.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "kinesis:PutRecord",
                   "kinesis:PutRecords"
               ],
               "Resource": "data-arn"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "kinesisvideo:GetDataEndpoint",
                   "kinesisvideo:GetMedia"
               ],
               "Resource": "video-arn"
           }
       ]
   }
   ```

1. [Create an IAM service role](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html?icmpid=docs_iam_console), or update an existing IAM service role\. Use the following information to create the IAM service role:

   1. Choose **Rekognition** for the service name\.

   1. Choose **Rekognition** for the service role use case\.

   1. Attach the permissions policy that you created in step 1\.

1. Note the ARN of the service role\. You need it to start video analysis operations\.