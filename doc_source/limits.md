# Limits in Amazon Rekognition<a name="limits"></a>

The following is a list of limits in Amazon Rekognition:

+ Maximum image size stored as an Amazon S3 object is limited to 15 MB\. 

+ The minimum pixel resolution for height and width is 80 pixels

+ To be detected, a face must be no smaller that 40x40 pixels in an image with 1920X1080 pixels\. Images with dimensions higher than 1920X1080 pixels will need a larger minimum face size proportionally\. 

+ Maximum images size as raw bytes passed in as parameter to an API is 5 MB\.

+ Amazon Rekognition supports the PNG and JPEG image formats\. That is, the images you provide as input to various API operations, such as `DetectLabels` and `IndexFaces` must be in one of the supported formats\.

+ Maximum number of faces you can store in a single face collection is 20 million\.

+ The maximum matching faces the search API returns is 4096\.

+ Rekognition Video can analyze stored videos up to 8GB in size\.

+ A Kinesis Video input stream can be associated with at most 1 Rekognition Video stream processor\.

+ A Kinesis Data output stream can be associated with at most 1 Rekognition Video stream processor\. 

+ The Kinesis Video input stream and Kinesis Data output stream associated with a Rekognition Video stream processor cannot be shared by multiple processors\.

+ For a given AWS account, the maximum number of Rekognition Video stream processors that can simultaneously exist in a single region is 10\. An AWS account can have more than 10 simultaneously existing stream processors by using multiple regions\. 