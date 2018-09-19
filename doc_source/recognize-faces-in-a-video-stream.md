# Recognizing Faces in a Streaming Video<a name="recognize-faces-in-a-video-stream"></a>

Amazon Rekognition Video can search faces in a collection that match faces that are detected in a streaming video\. For more information about collections, see [Searching Faces in a Collection](collections.md)\. The following procedure describes the steps you take to recognize faces in a streaming video\.

## Prerequisites<a name="streaming-video-prerequisites"></a>

To run this procedure, you need to have the AWS SDK for Java installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. 

**To recognize faces in a video stream \(AWS SDK\)**

1. If you haven't already, create an IAM service role to give Amazon Rekognition Video access to your Kinesis video streams and your Kinesis data streams\. Note the ARN\. For more information, see [Giving Access to Your Kinesis Video Streams and Kinesis Data Streams](api-streaming-video-roles.md#api-streaming-video-roles-all-stream)\.

1. [Create a collection](create-collection-procedure.md) and note the collection identifier you used\.

1. [Index the faces](add-faces-to-collection-procedure.md) you want to search for into the collection you created in step 2\.

1. [Create a Kinesis video stream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-createstream.html) and note the stream's Amazon Resource Name \(ARN\)\.

1. [Create a Kinesis data stream](https://docs.aws.amazon.com/streams/latest/dev/learning-kinesis-module-one-create-stream.html)\. Prepend the stream name with *AmazonRekognition* and note the stream's ARN\.

1. [Create the stream processor](streaming-video-starting-analysis.md#streaming-video-creating-stream-processor)\. Pass the following as parameters to [CreateStreamProcessor](API_CreateStreamProcessor.md): a name of your choosing, the Kinesis video stream ARN \(step 4\), the Kinesis data stream ARN \(step 5\), and the collection identifier \(step 2\)\.

1. [Start the stream processor](streaming-video-starting-analysis.md#streaming-video-starting-stream-processor.title) using the stream processor name that you chose in step 6\.

1. Use the [PutMedia](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_PutMedia.html) operation to stream the source video into the Kinesis video stream that you created in step 4\. For more information, see [PutMedia API Example](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-putmedia.html)\.

1. [Consume the analysis output from Amazon Rekognition Video](streaming-video-kinesis-output.md)\.