# Managing Collections<a name="managing-collections"></a>

This section covers creating and managing collections\. A collection is a container for persisting faces detected by the [IndexFaces](API_IndexFaces.md) operation\. 

The face collection is the primary Amazon Rekognition resource, each face collection you create has a unique Amazon Resource Name \(ARN\)\. You create each face collection in a specific AWS Region in your account\.

Amazon Rekognition provides the following operations for you to manage collections:

+ [CreateCollection](API_CreateCollection.md)

  Amazon Rekognition creates the collection and returns the Amazon Resource Name \(ARN\) of the newly created collection\. An example response is shown following:

  ```
  {
     "CollectionArn": "aws:rekognition:us-east-1:acct-id:collection/examplecollection",
     "StatusCode": 200
  }
  ```

+ [ListCollections](API_ListCollections.md)

  Amazon Rekognition returns a list of collections\. The following is an example response:

  ```
  {
     "CollectionIds": [
        "examplecollection1",
        "examplecollection2",
        "examplecollection3"
     ]
  }
  ```

+ [DeleteCollection](API_DeleteCollection.md)

  Amazon Rekognition deletes the specified collection\. 

For information about storing faces in a collection, see [Storing Faces in a Face Collection](collections-index-faces.md)\. For information about searching faces, see [Searching for Faces with Rekognition Image Collection](collections-search-faces.md) and [Searching for Faces with Rekognition Video](collections-search-person.md)\.