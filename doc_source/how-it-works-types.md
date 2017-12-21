# Types of Detection and Recognition<a name="how-it-works-types"></a>

The following are the types of detection and recognition that the Rekognition Image API and Rekognition Video API can perform\. For information about the APIs, see [](how-it-works-operations-intro.md)\.

## Labels<a name="how-it-works-labels-intro"></a>

 A *label* refers to any of the following: objects \(for example, flower, tree, or table\), events \(for example, a wedding, graduation, or birthday party\), concepts \(for example, a landscape, evening, and nature\) or activities \(for example, getting out of a car\)\. Amazon Rekognition can detect labels in images and videos\. However activities are not detected in images\. For more information, see [Detecting Objects and Scenes](labels.md)\.

To detect labels in images, use [DetectLabels](API_DetectLabels.md)\. To detect labels in stored videos, use [StartLabelDetection](API_StartLabelDetection.md)\.

## Faces<a name="how-it-works-faces-intro"></a>

Amazon Rekognition can detect faces in images and stored videos\. With Amazon Rekognition you can get information about where faces are detected in an image or video, facial landmarks such as the position of eyes, and detected emotions such as happy or sad\. You can also compare a face in an image with faces detected in another image\. Information about faces can also be stored for later retrieval\. For more information, see [Detecting and Analyzing Faces](faces.md)\.

To detect faces in images, use [DetectFaces](API_DetectFaces.md)\. To detect faces in stored videos, use [StartFaceDetection](API_StartFaceDetection.md)\.

## Face Search<a name="how-it-works-search-faces-intro"></a>

Amazon Rekognition can search for faces\. Facial information is indexed into a container known as a collection\. Face information in the collection can then be matched with faces detected in images, stored videos, and streaming video\. For more information, [Searching Faces in a Collection](collections.md)\.

To search for known faces in images, use [DetectFaces](API_DetectFaces.md)\. To search for known faces in stored videos, use [StartFaceDetection](API_StartFaceDetection.md)\. To search for known faces in streaming videos, use [CreateStreamProcessor](API_CreateStreamProcessor.md)\.

## Persons<a name="how-it-works-persons-intro"></a>

Amazon Rekognition can track persons in a stored video\. Rekognition Video provides tracking, face details, and in\-frame location information for persons detected in a video\. Persons cannot be detected in images\. For more information, see [Tracking People](persons.md)\. 

To detect persons in stored videos, use [StartPersonTracking](API_StartPersonTracking.md)\.

## Celebrities<a name="how-it-works-celebrities-intro"></a>

 Amazon Rekognition can recognize thousand of celebrities in images and stored videos\. You can get information about where a celebrity's face is located on an image, facial landmarks and the pose of a celebrity's face\. You can get tracking information for celebrities as the appear throughout a stored video\. You can also get further information about a recognize celebrity\. For more information, see [Recognizing Celebrities](celebrities.md)\. 

To recognize celebrities in images, use [RecognizeCelebrities](API_RecognizeCelebrities.md)\. To recognize celebrities in stored videos, use [StartCelebrityRecognition](API_StartCelebrityRecognition.md)\.

## Unsafe Content<a name="how-it-works-moderation-intro"></a>

Amazon Rekognition can analyse images and stored videos for explicit or suggestive adult content\. For more information, see [Detecting Unsafe Content](moderation.md)\.

To detect unsage images, use [DetectModerationLabels](API_DetectModerationLabels.md)\. To detect unsafe stored videos, use [StartContentModeration](API_StartContentModeration.md)\.