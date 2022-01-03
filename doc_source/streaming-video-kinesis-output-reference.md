# Reference: Kinesis face recognition record<a name="streaming-video-kinesis-output-reference"></a>

Amazon Rekognition Video can recognize faces in a streaming video\. For each analyzed frame, Amazon Rekognition Video outputs a JSON frame record to a Kinesis data stream\. Amazon Rekognition Video doesn't analyze every frame that's passed to it through the Kinesis video stream\. 

The JSON frame record contains information about the input and output stream, the status of the stream processor, and information about faces that are recognized in the analyzed frame\. This section contains reference information for the JSON frame record\.

The following is the JSON syntax for a Kinesis data stream record\. For more information, see [Working with streaming videos](streaming-video.md)\.

**Note**  
The Amazon Rekognition Video API works by comparing the faces in your input stream to a collection of faces, and returning the closest found matches, along with a similarity score\.

```
{
    "InputInformation": {
        "KinesisVideo": {
            "StreamArn": "string",
            "FragmentNumber": "string",
            "ProducerTimestamp": number,
            "ServerTimestamp": number,
            "FrameOffsetInSeconds": number
        }
    },
    "StreamProcessorInformation": {
        "Status": "RUNNING"
    },
    "FaceSearchResponse": [
        {
            "DetectedFace": {
                "BoundingBox": {
                    "Width": number,
                    "Top": number,
                    "Height": number,
                    "Left": number
                },
                "Confidence": number,
                "Landmarks": [
                    {
                        "Type": "string",
                        "X": number,
                        "Y": number
                    }
                ],
                "Pose": {
                    "Pitch": number,
                    "Roll": number,
                    "Yaw": number
                },
                "Quality": {
                    "Brightness": number,
                    "Sharpness": number
                }
            },
            "MatchedFaces": [
                {
                    "Similarity": number,
                    "Face": {
                        "BoundingBox": {
                            "Width": number,
                            "Top": number,
                            "Height": number,
                            "Left": number
                        },
                        "Confidence": number,
                        "ExternalImageId": "string",
                        "FaceId": "string",
                        "ImageId": "string"
                    }
                }
            ]
        }
    ]
}
```

## JSON record<a name="streaming-video-kinesis-output-reference-processorresult"></a>

The JSON record includes information about a frame that's processed by Amazon Rekognition Video\. The record includes information about the streaming video, the status for the analyzed frame, and information about faces that are recognized in the frame\.

**InputInformation**

Information about the Kinesis video stream that's used to stream video into Amazon Rekognition Video\.

Type: [InputInformation](streaming-video-kinesis-output-reference-inputinformation.md) object

**StreamProcessorInformation**

Information about the Amazon Rekognition Video stream processor\. This includes status information for the current status of the stream processor\.

Type: [StreamProcessorInformation](streaming-video-kinesis-output-reference-streamprocessorinformation.md) object 

**FaceSearchResponse**

Information about the faces detected in a streaming video frame and the matching faces found in the input collection\.

Type: [FaceSearchResponse](streaming-video-kinesis-output-reference-facesearchresponse.md) object array