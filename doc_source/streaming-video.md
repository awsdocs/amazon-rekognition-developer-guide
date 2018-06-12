# Working with Streaming Videos<a name="streaming-video"></a>

You can use Amazon Rekognition Video to detect and recognize faces in streaming video\. A typical use case is surveillance where you want to detect a known face in a video stream\. Rekognition Video uses Amazon Kinesis Video Streams to receive and process a video stream\. The analysis results are output from Rekognition Video to a Kinesis data stream and then read by your client application\. Rekognition Video provides a stream processor \([CreateStreamProcessor](API_CreateStreamProcessor.md)\) that you can use to start and manage the analysis of streaming video\.

**Note**  
The Rekognition Video streaming API is not available in either the US East \(Ohio\) region or the Asia Pacific \(Sydney\) region\.

The following diagram shows how Rekognition Video detects and recognizes faces in a streaming video\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/VideoRekognitionStream.png)

To use Rekognition Video with streaming video, your application needs to implement the following:
+ A Kinesis video stream for sending streaming video to Rekognition Video\. For more information, see [Kinesis video stream](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html)\. 
+ A Rekognition Video stream processor to manage the analysis of the streaming video\. For more information, see [Starting Streaming Video Analysis](streaming-video-starting-analysis.md)\.
+ A Kinesis data stream consumer to read the analysis results that Rekognition Video sends to the Kinesis data stream\. For more information, see [Consumers for Amazon Kinesis Streams](http://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-consumers.html)\. 

This section contains information about writing an application that creates the Kinesis video stream and the Kinesis data stream, streams video into Rekognition Video, and consumes the analysis results\. For more information, see [Recognizing Faces in a Streaming Video](recognize-faces-in-a-video-stream.md)\.

**Topics**
+ [Recognizing Faces in a Streaming Video](recognize-faces-in-a-video-stream.md)
+ [Giving Rekognition Video Access to Your Kinesis Streams](api-streaming-video-roles.md)
+ [Starting Streaming Video Analysis](streaming-video-starting-analysis.md)
+ [Reading Streaming Video Analysis Results](streaming-video-kinesis-output.md)
+ [Reference: Kinesis Face Recognition Record](streaming-video-kinesis-output-reference.md)