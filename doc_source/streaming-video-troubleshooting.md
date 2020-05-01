# Troubleshooting Streaming Video<a name="streaming-video-troubleshooting"></a>

This topic provides troubleshooting information for using Amazon Rekognition Video with streaming videos\.

**Topics**
+ [I don't know if my stream processor was successfully created](#ts-streaming-video-create-sp)
+ [I don't know if I've configured my stream processor correctly](#ts-configured-sp)
+ [My stream processor isn't returning results](#ts-streaming-video-no-results-from-sp)
+ [The state of my stream processor is FAILED](#ts-failed-state)
+ [My stream processor isn't returning the expected results](#w22aac18c13c33c15)

## I don't know if my stream processor was successfully created<a name="ts-streaming-video-create-sp"></a>

Use the following AWS CLI command to get a list of stream processors and their current status\.

```
aws rekognition list-stream-processors
```

You can get additional details by using the following AWS CLI command\. Replace `stream-processor-name` with the name of the required stream processor\.

```
aws rekognition describe-stream-processor --name stream-processor-name
```

## I don't know if I've configured my stream processor correctly<a name="ts-configured-sp"></a>

If your code isn't outputting the analysis results from Amazon Rekognition Video, your stream processor might not be configured correctly\. Do the following to confirm that your stream processor is configured correctly and able to produce results\.

**To determine if your solution is configured correctly**

1. Run the following command to confirm that your stream processor is in the running state\. Change `stream-processor-name` to the name of your stream processor\. The stream processor is running if the value of `Status` is `RUNNING`\. If the status is `RUNNING` and you aren't getting results, see [My stream processor isn't returning results](#ts-streaming-video-no-results-from-sp)\. If the status is `FAILED`, see [The state of my stream processor is FAILED](#ts-failed-state)\.

   ```
   aws rekognition describe-stream-processor --name stream-processor-name
   ```

1. If your stream processor is running, run the following Bash or PowerShell command to read data from the output Kinesis data stream\. 

   **Bash**

   ```
   SHARD_ITERATOR=$(aws kinesis get-shard-iterator --shard-id shardId-000000000000 --shard-iterator-type TRIM_HORIZON --stream-name kinesis-data-stream-name --query 'ShardIterator')
                           aws kinesis get-records --shard-iterator $SHARD_ITERATOR
   ```

   **PowerShell**

   ```
   aws kinesis get-records --shard-iterator ((aws kinesis get-shard-iterator --shard-id shardId-000000000000 --shard-iterator-type TRIM_HORIZON --stream-name kinesis-data-stream-name).split('"')[4])
   ```

1. Use the [Decode tool](https://www.base64decode.org/) on the Base64 Decode website to decode the output into a human\-readable string\. For more information, see [Step 3: Get the Record](https://docs.aws.amazon.com/streams/latest/dev/fundamental-stream.html#get-records)\.

1. If the commands work and you see face detection results in the Kinesis data stream, then your solution is properly configured\. If the command fails, check the other troubleshooting suggestions and see [Giving Amazon Rekognition Video Access to Your Kinesis Streams](api-streaming-video-roles.md)\.

Alternatively, you can use the "kinesis\-process\-record" AWS Lambda blueprint to log messages from the Kinesis data stream to CloudWatch for continuous visualization\. This incurs additional costs for AWS Lambda and CloudWatch\. 

## My stream processor isn't returning results<a name="ts-streaming-video-no-results-from-sp"></a>

Your stream processor might not return results for several reasons\. 

### Reason 1: Your stream processor isn't configured correctly<a name="w22aac18c13c33c11b5"></a>

Your stream processor might not be configured correctly\. For more information, see [I don't know if I've configured my stream processor correctly](#ts-configured-sp)\.

### Reason 2: Your stream processor isn't in the RUNNING state<a name="w22aac18c13c33c11b7"></a>

**To troubleshoot the status of a stream processor**

1. Check the status of the stream processor with the following AWS CLI command\.

   ```
   aws rekognition describe-stream-processor --name stream-processor-name
   ```

1. If the value of `Status` is `STOPPED`, start your stream processor with the following command:

   ```
   aws rekognition start-stream-processor --name stream-processor-name
   ```

1. If the value of `Status` is `FAILED`, see [The state of my stream processor is FAILED](#ts-failed-state)\.

1. If the value of `Status` is `STARTING`, wait for 2 minutes and check the status by repeating step 1\. If the value of Status is still `STARTING`, do the following:

   1. Delete the stream processor with the following command\.

      ```
      aws rekognition delete-stream-processor --name stream-processor-name
      ```

   1. Create a new stream processor with the same configuration\. For more information, see [Working with Streaming Videos](streaming-video.md)\.

   1. If you're still having problems, contact AWS Support\.

1. If the value of `Status` is `RUNNING`, see [Reason 3: There isn't active data in the Kinesis video stream](#ts-no-data)\.

### Reason 3: There isn't active data in the Kinesis video stream<a name="ts-no-data"></a>

**To check if there's active data in the Kinesis video stream**

1. Sign in to the AWS Management Console, and open the Amazon Kinesis Video Streams console at [https://console\.aws\.amazon\.com/kinesisvideo/](https://console.aws.amazon.com/kinesisvideo/)\.

1. Select the Kinesis video stream that's the input for the Amazon Rekognition stream processor\.

1. If the preview states **No data on stream**, then there's no data in the input stream for Amazon Rekognition Video to process\.

For information about producing video with Kinesis Video Streams, see [Kinesis Video Streams Producer Libraries](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk.html)\. 

## The state of my stream processor is FAILED<a name="ts-failed-state"></a>

You can check the state of a stream processor by using the following AWS CLI command\.

```
aws rekognition describe-stream-processor --name stream-processor-name
```

If the value of Status is FAILED, check the troubleshooting information for the following error messages\.

### Error: "Access denied to Role"<a name="w22aac18c13c33c13b9"></a>

The IAM role that's used by the stream processor doesn't exist or Amazon Rekognition Video doesn't have permission to assume the role\.

**To troubleshoot access to the IAM role**

1. Sign in to the AWS Management Console and open the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

1. From the left navigation pane, choose **Roles**and confirm that the role exists\. 

1. If the role exists, check that the role has the *AmazonRekognitionServiceRole* permissions policy\.

1. If the role doesn't exist or doesn't have the right permissions, see [Giving Amazon Rekognition Video Access to Your Kinesis Streams](api-streaming-video-roles.md)\.

1. Start the stream processor with the following AWS CLI command\.

   ```
   aws rekognition start-stream-processor --name stream-processor-name
   ```

### Error: "Access denied to Kinesis Video *or* Access denied to Kinesis Data"<a name="w22aac18c13c33c13c11"></a>

The role doesn't have access to the Kinesis Video Streams API operations `GetMedia` and `GetDataEndpoint`\. It also might not have access to the Kinesis Data Streams API operations `PutRecord` and `PutRecords`\. 

**To troubleshoot API permissions**

1. Sign in to the AWS Management Console and open the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

1. Open the role and make sure that it has the following permissions policy attached\.

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

1. If any of the permissions are missing, update the policy\. For more information, see [Giving Amazon Rekognition Video Access to Your Kinesis Streams](api-streaming-video-roles.md)\.

### Error: "Stream *input\-video\-stream\-name* doesn't exist"<a name="w22aac18c13c33c13c13"></a>

The Kinesis video stream input to the stream processor doesn't exist or isn't configured correctly\. 

**To troubleshoot the Kinesis video stream**

1. Use the following command to confirm that the stream exists\. 

   ```
   aws kinesisvideo list-streams
   ```

1. If the stream exists, check the following\.
   + The Amazon Resource Name \(ARN\) is same as the ARN of the input stream for the stream processor\.
   + The Kinesis video stream is in the same Region as the stream processor\.

   If the stream processor isn't configured correctly, delete it with the following AWS CLI command\.

   ```
   aws rekognition delete-stream-processor --name stream-processor-name
   ```

1. Create a new stream processor with the intended Kinesis video stream\. For more information, see [Creating the Amazon Rekognition Video Stream Processor](streaming-video-starting-analysis.md#streaming-video-creating-stream-processor)\.

### Error: "Collection not found"<a name="w22aac18c13c33c13c15"></a>

The Amazon Rekognition collection that's used by the stream processor to match faces doesn't exist, or the wrong collection is being used\.

**To confirm the collection**

1. Use the following AWS CLI command to determine if the required collection exists\. Change `region` to the AWS Region in which you're running your stream processor\.

   ```
   aws rekognition list-collections --region region
   ```

   If the required collection doesn't exist, create a new collection and add face information\. For more information, see [](collections.md)\.

1. In your call to [CreateStreamProcessor](API_CreateStreamProcessor.md), check that the value of the `CollectionId` input parameter is correct\.

1. Start the stream processor with the following AWS CLI command\.

   ```
   aws rekognition start-stream-processor --name stream-processor-name
   ```

### Error: "Stream *output\-kinesis\-data\-stream\-name* under account *account\-id* not found"<a name="w22aac18c13c33c13c17"></a>

The output Kinesis data stream that's used by the stream processor doesn't exist in your AWS account or isn't in the same AWS Region as your stream processor\.

**To troubleshoot the Kinesis data stream**

1. Use the following AWS CLI command to determine if the Kinesis data stream exists\. Change `region` to the AWS Region in which you're using your stream processor\.

   ```
   aws kinesis list-streams --region region
   ```

1. If the Kinesis data stream exists, check that the Kinesis data stream name is same as the name of the output stream that's used by the stream processor\.

1. If the Kinesis data stream doesn't exist, it might exist in another AWS Region\. The Kinesis data stream must be in the same Region as the stream processor\.

1. If necessary, create a new Kinesis data stream\. 

   1. Create a Kinesis data stream with the same name as the name used by the stream processor\. For more information, see [ Step 1: Create a Data Stream](https://docs.aws.amazon.com/streams/latest/dev/learning-kinesis-module-one-create-stream.html)\.

   1. Start the stream processor with the following AWS CLI command\.

      ```
      aws rekognition start-stream-processor --name stream-processor-name
      ```

## My stream processor isn't returning the expected results<a name="w22aac18c13c33c15"></a>

If your stream processor isn't returning the expected face matches, use the following information\.
+ [Searching Faces in a Collection](collections.md)
+ [Recommendations for Camera Set\-Up \(Streaming Video\)](recommendations-camera-streaming-video.md)