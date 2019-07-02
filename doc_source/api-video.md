# Calling Amazon Rekognition Video Operations<a name="api-video"></a>

Amazon Rekognition Video is an asynchronous API that you can use to analyze videos that are stored in an Amazon Simple Storage Service \(Amazon S3\) bucket\. You start the analysis of a video by calling an Amazon Rekognition Video `Start` operation, such as [StartPersonTracking](API_StartPersonTracking.md)\. Amazon Rekognition Video publishes the result of the analysis request to an Amazon Simple Notification Service \(Amazon SNS\) topic\. You can use an Amazon Simple Queue Service \(Amazon SQS\) queue or an AWS Lambda function to get the completion status of the video analysis request from the Amazon SNS topic\. Finally, you get the video analysis request results by calling an Amazon Rekognition `Get` operation, such as [GetPersonTracking](API_GetPersonTracking.md)\. 

The information in the following sections uses label detection operations to show how Amazon Rekognition Video detects labels \(objects, events, concepts, and activities\) in a video that's stored in an Amazon S3 bucket\. The same approach works for the other Amazon Rekognition Video operations—for example, [StartFaceDetection](API_StartFaceDetection.md) and [StartPersonTracking](API_StartPersonTracking.md)\. The example [Analyzing a Video Stored in an Amazon S3 Bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md) shows how to analyze a video by using an Amazon SQS queue to get the completion status from the Amazon SNS topic\. It's also used as a basis for other Amazon Rekognition Video examples, such as [People Pathing](persons.md)\. For AWS CLI examples, see [Analyzing a Video with the AWS Command Line Interface](video-cli-commands.md)\.

**Topics**
+ [Starting Video Analysis](#api-video-start)
+ [Getting the Completion Status of an Amazon Rekognition Video Analysis Request](#api-video-get-status)
+ [Getting Amazon Rekognition Video Analysis Results](#api-video-get)

## Starting Video Analysis<a name="api-video-start"></a>

You start an Amazon Rekognition Video label detection request by calling [StartLabelDetection](API_StartLabelDetection.md)\. The following is an example of a JSON request that's passed by `StartLabelDetection`\.

```
{
    "Video": {
        "S3Object": {
            "Bucket": "bucket",
            "Name": "video.mp4"
        }
    },
    "ClientRequestToken": "LabelDetectionToken",
    "MinConfidence": 50,
    "NotificationChannel": {
        "SNSTopicArn": "arn:aws:sns:us-east-1:nnnnnnnnnn:topic",
        "RoleArn": "arn:aws:iam::nnnnnnnnnn:role/roleopic"
    },
    "JobTag": "DetectingLabels"
}
```

The input parameter `Video` provides the video file name and the Amazon S3 bucket to retrieve it from\. `NotificationChannel` contains the Amazon Resource Name \(ARN\) of the Amazon SNS topic that Amazon Rekognition Video notifies when the video analysis request finishes\. The Amazon SNS topic must be in the same AWS region as the Amazon Rekognition Video endpoint that you're calling\. `NotificationChannel` also contains the ARN for a role that allows Amazon Rekognition Video to publish to the Amazon SNS topic\. You give Amazon Rekognition publishing permissions to your Amazon SNS topics by creating an IAM service role\. For more information, see [Configuring Amazon Rekognition Video](api-video-roles.md)\.

You can also specify an optional input parameter, `JobTag`, that allows you to identify the job in the completion status that's published to the Amazon SNS topic\. 

To prevent accidental duplication of analysis jobs, you can optionally provide an idempotent token, `ClientRequestToken`\. If you supply a value for `ClientRequestToken`, the `Start` operation returns the same `JobId` for multiple identical calls to the start operation, such as `StartLabelDetection`\. A `ClientRequestToken` token has a lifetime of 7 days\. After 7 days, you can reuse it\. If you reuse the token during the token lifetime, the following happens: 
+ If you reuse the token with same `Start` operation and the same input parameters, the same `JobId` is returned\. The job is not performed again and Amazon Rekognition Video does not send a completion status to the registered Amazon SNS topic\.
+ If you reuse the token with the same `Start` operation and a minor input parameter change, you get an `idempotentparametermismatchexception` \(HTTP status code: 400\) exception raised\.
+ If you reuse the token with a different `Start` operation, the operation succeeds\.

The response to the `StartLabelDetection` operation is a job identifier \(`JobId`\)\. Use `JobId` to track requests and get the analysis results after Amazon Rekognition Video has published the completion status to the Amazon SNS topic\. For example:

```
{"JobId":"270c1cc5e1d0ea2fbc59d97cb69a72a5495da75851976b14a1784ca90fc180e3"}
```

If you start too many jobs concurrently, calls to `StartLabelDetection` raise a `LimitExceededException` exception \(HTTP status code: 400\) until the number of concurrently running jobs is below the Amazon Rekognition service limit\. 

If you find that LimitExceededException exceptions are raised with bursts of activity, consider using an Amazon SQS queue to manage incoming requests\. Contact AWS support if you find that your average number of concurrent requests cannot be managed by an Amazon SQS queue and you are still receiving `LimitExceededException` exceptions\. 

## Getting the Completion Status of an Amazon Rekognition Video Analysis Request<a name="api-video-get-status"></a>

Amazon Rekognition Video sends an analysis completion notification to the registered Amazon SNS topic\. The notification includes the job identifier and the completion status of the operation in a JSON string\. A successful video analysis request has a `SUCCEEDED` status\. For example, the following result shows the successful processing of a label detection job\.

```
{
    "JobId": "270c1cc5e1d0ea2fbc59d97cb69a72a5495da75851976b14a1nnnnnnnnnnnn",
    "Status": "SUCCEEDED",
    "API": "StartLabelDetection",
    "JobTag": "DetectingLabels",
    "Timestamp": 1510865364756,
    "Video": {
        "S3ObjectName": "video.mp4",
        "S3Bucket": "bucket"
    }
}
```

For more information, see [Reference: Video Analysis Results Notification](video-notification-payload.md)\.

To get the status information that's published to the Amazon SNS topic by Amazon Rekognition Video, use one of the following options:
+ **AWS Lambda** – You can subscribe an AWS Lambda function that you write to an Amazon SNS topic\. The function is called when Amazon Rekognition notifies the Amazon SNS topic that the request has completed\. Use a Lambda function if you want server\-side code to process the results of a video analysis request\. For example, you might want to use server\-side code to annotate the video or create a report on the video contents before returning the information to a client application\. We also recommend server\-side processing for large videos because the Amazon Rekognition API might return large volumes of data\. 
+ **Amazon Simple Queue Service** – You can subscribe an Amazon SQS queue to an Amazon SNS topic\. You then poll the Amazon SQS queue to retrieve the completion status that's published by Amazon Rekognition when a video analysis request completes\. For more information, see [Analyzing a Video Stored in an Amazon S3 Bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md)\. Use an Amazon SQS queue if you want to call Amazon Rekognition Video operations only from a client application\. 

**Important**  
We don't recommend getting the request completion status by repeatedly calling the Amazon Rekognition Video `Get` operation\. This is because Amazon Rekognition Video throttles the `Get` operation if too many requests are made\. If you're processing multiple videos concurrently, it's simpler and more efficient to monitor one SQS queue for the completion notification than to poll Amazon Rekognition Video for the status of each video individually\.

## Getting Amazon Rekognition Video Analysis Results<a name="api-video-get"></a>

 To get the results of a video analysis request, first ensure that the completion status that's retrieved from the Amazon SNS topic is `SUCCEEDED`\. Then call `GetLabelDetection`, which passes the `JobId` value that's returned from `StartLabelDetection`\. The request JSON is similar to the following example:

```
{
    "JobId": "270c1cc5e1d0ea2fbc59d97cb69a72a5495da75851976b14a1784ca90fc180e3",
    "MaxResults": 10,
    "SortBy": "TIMESTAMP"
}
```

JobId is the identifier for the video analysis operation\. Because video analysis can generate large amounts of data, use `MaxResults` to specify the maximum number of results to return in a single Get operation\. The default value for `MaxResults` is 1000\. If you specify a value greater than 1000, a maximum of 1000 results is returned\. If the operation doesn't return the entire set of results, a pagination token for the next page is returned in the operation response\. If you have a pagination token from a previous Get request, use it with `NextToken` to get the next page of results\.

**Note**  
Amazon Rekognition retains the results of a video analysis operation for 7 days\. You will not be able to retrieve the analysis results after this time\.

The `GetLabelDetection` operation response JSON is similar to the following:

```
{
    "Labels": [
        {
            "Timestamp": 0,
            "Label": {
                "Instances": [],
                "Confidence": 60.51791763305664,
                "Parents": [],
                "Name": "Electronics"
            }
        },
        {
            "Timestamp": 0,
            "Label": {
                "Instances": [],
                "Confidence": 99.53411102294922,
                "Parents": [],
                "Name": "Human"
            }
        },
        {
            "Timestamp": 0,
            "Label": {
                "Instances": [
                    {
                        "BoundingBox": {
                            "Width": 0.11109819263219833,
                            "Top": 0.08098889887332916,
                            "Left": 0.8881205320358276,
                            "Height": 0.9073750972747803
                        },
                        "Confidence": 99.5831298828125
                    },
                    {
                        "BoundingBox": {
                            "Width": 0.1268676072359085,
                            "Top": 0.14018426835536957,
                            "Left": 0.0003282368124928324,
                            "Height": 0.7993982434272766
                        },
                        "Confidence": 99.46029663085938
                    }
                ],
                "Confidence": 99.53411102294922,
                "Parents": [],
                "Name": "Person"
            }
        },
        .
        .   
        .

        {
            "Timestamp": 166,
            "Label": {
                "Instances": [],
                "Confidence": 73.6471176147461,
                "Parents": [
                    {
                        "Name": "Clothing"
                    }
                ],
                "Name": "Sleeve"
            }
        }
        
    ],
    "LabelModelVersion": "2.0",
    "JobStatus": "SUCCEEDED",
    "VideoMetadata": {
        "Format": "QuickTime / MOV",
        "FrameRate": 23.976024627685547,
        "Codec": "h264",
        "DurationMillis": 5005,
        "FrameHeight": 674,
        "FrameWidth": 1280
    }
}
```

You can sort the results by detection time \(milliseconds from the start of the video\) or alphabetically by the detected entity \(object, face, celebrity, moderation label, or person\)\. To sort by time, set the value of the `SortBy` input parameter to `TIMESTAMP`\. If `SortBy` isn't specified, the default behavior is to sort by time\. The preceding example is sorted by time\. To sort by entity, use the `SortBy` input parameter with the value that's appropriate for the operation you're performing\. For example, to sort by detected label in a call to `GetLabelDetection`, use the value `NAME`\.