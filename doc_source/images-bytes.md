# Analysing an Image Loaded from a Local File System<a name="images-bytes"></a>

Rekognition Image operations can analyze images supplied as images bytes or images stored in an S3 bucket\.

These topics provides AWS SDK examples of supplying image bytes to Rekognition Image API operations by using a file loaded from a local file system\. A Rekognition API operation can analyse an image provided as base64 encoded image bytes or it can analyze an image retrieved from an Amazon S3 bucket\. You pass an image to a Rekognition API operation by using the [Image](API_Image.md) input parameter\. Within `Image` you specify the `Bytes` property to pass base64 encoded image bytes or you specify the [S3Object](API_S3Object.md) object property to reference an image stored in an S3 bucket\.

Image bytes passed to a Rekognition API operation using the `Bytes` input parameter must be base64 encoded\. The following common AWS SDKs automatically base64 encode images and you do not need to encode image bytes prior to calling a Rekognition API operation\.
+ Java
+ JavaScript
+ Python
+ PHP

If you are using another AWS SDK and get an image format error when calling a Rekognition API operation, try base64 encoding the image bytes before passing them to a Rekognition API operation\.

**Note**  
The image does not need to be base64 encoded if you pass an image stored in an `S3Object` instead of image bytes\.

 If you use HTTP to call Rekognition Image operations, the image bytes must be a base64\-encoded string\. For more information, see [Working with Images](images.md)\.

If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported\.

 The following examples show how to load images from the local file system and supply the image bytes to a Rekognition operation\. 

**Topics**
+ [Using Java](images-bytes-java.md)
+ [Using JavaScript](image-bytes-javascript.md)
+ [Using Python](images-bytes-python.md)
+ [Using PHP](images-bytes-php.md)