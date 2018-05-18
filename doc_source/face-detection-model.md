# Model Versioning<a name="face-detection-model"></a>

Amazon Rekognition uses deep learning models to perform face detection and to search for faces in collections\. It continues to improve the accuracy of its models based on customer feedback and advances in deep learning research\. These improvements are shipped as model updates\. For example, with version 1\.0 of the model, [IndexFaces](API_IndexFaces.md) can index the 15 largest faces in an image\. Later versions of the model allow `IndexFaces` to index the 100 largest faces in an image\.

When you create a new collection, it's associated with the most recent version of the model\. To improve accuracy, the model is occasionally updated\.

 When a new version of the model is released, the following happens: 
+ New collections you create are associated with the latest model\. Faces that you add to new collections by using [IndexFaces](API_IndexFaces.md) are detected using the latest model\.
+ Your existing collections to use the version of the model that they were created with\. The face vectors stored in these collections aren't automatically updated to the latest version of the model\.
+ New faces that are added to an existing collection are detected by using the model that's already associated with the collection\.

Different versions of the model aren't compatible with each other\. Specifically, if an image is indexed into multiples collections that use different versions of the model, the face identifiers for the same detected faces are different\. If an image is indexed into multiple collections that are associated with the same model, the face identifiers are the same\. 

Your application might face compatibility issues if your collection management doesn't account for updates to the model\. You can determine the version of the model a collection uses by using the `FaceModelVersion` field that's returned by collection operation responses\. For example, `CreateCollection`\. 

Existing face vectors in a collection can't be updated to a later version of the model\. Because Amazon Rekognition doesn't store source image bytes, it can't automatically reindex images by using a later version of the model\.

To use the latest model on faces that are stored in an existing collection, create a new collection \([CreateCollection](API_CreateCollection.md)\) and reindex the source images into the new collection \(`Indexfaces`\)\. You need to update any face identifiers that are stored by your application because the face identifiers in the new collection are different from the face identifiers in the old collection\. If you no longer need the old collection, you can delete it by using [DeleteCollection](API_DeleteCollection.md)\. 