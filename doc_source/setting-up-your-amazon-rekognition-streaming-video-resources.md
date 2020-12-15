# Setting up your Amazon Rekognition Video and Amazon Kinesis resources<a name="setting-up-your-amazon-rekognition-streaming-video-resources"></a>

Amazon Rekognition Video can search faces in a collection that match faces that are detected in a streaming video\. For more information about collections, see [Searching faces in a collection](collections.md)\. The following procedure describes the steps you take to provision the Kinesis video stream and Kinesis data stream that will be used to recognize faces in a streaming video\.

## Prerequisites<a name="streaming-video-prerequisites"></a>

To run this procedure, you need to have the AWS SDK for Java installed\. For more information, see [Getting started with Amazon Rekognition](getting-started.md)\. The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Actions Defined by Amazon Rekognition](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonrekognition.html#amazonrekognition-actions-as-permissions) in the *IAM User Guide*\. 

**To recognize faces in a video stream \(AWS SDK\)**

1. If you haven't already, create an IAM service role to give Amazon Rekognition Video access to your Kinesis video streams and your Kinesis data streams\. Note the ARN\. For more information, see [Giving access to your Kinesis video streams and Kinesis data streams](api-streaming-video-roles.md#api-streaming-video-roles-all-stream)\.

1. [Create a collection](create-collection-procedure.md) and note the collection identifier you used\.

1. [Index the faces](add-faces-to-collection-procedure.md) you want to search for into the collection you created in step 2\.

1. [Create a Kinesis video stream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-createstream.html) and note the stream's Amazon Resource Name \(ARN\)\.

1. [Create a Kinesis data stream](https://docs.aws.amazon.com/streams/latest/dev/learning-kinesis-module-one-create-stream.html)\. Prepend the stream name with *AmazonRekognition* and note the stream's ARN\.

1. [Create the stream processor](using-rekognition-video-stream-processor.md#streaming-video-creating-stream-processor)\. Pass the following as parameters to [CreateStreamProcessor](API_CreateStreamProcessor.md): a name of your choosing, the Kinesis video stream ARN \(step 4\), the Kinesis data stream ARN \(step 5\), and the collection identifier \(step 2\)\.

1. [Start the stream processor](using-rekognition-video-stream-processor.md#streaming-video-starting-stream-processor.title) using the stream processor name that you chose in step 6\.
**Note**  
 You should start the stream processor only after you have verified you can ingest media into the Kinesis video stream\. 

## See next:<a name="see-next"></a>
+  If you are streaming from an Matroska \(MKV\) encoded source, use the [PutMedia](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_PutMedia.html) operation to stream the source video into the Kinesis video stream that you created\. For more information, see [PutMedia API Example](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-putmedia.html)\. 
+  If you are streaming from a device camera, see [Streaming using a GStreamer plugin](streaming-using-gstreamer-plugin.md)\.