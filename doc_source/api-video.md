# Calling Rekognition Video Operations<a name="api-video"></a>

Rekognition Video is an asynchronous API that you can use to analyze videos that are stored in an Amazon Simple Storage Service \(Amazon S3\) bucket\. You start the analysis of a video by calling a Rekognition Video `Start` operation, such as [StartPersonTracking](API_StartPersonTracking.md)\. Rekognition Video publishes the result of the analysis request to an Amazon Simple Notification Service \(Amazon SNS\) topic\. You can use an Amazon Simple Queue Service \(Amazon SQS\) queue or an AWS Lambda function to get the completion status of the video analysis request from the Amazon SNS topic\. Finally, you get the video analysis request results by calling an Amazon Rekognition `Get` operation, such as [GetPersonTracking](API_GetPersonTracking.md)\. 

The information in the following sections uses label detection operations to show how Rekognition Video detects labels \(objects, events, concepts, and activities\) in a video that's stored in an Amazon S3 bucket\. The same approach works for the other Rekognition Video operations—for example, [StartFaceDetection](API_StartFaceDetection.md) and [StartPersonTracking](API_StartPersonTracking.md)\. The AWS SDK for Java example [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md) shows how to analyze a video by using an Amazon SQS queue to get the completion status from the Amazon SNS topic\. It's also used as a basis for other Rekognition Video examples, such as [Tracking People through a Stored Video \(SDK for Java\)](video-sqs-persons.md)\. For AWS CLI examples, see [Analyzing a Video with the AWS Command Line Interface](video-cli-commands.md)\.


+ [Starting Video Analysis](#api-video-start)
+ [Getting the Completion Status of a Rekognition Video Analysis Request](#api-video-get-status)
+ [Getting Rekognition Video Analysis Results](#api-video-get)

## Starting Video Analysis<a name="api-video-start"></a>

You start a Rekognition Video label detection request by calling `StartLabelDetection`\. The following is an example of a JSON request that's passed by `StartLabelDetection`\.

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

The input parameter `Video` provides the video file name and the Amazon S3 bucket to retrieve it from\. `NotificationChannel` contains the Amazon Resource Name \(ARN\) of the Amazon SNS topic that Rekognition Video notifies when the video analysis request finishes\. The Amazon SNS topic must be in the same AWS region as the Rekognition Video endpoint that you're calling\. `NotificationChannel` also contains the ARN for a role that allows Rekognition Video to publish to the Amazon SNS topic\. You give Amazon Rekognition publishing permissions to your Amazon SNS topics by creating an IAM service role\. For more information, see [Giving Rekognition Video Access to Your Amazon SNS Topics](api-video-roles.md)\.

You can also specify an optional input parameter, `JobTag`, that allows you to identify the job in the completion status that's published to the Amazon SNS topic\. 

To prevent accidental duplication of analysis jobs, you can optionally provide an idempotent token, `ClientRequestToken`\. If you supply a value for `ClientRequestToken`, the `Start` operation returns the same `JobId` for multiple identical calls to the start operation, such as `StartLabelDetection`\. A `ClientRequestToken` token has a lifetime of 7 days\. After 7 days, you can reuse it\. If you reuse the token during the token lifetime, the following happens: 

+ If you reuse the token with same `Start` operation and the same input parameters, the same `JobId` is returned\. The job is not performed again and Rekognition Video does not send a completion status to the registered Amazon SNS topic\.

+ If you reuse the token with the same `Start` operation and a minor input parameter change, you get an `idempotentparametermismatchexception` exception raised\.

+ If you reuse the token with a different `Start` operation, the operation succeeds\.

The response to the `StartLabelDetection` operation is a job identifier \(`JobId`\)\. Use `JobId` to track requests and get the analysis results after Rekognition Video has published the completion status to the Amazon SNS topic\. For example:

```
{"JobId":"270c1cc5e1d0ea2fbc59d97cb69a72a5495da75851976b14a1784ca90fc180e3"}
```

## Getting the Completion Status of a Rekognition Video Analysis Request<a name="api-video-get-status"></a>

Rekognition Video sends an analysis completion notification to the registered Amazon SNS topic\. The notification includes the job identifier and the completion status of the operation in a JSON string\. A successful video analysis request has a `SUCCEEDED` status\. For example, the following result shows the successful processing of a label detection job\.

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

To get the status information that's published to the Amazon SNS topic by Rekognition Video, use one of the following options:

+ **AWS Lambda** – You can subscribe an AWS Lambda function that you write to an Amazon SNS topic\. The function is called when Amazon Rekognition notifies the Amazon SNS topic that the request has completed\. Use a Lambda function if you want server\-side code to process the results of a video analysis request\. For example, you might want to use server\-side code to annotate the video or create a report on the video contents before returning the information to a client application\. We also recommend server\-side processing for large videos because the Amazon Rekognition API might return large volumes of data\. 

+ **Amazon Simple Queue Service** – You can subscribe an Amazon SQS queue to an Amazon SNS topic\. You then poll the Amazon SQS queue to retrieve the completion status that's published by Amazon Rekognition when a video analysis request completes\. For more information, see [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md)\. Use an Amazon SQS queue if you want to call Rekognition Video operations only from a client application\. 

**Important**  
We don't recommend getting the request completion status by repeatedly calling the Rekognition Video `Get` operation\. This is because Rekognition Video throttles the `Get` operation if too many requests are made\. If you're processing multiple videos concurrently, it's simpler and more efficient to monitor one SQS queue for the completion notification than to poll Rekognition Video for the status of each video individually\.

## Getting Rekognition Video Analysis Results<a name="api-video-get"></a>

 To get the results of a video analysis request, first ensure that the completion status that's retrieved from the Amazon SNS topic is `SUCCEEDED`\. Then call `GetLabelDetection`, which passes the `JobId` value that's returned from `StartLabelDetection`\. The request JSON is similar to the following example:

```
{
    "JobId": "270c1cc5e1d0ea2fbc59d97cb69a72a5495da75851976b14a1784ca90fc180e3",
    "MaxResults": 10,
    "SortBy": "TIMESTAMP"
}
```

JobId is the identifier for the video analysis operation\. Because video analysis can generate large amounts of data, use `MaxResults` to specify the maximum number of results to return in a single Get operation\. If the operation doesn't return the entire set of results, a pagination token for the next page is returned in the operation response\. If you have a pagination token from a previous Get request, use it with `NextToken` to get the next page of results\. The default page size is 1000\.

**Note**  
Amazon Rekognition retains the results of a video analysis operation for 7 days\. You will not be able to retrieve the analysis results after this time\.

The `GetLabelDetectionResponse` operation response JSON is similar to the following:

```
{
    "JobStatus": "SUCCEEDED",
    "Labels": [
        {
            "Label": {
                "Confidence": 56.49449920654297,
                "Name": "Bowl"
            },
            "Timestamp": 0
        },
        {
            "Label": {
                "Confidence": 77.5353012084961,
                "Name": "Clothing"
            },
            "Timestamp": 0
        },
        {
            "Label": {
                "Confidence": 53.91270065307617,
                "Name": "Guitar"
            },
            "Timestamp": 0
        },
        {
            "Label": {
                "Confidence": 53.91270065307617,
                "Name": "Musical Instrument"
            },
            "Timestamp": 0
        },
        {
            "Label": {
                "Confidence": 77.5353012084961,
                "Name": "Overcoat"
            },
            "Timestamp": 0
        },
        {
            "Label": {
                "Confidence": 50.50969696044922,
                "Name": "Person"
            },
            "Timestamp": 0
        },
        {
            "Label": {
                "Confidence": 67.22470092773438,
                "Name": "Pumpkin"
            },
            "Timestamp": 0
        },
        {
            "Label": {
                "Confidence": 99.03849792480469,
                "Name": "Speech"
            },
            "Timestamp": 0
        },
        {
            "Label": {
                "Confidence": 67.22470092773438,
                "Name": "Squash"
            },
            "Timestamp": 0
        },
        {
            "Label": {
                "Confidence": 77.5353012084961,
                "Name": "Suit"
            },
            "Timestamp": 0
        }
    ],
    "NextToken": "WlKfzZED1PzBLyAmTpda655kICVnPPAtQ/8V9Mci6097JKjqP08uQun6j6fwGEaJFDUQVawYsg==",
    "VideoMetadata": {
        "Codec": "h264",
        "DurationMillis": 67301,
        "FileExtension": "mp4",
        "Format": "QuickTime / MOV",
        "FrameHeight": 1080,
        "FrameRate": 29.970029830932617,
        "FrameWidth": 1920
    }
}
```

You can sort the results by detection time \(milliseconds from the start of the video\) or alphabetically by the detected entity \(object, face, celebrity, moderation label, or person\)\. To sort by time, set the value of the `SortBy` input parameter to `TIMESTAMP`\. If `SortBy` isn't specified, the default behavior is to sort by time\. The preceding example is sorted by time\. To sort by entity, use the `SortBy` input parameter with the value that's appropriate for the operation you're performing\. For example, to sort by detected label in a call to `GetLabelDetection`, use the value `NAME`\. The following example shows sorting by label name for the detected labels *Apparel* and *badge*\. 

```
{
    "JobStatus": "SUCCEEDED",
    "Labels": [
        {
            "Label": {
                "Confidence": 50.53730010986328,
                "Name": "Apparel"
            },
            "Timestamp": 46813
        },
        {
            "Label": {
                "Confidence": 50.538700103759766,
                "Name": "Apparel"
            },
            "Timestamp": 47013
        },
        {
            "Label": {
                "Confidence": 50.76940155029297,
                "Name": "Apparel"
            },
            "Timestamp": 47213
        },
        {
            "Label": {
                "Confidence": 50.504798889160156,
                "Name": "Apparel"
            },
            "Timestamp": 63229
        },
        {
            "Label": {
                "Confidence": 54.01129913330078,
                "Name": "Badge"
            },
            "Timestamp": 8775
        },
        {
            "Label": {
                "Confidence": 55.24839782714844,
                "Name": "Badge"
            },
            "Timestamp": 8975
        },
        {
            "Label": {
                "Confidence": 60.499000549316406,
                "Name": "Badge"
            },
            "Timestamp": 9175
        },
        {
            "Label": {
                "Confidence": 60.73529815673828,
                "Name": "Badge"
            },
            "Timestamp": 9376
        },
        {
            "Label": {
                "Confidence": 60.914302825927734,
                "Name": "Badge"
            },
            "Timestamp": 9576
        },
        {
            "Label": {
                "Confidence": 50.74089813232422,
                "Name": "Badge"
            },
            "Timestamp": 9776
        }
    ],
    "NextToken": "CmUTsWamUKmnzPvN+FB0REjh+xv6+iY3H0IXrHCn3yMSW1zuOcWyLKob2JjvfPjznalo3m/MGw==",
    "VideoMetadata": {
        "Codec": "h264",
        "DurationMillis": 67301,
        "FileExtension": "mp4",
        "Format": "QuickTime / MOV",
        "FrameHeight": 1080,
        "FrameRate": 29.970029830932617,
        "FrameWidth": 1920
    }
}
```