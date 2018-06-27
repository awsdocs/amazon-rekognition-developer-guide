# KinesisVideo<a name="streaming-video-kinesis-output-reference-kinesisvideostreams-kinesisvideo"></a>

Information about the Kinesis video stream that streams the source video into Amazon Rekognition Video\. For more information, see [Working with Streaming Videos](streaming-video.md)\.

**StreamArn**

The Amazon Resource Name \(ARN\) of the Kinesis video stream\.

Type: String 

**FragmentNumber**

The fragment of streaming video that contains the frame that this record represents\.

Type: String

**ProducerTimestamp**

The producer\-side Unix time stamp of the fragment\. For more information, see [PutMedia](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_PutMedia.html)\.

Type: Number

**ServerTimestamp**

The server\-side Unix time stamp of the fragment\. For more information, see [PutMedia](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_PutMedia.html)\.

Type: Number

**FrameOffsetInSeconds**

The offset of the frame \(in seconds\) inside the fragment\.

Type: Number 