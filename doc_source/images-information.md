# Image specifications<a name="images-information"></a>

Amazon Rekognition Image operations can analyze images in \.jpg or \.png format\.

You pass image bytes to an Amazon Rekognition Image operation as part of the call or you reference an existing Amazon S3 object\. For an example of analyzing an image stored in an Amazon S3 bucket, see [Analyzing images stored in an Amazon S3 bucket](images-s3.md)\. For an example of passing image bytes to an Amazon Rekognition Image API operation, see [Analyzing an image loaded from a local file system](images-bytes.md)\.

If you use HTTP and pass the image bytes as part of an Amazon Rekognition Image operation, the image bytes must be a base64\-encoded string\. If you use the AWS SDK and pass image bytes as part of the API operation call, the need to base64\-encode the image bytes depends on the language you use\. 

The following common AWS SDKs automatically base64\-encode images, and you don't need to encode image bytes before calling an Amazon Rekognition Image API operation\.
+ Java
+ JavaScript
+ Python
+ PHP

If you're using another AWS SDK and get an image format error when calling a Rekognition API operation, try base64\-encoding the image bytes before passing them to a Rekognition API operation\.

If you use the AWS CLI to call Amazon Rekognition Image operations, passing image bytes as part of the call isn't supported\. You must first upload the image to an Amazon S3 bucket, and then call the operation referencing the uploaded image\.

**Note**  
The image doesn't need to be base64 encoded if you pass an image stored in an `S3Object` instead of image bytes\.

For information about ensuring the lowest possible latency for Amazon Rekognition Image operations, see [Amazon Rekognition Image operation latency](operation-latency.md)\. 

## Correcting image orientation<a name="images-image-orientation-correction"></a>

In several Rekognition API operations, the orientation of an analyzed image is returned\. Knowing image orientation is important as it allows you to reorient images for display\. Rekognition API operations that analyze faces also return bounding boxes for the location of faces within an image\. You can use bounding boxes to display a box around a face on an image\. The bounding box coordinates returned are affected by image orientation and you may need to translate bounding box coordinates to correctly display a box around a face\. For more information, see [Getting image orientation and bounding box coordinates](images-orientation.md)\. 

## Image resizing<a name="images-image-sizing"></a>

During analysis, Amazon Rekognition internally resizes images using a set of predefined ranges that best suit a particular model or algorithm\. Because of this, Amazon Rekognition might detect a different number of objects, or provide different results, depending on the resolution of the input image\. For example, suppose you have two images\. The first image has a resolution of 1024x768 pixels\. The second image, a resized version of the first image, has a resolution of 640x480 pixels\. If you submit the images to [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html), the responses from the two calls to `DetectLabels` might differ slightly\.