# Best Practices for Working With Images<a name="image-best-practices"></a>

The following are best practices for working with images\.

## Rekognition Image Operation Latency<a name="operation-latency"></a>

To ensure the lowest possible latency for Rekognition Image operations, consider the following:

+ The region for the Amazon S3 bucket containing your images must match the region you use for Rekognition Image API operations\. 

+ Calling an Rekognition Image operation with image bytes is faster than uploading the image to an Amazon S3 bucket and then referencing the uploaded image in an Rekognition Image operation\. Consider this approach if you are uploading images to Rekognition Image for near real\-time processing\. For example, images uploaded from an IP camera or images uploaded through a web portal\.

+ If the image is already in an Amazon S3 bucket, referencing it in an Rekognition Image operation will probably be faster than passing image bytes to the operation\.

+ Low resolution images are processed faster than high resolution images\. Consider resizing input images to a lower resolution for faster processing\.

## Recommendations for Facial Recognition Input Images<a name="recommendations-for-images"></a>

Whilst Rekognition Image works across a variety of image conditions and sizes, we recommend the following guidelines when choosing reference photos for facial recognition:

+ Have a front\-facing face\.

+ Have flat lighting on the face, as opposed to varying shades such as shadows\.

+ Have sufficient contrast with the background\. A high\-contrast monochrome background works well\.

+ Be sufficiently large\. Rekognition Image can detect faces as small as 40x40 pixels in an HD resolution image \(1920x1080\)\. Higher resolution images will need a larger minimum face size\. 

+ Be bright and sharp\. You can use [DetectFaces](API_DetectFaces.md) to determine the brightness and sharpness of a face\.

+ Avoid occlusions such as head\-bands or masks\.