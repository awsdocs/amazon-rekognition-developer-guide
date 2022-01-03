# Detect and display elements in images with Amazon Rekognition using an AWS SDK<a name="example_rekognition_Usage_DetectAndDisplayImage_section"></a>

The following code example shows how to detect and display elements in images with Amazon Rekognition\.

For more information, see [Displaying bounding boxes](https://docs.aws.amazon.com/rekognition/latest/dg/images-displaying-bounding-boxes.html)\.

------
#### [ Python ]

**SDK for Python \(Boto3\)**  
Create classes to wrap Amazon Rekognition functions\.  

```
import logging
from pprint import pprint
import boto3
from botocore.exceptions import ClientError
import requests

from rekognition_objects import (
    RekognitionFace, RekognitionCelebrity, RekognitionLabel,
    RekognitionModerationLabel, RekognitionText, show_bounding_boxes, show_polygons)

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

    @classmethod
    def from_bucket(cls, s3_object, rekognition_client):
        """
        Creates a RekognitionImage object from an Amazon S3 object.

        :param s3_object: An Amazon S3 object that identifies the image. The image
                          is not retrieved until needed for a later call.
        :param rekognition_client: A Boto3 Rekognition client.
        :return: The RekognitionImage object, initialized with Amazon S3 object data.
        """
        image = {'S3Object': {'Bucket': s3_object.bucket_name, 'Name': s3_object.key}}
        return cls(image, s3_object.key, rekognition_client)

    def detect_faces(self):
        """
        Detects faces in the image.

        :return: The list of faces found in the image.
        """
        try:
            response = self.rekognition_client.detect_faces(
                Image=self.image, Attributes=['ALL'])
            faces = [RekognitionFace(face) for face in response['FaceDetails']]
            logger.info("Detected %s faces.", len(faces))
        except ClientError:
            logger.exception("Couldn't detect faces in %s.", self.image_name)
            raise
        else:
            return faces

    def detect_labels(self, max_labels):
        """
        Detects labels in the image. Labels are objects and people.

        :param max_labels: The maximum number of labels to return.
        :return: The list of labels detected in the image.
        """
        try:
            response = self.rekognition_client.detect_labels(
                Image=self.image, MaxLabels=max_labels)
            labels = [RekognitionLabel(label) for label in response['Labels']]
            logger.info("Found %s labels in %s.", len(labels), self.image_name)
        except ClientError:
            logger.info("Couldn't detect labels in %s.", self.image_name)
            raise
        else:
            return labels

    def recognize_celebrities(self):
        """
        Detects celebrities in the image.

        :return: A tuple. The first element is the list of celebrities found in
                 the image. The second element is the list of faces that were
                 detected but did not match any known celebrities.
        """
        try:
            response = self.rekognition_client.recognize_celebrities(
                Image=self.image)
            celebrities = [RekognitionCelebrity(celeb)
                           for celeb in response['CelebrityFaces']]
            other_faces = [RekognitionFace(face)
                           for face in response['UnrecognizedFaces']]
            logger.info(
                "Found %s celebrities and %s other faces in %s.", len(celebrities),
                len(other_faces), self.image_name)
        except ClientError:
            logger.exception("Couldn't detect celebrities in %s.", self.image_name)
            raise
        else:
            return celebrities, other_faces

    def compare_faces(self, target_image, similarity):
        """
        Compares faces in the image with the largest face in the target image.

        :param target_image: The target image to compare against.
        :param similarity: Faces in the image must have a similarity value greater
                           than this value to be included in the results.
        :return: A tuple. The first element is the list of faces that match the
                 reference image. The second element is the list of faces that have
                 a similarity value below the specified threshold.
        """
        try:
            response = self.rekognition_client.compare_faces(
                SourceImage=self.image,
                TargetImage=target_image.image,
                SimilarityThreshold=similarity)
            matches = [RekognitionFace(match['Face']) for match
                       in response['FaceMatches']]
            unmatches = [RekognitionFace(face) for face in response['UnmatchedFaces']]
            logger.info(
                "Found %s matched faces and %s unmatched faces.",
                len(matches), len(unmatches))
        except ClientError:
            logger.exception(
                "Couldn't match faces from %s to %s.", self.image_name,
                target_image.image_name)
            raise
        else:
            return matches, unmatches

    def detect_moderation_labels(self):
        """
        Detects moderation labels in the image. Moderation labels identify content
        that may be inappropriate for some audiences.

        :return: The list of moderation labels found in the image.
        """
        try:
            response = self.rekognition_client.detect_moderation_labels(
                Image=self.image)
            labels = [RekognitionModerationLabel(label)
                      for label in response['ModerationLabels']]
            logger.info(
                "Found %s moderation labels in %s.", len(labels), self.image_name)
        except ClientError:
            logger.exception(
                "Couldn't detect moderation labels in %s.", self.image_name)
            raise
        else:
            return labels

    def detect_text(self):
        """
        Detects text in the image.

        :return The list of text elements found in the image.
        """
        try:
            response = self.rekognition_client.detect_text(Image=self.image)
            texts = [RekognitionText(text) for text in response['TextDetections']]
            logger.info("Found %s texts in %s.", len(texts), self.image_name)
        except ClientError:
            logger.exception("Couldn't detect text in %s.", self.image_name)
            raise
        else:
            return texts
```
Create helper functions to draw bounding boxes and polygons\.  

```
import io
import logging
from PIL import Image, ImageDraw

logger = logging.getLogger(__name__)


def show_bounding_boxes(image_bytes, box_sets, colors):
    """
    Draws bounding boxes on an image and shows it with the default image viewer.

    :param image_bytes: The image to draw, as bytes.
    :param box_sets: A list of lists of bounding boxes to draw on the image.
    :param colors: A list of colors to use to draw the bounding boxes.
    """
    image = Image.open(io.BytesIO(image_bytes))
    draw = ImageDraw.Draw(image)
    for boxes, color in zip(box_sets, colors):
        for box in boxes:
            left = image.width * box['Left']
            top = image.height * box['Top']
            right = (image.width * box['Width']) + left
            bottom = (image.height * box['Height']) + top
            draw.rectangle([left, top, right, bottom], outline=color, width=3)
    image.show()

def show_polygons(image_bytes, polygons, color):
    """
    Draws polygons on an image and shows it with the default image viewer.

    :param image_bytes: The image to draw, as bytes.
    :param polygons: The list of polygons to draw on the image.
    :param color: The color to use to draw the polygons.
    """
    image = Image.open(io.BytesIO(image_bytes))
    draw = ImageDraw.Draw(image)
    for polygon in polygons:
        draw.polygon([
            (image.width * point['X'], image.height * point['Y']) for point in polygon],
            outline=color)
    image.show()
```
Create classes to parse objects returned by Amazon Rekognition\.  

```
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

class RekognitionCelebrity:
    """Encapsulates an Amazon Rekognition celebrity."""
    def __init__(self, celebrity, timestamp=None):
        """
        Initializes the celebrity object.

        :param celebrity: Celebrity data, in the format returned by Amazon Rekognition
                          functions.
        :param timestamp: The time when the celebrity was detected, if the celebrity
                          was detected in a video.
        """
        self.info_urls = celebrity.get('Urls')
        self.name = celebrity.get('Name')
        self.id = celebrity.get('Id')
        self.face = RekognitionFace(celebrity.get('Face'))
        self.confidence = celebrity.get('MatchConfidence')
        self.bounding_box = celebrity.get('BoundingBox')
        self.timestamp = timestamp

    def to_dict(self):
        """
        Renders some of the celebrity data to a dict.

        :return: A dict that contains the celebrity data.
        """
        rendering = self.face.to_dict()
        if self.name is not None:
            rendering['name'] = self.name
        if self.info_urls:
            rendering['info URLs'] = self.info_urls
        if self.timestamp is not None:
            rendering['timestamp'] = self.timestamp
        return rendering

class RekognitionPerson:
    """Encapsulates an Amazon Rekognition person."""
    def __init__(self, person, timestamp=None):
        """
        Initializes the person object.

        :param person: Person data, in the format returned by Amazon Rekognition
                       functions.
        :param timestamp: The time when the person was detected, if the person
                          was detected in a video.
        """
        self.index = person.get('Index')
        self.bounding_box = person.get('BoundingBox')
        face = person.get('Face')
        self.face = RekognitionFace(face) if face is not None else None
        self.timestamp = timestamp

    def to_dict(self):
        """
        Renders some of the person data to a dict.

        :return: A dict that contains the person data.
        """
        rendering = self.face.to_dict() if self.face is not None else {}
        if self.index is not None:
            rendering['index'] = self.index
        if self.bounding_box is not None:
            rendering['bounding_box'] = self.bounding_box
        if self.timestamp is not None:
            rendering['timestamp'] = self.timestamp
        return rendering

class RekognitionLabel:
    """Encapsulates an Amazon Rekognition label."""
    def __init__(self, label, timestamp=None):
        """
        Initializes the label object.

        :param label: Label data, in the format returned by Amazon Rekognition
                      functions.
        :param timestamp: The time when the label was detected, if the label
                          was detected in a video.
        """
        self.name = label.get('Name')
        self.confidence = label.get('Confidence')
        self.instances = label.get('Instances')
        self.parents = label.get('Parents')
        self.timestamp = timestamp

    def to_dict(self):
        """
        Renders some of the label data to a dict.

        :return: A dict that contains the label data.
        """
        rendering = {}
        if self.name is not None:
            rendering['name'] = self.name
        if self.timestamp is not None:
            rendering['timestamp'] = self.timestamp
        return rendering

class RekognitionModerationLabel:
    """Encapsulates an Amazon Rekognition moderation label."""
    def __init__(self, label, timestamp=None):
        """
        Initializes the moderation label object.

        :param label: Label data, in the format returned by Amazon Rekognition
                      functions.
        :param timestamp: The time when the moderation label was detected, if the
                          label was detected in a video.
        """
        self.name = label.get('Name')
        self.confidence = label.get('Confidence')
        self.parent_name = label.get('ParentName')
        self.timestamp = timestamp

    def to_dict(self):
        """
        Renders some of the moderation label data to a dict.

        :return: A dict that contains the moderation label data.
        """
        rendering = {}
        if self.name is not None:
            rendering['name'] = self.name
        if self.parent_name is not None:
            rendering['parent_name'] = self.parent_name
        if self.timestamp is not None:
            rendering['timestamp'] = self.timestamp
        return rendering

class RekognitionText:
    """Encapsulates an Amazon Rekognition text element."""
    def __init__(self, text_data):
        """
        Initializes the text object.

        :param text_data: Text data, in the format returned by Amazon Rekognition
                          functions.
        """
        self.text = text_data.get('DetectedText')
        self.kind = text_data.get('Type')
        self.id = text_data.get('Id')
        self.parent_id = text_data.get('ParentId')
        self.confidence = text_data.get('Confidence')
        self.geometry = text_data.get('Geometry')

    def to_dict(self):
        """
        Renders some of the text data to a dict.

        :return: A dict that contains the text data.
        """
        rendering = {}
        if self.text is not None:
            rendering['text'] = self.text
        if self.kind is not None:
            rendering['kind'] = self.kind
        if self.geometry is not None:
            rendering['polygon'] = self.geometry.get('Polygon')
        return rendering
```
Use the wrapper classes to detect elements in images and display their bounding boxes\. The images used in this example can be found on GitHub along with instructions and more code\.  

```
def usage_demo():
    print('-'*88)
    print("Welcome to the Amazon Rekognition image detection demo!")
    print('-'*88)

    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    rekognition_client = boto3.client('rekognition')
    street_scene_file_name = ".media/pexels-kaique-rocha-109919.jpg"
    celebrity_file_name = ".media/pexels-pixabay-53370.jpg"
    one_girl_url = 'https://dhei5unw3vrsx.cloudfront.net/images/source3_resized.jpg'
    three_girls_url = 'https://dhei5unw3vrsx.cloudfront.net/images/target3_resized.jpg'
    swimwear_object = boto3.resource('s3').Object(
        'console-sample-images-pdx', 'yoga_swimwear.jpg')
    book_file_name = '.media/pexels-christina-morillo-1181671.jpg'

    street_scene_image = RekognitionImage.from_file(
        street_scene_file_name, rekognition_client)
    print(f"Detecting faces in {street_scene_image.image_name}...")
    faces = street_scene_image.detect_faces()
    print(f"Found {len(faces)} faces, here are the first three.")
    for face in faces[:3]:
        pprint(face.to_dict())
    show_bounding_boxes(
        street_scene_image.image['Bytes'], [[face.bounding_box for face in faces]],
        ['aqua'])
    input("Press Enter to continue.")

    print(f"Detecting labels in {street_scene_image.image_name}...")
    labels = street_scene_image.detect_labels(100)
    print(f"Found {len(labels)} labels.")
    for label in labels:
        pprint(label.to_dict())
    names = []
    box_sets = []
    colors = ['aqua', 'red', 'white', 'blue', 'yellow', 'green']
    for label in labels:
        if label.instances:
            names.append(label.name)
            box_sets.append([inst['BoundingBox'] for inst in label.instances])
    print(f"Showing bounding boxes for {names} in {colors[:len(names)]}.")
    show_bounding_boxes(
        street_scene_image.image['Bytes'], box_sets, colors[:len(names)])
    input("Press Enter to continue.")

    celebrity_image = RekognitionImage.from_file(
        celebrity_file_name, rekognition_client)
    print(f"Detecting celebrities in {celebrity_image.image_name}...")
    celebs, others = celebrity_image.recognize_celebrities()
    print(f"Found {len(celebs)} celebrities.")
    for celeb in celebs:
        pprint(celeb.to_dict())
    show_bounding_boxes(
        celebrity_image.image['Bytes'],
        [[celeb.face.bounding_box for celeb in celebs]], ['aqua'])
    input("Press Enter to continue.")

    girl_image_response = requests.get(one_girl_url)
    girl_image = RekognitionImage(
        {'Bytes': girl_image_response.content}, "one-girl", rekognition_client)
    group_image_response = requests.get(three_girls_url)
    group_image = RekognitionImage(
        {'Bytes': group_image_response.content}, "three-girls", rekognition_client)
    print("Comparing reference face to group of faces...")
    matches, unmatches = girl_image.compare_faces(group_image, 80)
    print(f"Found {len(matches)} face matching the reference face.")
    show_bounding_boxes(
        group_image.image['Bytes'], [[match.bounding_box for match in matches]],
        ['aqua'])
    input("Press Enter to continue.")

    swimwear_image = RekognitionImage.from_bucket(swimwear_object, rekognition_client)
    print(f"Detecting suggestive content in {swimwear_object.key}...")
    labels = swimwear_image.detect_moderation_labels()
    print(f"Found {len(labels)} moderation labels.")
    for label in labels:
        pprint(label.to_dict())
    input("Press Enter to continue.")

    book_image = RekognitionImage.from_file(book_file_name, rekognition_client)
    print(f"Detecting text in {book_image.image_name}...")
    texts = book_image.detect_text()
    print(f"Found {len(texts)} text instances. Here are the first seven:")
    for text in texts[:7]:
        pprint(text.to_dict())
    show_polygons(
        book_image.image['Bytes'], [text.geometry['Polygon'] for text in texts], 'aqua')

    print("Thanks for watching!")
    print('-'*88)
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/rekognition#code-examples)\. 

------

For a complete list of AWS SDK developer guides and code examples, including help getting started and information about previous versions, see [Using Rekognition with an AWS SDK](sdk-general-information-section.md)\.