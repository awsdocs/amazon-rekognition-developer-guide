# Tracking People<a name="persons"></a>

Amazon Rekognition Video can track people in videos and provide information such as: 
+ The location of the person in the video frame at the time they were tracked\.
+ Facial landmarks such as the position of the left eye, when detected\. 

With Amazon Rekognition Video you can also search a video for people whose facial metadata is stored in a collection\. For more information, see [Searching for Faces with Amazon Rekognition Video](collections-search-person.md)\.

Amazon Rekognition Video person tracking in videos is an asynchronous operation\. To start the tracking of people in videos call [StartPersonTracking](API_StartPersonTracking.md)\. Amazon Rekognition Video publishes the completion status of the video analysis to an Amazon Simple Notification Service topic\. If the video analysis is succesful, call [GetPersonTracking](API_GetPersonTracking.md) to get results of the video analysis\. 

For information about calling the video recognition API operations, see [Calling Amazon Rekognition Video Operations](api-video.md)\. For an example, see [Tracking People through a Stored Video \(SDK for Java\)](video-sqs-persons.md)\.