# Working with Images<a name="images"></a>

This section covers the types of detection and recognition that Rekognition Image can perform on images\. Rekognition Image can perform the following analysis on images: 
+ Label detection
+ Face detection and comparison
+ Celebrity recognition
+ Image moderation
+ Text in image detection

These are performed by non\-storage API operations where Rekognition Image doesn't persist any information discovered by the operation\. No input image bytes are persisted by non\-storage API operations\. For more information, see [Non\-Storage and Storage API Operations](how-it-works-storage-non-storage.md)\.

Rekognition Image can also store facial metadata in collections for later retrieval\. For more information, see [Searching Faces in a Collection](collections.md)\.

In this section you use the Rekognition Image API operations to analyze images stored in an Amazon S3 bucket and images bytes loaded from the local file system\. This section also covers getting image orientation information from a \.jpg image\. 

**Topics**
+ [Images](#images-information)
+ [Best Practices for Working With Images](image-best-practices.md)
+ [Analysing Images Stored in an Amazon S3 Bucket](images-s3.md)
+ [Analysing an Image Loaded from a Local File System](images-bytes.md)
+ [Getting Image Orientation and Bounding Box Coordinates](images-orientation.md)

## Images<a name="images-information"></a>

Rekognition Image operations can analyse images in \.jpg or \.png format\.

You pass image bytes to an Rekognition Image operation as part of the call or you reference an existing Amazon S3 object\. For an example of analyzing an image stored in an Amazon S3 bucket, see [Analysing Images Stored in an Amazon S3 Bucket](images-s3.md)\.

If you use HTTP and pass the image bytes as part of an Rekognition Image operation, the image bytes must be a base64\-encoded string\. If you use the AWS SDK and pass image bytes as part of the API operation call, the need to base64\-encode the image bytes depends on the language you use\. For more information, see [Analysing an Image Loaded from a Local File System](images-bytes.md)\. 

If you use the AWS CLI to call Rekognition Image operations, passing image bytes as part of the call is not supported\. You must first upload the image to an Amazon S3 bucket and then call the operation referencing the uploaded image\.

For information about ensuring the lowest possible latency for Rekognition Image operations, see [Rekognition Image Operation Latency](image-best-practices.md#operation-latency)\. 

### Correcting Image Orientation<a name="images-image-orientation-correction"></a>

In several Rekognition API operations, the orientation of an analyzed image is returned\. For example, the [DetectFaces](API_DetectFaces.md) API operation returns orientation information about the source image in the `OrientationCorrection` field\. Knowing image orientation is important as it allows you to reorient images for display\. Rekognition API operations that analyze faces also return bounding boxes for the location of faces within an image\. You can use bounding boxes to display a box around a face on an image\. The bounding box coordinates returned are affected by image orientation and you may need to translate bounding box coordinates to correctly display a box around a face\. For more information, see [Getting Image Orientation and Bounding Box Coordinates](images-orientation.md)\. 