# Searching Faces in a Collection<a name="collections"></a>

Amazon Rekognition can store information about detected faces in server\-side containers known as collections\. You can use the facial information stored in a collection to search for known faces in images, stored videos and streaming videos\. Amazon Rekognition supports the [IndexFaces](API_IndexFaces.md) operation, which you can use to detect faces in an image and persist information about facial features detected into a collection\. This is an example of a *storage\-based* API operation because the service persists information on the server\. 

To store facial information, you must first create \([CreateCollection](API_CreateCollection.md)\) a face collection in one of the AWS Regions in your account\. You specify this face collection when you call the `IndexFaces` operation\. After you create a face collection and store facial feature information for all faces, you can search the collection for face matches\. To search for faces in an image, call [SearchFacesByImage](API_SearchFacesByImage.md)\. To search for faces in a stored video, call [StartFaceSearch](API_StartFaceSearch.md)\. To search for faces in a streaming video, call [CreateStreamProcessor](API_CreateStreamProcessor.md)\.

**Note**  
The service does not persist actual image bytes\. Instead, the underlying detection algorithm first detects the faces in the input image, extracts facial features into a feature vector for each face, and then stores it in the collection\. Amazon Rekognition uses these feature vectors when performing face matches\.

You can use collections in a variety of scenarios\. For example, you might create a face collection to store scanned badge images using the `IndexFaces` operation\. When an employee enters the building, an image of the employee's face is captured and sent to the `SearchFacesByImage` operation\. If the face match produces a sufficiently high similarity score \(say 99%\), you can authenticate the employee\. 


+ [Managing Collections](managing-collections.md)
+ [Storing Faces in a Face Collection](collections-index-faces.md)
+ [Searching for Faces with Rekognition Image Collection](collections-search-faces.md)
+ [Searching for Faces with Rekognition Video](collections-search-person.md)