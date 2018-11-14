# Analyzing a Video with the AWS Command Line Interface<a name="video-cli-commands"></a>

You can use the AWS Command Line Interface \(AWS CLI\) to call Amazon Rekognition Video operations\. The design pattern is the same as using the Amazon Rekognition Video API with the AWS SDK for Java or other AWS SDKs\. For more information, see [Amazon Rekognition Video API Overview](video.md#video-api-overview)\. The following procedures show how to use the AWS CLI to detect labels in a video\.

You start detecting labels in a video by calling `start-label-detection`\. When Amazon Rekognition finishes analyzing the video, the completion status is sent to the Amazon SNS topic that's specified in the `--notification-channel` parameter of `start-label-detection`\. You can get the completion status by subscribing an Amazon Simple Queue Service \(Amazon SQS\) queue to the Amazon SNS topic\. You then poll [receive\-message](http://docs.aws.amazon.com/cli/latest/reference/sqs/receive-message.html) to get the completion status from the Amazon SQS queue\.

The completion status notification is a JSON structure within the `receive-message` response\. You need to extract the JSON from the response\. For information about the completion status JSON, see [Reference: Video Analysis Results Notification](video-notification-payload.md)\. If the value of the `Status` field of the completed status JSON is `SUCCEEDED`, you can get the results of the video analysis request by calling `get-label-detection`\.

The following procedures don't include code to poll the Amazon SQS queue\. Also, they don't include code to parse the JSON that's returned from the Amazon SQS queue\. For an example in Java, see [Analyzing a Video Stored in an Amazon S3 Bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md)\. 

## Prerequisites<a name="video-prerequisites"></a>

To run this procedure, you need to have the AWS CLI installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account that you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. 

**To configure Amazon Rekognition Video and upload a video**

1. Configure user access to Amazon Rekognition Video and configure Amazon Rekognition Video access to Amazon SNS\. For more information, see [Configuring Amazon Rekognition Video](api-video-roles.md)\.

1. [Create an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) by using the [Amazon SNS console](https://console.aws.amazon.com/sns/v2/home)\. Prepend the topic name with *AmazonRekognition*\. Note the topic Amazon Resource Name \(ARN\)\. 

1. [Create an Amazon SQS standard queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-create-queue.html) by using the [Amazon SQS console](https://console.aws.amazon.com/sqs/)\. Note the queue ARN\.

1. [Subscribe the queue to the topic](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-subscribe-queue-sns-topic.html) you created in step 2\.

1. [Give permission to the Amazon SNS topic to send messages to the Amazon SQS queue](https://docs.aws.amazon.com/sns/latest/dg/SendMessageToSQS.html#SendMessageToSQS.sqs.permissions)\.

1. Upload an \.mp4, \.mov or \.avi format video file to your S3 bucket\. While developing and testing, we suggest using short videos no longer than 30 seconds in length\.

   For instructions, see [Uploading Objects into Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

**To detect labels in a video**

1. Run the following AWS CLI command to start detecting labels in a video\.

   ```
   aws rekognition start-label-detection --video "S3Object={Bucket="bucketname",Name="videofile"}" \
   --notification-channel "SNSTopicArn=TopicARN,RoleArn=RoleARN" \
   --region us-east-1 \
   --profile RekognitionUser
   ```

   Update the following values:
   + Change `bucketname` and `videofile` to the Amazon S3 bucket name and file name that you specified in step 6\.
   + Change `TopicARN` to the ARN of the Amazon SNS topic you created in step 2 of the previous procedure\.
   + Change `RoleARN` to the ARN of the IAM role you created in step 1 of the previous procedure\.
   + Change `us-east-1` to the AWS region that you're using.
   + Change `RekognitionUser` to an AWS account that has permissions to call Amazon Rekognition Video operations\.

1. Note the value of `JobId` in the response\. The response looks similar to the following JSON example\.

   ```
   {
       "JobId": "547089ce5b9a8a0e7831afa655f42e5d7b5c838553f1a584bf350ennnnnnnnnn"
   }
   ```

1. Write code to poll the Amazon SQS queue for the completion status JSON \(by using [receive\-message](http://docs.aws.amazon.com/cli/latest/reference/sqs/receive-message.html)\)\.

1. Write code to extract the `Status` field from the completion status JSON\.

1. If the value of `Status` is `SUCCESS`, run the following AWS CLI command to show the label detection results\.

   ```
   aws rekognition get-label-detection  --job-id JobId \
   --region us-east-1 \
   --profile RekognitionUser
   ```

   Update the following values:
   + Change `JobId` to match the job identifier that you noted in step 2\.
   + Change `us-east-1` to the AWS region that you're using\.
   + Change `RekognitionUser` to an AWS account that has permissions to call Amazon Rekognition Video operations\.

   The results look similar to the following example JSON:

   ```
   {
       "Labels": [
           {
               "Timestamp": 0,
               "Label": {
                   "Confidence": 99.03720092773438,
                   "Name": "Speech"
               }
           },
           {
               "Timestamp": 0,
               "Label": {
                   "Confidence": 71.6698989868164,
                   "Name": "Pumpkin"
               }
           },
           {
               "Timestamp": 0,
               "Label": {
                   "Confidence": 71.6698989868164,
                   "Name": "Squash"
               }
           },
           {
               "Timestamp": 0,
               "Label": {
                   "Confidence": 71.6698989868164,
                   "Name": "Vegetable"
               }
           }, .......
   ```
