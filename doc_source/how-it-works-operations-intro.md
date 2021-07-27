# Image and video operations<a name="how-it-works-operations-intro"></a>

Amazon Rekognition provides two API sets\. You use Amazon Rekognition Image for analyzing images, and Amazon Rekognition Video for analyzing stored and streaming videos\. The following topic gives a brief overview of each API set\.

The Amazon Rekognition Image and Amazon Rekognition Video API can detect a variety of entities such as faces or objects\. For information about the types of comparison and detection that are supported, see [Types of analysis](how-it-works-types.md)\.

## Amazon Rekognition Image operations<a name="how-it-works-operations-images"></a>

Amazon Rekognition image operations are synchronous\. The input and response are in JSON format\. Amazon Rekognition Image operations analyze an input image that is in \.jpg or \.png image format\. The image passed to an Amazon Rekognition Image operation can be stored in an Amazon S3 bucket\. If you are not using the AWS CLI, you can also pass Base64 encoded images bytes directly to an Amazon Rekognition operation\. For more information, see [Working with images](images.md)\.

## Amazon Rekognition Video operations<a name="how-it-works-operations-video-intro"></a>

Amazon Rekognition Video can analyze videos stored in an Amazon S3 bucket and videos streamed through Amazon Kinesis Video Streams\.

Amazon Rekognition Video video operations are asynchronous\. With Amazon Rekognition Video storage video operations, you start analysis by calling the start operation for the type of analysis you want\. For example, to detect faces in a stored video, call [StartFaceDetection](API_StartFaceDetection.md)\. Once completed, Amazon Rekognition publishes the completion status to an Amazon SNS topic\. To get the results of the analysis operation, you call the get operation for the type of analysis you requested—for example, [GetFaceDetection](API_GetFaceDetection.md)\. For more information, see [Working with stored videos](video.md)\. 

With Amazon Rekognition Video streaming video operations, you can search for faces stored in Amazon Rekognition Video collections\. Amazon Rekognition Video analyzes a Kinesis video stream and outputs the search results to a Kinesis data stream\. You manage video analysis by creating and using an Amazon Rekognition Video stream processor\. For example, you create a stream processor by calling [CreateStreamProcessor](API_CreateStreamProcessor.md)\. For more information, see [Working with streaming videos](streaming-video.md)\. 

## Non\-storage and storage\-based operations<a name="how-it-works-operations-video-storage"></a>

Amazon Rekognition operations are grouped into the following categories\.
+ **Non\-storage API operations** – In these operations, Amazon Rekognition doesn't persist any information\. You provide input images and videos, the operation performs the analysis, and returns results, but nothing is saved by Amazon Rekognition\. For more information, see [Non\-storage operations](how-it-works-storage-non-storage.md#how-it-works-non-storage)\.
+ **Storage\-based API operations** – Amazon Rekognition servers can store detected facial information in containers known as collections\. Amazon Rekognition provides additional API operations you can use to search the persisted face information for face matches\. For more information, see [Storage\-based API operations](how-it-works-storage-non-storage.md#how-it-works-storage-based)\.

## Using the AWS SDK or HTTP to call Amazon Rekognition API operations<a name="images-java-http"></a>

You can call Amazon Rekognition API operations using either the AWS SDK or directly by using HTTP\. Unless you have a good reason not to, you should always use the AWS SDK\. The Java examples in this section use the [AWS SDK](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup-install.html)\. A Java project file is not provided, but you can use the [AWS Toolkit for Eclipse](https://docs.aws.amazon.com/AWSToolkitEclipse/latest/GettingStartedGuide/) to develop AWS applications using Java\. 

The \.NET examples in this section use the [AWS SDK for \.NET](https://docs.aws.amazon.com/sdk-for-net/latest/developer-guide/welcome.html)\. You can use the [AWS Toolkit for Visual Studio](https://docs.aws.amazon.com/AWSToolkitVS/latest/UserGuide/welcome.html) to develop AWS applications using \.NET\. It includes helpful templates and the AWS Explorer for deploying applications and managing services\. 

The [API Reference](API_Reference.md) in this guide covers calling Amazon Rekognition operations using HTTP\. For Java reference information, see [AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/latest/reference/index.html)\.

The Amazon Rekognition service endpoints you can use are documented at [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#rekognition_region)\. 

When calling Amazon Rekognition with HTTP, use POST HTTP operations\.