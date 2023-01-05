# How Amazon Rekognition works<a name="how-it-works"></a>

Amazon Rekognition provides two API sets\. You use Amazon Rekognition Image for analyzing images, and Amazon Rekognition Video for analyzing videos\.

Both APIs analyze images and videos to provide insights you can use in your applications\. For example, you could use Amazon Rekognition Image to enhance the customer experience for a photo management application\. When a customer uploads a photo, your application can use Amazon Rekognition Image to detect real\-world objects or faces in the image\. After your application stores the information returned from Amazon Rekognition Image, the user could then query their photo collection for photos with a specific object or face\. Deeper querying is possible\. For example, the user could query for faces that are smiling or query for faces that are a certain age\.

You can use Amazon Rekognition Video to track the path of people in a stored video\. Alternatively, you can use Amazon Rekognition Video to search a streaming video for persons whose facial descriptions match facial descriptions already stored by Amazon Rekognition\. 

The Amazon Rekognition API makes deep learning image analysis easy to use\. For example, [RecognizeCelebrities](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RecognizeCelebrities.html) returns information for up to 100 celebrities detected in an image\. This includes information about where celebrity faces are detected on the image and where to get further information about the celebrity\.

The following information covers the types of analysis that Amazon Rekognition provides and an overview of Amazon Rekognition Image and Amazon Rekognition Video operations\. Also covered is the difference between non\-storage and storage operations\.

**Topics**
+ [Types of analysis](how-it-works-types.md)
+ [Image and video operations](how-it-works-operations-intro.md)
+ [Non\-storage and storage API operations](how-it-works-storage-non-storage.md)
+ [Model versioning](face-detection-model.md)