# Reference: Kinesis Face Recognition Record<a name="streaming-video-kinesis-output-reference"></a>

Rekognition Video can recognize faces in a streaming video\. For each analyzed frame, Rekognition Video outputs a JSON frame record to a Kinesis data stream\. Rekognition Video doesn't analyze every frame that's passed to it though the Kinesis video stream\. 

The JSON frame record contains information about the input and output stream, the status of the stream processor, and information about faces that are recognized in the analyzed frame\. This section contains reference information for the JSON frame record\.

The following is the JSON syntax for a Kinesis data stream record\. For more information, see [Working with Streaming Videos](streaming-video.md)\.

```
{

        "InputInformation":{
          "KinesisVideo": {
            "StreamArn": "string",
            "FragmentNumber": "string",
            "ProducerTimestamp": double,
            "ServerTimestamp": double,
            "FrameOffsetInSeconds": double
          },
        },
        "StreamProcessorInformation":{
            "Status": "STARTING|IN_PROGRESS|STOPPING|STOPPED|FAILED"
           },
        "FaceSearchResponse":{
          "DetectedFace":[
             {
                "BoundingBox":{
                    "Width":number,
                    "Top":number,
                    "Height":number,
                    "Left":number
                 },
                 "Confidence":number,
                 "Landmarks":[
                    {
                       "Type":"string",
                       "X":number,
                       "Y":number
                    }
                 ],
                 "Pose":{
                    "Pitch":number,
                    "Roll":number,
                    "Yaw":number
                 },
                 "Quality":{
                    "Brightness":number,
                    "Sharpness":number
                 },
                 "MatchedFaces":[
                    {
                       "Face": {
                          "BoundingBox": <>,
                          "Confidence": number,
                          "ExternalImageId": "string",
                          "FaceId":"string",
                          "ImageId":"string"
                       },
                       "Similarity":number
                    }
                 ]
              }
           ]
      }
    }
```

## JSON Record<a name="streaming-video-kinesis-output-reference-processorresult"></a>

The JSON record includes information about a frame that's processed by Rekognition Video\. The record includes information about the streaming video, the status for the analyzed frame, and information about faces that are recognized in the frame\.

**InputInformation**

Information about the Kinesis video stream that's used to stream video into Rekognition Video\.

Type: [InputInformation](streaming-video-kinesis-output-reference-inputinformation.md) object

**StreamProcessorInformation**

Information about the Rekognition Video stream processor\. This includes status information for the current status of the stream processor\.

Type: [StreamProcessorInformation](streaming-video-kinesis-output-reference-streamprocessorinformation.md) object 

**FaceSearchResponse**

Information about faces in the streaming video frame that match faces in the input collection\.

Type: [FaceSearchResponse](streaming-video-kinesis-output-reference-facesearchresponse.md) object