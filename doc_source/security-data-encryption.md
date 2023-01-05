# Data encryption<a name="security-data-encryption"></a>

The following information explains where Amazon Rekognition uses data encryption to protect your data\.

## Encryption at rest<a name="security-data-encryption-at-rest"></a>

### Amazon Rekognition Image<a name="security-ear-rekognition-image"></a>

#### Images<a name="security-image-ear-images"></a>

Images passed to Amazon Rekognition API operations may be stored and used to improve the service unless you have opted out by visiting the [AI services opt\-out policy page](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html) and following the process explained there\. The stored images are encrypted at rest \(Amazon S3\) using AWS Key Management Service \(SSE\-KMS\)\. 

#### Collections<a name="security-ear-face-comparison-collections"></a>

For face comparison operations that store information in a collection, the underlying detection algorithm first detects the faces in the input image, extracts a vector for each face, and then stores the facial vectors in the collection\. Amazon Rekognition uses these facial vectors when performing face comparison\. Facial vectors are stored as an array of floats\. The data is meaningless on its own, effectively acting as a hash, and cannot be reverse engineered\. The data is not further encrypted\. 

### Amazon Rekognition Video<a name="security-ear-rekognition-video"></a>

#### Videos<a name="security-video-ear-videos"></a>

 To analyze a video, Amazon Rekognition copies your videos into the service for processing\. The video may be stored and used to improve the service unless you have opted out by visiting the [AI services opt\-out policy page](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html) and following the process explained there\. The videos are encrypted at rest \(Amazon S3\) using AWS Key Management Service \(SSE\-KMS\)\. 

### Amazon Rekognition Custom Labels<a name="security-ear-custom-labels"></a>

Amazon Rekognition Custom Labels encrypts your data at rest\. 

#### Images<a name="security-ear-cl-images"></a>

 To train your model, Amazon Rekognition Custom Labels makes a copy of your source training and test images\. The copied images are encrypted at rest in Amazon Simple Storage Service \(S3\) using server\-side encryption with an AWS KMS key that you provide or an AWS owned KMS key\. Amazon Rekognition Custom Labels only supports symmetric KMS keys\. Your source images are unaffected\. For more information, see [Training an Amazon Rekognition Custom Labels Model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tm-train-model.html)\. 

#### Models<a name="security-ear-cl-models"></a>

By default, Amazon Rekognition Custom Labels encrypts trained models and manifest files stored in Amazon S3 buckets using server\-side encryption with an AWS owned key\. For more information, see [ Protecting Data Using Server\-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html)\. Training results are written to the bucket specified in the `OutputConfig` input parameter to [CreateProjectVersion](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateProjectVersion.html)\. The training results are encrypted using the configured encryption settings for the bucket \(`OutputConfig`\)\. 

#### Console bucket<a name="security-ear-cl-console"></a>

The Amazon Rekognition Custom Labels console creates an Amazon S3 bucket \(console bucket\) that you can use to manage your projects\. The console bucket is encrypted using the default Amazon S3 encryption\. For more information, see [Amazon Simple Storage Service default encryption for S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html)\. If you are using your own KMS key, configure the console bucket after it is created\. For more information, see [ Protecting Data Using Server\-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html)\. Amazon Rekognition Custom Labels blocks public access to the console bucket\.

## Encryption in transit<a name="security-data-encryption-in-transit"></a>

Amazon Rekognition API endpoints only support secure connections over HTTPS\. All communication is encrypted with Transport Layer Security \(TLS\)\. 

## Key management<a name="security-data-encryption-key-management"></a>

You can use AWS Key Management Service \(KMS\) to manage keys for the input images and videos you store in Amazon S3 buckets\. For more information, see [AWS Key Management Service concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys)\.