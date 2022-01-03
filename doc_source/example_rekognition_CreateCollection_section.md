# Create an Amazon Rekognition collection using an AWS SDK<a name="example_rekognition_CreateCollection_section"></a>

The following code examples show how to create an Amazon Rekognition collection\.

For more information, see [Creating a collection](https://docs.aws.amazon.com/rekognition/latest/dg/create-collection-procedure.html)\.

------
#### [ \.NET ]

**AWS SDK for \.NET**  
  

```
        public static async Task Main()
        {
            var rekognitionClient = new AmazonRekognitionClient();

            string collectionId = "MyCollection";
            Console.WriteLine("Creating collection: " + collectionId);

            var createCollectionRequest = new CreateCollectionRequest
            {
                CollectionId = collectionId,
            };

            CreateCollectionResponse createCollectionResponse = await rekognitionClient.CreateCollectionAsync(createCollectionRequest);
            Console.WriteLine($"CollectionArn : {createCollectionResponse.CollectionArn}");
            Console.WriteLine($"Status code : {createCollectionResponse.StatusCode}");
        }
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Rekognition/#code-examples)\. 
+  For API details, see [CreateCollection](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/CreateCollection) in *AWS SDK for \.NET API Reference*\. 

------
#### [ Java ]

**SDK for Java 2\.x**  
  

```
    public static void createMyCollection(RekognitionClient rekClient,String collectionId ) {

        try {
            CreateCollectionRequest collectionRequest = CreateCollectionRequest.builder()
                    .collectionId(collectionId)
                    .build();

            CreateCollectionResponse collectionResponse = rekClient.createCollection(collectionRequest);
            System.out.println("CollectionArn : " +
                    collectionResponse.collectionArn());
            System.out.println("Status code : " +
                    collectionResponse.statusCode().toString());

        } catch(RekognitionException e) {
                System.out.println(e.getMessage());
                System.exit(1);
        }
    }
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/rekognition/#readme)\. 
+  For API details, see [CreateCollection](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/CreateCollection) in *AWS SDK for Java 2\.x API Reference*\. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
This is prerelease documentation for a feature in preview release\. It is subject to change\.
  

```
 suspend fun createMyCollection(collectionIdVal: String) {

        val request = CreateCollectionRequest {
            collectionId = collectionIdVal
        }

        RekognitionClient { region = "us-east-1" }.use { rekClient ->
            val response = rekClient.createCollection(request)
            println("Collection ARN is ${response.collectionArn}")
            println("Status code is ${response.statusCode}" )
        }
    }
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/rekognition#code-examples)\. 
+  For API details, see [CreateCollection](https://github.com/awslabs/aws-sdk-kotlin#generating-api-documentation) in *AWS SDK for Kotlin API reference*\. 

------
#### [ Python ]

**SDK for Python \(Boto3\)**  
  

```
class RekognitionCollectionManager:
    """
    Encapsulates Amazon Rekognition collection management functions.
    This class is a thin wrapper around parts of the Boto3 Amazon Rekognition API.
    """
    def __init__(self, rekognition_client):
        """
        Initializes the collection manager object.

        :param rekognition_client: A Boto3 Rekognition client.
        """
        self.rekognition_client = rekognition_client

    def create_collection(self, collection_id):
        """
        Creates an empty collection.

        :param collection_id: Text that identifies the collection.
        :return: The newly created collection.
        """
        try:
            response = self.rekognition_client.create_collection(
                CollectionId=collection_id)
            response['CollectionId'] = collection_id
            collection = RekognitionCollection(response, self.rekognition_client)
            logger.info("Created collection %s.", collection_id)
        except ClientError:
            logger.exception("Couldn't create collection %s.", collection_id)
            raise
        else:
            return collection
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/rekognition#code-examples)\. 
+  For API details, see [CreateCollection](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/CreateCollection) in *AWS SDK for Python \(Boto3\) API Reference*\. 

------

For a complete list of AWS SDK developer guides and code examples, including help getting started and information about previous versions, see [Using Rekognition with an AWS SDK](sdk-general-information-section.md)\.