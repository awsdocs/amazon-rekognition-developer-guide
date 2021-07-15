# Working with images<a name="images"></a>

This section covers the types of analysis that Amazon Rekognition Image can perform on images\. 
+ [Object and scene detection](labels.md)
+ [Face detection and comparison](faces.md)
+ [Searching faces in a collection](collections.md)
+ [Celebrity recognition](celebrities.md)
+ [Image moderation](moderation.md)
+ [Text in image detection](text-detection.md)

These are performed by non\-storage API operations where Amazon Rekognition Image doesn't persist any information discovered by the operation\. No input image bytes are persisted by non\-storage API operations\. For more information, see [Non\-storage and storage API operations](how-it-works-storage-non-storage.md)\.

Amazon Rekognition Image can also store facial metadata in collections for later retrieval\. For more information, see [Searching faces in a collection](collections.md)\.

In this section, you use the Amazon Rekognition Image API operations to analyze images stored in an Amazon S3 bucket and image bytes loaded from the local file system\. This section also covers getting image orientation information from a \.jpg image\. 

**Topics**
+ [Images](images-information.md)
+ [Analyzing images stored in an Amazon S3 bucket](images-s3.md)
+ [Analyzing an image loaded from a local file system](images-bytes.md)
+ [Displaying bounding boxes](images-displaying-bounding-boxes.md)
+ [Getting image orientation and bounding box coordinates](images-orientation.md)
+ [Tutorial: Using Amazon Rekognition and Lambda to tag assets in an Amazon S3 bucket](images-lambda-s3-tutorial.md)