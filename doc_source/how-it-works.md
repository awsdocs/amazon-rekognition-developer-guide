# Amazon Rekognition: How It Works<a name="how-it-works"></a>

Amazon Rekognition provides two API sets\. They are Rekognition Image, for analyzing images, and Rekognition Video, for analyzing videos\.

Both API perform detection and recognition analysis of images and videos to provide insights you can use in your applications\. For example, you could use Rekognition Image to enhance the customer experience for a photo management application\. When a customer uploads a photo, your application can use Rekognition Image to detect real\-world objects or faces in the image\. After your application stores the information returned from Rekognition Image, the user could then query their photo collection for photos with a specific object or face\. Deeper querying is possible\. For example, the user could query for faces that are smiling or query for faces that are a certain age\.

For video applications, You could use Rekognition Video to create a surveilance application\. Rekognition Video can track where a person is detected throughout a stored video\. Alternatively, you can use Rekognition Video to search a streaming video for persons whose facial descriptions match facial descriptions already stored by Amazon Rekognition\. 

The Amazon Rekognition API makes deep learning image analysis easy to use\. For example, [RecognizeCelebrities](API_RecognizeCelebrities.md) returns information for up to 100 celebrities detected in an image\. This includes information about where celebrity faces are detected on the image and where to get further information about the celebrity\.

The following information covers the types of analysis that Amazon Rekognition provides and an overview of Rekognition Image and Rekognition Video operations\. Also covered is the difference between non\-storage and storage operations\.

**Topics**
+ [Types of Detection and Recognition](how-it-works-types.md)
+ [Image and Video Operations](how-it-works-operations-intro.md)
+ [Non\-Storage and Storage API Operations](how-it-works-storage-non-storage.md)
+ [Model Versioning](face-detection-model.md)