# Searching Faces in a Collection<a name="collections"></a>

Amazon Rekognition can store information about detected faces in server\-side containers known as collections\. You can use the facial information that's stored in a collection to search for known faces in images, stored videos, and streaming videos\. Amazon Rekognition supports the [IndexFaces](API_IndexFaces.md) operation\. You can use this operation to detect faces in an image and persist information about facial features that are detected into a collection\. This is an example of a *storage\-based* API operation because the service persists information on the server\. 

To store facial information, you must first create \([CreateCollection](API_CreateCollection.md)\) a face collection in one of the AWS Regions in your account\. You specify this face collection when you call the `IndexFaces` operation\. After you create a face collection and store facial feature information for all faces, you can search the collection for face matches\. To search for faces in an image, call [SearchFacesByImage](API_SearchFacesByImage.md)\. To search for faces in a stored video, call [StartFaceSearch](API_StartFaceSearch.md)\. To search for faces in a streaming video, call [CreateStreamProcessor](API_CreateStreamProcessor.md)\.

**Note**  
The service doesn't persist actual image bytes\. Instead, the underlying detection algorithm first detects the faces in the input image, extracts facial features into a feature vector for each face, and then stores it in the collection\. Amazon Rekognition uses these feature vectors when performing face matches\.

You can use collections in a variety of scenarios\. For example, you might create a face collection to store scanned badge images by using the `IndexFaces` operation\. When an employee enters the building, an image of the employee's face is captured and sent to the `SearchFacesByImage` operation\. If the face match produces a sufficiently high similarity score \(say 99%\), you can authenticate the employee\. 

## Managing Collections<a name="managing-collections"></a>

The face collection is the primary Amazon Rekognition resource, and each face collection you create has a unique Amazon Resource Name \(ARN\)\. You create each face collection in a specific AWS Region in your account\. When a collection is created, it's associated with the most recent version of the face detection model\. For more information, see [Model Versioning](face-detection-model.md)\. 

You can perform the following management operations on a collection\.
+ Create a collection with [CreateCollection](API_CreateCollection.md)\. For more information, see [Creating a Collection](create-collection-procedure.md)\.
+ List the available collections with [ListCollections](API_ListCollections.md)\. For more information, see [Listing Collections](list-collection-procedure.md)\.
+ Describe a collection with [DescribeCollection](API_DescribeCollection.md)\. For more information, see [Describing a Collection](describe-collection-procedure.md)\.
+ Delete a collection with [DeleteCollection](API_DeleteCollection.md)\. For more information, see [Deleting a Collection](delete-collection-procedure.md)\.

## Managing Faces in a Collection<a name="collections-index-faces"></a>

After you create a face collection, you can store faces in it\. Amazon Rekognition provides the following operations for managing faces in a collection\.
+  The [IndexFaces](API_IndexFaces.md) operation detects faces in the input image \(JPEG or PNG\), and adds them to the specified face collection\. A unique face ID is returned for each face that's detected in the image\. After you persist faces, you can search the face collection for face matches\. For more information, see [Adding Faces to a Collection](add-faces-to-collection-procedure.md)\.
+ The [ListFaces](API_ListFaces.md) operation lists the faces in a collection\. For more information, see [Adding Faces to a Collection](add-faces-to-collection-procedure.md)\.
+ The [DeleteFaces](API_DeleteFaces.md) operation deletes faces from a collection\. For more information, see [Deleting Faces from a Collection](delete-faces-procedure.md)\.

## Guidance for using IndexFaces<a name="guidance-index-faces"></a>

The following is guidance for using `IndexFaces` in common scenarios\.

### Critical or Public Safety Applications<a name="guidance-index-faces-critical"></a>
+ Call [IndexFaces](API_IndexFaces.md) with images which contain only one face in each image and associate the returned Face ID with the identifier for the subject of the image\.
+ You can use [DetectFaces](API_DetectFaces.md) ahead of indexing to verify there is only one face in the image\. If more than one face is detected, re\-submit the image after review and with only one face present\. This prevents inadvertently indexing multiple faces and associating them with the same person\.

### Photo Sharing and Social Media Applications<a name="guidance-index-faces-social"></a>
+ You should call `IndexFaces` without restrictions on images that contain multiple faces in use cases such as family albums\. In such cases, you need to identify each person in every photo and use that information to group photos by the people present in them\. 

### General Usage<a name="guidance-index-faces-general"></a>
+ Index multiple different images of the same person, particularly with different face attributes \(facial poses, facial hair, etc\) to improve matching quality\. 
+ Include a review process so that failed matches can be indexed with the correct face identifier to improve subsequent face matching ability\.
+ For information about image quality, see [Recommendations for Facial Recognition Input Images](recommendations-facial-input-images.md)\. 

## Searching for Faces Within a Collection<a name="collections-search-faces"></a>

After you create a face collection and store faces, you can search a face collection for face matches\. With Amazon Rekognition, you can search for faces in a collection that match:
+ A supplied face ID \([SearchFaces](API_SearchFaces.md)\)\. For more information, see [Searching for a Face Using Its Face ID](search-face-with-id-procedure.md)\.
+ The largest face in a supplied image \([SearchFacesByImage](API_SearchFacesByImage.md)\)\. For more information, see [Searching for a Face Using an Image](search-face-with-image-procedure.md)\.
+ Faces in a stored video\. For more information, see [ Searching Stored Videos for Faces](procedure-person-search-videos.md)\.
+ Faces in a streaming video\. For more information, see [Working with Streaming Videos](streaming-video.md)\.

The `CompareFaces` operation and the search faces operations differ as follows:
+ The `CompareFaces` operation compares a face in a source image with faces in the target image\. The scope of this comparison is limited to the faces that are detected in the target image\. For more information, see [Comparing Faces in Images](faces-comparefaces.md)\.
+ `SearchFaces` and `SearchFacesByImage` compare a face \(identified either by a `FaceId` or an input image\) with all faces in a given face collection\. Therefore, the scope of this search is much larger\. Also, because the facial feature information is persisted for faces that are already stored in the face collection, you can search for matching faces multiple times\.

### Using Similarity Thresholds to Match Faces<a name="face-match-similarity"></a>

We allow you to control the results of all search operations \([CompareFaces](API_CompareFaces.md), [SearchFaces](API_SearchFaces.md), and [SearchFacesByImage](API_SearchFacesByImage.md)\) by providing a similarity threshold as an input parameter\.

The similarity threshold input attribute for `SearchFaces` and `SearchFacesByImage`, `FaceMatchThreshold`, controls how many results are returned based on the similarity to the face being matched\. \(This attribute is `SimilarityThreshold` for `CompareFaces`\.\) Responses with a `Similarity` response attribute value that's lower than the threshold aren't returned\. This threshold is important to calibrate for your use case, because it can determine how many false positives are included in your match results\. This controls the recall of your search results—the lower the threshold, the higher the recall\.

All machine learning systems are probabilistic\. You should use your judgment in setting the right similarity threshold, depending on your use case\. For example, if you're looking to build a photos app to identify similar\-looking family members, you might choose a lower threshold \(such as 80%\)\. On the other hand, for many law enforcement use cases, we recommend using a high threshold value of 99% or above to reduce accidental misidentification\.

In addition to `FaceMatchThreshold`, you can use the `Similarity` response attribute as a means to reduce accidental misidentification\. For instance, you can choose to use a low threshold \(like 80%\) to return more results\. Then you can use the response attribute `Similarity` \(percentage of similarity\) to narrow the choice and filter for the right responses in your application\. Again, using a higher similarity \(such as 99% and above\) reduces the risk of misidentification\. 