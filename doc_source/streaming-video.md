# Working with streaming videos<a name="streaming-video"></a>

You can use Amazon Rekognition Video to detect and recognize faces in streaming video\. A typical use case is when you want to detect a known face in a video stream\. Amazon Rekognition Video uses Amazon Kinesis Video Streams to receive and process a video stream\. The analysis results are output from Amazon Rekognition Video to a Kinesis data stream and then read by your client application\. Amazon Rekognition Video provides a stream processor \([CreateStreamProcessor](API_CreateStreamProcessor.md)\) that you can use to start and manage the analysis of streaming video\.

**Note**  
The Amazon Rekognition Video streaming API is available in the following regions only: US East \(N\. Virginia\), US West \(Oregon\), Asia Pacific \(Tokyo\), EU \(Frankfurt\), and EU \(Ireland\)\.

The following diagram shows how Amazon Rekognition Video detects and recognizes faces in a streaming video\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/VideoRekognitionStream.png)

To use Amazon Rekognition Video with streaming video, your application needs to implement the following:
+ A Kinesis video stream for sending streaming video to Amazon Rekognition Video\. For more information, see the [Amazon Kinesis Video Streams Developer Guide](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html)\. 
+ An Amazon Rekognition Video stream processor to manage the analysis of the streaming video\. For more information, see [Analyze streaming videos with Amazon Rekognition Video stream processors](using-rekognition-video-stream-processor.md)\.
+ A Kinesis data stream consumer to read the analysis results that Amazon Rekognition Video sends to the Kinesis data stream\. For more information, see [Kinesis Data Streams Consumers](https://docs.aws.amazon.com/streams/latest/dev/amazon-kinesis-consumers.html)\. 

This section contains information about writing an application that creates the Kinesis video stream and the Kinesis data stream, streams video into Amazon Rekognition Video, and consumes the analysis results\. If you are streaming from a Matroska \(MKV\) encoded file, you can use the [PutMedia](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_PutMedia.html) operation to stream the source video into the Kinesis video stream that you created\. For more information, see [PutMedia API Example](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-putmedia.html)\. Otherwise, you can use Gstreamer, a third\-party multimedia framework software, and you can install a Amazon Kinesis Video Streams plugin that streams video from a device camera\. 

**Topics**
+ [Setting up your Amazon Rekognition Video and Amazon Kinesis resources](setting-up-your-amazon-rekognition-streaming-video-resources.md)
+ [Streaming using a GStreamer plugin](streaming-using-gstreamer-plugin.md)
+ [Reading streaming video analysis results](streaming-video-kinesis-output.md)
+ [Reference: Kinesis face recognition record](streaming-video-kinesis-output-reference.md)
+ [Troubleshooting streaming video](streaming-video-troubleshooting.md)