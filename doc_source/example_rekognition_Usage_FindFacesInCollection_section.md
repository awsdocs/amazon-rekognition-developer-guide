# Build an Amazon Rekognition collection and find faces in it using an AWS SDK<a name="example_rekognition_Usage_FindFacesInCollection_section"></a>

The following code example shows how to build an Amazon Rekognition collection and find faces in it\.

For more information, see [Searching faces in a collection](https://docs.aws.amazon.com/rekognition/latest/dg/collections.html)\.

------
#### [ Python ]

**SDK for Python \(Boto3\)**  
Create classes that wrap Amazon Rekognition functions\.  

```
import logging
from pprint import pprint
import boto3
from botocore.exceptions import ClientError
from rekognition_objects import RekognitionFace
from rekognition_image_detection import RekognitionImage

logger = logging.getLogger(__name__)


class RekognitionImage:
    """
    Encapsulates an Amazon Rekognition image. This class is a thin wrapper
    around parts of the Boto3 Amazon Rekognition API.
    """
    def __init__(self, image, image_name, rekognition_client):
        """
        Initializes the image object.

        :param image: Data that defines the image, either the image bytes or
                      an Amazon S3 bucket and object key.
        :param image_name: The name of the image.
        :param rekognition_client: A Boto3 Rekognition client.
        """
        self.image = image
        self.image_name = image_name
        self.rekognition_client = rekognition_client

    @classmethod
    def from_file(cls, image_file_name, rekognition_client, image_name=None):
        """
        Creates a RekognitionImage object from a local file.

        :param image_file_name: The file name of the image. The file is opened and its
                                bytes are read.
        :param rekognition_client: A Boto3 Rekognition client.
        :param image_name: The name of the image. If this is not specified, the
                           file name is used as the image name.
        :return: The RekognitionImage object, initialized with image bytes from the
                 file.
        """
        with open(image_file_name, 'rb') as img_file:
            image = {'Bytes': img_file.read()}
        name = image_file_name if image_name is None else image_name
        return cls(image, name, rekognition_client)

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

    def list_collections(self, max_results):
        """
        Lists collections for the current account.

        :param max_results: The maximum number of collections to return.
        :return: The list of collections for the current account.
        """
        try:
            response = self.rekognition_client.list_collections(MaxResults=max_results)
            collections = [
                RekognitionCollection({'CollectionId': col_id}, self.rekognition_client)
                for col_id in response['CollectionIds']]
        except ClientError:
            logger.exception("Couldn't list collections.")
            raise
        else:
            return collections

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

    def to_dict(self):
        """
        Renders parts of the collection data to a dict.

        :return: The collection data as a dict.
        """
        rendering = {
            'collection_id': self.collection_id,
            'collection_arn': self.collection_arn,
            'face_count': self.face_count,
            'created': self.created
        }
        return rendering

    def describe_collection(self):
        """
        Gets data about the collection from the Amazon Rekognition service.

        :return: The collection rendered as a dict.
        """
        try:
            response = self.rekognition_client.describe_collection(
                CollectionId=self.collection_id)
            # Work around capitalization of Arn vs. ARN
            response['CollectionArn'] = response.get('CollectionARN')
            (self.collection_arn, self.face_count,
             self.created) = self._unpack_collection(response)
            logger.info("Got data for collection %s.", self.collection_id)
        except ClientError:
            logger.exception("Couldn't get data for collection %s.", self.collection_id)
            raise
        else:
            return self.to_dict()

    def delete_collection(self):
        """
        Deletes the collection.
        """
        try:
            self.rekognition_client.delete_collection(CollectionId=self.collection_id)
            logger.info("Deleted collection %s.", self.collection_id)
            self.collection_id = None
        except ClientError:
            logger.exception("Couldn't delete collection %s.", self.collection_id)
            raise

    def index_faces(self, image, max_faces):
        """
        Finds faces in the specified image, indexes them, and stores them in the
        collection.

        :param image: The image to index.
        :param max_faces: The maximum number of faces to index.
        :return: A tuple. The first element is a list of indexed faces.
                 The second element is a list of faces that couldn't be indexed.
        """
        try:
            response = self.rekognition_client.index_faces(
                CollectionId=self.collection_id, Image=image.image,
                ExternalImageId=image.image_name, MaxFaces=max_faces,
                DetectionAttributes=['ALL'])
            indexed_faces = [
                RekognitionFace({**face['Face'], **face['FaceDetail']})
                for face in response['FaceRecords']]
            unindexed_faces = [
                RekognitionFace(face['FaceDetail'])
                for face in response['UnindexedFaces']]
            logger.info(
                "Indexed %s faces in %s. Could not index %s faces.", len(indexed_faces),
                image.image_name, len(unindexed_faces))
        except ClientError:
            logger.exception("Couldn't index faces in image %s.", image.image_name)
            raise
        else:
            return indexed_faces, unindexed_faces

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

    def search_faces(self, face_id, threshold, max_faces):
        """
        Searches for faces in the collection that match another face from the
        collection.

        :param face_id: The ID of the face in the collection to search for.
        :param threshold: The match confidence must be greater than this value
                          for a face to be included in the results.
        :param max_faces: The maximum number of faces to return.
        :return: The list of matching faces found in the collection. This list does
                 not contain the face specified by `face_id`.
        """
        try:
            response = self.rekognition_client.search_faces(
                CollectionId=self.collection_id, FaceId=face_id,
                FaceMatchThreshold=threshold, MaxFaces=max_faces)
            faces = [RekognitionFace(face['Face']) for face in response['FaceMatches']]
            logger.info(
                "Found %s faces in %s that match %s.", len(faces), self.collection_id,
                face_id)
        except ClientError:
            logger.exception(
                "Couldn't search for faces in %s that match %s.", self.collection_id,
                face_id)
            raise
        else:
            return faces

    def search_faces_by_image(self, image, threshold, max_faces):
        """
        Searches for faces in the collection that match the largest face in the
        reference image.

        :param image: The image that contains the reference face to search for.
        :param threshold: The match confidence must be greater than this value
                          for a face to be included in the results.
        :param max_faces: The maximum number of faces to return.
        :return: A tuple. The first element is the face found in the reference image.
                 The second element is the list of matching faces found in the
                 collection.
        """
        try:
            response = self.rekognition_client.search_faces_by_image(
                CollectionId=self.collection_id, Image=image.image,
                FaceMatchThreshold=threshold, MaxFaces=max_faces)
            image_face = RekognitionFace({
                'BoundingBox': response['SearchedFaceBoundingBox'],
                'Confidence': response['SearchedFaceConfidence']
            })
            collection_faces = [
                RekognitionFace(face['Face']) for face in response['FaceMatches']]
            logger.info("Found %s faces in the collection that match the largest "
                        "face in %s.", len(collection_faces), image.image_name)
        except ClientError:
            logger.exception(
                "Couldn't search for faces in %s that match %s.", self.collection_id,
                image.image_name)
            raise
        else:
            return image_face, collection_faces

class RekognitionFace:
    """Encapsulates an Amazon Rekognition face."""
    def __init__(self, face, timestamp=None):
        """
        Initializes the face object.

        :param face: Face data, in the format returned by Amazon Rekognition
                     functions.
        :param timestamp: The time when the face was detected, if the face was
                          detected in a video.
        """
        self.bounding_box = face.get('BoundingBox')
        self.confidence = face.get('Confidence')
        self.landmarks = face.get('Landmarks')
        self.pose = face.get('Pose')
        self.quality = face.get('Quality')
        age_range = face.get('AgeRange')
        if age_range is not None:
            self.age_range = (age_range.get('Low'), age_range.get('High'))
        else:
            self.age_range = None
        self.smile = face.get('Smile', {}).get('Value')
        self.eyeglasses = face.get('Eyeglasses', {}).get('Value')
        self.sunglasses = face.get('Sunglasses', {}).get('Value')
        self.gender = face.get('Gender', {}).get('Value', None)
        self.beard = face.get('Beard', {}).get('Value')
        self.mustache = face.get('Mustache', {}).get('Value')
        self.eyes_open = face.get('EyesOpen', {}).get('Value')
        self.mouth_open = face.get('MouthOpen', {}).get('Value')
        self.emotions = [emo.get('Type') for emo in face.get('Emotions', [])
                         if emo.get('Confidence', 0) > 50]
        self.face_id = face.get('FaceId')
        self.image_id = face.get('ImageId')
        self.timestamp = timestamp

    def to_dict(self):
        """
        Renders some of the face data to a dict.

        :return: A dict that contains the face data.
        """
        rendering = {}
        if self.bounding_box is not None:
            rendering['bounding_box'] = self.bounding_box
        if self.age_range is not None:
            rendering['age'] = f'{self.age_range[0]} - {self.age_range[1]}'
        if self.gender is not None:
            rendering['gender'] = self.gender
        if self.emotions:
            rendering['emotions'] = self.emotions
        if self.face_id is not None:
            rendering['face_id'] = self.face_id
        if self.image_id is not None:
            rendering['image_id'] = self.image_id
        if self.timestamp is not None:
            rendering['timestamp'] = self.timestamp
        has = []
        if self.smile:
            has.append('smile')
        if self.eyeglasses:
            has.append('eyeglasses')
        if self.sunglasses:
            has.append('sunglasses')
        if self.beard:
            has.append('beard')
        if self.mustache:
            has.append('mustache')
        if self.eyes_open:
            has.append('open eyes')
        if self.mouth_open:
            has.append('open mouth')
        if has:
            rendering['has'] = has
        return rendering
```
Use the wrapper classes to build a collection of faces from a set of images and then search for faces in the collection\.  

```
def usage_demo():
    print('-'*88)
    print("Welcome to the Amazon Rekognition face collection demo!")
    print('-'*88)

    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

    rekognition_client = boto3.client('rekognition')
    images = [
        RekognitionImage.from_file(
            '.media/pexels-agung-pandit-wiguna-1128316.jpg', rekognition_client,
            image_name='sitting'),
        RekognitionImage.from_file(
            '.media/pexels-agung-pandit-wiguna-1128317.jpg', rekognition_client,
            image_name='hopping'),
        RekognitionImage.from_file(
            '.media/pexels-agung-pandit-wiguna-1128318.jpg', rekognition_client,
            image_name='biking')]

    collection_mgr = RekognitionCollectionManager(rekognition_client)
    collection = collection_mgr.create_collection('doc-example-collection-demo')
    print(f"Created collection {collection.collection_id}:")
    pprint(collection.describe_collection())

    print("Indexing faces from three images:")
    for image in images:
        collection.index_faces(image, 10)
    print("Listing faces in collection:")
    faces = collection.list_faces(10)
    for face in faces:
        pprint(face.to_dict())
    input("Press Enter to continue.")

    print(f"Searching for faces in the collection that match the first face in the "
          f"list (Face ID: {faces[0].face_id}.")
    found_faces = collection.search_faces(faces[0].face_id, 80, 10)
    print(f"Found {len(found_faces)} matching faces.")
    for face in found_faces:
        pprint(face.to_dict())
    input("Press Enter to continue.")

    print(f"Searching for faces in the collection that match the largest face in "
          f"{images[0].image_name}.")
    image_face, match_faces = collection.search_faces_by_image(images[0], 80, 10)
    print(f"The largest face in {images[0].image_name} is:")
    pprint(image_face.to_dict())
    print(f"Found {len(match_faces)} matching faces.")
    for face in match_faces:
        pprint(face.to_dict())
    input("Press Enter to continue.")

    collection.delete_collection()
    print('Thanks for watching!')
    print('-'*88)
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/rekognition#code-examples)\. 

------

For a complete list of AWS SDK developer guides and code examples, including help getting started and information about previous versions, see [Using Rekognition with an AWS SDK](sdk-general-information-section.md)\.