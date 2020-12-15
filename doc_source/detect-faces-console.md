# Exercise 2: Analyze faces in an image \(console\)<a name="detect-faces-console"></a>

This section shows you how to use the Amazon Rekognition console to detect faces and analyze facial attributes in an image\. When you provide an image that contains a face as input, the service detects the face in the image, analyzes the facial attributes of the face, and then returns a percent confidence score for the face and the facial attributes detected in the image\. For more information, see [How Amazon Rekognition works](how-it-works.md)\.

For example, if you choose the following sample image as input, Amazon Rekognition detects it as a face and returns confidence scores for the face and the facial attributes detected\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/sample-detect-faces.png)

The following shows the sample response\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/detect-faces-confidence-score.png)

If there are multiple faces in the input image, Rekognition detects up to 100 faces in the image\. Each face detected is marked with a square\. When you click the area marked with a square on a face, Rekognition displays the confidence score of that face and its attributes detected in the **Faces \| Confidence** pane\. 

## Analyze faces in an image you provide<a name="detect-faces-own-image"></a>

You can upload your own image or provide the URL to the image in the Amazon Rekognition console\.

**Note**  
The image must be less than 5MB in size and must be of JPEG or PNG format\.

**To analyze a face in an image you provide**

1. Open the Amazon Rekognition console at [https://console\.aws\.amazon\.com/rekognition/](https://console.aws.amazon.com/rekognition/)\.

1. Choose **Facial analysis**\.

1. Do one of the following: 
   + Upload an image – Choose **Upload**, go to the location where you stored your image, and then select the image\. 
   + Use a URL – Type the URL in the text box, and then choose **Go**\.

1. View the confidence score of one the faces detected and its facial attributes in the **Faces \| Confidence** pane\.

1. If there are multiple faces in the image, choose one of the other faces to see its attributes and scores\.