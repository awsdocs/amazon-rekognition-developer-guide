# Setting up your Amazon Rekognition Video and Amazon Kinesis resources<a name="setting-up-your-amazon-rekognition-streaming-video-resources"></a>

 The following procedures describe the steps you take to provision the Kinesis video stream and other resources that are used to recognize faces in a streaming video\.

## Prerequisites<a name="streaming-video-prerequisites"></a>

To run this procedure, you need to have the AWS SDK for Java installed\. For more information, see [Getting started with Amazon Rekognition](getting-started.md)\. The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Actions Defined by Amazon Rekognition](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonrekognition.html#amazonrekognition-actions-as-permissions) in the *IAM User Guide*\. 

**To recognize faces in a video stream \(AWS SDK\)**

1. If you haven't already, create an IAM service role to give Amazon Rekognition Video access to your Kinesis video streams and your Kinesis data streams\. Note the ARN\. For more information, see [Giving access to streams using AmazonRekognitionServiceRole](api-streaming-video-roles.md#api-streaming-video-roles-all-stream)\.

1. [Create a collection](create-collection-procedure.md) and note the collection identifier you used\.

1. [Index the faces](add-faces-to-collection-procedure.md) you want to search for into the collection you created in step 2\.

1. [Create a Kinesis video stream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-createstream.html) and note the stream's Amazon Resource Name \(ARN\)\.

1. [Create a Kinesis data stream](https://docs.aws.amazon.com/streams/latest/dev/learning-kinesis-module-one-create-stream.html)\. Prepend the stream name with *AmazonRekognition* and note the stream's ARN\.

You can then [create the face search stream processor](rekognition-video-stream-processor-search-faces.md#streaming-video-creating-stream-processor) and [start the stream processor](rekognition-video-stream-processor-search-faces.md#streaming-video-starting-stream-processor) using the stream processor name that you chose\.

**Note**  
 You should start the stream processor only after you have verified you can ingest media into the Kinesis video stream\. 

## Streaming video into Amazon Rekognition Video<a name="video-streaming-kinesisvideostreams-stream"></a>

To stream video into Amazon Rekognition Video, you use the Amazon Kinesis Video Streams SDK to create and use a Kinesis video stream\. The `PutMedia` operation writes video data *fragments* into a Kinesis video stream that Amazon Rekognition Video consumes\. Each video data fragment is typically 2–10 seconds in length and contains a self\-contained sequence of video frames\. Amazon Rekognition Video supports H\.264 encoded videos, which can have three types of frames \(I, B, and P\)\. For more information, see [Inter Frame](https://en.wikipedia.org/wiki/Inter_frame)\. The first frame in the fragment must be an I\-frame\. An I\-frame can be decoded independent of any other frame\. 

As video data arrives into the Kinesis video stream, Kinesis Video Streams assigns a unique number to the fragment\. For an example, see [PutMedia API Example](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-putmedia.html)\.
+  If you are streaming from an Matroska \(MKV\) encoded source, use the [PutMedia](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_PutMedia.html) operation to stream the source video into the Kinesis video stream that you created\. For more information, see [PutMedia API Example](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-putmedia.html)\. 
+  If you are streaming from a device camera, see [Streaming using a GStreamer plugin](streaming-using-gstreamer-plugin.md)\.