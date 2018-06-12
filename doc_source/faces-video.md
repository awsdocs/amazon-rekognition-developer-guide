# Detecting Faces in a Stored Video<a name="faces-video"></a>

Amazon Rekognition Video can detect faces in videos that are stored in an Amazon S3 bucket and provide information such as: 
+ The time or times faces are detected in a video\.
+ The location of faces in the video frame at the time they were detected\.
+ Facial landmarks such as the position of the left eye\. 

## Using Amazon Rekognition Video Face Operations with Video<a name="video-face-overview"></a>

Amazon Rekognition Video face detection in videos is an asynchronous operation\. To start the detection of persons in videos, call [StartFaceDetection](API_StartFaceDetection.md)\. Amazon Rekognition Video publishes the completion status of the video analysis to an Amazon Simple Notification Service \(Amazon SNS\) topic\. If the video analysis is successful, you can call [GetFaceDetection](API_GetFaceDetection.md) to get results of the video analysis\. 

For information about calling the video recognition API operations, see [Calling Amazon Rekognition Video Operations](api-video.md)\. For an example, see [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md)\.