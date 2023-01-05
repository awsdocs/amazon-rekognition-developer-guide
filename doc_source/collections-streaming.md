# Searching faces in a collection in streaming video<a name="collections-streaming"></a>

You can use Amazon Rekognition Video to detect and recognize faces from a collection in streaming video\. With Amazon Rekognition Video you can create a stream processor \([CreateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html)\) to start and manage the analysis of streaming video\. 

To detect a known face in a video stream \(face search\), Amazon Rekognition Video uses Amazon Kinesis Video Streams to receive and process a video stream\. The analysis results are output from Amazon Rekognition Video to a Kinesis data stream and then read by your client application\. 

To use Amazon Rekognition Video with streaming video, your application needs to implement the following:
+ A Kinesis video stream for sending streaming video to Amazon Rekognition Video\. For more information, see the [Amazon Kinesis Video Streams Developer Guide](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html)\. 
+ An Amazon Rekognition Video stream processor to manage the analysis of the streaming video\. For more information, see [Overview of Amazon Rekognition Video stream processor operations](streaming-video.md#using-rekognition-video-stream-processor)\.
+ A Kinesis data stream consumer to read the analysis results that Amazon Rekognition Video sends to the Kinesis data stream\. For more information, see [Kinesis Data Streams Consumers](https://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-consumers.html)\. 

This section contains information about writing an application that creates the Kinesis video stream and other necessary resources, streams video into Amazon Rekognition Video, and receives the analysis results\.

**Topics**
+ [Setting up your Amazon Rekognition Video and Amazon Kinesis resources](setting-up-your-amazon-rekognition-streaming-video-resources.md)
+ [Searching faces in a streaming video](rekognition-video-stream-processor-search-faces.md)
+ [Streaming using a GStreamer plugin](streaming-using-gstreamer-plugin.md)
+ [Troubleshooting streaming video](streaming-video-troubleshooting.md)