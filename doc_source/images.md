# Working with Images<a name="images"></a>

This section covers the types of analysis that Amazon Rekognition Image can perform on images\. 
+ Label detection
+ Face detection and comparison
+ Celebrity recognition
+ Image moderation
+ Text in image detection

These are performed by non\-storage API operations where Amazon Rekognition Image doesn't persist any information discovered by the operation\. No input image bytes are persisted by non\-storage API operations\. For more information, see [Non\-Storage and Storage API Operations](how-it-works-storage-non-storage.md)\.

Amazon Rekognition Image can also store facial metadata in collections for later retrieval\. For more information, see [Searching Faces in a Collection](collections.md)\.

In this section, you use the Amazon Rekognition Image API operations to analyze images stored in an Amazon S3 bucket and image bytes loaded from the local file system\. This section also covers getting image orientation information from a \.jpg image\. 

**Topics**
+ [Images](images-information.md)
+ [Analyzing Images Stored in an Amazon S3 Bucket](images-s3.md)
+ [Analyzing an Image Loaded from a Local File System](images-bytes.md)
+ [Displaying Bounding Boxes](images-displaying-bounding-boxes.md)
+ [Getting Image Orientation and Bounding Box Coordinates](images-orientation.md)