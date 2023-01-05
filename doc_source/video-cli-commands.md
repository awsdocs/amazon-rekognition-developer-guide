# Analyzing a video with the AWS Command Line Interface<a name="video-cli-commands"></a>

You can use the AWS Command Line Interface \(AWS CLI\) to call Amazon Rekognition Video operations\. The design pattern is the same as using the Amazon Rekognition Video API with the AWS SDK for Java or other AWS SDKs\. For more information, see [Amazon Rekognition Video API overview](video.md#video-api-overview)\. The following procedures show how to use the AWS CLI to detect labels in a video\.

You start detecting labels in a video by calling `start-label-detection`\. When Amazon Rekognition finishes analyzing the video, the completion status is sent to the Amazon SNS topic that's specified in the `--notification-channel` parameter of `start-label-detection`\. You can get the completion status by subscribing an Amazon Simple Queue Service \(Amazon SQS\) queue to the Amazon SNS topic\. You then poll [receive\-message](https://docs.aws.amazon.com/cli/latest/reference/sqs/receive-message.html) to get the completion status from the Amazon SQS queue\.

The completion status notification is a JSON structure within the `receive-message` response\. You need to extract the JSON from the response\. For information about the completion status JSON, see [Reference: Video analysis results notification](video-notification-payload.md)\. If the value of the `Status` field of the completed status JSON is `SUCCEEDED`, you can get the results of the video analysis request by calling `get-label-detection`\.

The following procedures don't include code to poll the Amazon SQS queue\. Also, they don't include code to parse the JSON that's returned from the Amazon SQS queue\. For an example in Java, see [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md)\. 

## Prerequisites<a name="video-prerequisites"></a>

To run this procedure, you need to have the AWS CLI installed\. For more information, see [Getting started with Amazon Rekognition](getting-started.md)\. The AWS account that you use must have access permissions to the Amazon Rekognition API\. For more information, [Actions Defined by Amazon Rekognition](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonrekognition.html#amazonrekognition-actions-as-permissions)\. 

**To configure Amazon Rekognition Video and upload a video**

1. Configure user access to Amazon Rekognition Video and configure Amazon Rekognition Video access to Amazon SNS\. For more information, see [Configuring Amazon Rekognition Video](api-video-roles.md)\.

1. Upload an MOV or MPEG\-4 format video file to your S3 bucket\. While developing and testing, we suggest using short videos no longer than 30 seconds in length\.

   For instructions, see [Uploading Objects into Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service User Guide*\.

**To detect labels in a video**

1. Run the following AWS CLI command to start detecting labels in a video\.

   ```
   aws rekognition start-label-detection --video "S3Object={Bucket=bucketname,Name=videofile}" \
   --notification-channel "SNSTopicArn=TopicARN,RoleArn=RoleARN" \
   --endpoint-url Endpoint \
   --region us-east-1
   --features GENERAL_LABELS
   --settings GeneralLabels={LabelsInclusionFilter=["values"]}
   ```

   Update the following values:
   + Change `bucketname` and `videofile` to the Amazon S3 bucket name and file name that you specified in step 2\.
   + Change `us-east-1` to the AWS region that you're using\.
   + Change `TopicARN` to the ARN of the Amazon SNS topic you created in step 3 of [Configuring Amazon Rekognition Video](api-video-roles.md)\.
   + Change `RoleARN` to the ARN of the IAM service role you created in step 7 of [Configuring Amazon Rekognition Video](api-video-roles.md)\.
   + If required, you can specify the `endpoint-url`\. The AWS CLI should automatically determine the proper endpoint URL based on the provided region\. However, if you are using an endpoint [from your private VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html#what-is-privatelink), you may need to specify the `endpoint-url`\. The [AWS Service Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints) resource lists the syntax for specifying endpoint urls and the names and codes for each region\.
   + You can also include filtration criteria in the settings paramter\. For example, you can use a `LabelsInclusionFilter` or a `LabelsExclusionFilter` alongside a list of desired values\.

1. Note the value of `JobId` in the response\. The response looks similar to the following JSON example\.

   ```
   {
       "JobId": "547089ce5b9a8a0e7831afa655f42e5d7b5c838553f1a584bf350ennnnnnnnnn"
   }
   ```

1. Write code to poll the Amazon SQS queue for the completion status JSON \(by using [receive\-message](https://docs.aws.amazon.com/cli/latest/reference/sqs/receive-message.html)\)\.

1. Write code to extract the `Status` field from the completion status JSON\.

1. If the value of `Status` is `SUCCEEDED`, run the following AWS CLI command to show the label detection results\.

   ```
   aws rekognition get-label-detection  --job-id JobId \
   --region us-east-1
   ```

   Update the following values:
   + Change `JobId` to match the job identifier that you noted in step 2\.
   + Change `Endpoint` and `us-east-1` to the AWS endpoint and region that you're using\.

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