# Image and Video Operations<a name="how-it-works-operations-intro"></a>

Amazon Rekognition provides two API sets\. Rekognition Image for analyzing images and Rekognition Video for analyzing stored and streaming videos\. The following topic gives a brief overview of each API set\.

The Rekognition Image and Rekognition Video API can detect or recognize a variety of entities such as faces or objects\. For information about the types of recognition and detection that are supported, see [](how-it-works-types.md)\.

## Rekognition Image Operations<a name="how-it-works-operations-images"></a>

Amazon Rekognition image operations are synchronous\. The input and response are in JSON format\. Amazon Rekognition Image operations analyze an input image that is in \.jpg or \.png image format\. The image passed to a Rekognition Image operation can be stored in an Amazon S3 bucket\. If you are not using the AWS CLI, you can also pass byte64 encoded images bytes directly to an Amazon Rekognition operation\. For more information, see [Working with Images](images.md)\.

## Rekognition Video Operations<a name="how-it-works-operations-video-intro"></a>

Rekognition Video can analyze videos stored in an Amazon S3 bucket and videos streamed through Amazon Kinesis Video Streams\.

Rekognition Video video operations are asynchronous\. With Rekognition Video storage video operations, you start analysis by calling the start operation for the type of analysis you want\. For example, to detect faces in a stored video, call [StartFaceDetection](API_StartFaceDetection.md)\. Once completed, Amazon Rekognition publishes the completion status to an Amazon SNS topic\. To get the results of the analysis operation, you call the get operation for the type of analysis you requested\. For example [GetFaceDetection](API_GetFaceDetection.md)\. For more information, see [Working with Stored Videos](video.md)\. 

With Rekognition Video streaming video operations you can search for faces stored in Rekognition Video collections\. Rekognition Video analyzes a Kinesis video stream and outputs the search results to a Kinesis data stream\. You manage video analysis by creating and using a Rekognition Video stream processor\. For example, you create a stream processor by calling [CreateStreamProcessor](API_CreateStreamProcessor.md)\. For more information, see [Working with Streaming Videos](streaming-video.md)\. 

## Non\-Storage and Storage Based Operations<a name="how-it-works-operations-video-storage"></a>

Amazon Rekognition operations are grouped into the following categories\.

+ **Non\-storage API operations** – In these operations, Amazon Rekognition does not persist any information\. You provide input images and videos, the operation performs the analysis, and returns results, but nothing is saved by Amazon Rekognition\. For more information, see [](how-it-works-storage-non-storage.md#how-it-works-non-storage)\.

+ **Storage\-based API operations** – Amazon Rekognition servers can store detected facial information in containers known as collections\. Amazon Rekognition provides additional API operations you can use to search the persisted face information for face matches\. For more information, see [Storage\-Based API Operations](how-it-works-storage-non-storage.md#how-it-works-storage-based)\.

## Using the AWS SDK or HTTP to Call Amazon Rekognition API Operations<a name="images-java-http"></a>

You can call Amazon Rekognition API operations using either the AWS SDK or directly by using HTTP\. Unless you have a good reason not to, you should always use the AWS SDK\. The Java examples in this section use the [AWS SDK](http://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-install.html)\. A Java project file is not provided, but you can use the [AWS Toolkit for Eclipse](http://docs.aws.amazon.com/AWSToolkitEclipse/latest/GettingStartedGuide/) to develop AWS applications using Java\. 

The [API Reference](API_Reference.md) in this guide covers calling Amazon Rekognition operations using HTTP\. For Java reference information, see [AWS SDK for Java](http://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/index.html)\.

The Amazon Rekognition service endpoints you can use are documented at [AWS Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html#rekognition_region)\. 

When calling Amazon Rekognition with HTTP, use POST HTTP operations\.