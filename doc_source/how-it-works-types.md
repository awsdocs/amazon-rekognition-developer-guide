# Types of analysis<a name="how-it-works-types"></a>

The following are the types of analysis that the Amazon Rekognition Image API and Amazon Rekognition Video API can perform\. For information about the APIs, see [Image and video operations](how-it-works-operations-intro.md)\.

## Labels<a name="how-it-works-labels-intro"></a>

 A *label* refers to any of the following: objects \(for example, flower, tree, or table\), events \(for example, a wedding, graduation, or birthday party\), concepts \(for example, a landscape, evening, and nature\) or activities \(for example, getting out of a car\)\. Amazon Rekognition can detect labels in images and videos\. However activities are not detected in images\. For more information, see [Detecting objects and scenes](labels.md)\.

To detect labels in images, use [DetectLabels](API_DetectLabels.md)\. To detect labels in stored videos, use [StartLabelDetection](API_StartLabelDetection.md)\.

## Custom labels<a name="how-it-works-custom-labels-intro"></a>

Amazon Rekognition Custom Labels can identify the objects and scenes in images that are specific to your business needs by training a machine learning model\. For example, you can train a model to detect logos or detect engineering machine parts on an assembly line\.

**Note**  
For information about Amazon Rekognition Custom Labels, see the [Amazon Rekognition Custom Labels Developer Guide](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/what-is.html)\.

Amazon Rekognition provides a console that you use to create, train, evaluate, and run a machine learning model\. For more information, see [Getting Started with Amazon Rekognition Custom Labels](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/gs-introduction.html) in the *Amazon Rekognition Custom Labels Develope Guide*\. You can also use the Amazon Rekognition Custom Labels API to train and run a model\. For more information, see [Getting Started with the Amazon Rekognition Custom Labels SDK](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/gs-cli.html) in the *Amazon Rekognition CustomLabels Developer Guide*\.

To analyze images using a trained model, use [DetectCustomLabels](https://docs.aws.amazon.com/rekognition/latest/dg/API_DetectCustomLabels)\.

## Faces<a name="how-it-works-faces-intro"></a>

Amazon Rekognition can detect faces in images and stored videos\. With Amazon Rekognition, you can get information about where faces are detected in an image or video, facial landmarks such as the position of eyes, and detected emotions such as happy or sad\. You can also compare a face in an image with faces detected in another image\. Information about faces can also be stored for later retrieval\. For more information, see [Detecting and analyzing faces](faces.md)\.

To detect faces in images, use [DetectFaces](API_DetectFaces.md)\. To detect faces in stored videos, use [StartFaceDetection](API_StartFaceDetection.md)\.

## Face search<a name="how-it-works-search-faces-intro"></a>

Amazon Rekognition can search for faces\. Facial information is indexed into a container known as a collection\. Face information in the collection can then be matched with faces detected in images, stored videos, and streaming video\. For more information, [Searching faces in a collection](collections.md)\.

To search for known faces in images, use [DetectFaces](API_DetectFaces.md)\. To search for known faces in stored videos, use [StartFaceDetection](API_StartFaceDetection.md)\. To search for known faces in streaming videos, use [CreateStreamProcessor](API_CreateStreamProcessor.md)\.

## People paths<a name="how-it-works-persons-intro"></a>

Amazon Rekognition can track the paths of people detected in a stored video\. Amazon Rekognition Video provides path tracking, face details, and in\-frame location information for people detected in a video\. For more information, see [People pathing](persons.md)\. 

To detect people in stored videos, use [StartPersonTracking](API_StartPersonTracking.md)\.

## Personal Protective Equipment<a name="how-it-works-ppe-intro"></a>

 Amazon Rekognition can detect Personal Protective Equipment \(PPE\) worn by persons detected in an image\. Amazon Rekognition detects face covers, hand covers, and head covers\. Amazon Rekognition predicts if an item of PPE covers the appropriate body part\. You can also get bounding boxes for detected persons and PPE items\. For more information, see [Detecting personal protective equipment](ppe-detection.md)\. 

To detect PPE in images, use [DetectProtectiveEquipment](API_DetectProtectiveEquipment.md)\.

## Celebrities<a name="how-it-works-celebrities-intro"></a>

 Amazon Rekognition can recognize thousands of celebrities in images and stored videos\. You can get information about where a celebrity's face is located on an image, facial landmarks, and the pose of a celebrity's face\. You can get tracking information for celebrities as they appear throughout a stored video\. You can also get further information about a recognized celebrity\. For more information, see [Recognizing celebrities](celebrities.md)\. 

To recognize celebrities in images, use [RecognizeCelebrities](API_RecognizeCelebrities.md)\. To recognize celebrities in stored videos, use [StartCelebrityRecognition](API_StartCelebrityRecognition.md)\.

## Text detection<a name="how-it-works-text-intro"></a>

Amazon Rekognition Text in Image can detect text in images and convert it into machine\-readable text\. For more information, see [Detecting text](text-detection.md)\.

To detect text in images, use [DetectText](API_DetectText.md)\.

## Inappropriate or offensive content<a name="how-it-works-moderation-intro"></a>

Amazon Rekognition can analyze images and stored videos for adult and violent content\. For more information, see [Content moderation](moderation.md)\.

To detect unsafe images, use [DetectModerationLabels](API_DetectModerationLabels.md)\. To detect unsafe stored videos, use [StartContentModeration](API_StartContentModeration.md)\.