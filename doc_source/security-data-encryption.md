# Data Encryption<a name="security-data-encryption"></a>

The following information explains where Amazon Rekognition uses data encryption to protect your data\.

## Encryption at Rest<a name="security-data-encryption-at-rest"></a>

### Images<a name="security-images"></a>

Images passed to Amazon Rekognition API operations may be stored and used to improve the service unless you have opted out by contacting [AWS Support](http://aws.amazon.com/contact-us/) and following the process provided to you\. The stored images are encrypted at rest \(Amazon S3\) using AWS Key Management Service \(SSE\-KMS\)\. 

### Collections<a name="security-face-comparison-collections"></a>

For face comparison operations that store information in a collection, the underlying detection algorithm first detects the faces in the input image, extracts a vector for each face, and then stores the facial vectors in the collection\. Amazon Rekognition uses these facial vectors when performing face comparison\. Facial vectors are stored as an array of floats\. The data is meaningless on its own, effectively acting as a hash, and cannot be reverse engineered\. The data is not further encrypted\. 

### Videos<a name="security-videos"></a>

 To analyze a video, Amazon Rekognition copies your videos into the service for processing\. The video may be stored and used to improve the service unless you have opted out by contacting [AWS Support](http://aws.amazon.com/contact-us/) and following the process provided to you\. The videos are encrypted at rest \(Amazon S3\) using AWS Key Management Service \(SSE\-KMS\)\. 

### Amazon Rekognition Custom Labels Models<a name="security-models"></a>

 Trained models and other customer data is encrypted using server\-side encryption with Amazon S3\-Managed Keys \(SSE\-S3\)\. For more information, see [ Protecting Data Using Server\-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html)\.

## Encryption in Transit<a name="security-data-encryption-in-transit"></a>

Amazon Rekognition API endpoints only support secure connections over HTTPS\. All communication is encrypted with Transport Layer Security \(TLS\)\. 

## Key Management<a name="security-data-encryption-key-management"></a>

You can use AWS Key Management Service \(KMS\) to manage keys for the input images and videos you store in Amazon S3 buckets\.