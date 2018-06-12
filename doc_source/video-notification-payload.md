# Reference: Video Analysis Results Notification<a name="video-notification-payload"></a>

Amazon Rekognition publishes the results of a Amazon Rekognition Video analysis request, including completion status, to an Amazon Simple Notification Service \(Amazon SNS\) topic\. To get the notification from an Amazon SNS topic, use an Amazon Simple Queue Service queue or an AWS Lambda function\. For more information, see [Calling Amazon Rekognition Video Operations](api-video.md)\. For an example, see [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md)\.

The payload is in the following JSON format:

```
{
  "JobId": "String",
  "Status": "String",
  "API": "String",
  "JobTag": "String",
  "Timestamp": Number,
  "Video": {
    "S3ObjectName": "Sting",
    "S3Bucket": "String"
  }
}
```


| Name | Description | 
| --- | --- | 
|  JobId  |  The job identifier\. Matches a job identifier that's returned from a `Start` operation, such as [StartPersonTracking](API_StartPersonTracking.md)\.  | 
|  Status  |  The status of the job\. Valid values are SUCCEEDED, FAILED, or ERROR\.  | 
|  API  |  The Amazon Rekognition Video operation used to analyze the input video\.  | 
|  JobTag  |  Identifier for the job\. You specify `JobTag` in a call to Start operation, such as [StartLabelDetection](API_StartLabelDetection.md)\.  | 
|  Timestamp  |  The Unix time stamp for when the job finished\.  | 
|  Video  |  Details about the video that was processed\. Includes the file name and the Amazon S3 bucket that the file is stored in\.  | 

The following is an example of a successful notification that was sent to an Amazon SNS topic\.

```
{
  "JobId": "6de014b0-2121-4bf0-9e31-856a18719e22",
  "Status": "SUCCEEDED",
  "JobType": "LABEL_DETECTION",
  "Message": "",
  "Timestamp": 1502230160926,
  "Video": {
    "S3ObjectName": "video.mpg",
    "S3Bucket": "videobucket"
  }
}
```