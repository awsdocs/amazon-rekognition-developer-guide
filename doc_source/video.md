# Working with Stored Videos<a name="video"></a>

Amazon Rekognition Video is an API that you can use to analyze videos\. With Rekognition Video, you can detect labels, faces, people, celebrities, and adult \(suggestive and explicit\) content in videos that are stored in an Amazon Simple Storage Service \(Amazon S3\) bucket\. You can use Rekognition Video in categories such as media/entertainment and surveillance\. Previously, scanning videos for objects or people would have taken many hours of error\-prone viewing by a human being\. Rekognition Video automates the detection of items and when they occur throughout a video\.

This section covers the types of detection and recognition that Rekognition Video can perform, an overview of the API, and examples for using Rekognition Video\.


+ [Types of Detection and Recognition](#video-recognition-types)
+ [Rekognition Video API Overview](#video-api-overview)
+ [Calling Rekognition Video Operations](api-video.md)
+ [Configuring Rekognition Video](api-video-roles.md)
+ [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md)
+ [Analyzing a Video with the AWS Command Line Interface](video-cli-commands.md)
+ [Reference: Video Analysis Results Notification](video-notification-payload.md)
+ [Troubleshooting Rekognition Video](video-troubleshooting.md)

## Types of Detection and Recognition<a name="video-recognition-types"></a>

You can use Rekognition Video to analyze videos for the following information:

+ [Labels](labels.md)

+ [Faces](faces.md)

+ [People](persons.md)

+ [Celebrities](celebrities.md)

+ [Suggestive and explicit adult content](moderation.md)

For more information, see [Amazon Rekognition: How It Works](how-it-works.md)\.

## Rekognition Video API Overview<a name="video-api-overview"></a>

Rekognition Video processes a video that's stored in an Amazon S3 bucket\. The design pattern is an asynchronous set of operations\. You start video analysis by calling a `Start` operation such as [StartLabelDetection](API_StartLabelDetection.md)\. The completion status of the request is published to an Amazon Simple Notification Service \(Amazon SNS\) topic\. To get the completion status from the Amazon SNS topic, you can use an Amazon Simple Queue Service \(Amazon SQS\) queue or an AWS Lambda function\. After you have the completion status, you call a `Get` operation, such as [GetLabelDetection](API_GetLabelDetection.md), to get the results of the request\. 

The following diagram shows the process for detecting labels in a video that's stored in an Amazon S3 bucket\. In the diagram, an Amazon SQS queue gets the completion status from the Amazon SNS topic\. Alternatively, you can use an AWS Lambda function\. 

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/VideoRekognition.png)

The process is the same for detecting faces and people\. The following table lists the `Start` and `Get` operations for each of the non\-storage Amazon Rekognition operations\.


| Detection | Start Operation | Get Operation | 
| --- | --- | --- | 
|  People  |  [StartPersonTracking](API_StartPersonTracking.md)  |  [GetPersonTracking](API_GetPersonTracking.md)  | 
|  Faces  |  [StartFaceDetection](API_StartFaceDetection.md)  |  [GetFaceDetection](API_GetFaceDetection.md)  | 
|  Labels  |  [StartLabelDetection](API_StartLabelDetection.md)  |  [GetLabelDetection](API_GetLabelDetection.md)  | 
|  Celebrities  |  [StartCelebrityRecognition](API_StartCelebrityRecognition.md)  |  [GetCelebrityRecognition](API_GetCelebrityRecognition.md)  | 
|  Explicit or suggestive adult content  |  [StartContentModeration](API_StartContentModeration.md)  |  [GetContentModeration](API_GetContentModeration.md)  | 

For `Get` operations other than `GetCelebrityRecognition`, Rekognition Video returns tracking information for when entities are detected throughout the input video\. 

For more information about using Rekognition Video, see [Calling Rekognition Video Operations](api-video.md)\. For an example that does video analysis by using Amazon SQS, see [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md)\. For AWS CLI examples, see [Analyzing a Video with the AWS Command Line Interface](video-cli-commands.md)\.

### Video Formats and Storage<a name="video-storage-formats"></a>

Amazon Rekognition operations can analyze videos that are stored in Amazon S3 buckets\. The video must be encoded using the H\.264 codec\. The supported file formats are MPEG\-4 and MOV\. 

A codec is software or hardware that compresses data for faster delivery and decompresses received data into its original form\. The H\.264 codec is commonly used for recording, compressing, and distributing video content\. A video file format can contain one or more codecs\. If your MOV or MPEG\-4 format video file doesn't work with Rekognition Video, check that the codec used to encode the video is H\.264\.

The maximum file size for a stored video is 8GB\.

### Searching for People<a name="video-searching-persons-overview"></a>

You can use facial metadata that's stored in a collection to search for people in a video\. For example, you can search an archived surveillance video for a specific person or for multiple people\. You store facial metadata from source images in a collection by using the [IndexFaces](API_IndexFaces.md) operation\. You can then use [StartFaceSearch](API_StartFaceSearch.md) to start asynchronously searching for faces in the collection\. You use [GetFaceSearch](API_GetFaceSearch.md) to get the search results\. For more information, see [Searching for Faces with Rekognition Video](collections-search-person.md)\. Searching for people is an example of a storage\-based Amazon Rekognition operation\. For more information, see [Storage\-Based API Operations](how-it-works-storage-non-storage.md#how-it-works-storage-based)\.

You can also search for people in a streaming video\. For more information, see [Working with Streaming Videos](streaming-video.md)\.