# Best Practices for Working With Images<a name="image-best-practices"></a>

The following are best practices for working with images\.

## Amazon Rekognition Image Operation Latency<a name="operation-latency"></a>

To ensure the lowest possible latency for Amazon Rekognition Image operations, consider the following:
+ The region for the Amazon S3 bucket containing your images must match the region you use for Amazon Rekognition Image API operations\. 
+ Calling an Amazon Rekognition Image operation with image bytes is faster than uploading the image to an Amazon S3 bucket and then referencing the uploaded image in an Amazon Rekognition Image operation\. Consider this approach if you are uploading images to Amazon Rekognition Image for near real\-time processing\. For example, images uploaded from an IP camera or images uploaded through a web portal\.
+ If the image is already in an Amazon S3 bucket, referencing it in an Amazon Rekognition Image operation will probably be faster than passing image bytes to the operation\.
+ Low\-resolution images are processed faster than high\-resolution images\. Consider resizing input images to a lower resolution for faster processing\.

## Recommendations for Facial Recognition Input Images<a name="recommendations-for-images"></a>

The models used for face and celebrity recognition operations are designed to work in as wide a variety of poses, rotations, lighting conditions, and range of sizes as possible\. We recommend the following guidelines when choosing reference photos for facial recognition:
+ Have a front\-facing face\.
+ Have a face that is not obscured or tightly cropped\. The image should contain the full head and shoulders of the person\. It should not be cropped to the face bounding box\.
+ Avoid occlusions such as head\-bands or masks\.
+ Have a face that occupies a large proportion of the image\. Proportionally larger faces are matched with greater accuracy\. 
+ Be sufficiently large\. Amazon Rekognition Image can detect faces as small as 40x40 pixels in an HD resolution image \(1920x1080\)\. Higher\-resolution images require a larger minimum face size\. Faces larger than the minimum size provide more accurate detection and attribute analysis\.
+ Use color images\.
+ Have flat lighting on the face, as opposed to varying shades such as shadows\.
+ Have sufficient contrast with the background\. A high\-contrast monochrome background works well\.
+ Be bright and sharp\. You can use [DetectFaces](API_DetectFaces.md) to determine the brightness and sharpness of a face\.

Faces recognized by Amazon Rekognition can be used to help identify potential matches in public safety and law enforcement scenarios\. For more information, see [Using Amazon Rekognition to Help Public Safety](collections.md#public-safety)\.