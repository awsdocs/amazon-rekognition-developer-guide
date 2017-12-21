# Reading Streaming Video Analysis Results<a name="streaming-video-kinesis-output"></a>

You can use the Amazon Kinesis Data Streams Client Library to consume analysis results that are sent to the Amazon Kinesis Data Streams output stream\. For more information, see [Reading Data from a Kinesis Data Stream](http://docs.aws.amazon.com/streams/latest/dev/building-consumers.html)\. Rekognition Video places a JSON frame record for each analyzed frame into the Kinesis output stream\. Rekognition Video doesn't analyze every frame that's passed to it though the Kinesis video stream\. 

A frame record that's sent to a Kinesis data stream contains information about which Kinesis video stream fragment the frame is in, where the frame is in the fragment, and faces that are recognized in the frame\. It also includes status information for the stream processor\. For more information, see [Reference: Kinesis Face Recognition Record](streaming-video-kinesis-output-reference.md)\.

Rekognition Video streams Rekognition Video analysis information to the Kinesis data stream\. The following is a JSON example for a single record\. 

```
{
  "InputInformation": {
    "KinesisVideo": {
      "StreamArn": "arn:aws:kinesisvideo:us-west-2:nnnnnnnnnnnn:stream/stream-name",
      "FragmentNumber": "91343852333289682796718532614445757584843717598",
      "ServerTimestamp": 1510552593.455,
      "ProducerTimestamp": 1510552593.193,
      "FrameOffsetInSeconds": 2
    }
  },
  "StreamProcessorInformation": {
    "Status": "RUNNING"
  },
  "FaceSearchResponse": [
    {
      "DetectedFace": {
        "BoundingBox": {
          "Height": 0.075,
          "Width": 0.05625,
          "Left": 0.428125,
          "Top": 0.40833333
        },
        "Confidence": 99.975174,
        "Landmarks": [
          {
            "X": 0.4452057,
            "Y": 0.4395594,
            "Type": "eyeLeft"
          },
          {
            "X": 0.46340984,
            "Y": 0.43744427,
            "Type": "eyeRight"
          },
          {
            "X": 0.45960626,
            "Y": 0.4526856,
            "Type": "nose"
          },
          {
            "X": 0.44958648,
            "Y": 0.4696949,
            "Type": "mouthLeft"
          },
          {
            "X": 0.46409217,
            "Y": 0.46704912,
            "Type": "mouthRight"
          }
        ],
        "Pose": {
          "Pitch": 2.9691637,
          "Roll": -6.8904796,
          "Yaw": 23.84388
        },
        "Quality": {
          "Brightness": 40.592964,
          "Sharpness": 96.09616
        }
      },
      "MatchedFaces": [
        {
          "Similarity": 88.863960,
          "Face": {
            "BoundingBox": {
              "Height": 0.557692,
              "Width": 0.749838,
              "Left": 0.103426,
              "Top": 0.206731
            },
            "FaceId": "ed1b560f-d6af-5158-989a-ff586c931545",
            "Confidence": 99.999201,
            "ImageId": "70e09693-2114-57e1-807c-50b6d61fa4dc",
            "ExternalImageId": "matchedImage.jpeg"
          }
        }
      ]
    }
  ]
}
```

In the JSON example, note the following:

+ **InputInformation** – Information about the Kinesis video stream that's used to stream video into Rekognition Video\. For more information, see [](streaming-video-kinesis-output-reference-inputinformation.md)\.

+ **StreamProcessorInformation** – Status information for the Rekognition Video stream processor\. Possible values for the `Status` field are STARTING, STARTED, IN\_PROGRESS, STOPPING, STOPPED, and FAILED\. For more information, see [](streaming-video-kinesis-output-reference-streamprocessorinformation.md)\.

+ **FaceSearchResponse** – Contains information about faces in the streaming video that match faces in the input collection\. `FaceSearchResponse` contains a `DetectedFaces` array, which is an array of faces that were matched in the analyzed video frame\. For each matched face, the array `MatchedFaces` contains information about the matching faces found in the input collection, along with a similarity score\. For more information, see [](streaming-video-kinesis-output-reference-facesearchresponse.md)\.