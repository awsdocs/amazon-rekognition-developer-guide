# Non\-storage and storage API operations<a name="how-it-works-storage-non-storage"></a>

Amazon Rekognition provides two types of API operations\. They are non\-storage operations where no information is stored by Amazon Rekognition, and storage operations where certain facial information is stored by Amazon Rekognition\. 

## Non\-storage operations<a name="how-it-works-non-storage"></a>

Amazon Rekognition provides the following non\-storage API operations for images:
+ [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html)
+ [DetectFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html) 
+ [CompareFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CompareFaces.html) 
+ [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html) 
+ [DetectProtectiveEquipment](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectProtectiveEquipment.html) 
+ [RecognizeCelebrities](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RecognizeCelebrities.html) 
+ [DetectText](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectText.html) 
+ [GetCelebrityInfo](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetCelebrityInfo.html) 

Amazon Rekognition provides the following non\-storage API operations for videos:
+ [StartLabelDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartlabelDetection.html) 
+ [StartFaceDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceDetection.html) 
+ [StartPersonTracking](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartPersonTracking.html)
+ [StartCelebrityRecognition](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartCelebrityRecognition.html)
+ [StartContentModeration](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartContentModeration.html)

These are referred to as *non\-storage* API operations because when you make the operation call, Amazon Rekognition does not persist any information discovered about the input image\. Like all other Amazon Rekognition API operations, no input image bytes are persisted by non\-storage API operations\. 

The following example scenarios show where you might integrate non\-storage API operations in your application\. These scenarios assume that you have a local repository of images\.

**Example 1: An application that finds images in your local repository that contain specific labels**  
First, you detect labels using the Amazon Rekognition `DetectLabels` operation in each of the images in your repository and build a client\-side index, as shown following:  

```
Label        ImageID

tree          image-1
flower        image-1
mountain      image-1
tulip         image-2
flower        image-2
apple         image-3
```
Then, your application can search this index to find images in your local repository that contain a specific label\. For example, display images that contain a tree\.  
Each label that Amazon Rekognition detects has a confidence value associated\. It indicates the level of confidence that the input image contains that label\. You can use this confidence value to optionally perform additional client\-side filtering on labels depending on your application requirements about the level of confidence in the detection\. For example, if you require precise labels, you might filter and choose only the labels with higher confidence \(such as 95% or higher\)\. If your application doesn't require higher confidence value, you might choose to filter labels with lower confidence value \(closer to 50%\)\.

**Example 2: An application to display enhanced face images**  
First, you can detect faces in each of the images in your local repository using the Amazon Rekognition `DetectFaces` operation and build a client\-side index\. For each face, the operation returns metadata that includes a bounding box, facial landmarks \(for example, the position of mouth and ear\), and facial attributes \(for example, gender\)\. You can store this metadata in a client\-side local index, as shown following:  

```
ImageID     FaceID     FaceMetaData

image-1     face-1     <boundingbox>, etc.
image-1     face-2     <boundingbox>, etc.
image-1     face-3     <boundingbox>, etc.
...
```
In this index, the primary key is a combination of both the `ImageID` and `FaceID`\.  
Then, you can use the information in the index to enhance the images when your application displays them from your local repository\. For example, you might add a bounding box around the face or highlight facial features\.  
 

## Storage\-based API operations<a name="how-it-works-storage-based"></a>

Amazon Rekognition Image supports the [IndexFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_IndexFaces.html) operation, which you can use to detect faces in an image and persist information about facial features detected in an Amazon Rekognition collection\. This is an example of a *storage\-based* API operation because the service persists information on the server\. 

Amazon Rekognition Image provides the following storage API operations:
+ [IndexFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_IndexFaces.html)
+ [ListFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListFaces.html) 
+ [SearchFacesByImage](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFacesByImage.html) 
+ [SearchFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFaces.html) 
+ [DeleteFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteFaces.html) 
+ [DescribeCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeCollection.html) 
+ [DeleteCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteCollection.html)
+ [ListCollections](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListCollections.html)
+ [CreateCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateCollection.html) 

Amazon Rekognition Video provides the following storage API operations:
+ [StartFaceSearch](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceSearch.html) 
+ [CreateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html)

To store facial information, you must first create a face collection in one of the AWS Regions in your account\. You specify this face collection when you call the `IndexFaces` operation\. After you create a face collection and store facial feature information for all faces, you can search the collection for face matches\. For example, you can detect the largest face in an image and search for matching faces in a collection by calling `searchFacesByImage.`

Facial information stored in collections by `IndexFaces` is accessible to Amazon Rekognition Video operations\. For example, you can search a video for persons whose faces match those in an existing collection by calling [StartFaceSearch](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceSearch.html)\.

For information about creating and managing collections, see [Searching faces in a collection](collections.md)\.

**Note**  
The service does not persist actual image bytes\. Instead, the underlying detection algorithm first detects the faces in the input image, extracts facial features into a feature vector for each face, and then stores it in the database\. Amazon Rekognition uses these feature vectors when performing face matches\.

**Example 1: An application that authenticates access to a building**  
You start by creating a face collection to store scanned badge images using the `IndexFaces` operation, which extracts faces and stores them as searchable image vectors\. Then, when an employee enters the building, an image of the employee's face is captured and sent to the `SearchFacesByImage` operation\. If the face match produces a sufficiently high similarity score \(say 99%\), you can authenticate the employee\.