# Amazon Rekognition Image Operation Latency<a name="operation-latency"></a>

To ensure the lowest possible latency for Amazon Rekognition Image operations, consider the following:
+ The region for the Amazon S3 bucket containing your images must match the region you use for Amazon Rekognition Image API operations\. 
+ Calling an Amazon Rekognition Image operation with image bytes is faster than uploading the image to an Amazon S3 bucket and then referencing the uploaded image in an Amazon Rekognition Image operation\. Consider this approach if you are uploading images to Amazon Rekognition Image for near real\-time processing\. For example, images uploaded from an IP camera or images uploaded through a web portal\.
+ If the image is already in an Amazon S3 bucket, referencing it in an Amazon Rekognition Image operation will probably be faster than passing image bytes to the operation\.