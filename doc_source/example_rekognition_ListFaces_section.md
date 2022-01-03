# List faces in an Amazon Rekognition collection using an AWS SDK<a name="example_rekognition_ListFaces_section"></a>

The following code examples show how to list faces in an Amazon Rekognition collection\.

For more information, see [Listing faces in a collection](https://docs.aws.amazon.com/rekognition/latest/dg/list-faces-in-collection-procedure.html)\.

------
#### [ \.NET ]

**AWS SDK for \.NET**  
  

```
        public static async Task Main()
        {
            string collectionId = "MyCollection2";

            var rekognitionClient = new AmazonRekognitionClient();

            var listFacesResponse = new ListFacesResponse();
            Console.WriteLine($"Faces in collection {collectionId}");

            var listFacesRequest = new ListFacesRequest
            {
                CollectionId = collectionId,
                MaxResults = 1,
            };

            do
            {
                listFacesResponse = await rekognitionClient.ListFacesAsync(listFacesRequest);
                listFacesResponse.Faces.ForEach(face =>
                {
                    Console.WriteLine(face.FaceId);
                });

                listFacesRequest.NextToken = listFacesResponse.NextToken;
            }
            while (!string.IsNullOrEmpty(listFacesResponse.NextToken));
        }
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Rekognition/#code-examples)\. 
+  For API details, see [ListFaces](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/ListFaces) in *AWS SDK for \.NET API Reference*\. 

------
#### [ Java ]

**SDK for Java 2\.x**  
  

```
    public static void listFacesCollection(RekognitionClient rekClient, String collectionId ) {

        try {
            ListFacesRequest facesRequest = ListFacesRequest.builder()
                .collectionId(collectionId)
                .maxResults(10)
                .build();

            ListFacesResponse facesResponse = rekClient.listFaces(facesRequest);

            // For each face in the collection, print out the confidence level and face id value.
            List<Face> faces = facesResponse.faces();
            for (Face face: faces) {
                System.out.println("Confidence level there is a face: "+face.confidence());
                System.out.println("The face Id value is "+face.faceId());
            }

        } catch (RekognitionException e) {
            System.out.println(e.getMessage());
            System.exit(1);
         }
      }
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/rekognition/#readme)\. 
+  For API details, see [ListFaces](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ListFaces) in *AWS SDK for Java 2\.x API Reference*\. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
This is prerelease documentation for a feature in preview release\. It is subject to change\.
  

```
suspend fun listFacesCollection(collectionIdVal: String?) {

        val request = ListFacesRequest {
            collectionId = collectionIdVal
            maxResults =10
        }

        RekognitionClient { region = "us-east-1" }.use { rekClient ->
        val response = rekClient.listFaces(request)
        response.faces?.forEach { face ->
                println("Confidence level there is a face: ${face.confidence}")
                println("The face Id value is ${face.faceId}")
            }
       }
  }
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/rekognition#code-examples)\. 
+  For API details, see [ListFaces](https://github.com/awslabs/aws-sdk-kotlin#generating-api-documentation) in *AWS SDK for Kotlin API reference*\. 

------
#### [ Python ]

**SDK for Python \(Boto3\)**  
  

```
class RekognitionCollection:
    """
    Encapsulates an Amazon Rekognition collection. This class is a thin wrapper
    around parts of the Boto3 Amazon Rekognition API.
    """
    def __init__(self, collection, rekognition_client):
        """
        Initializes a collection object.

        :param collection: Collection data in the format returned by a call to
                           create_collection.
        :param rekognition_client: A Boto3 Rekognition client.
        """
        self.collection_id = collection['CollectionId']
        self.collection_arn, self.face_count, self.created = self._unpack_collection(
            collection)
        self.rekognition_client = rekognition_client

    @staticmethod
    def _unpack_collection(collection):
        """
        Unpacks optional parts of a collection that can be returned by
        describe_collection.

        :param collection: The collection data.
        :return: A tuple of the data in the collection.
        """
        return (
            collection.get('CollectionArn'),
            collection.get('FaceCount', 0),
            collection.get('CreationTimestamp'))

    def list_faces(self, max_results):
        """
        Lists the faces currently indexed in the collection.

        :param max_results: The maximum number of faces to return.
        :return: The list of faces in the collection.
        """
        try:
            response = self.rekognition_client.list_faces(
                CollectionId=self.collection_id, MaxResults=max_results)
            faces = [RekognitionFace(face) for face in response['Faces']]
            logger.info(
                "Found %s faces in collection %s.", len(faces), self.collection_id)
        except ClientError:
            logger.exception(
                "Couldn't list faces in collection %s.", self.collection_id)
            raise
        else:
            return faces
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/rekognition#code-examples)\. 
+  For API details, see [ListFaces](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/ListFaces) in *AWS SDK for Python \(Boto3\) API Reference*\. 

------

For a complete list of AWS SDK developer guides and code examples, including help getting started and information about previous versions, see [Using Rekognition with an AWS SDK](sdk-general-information-section.md)\.