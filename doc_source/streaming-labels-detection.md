# Label detection operations for streaming video events<a name="streaming-labels-detection"></a>

Amazon Rekognition Video can detect people or relevant objects in a streaming video and notify you when they're detected\. When you create a label detection stream processor, choose what labels that you want Amazon Rekognition Video to detect\. These can be people, packages and pets, or people, packages, and pets\. Choose only the specific labels that you want to detect\. That way, the only relevant labels create notifications\. You can configure options to determine when to store video information, and then do additional processing based on the labels that are detected in the frame\.

After you set up your resources, the process to detect labels in a streaming video is as follows:

1. Create the stream processor

1. Start the stream processor

1. If an object of interest is detected, you receive an Amazon SNS notification for the first occurrence of each object of interest\.

1. The stream processor stops when the time specified in `MaxDurationInSeconds` is complete\.

1. You receive a final Amazon SNS notification with an event summary\.

1. Amazon Rekognition Video publishes a detailed session summary to your S3 bucket\.

**Topics**
+ [Creating the Amazon Rekognition Video label detection stream processor](#streaming-video-create-labels-stream-processor)
+ [Starting the Amazon Rekognition Video label detection stream processor](#streaming-video-start-labels-stream-processor)
+ [Analyzing label detection results](#streaming-video-labels-stream-processor-results)

## Creating the Amazon Rekognition Video label detection stream processor<a name="streaming-video-create-labels-stream-processor"></a>

Before you can analyze a streaming video, you create an Amazon Rekognition Video stream processor \([CreateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html)\)\.

If you want to create a stream processor to detect labels of interest and people, provide as input a Kinesis video stream \(`Input`\), Amazon S3 bucket information \(`Output`\), and an Amazon SNS topic ARN \(`StreamProcessorNotificationChannel`\)\. You can also provide a KMS key ID to encrypt the data sent to your S3 bucket\. You specify what you want to detect in `Settings`, such as people, packages and people, or pets, people, and packages\. You can also specify where in the frame that you want Amazon Rekognition to monitor with `RegionsOfInterest`\. The following is a JSON example for the `CreateStreamProcessor` request\.

```
{
  "DataSharingPreference": { "OptIn":TRUE
  },
  "Input": {
    "KinesisVideoStream": {
      "Arn": "arn:aws:kinesisvideo:us-east-1:nnnnnnnnnnnn:stream/muh_video_stream/nnnnnnnnnnnnn"
    }
  },
  "KmsKeyId": "muhkey",
  "Name": "muh-default_stream_processor",
  "Output": {
    "S3Destination": {
      "Bucket": "s3bucket",
      "KeyPrefix": "s3prefix"
    }
  },
  "NotificationChannel": {
    "SNSTopicArn": "arn:aws:sns:us-east-2:nnnnnnnnnnnn:MyTopic"
  },
  "RoleArn": "arn:aws:iam::nnnnnnnnn:role/Admin",
  "Settings": {
    "ConnectedHome": {
      "Labels": [
        "PET"
      ]
    "MinConfidence": 80
    }
  },
  "RegionsOfInterest": [
    {
      "BoundingBox": {
        "Top": 0.11,
        "Left": 0.22,
        "Width": 0.33,
        "Height": 0.44
      }
    },
    {
      "Polygon": [
        {
          "X": 0.11,
          "Y": 0.11
        },
        {
          "X": 0.22,
          "Y": 0.22
        },
        {
          "X": 0.33,
          "Y": 0.33
        }
      ]
    }
  ]
}
```

Note that you can change the `MinConfidence` value when you specify the `ConnectedHomeSettings` for the stream processor\. `MinConfidence` is a numerical value ranging from 0 to 100 that indicates how certain the algorithm is about its predictions\. For example, a notification for `person` with a confidence value of 90 means that the algorithm is absolutely certain that the person is present in the video\. A confidence value of 10 indicates that there might be a person\. You can set `MinConfidence` to a desired value of your choice between 0 and 100 depending on how frequently you want to be notified\. For example, if you want to be notified only when Rekognition is absolutely certain there is a package in the video frame then you can set `MinConfidence` to 90\.

By default, `MinConfidence ` is set to 50\. If you want to optimize the algorithm for higher precision, then you can set `MinConfidence` to be higher than 50\. You then receive fewer notification, but each notification is more reliable\. If you want to optimize the algorithm for higher recall, then you can set `MinConfidence` to be lower than 50 to receive more notifications\. 

## Starting the Amazon Rekognition Video label detection stream processor<a name="streaming-video-start-labels-stream-processor"></a>

You start analyzing streaming video by calling [StartStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartStreamProcessor.html) with the stream processor name that you specified in `CreateStreamProcessor`\. When you run the `StartStreamProcessor` operation on a label detection stream processor, you input start and stop information to determine the processing time\.

When you start the stream processor, the label detection stream processor state changes in the following ways:

1. When you call `StartStreamProcessor`, the label detection stream processor state goes from `STOPPED` or `FAILED` to `STARTING`\.

1. While the label detection stream processor runs, it stays in `STARTING`\.

1. When the label detection stream processor is done running, the state becomes either `STOPPED` or `FAILED`\.

The `StartSelector` specifies the starting point in the Kinesis stream to start processing\. You can use the KVS Producer timestamp or the KVS Fragment number\. For more information, see [Fragment](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_Fragment.html)\.

**Note**  
If you use the KVS Producer timestamp, you must input the time in milliseconds\.

The `StopSelector` specifies when to stop processing the stream\. You can specify a maximum amount of time to process the video\. The default is a maximum duration of 10 seconds\. Note that the actual processing time might be a bit longer than the maximum duration, depending on the size of individual KVS fragments\. If the maximum duration has been reached or exceeded at the end of a fragment, the processing time stops\. 

The following is a JSON example for the `StartStreamProcessor` request\.

```
{
   "Name": "string",
   "StartSelector": {
     "KVSStreamStartSelector": { 
         "KVSProducerTimestamp": 1655930623123
      },
        "StopSelector": {
            "MaxDurationInSeconds": 11
      }
   }
}
```

If the stream processor successfully starts, an HTTP 200 response is returned\. An empty JSON body is included\.

## Analyzing label detection results<a name="streaming-video-labels-stream-processor-results"></a>

There are three ways that Amazon Rekognition Video publishes notifications from a label detection stream processor: Amazon SNS notifications for object detection events, an Amazon SNS notification for an end\-of\-session summary, and a detailed Amazon S3 bucket report\. 
+ Amazon SNS notifications for object detection events\. 

  If labels are detected in the video stream, you receive Amazon SNS notifications for object detection events\. Amazon Rekognition publishes a notification the first time that a person or an object of interest is detected in the video stream\. Notifications include information such as the type of label detected, the confidence, and a link to the hero image\. They also include a cropped image of the person or object detected and a detection timestamp\. The notification has the following format:

  ```
  {"Subject": "Rekognition Stream Processing Event",
      "Message": {    
          "inputInformation": {
              "kinesisVideo": {
                  "streamArn": string
              }
          },
          "eventNamespace": {
              "type": "LABEL_DETECTED"
          },
          "labels": [{
              "id": string,
              "name": "PERSON" | "PET" | "PACKAGE",
              "frameImageUri": string,
              "croppedImageUri": string,
              "videoMapping": {
                  "kinesisVideoMapping": {
                      "fragmentNumber": string,
                      "serverTimestamp": number,
                      "producerTimestamp": number,
                      "frameOffsetMillis": number
                  }
              },
              "boundingBox": {
                  "left": number,
                  "top": number,
                  "height": number,
                  "width": number
              }
          }],
          "eventId": string,
          "tags": {
              [string]: string
          },
          "sessionId": string,
          "startStreamProcessorRequest": object
      }
  }
  ```
+ Amazon SNS end\-of\-session summary\.

  You also receive an Amazon SNS notification when the stream processing session is finished\. This notification lists the metadata for the session\. This includes details such as the duration of the stream that was processed\. The notification has the following format:

  ```
  {"Subject": "Rekognition Stream Processing Event",
      "Message": {
          "inputInformation": {
              "kinesisVideo": {
                  "streamArn": string,
                  "processedVideoDurationMillis": number
              }
          },
          "eventNamespace": {
              "type": "STREAM_PROCESSING_COMPLETE"
          },
          "streamProcessingResults": {
              "message": string
          },
          "eventId": string,
          "tags": {
              [string]: string
          },
          "sessionId": string,
          "startStreamProcessorRequest": object
      }
  }
  ```
+ Amazon S3 bucket report\.

  Amazon Rekognition Video publishes detailed inference results of a video analysis operation to the Amazon S3 bucket that's provided in the `CreateStreamProcessor` operation\. These results include image frames where an object of interest or person was detected for first time\. 

  The frames are available in S3 in the following path: ObjectKeyPrefix/StreamProcessorName/SessionId/*service\_determined\_unique\_path*\. In this path, **LabelKeyPrefix** is a customer provided optional argument, **StreamProcessorName** is the name of the stream processor resource, and **SessionId** is a unique ID for the stream processing session\. Replace these according to your situation\.