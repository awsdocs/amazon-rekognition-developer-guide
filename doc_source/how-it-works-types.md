# Types of analysis<a name="how-it-works-types"></a>

The following are the types of analysis that the Amazon Rekognition Image API and Amazon Rekognition Video API can perform\. For information about the APIs, see [Image and video operations](how-it-works-operations-intro.md)\.

## Labels<a name="how-it-works-labels-intro"></a>

 A *label* refers to any of the following: objects \(for example, flower, tree, or table\), events \(for example, a wedding, graduation, or birthday party\), concepts \(for example, a landscape, evening, and nature\) or activities \(for example, getting out of a car\)\. Amazon Rekognition can detect labels in images and videos\. For more information, see [Detecting labels](labels.md)\.

Rekognition can detect a large list of labels in image and stored video\. Rekognition can also detect a small number of labels in streaming video\.

To detect labels in images, use [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html)\. As part of the [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html) API, you can identify image properties like dominant image colors and image quality\. To achieve this, use DetectLabels with `IMAGE_PROPERTIES` as input parameter\.

To detect labels in stored videos, use [StartLabelDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartLabelDetection.html)\. Detection of dominant image colors and image quality is not supported for stored video\.

To detect labels in streaming video, use [CreateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html)\. Detection of dominant image colors and image quality is not supported for streaming video\.

You can specify what types of labels you want returned for both image and stored video label detection by using inclusive and exclusive filtering options\.

## Custom labels<a name="how-it-works-custom-labels-intro"></a>

Amazon Rekognition Custom Labels can identify the objects and scenes in images that are specific to your business needs by training a machine learning model\. For example, you can train a model to detect logos or detect engineering machine parts on an assembly line\.

**Note**  
For information about Amazon Rekognition Custom Labels, see the [Amazon Rekognition Custom Labels Developer Guide](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/what-is.html)\.

Amazon Rekognition provides a console that you use to create, train, evaluate, and run a machine learning model\. For more information, see [Getting Started with Amazon Rekognition Custom Labels](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/gs-introduction.html) in the *Amazon Rekognition Custom Labels Develope Guide*\. You can also use the Amazon Rekognition Custom Labels API to train and run a model\. For more information, see [Getting Started with the Amazon Rekognition Custom Labels SDK](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/gs-cli.html) in the *Amazon Rekognition CustomLabels Developer Guide*\.

To analyze images using a trained model, use [DetectCustomLabels](https://docs.aws.amazon.com/rekognition/latest/dg/API_DetectCustomLabels)\.

## Faces<a name="how-it-works-faces-intro"></a>

Amazon Rekognition can detect faces in images and stored videos\. With Amazon Rekognition, you can get information about where faces are detected in an image or video, facial landmarks such as the position of eyes, and detected emotions such as happy or sad\. You can also compare a face in an image with faces detected in another image\. Information about faces can also be stored for later retrieval\. For more information, see [Detecting and analyzing faces](faces.md)\.

To detect faces in images, use [DetectFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html)\. To detect faces in stored videos, use [StartFaceDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceDetection.html)\.

## Face search<a name="how-it-works-search-faces-intro"></a>

Amazon Rekognition can search for faces\. Facial information is indexed into a container known as a collection\. Face information in the collection can then be matched with faces detected in images, stored videos, and streaming video\. For more information, [Searching faces in a collection](collections.md)\.

To search for known faces in images, use [DetectFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html)\. To search for known faces in stored videos, use [StartFaceDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceDetection.html)\. To search for known faces in streaming videos, use [CreateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html)\.

## People paths<a name="how-it-works-persons-intro"></a>

Amazon Rekognition can track the paths of people detected in a stored video\. Amazon Rekognition Video provides path tracking, face details, and in\-frame location information for people detected in a video\. For more information, see [People pathing](persons.md)\. 

To detect people in stored videos, use [StartPersonTracking](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartPersonTracking.html)\.

## Personal Protective Equipment<a name="how-it-works-ppe-intro"></a>

 Amazon Rekognition can detect Personal Protective Equipment \(PPE\) worn by persons detected in an image\. Amazon Rekognition detects face covers, hand covers, and head covers\. Amazon Rekognition predicts if an item of PPE covers the appropriate body part\. You can also get bounding boxes for detected persons and PPE items\. For more information, see [Detecting personal protective equipment](ppe-detection.md)\. 

To detect PPE in images, use [DetectProtectiveEquipment](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectProtectiveEquipment.html)\.

## Celebrities<a name="how-it-works-celebrities-intro"></a>

 Amazon Rekognition can recognize thousands of celebrities in images and stored videos\. You can get information about where a celebrity's face is located on an image, facial landmarks, and the pose of a celebrity's face\. You can get tracking information for celebrities as they appear throughout a stored video\. You can also get further information about a recognized celebrity, like the emotion expressed, and presentation of gender\. For more information, see [Recognizing celebrities](celebrities.md)\. 

To recognize celebrities in images, use [RecognizeCelebrities](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RecognizeCelebrities.html)\. To recognize celebrities in stored videos, use [StartCelebrityRecognition](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartCelebrityRecognition.html)\.

## Text detection<a name="how-it-works-text-intro"></a>

Amazon Rekognition Text in Image can detect text in images and convert it into machine\-readable text\. For more information, see [Detecting text](text-detection.md)\.

To detect text in images, use [DetectText](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectText.html)\.

## Inappropriate or offensive content<a name="how-it-works-moderation-intro"></a>

Amazon Rekognition can analyze images and stored videos for adult and violent content\. For more information, see [Moderating content](moderation.md)\.

To detect unsafe images, use [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html)\. To detect unsafe stored videos, use [StartContentModeration](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartContentModeration.html)\.