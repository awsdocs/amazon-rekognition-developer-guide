# Limits in Amazon Rekognition<a name="limits"></a>

The following is a list of limits in Amazon Rekognition\. For information about limits you can change, see [AWS Service Limits](http://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)\. To change a limit, see [Create Case](https://console.aws.amazon.com/support/v1#/case/create?issueType=service-limit-increase)\.

## Amazon Rekognition Image<a name="limits-image"></a>
+ Maximum image size stored as an Amazon S3 object is limited to 15 MB\. 
+ The minimum pixel resolution for height and width is 80 pixels
+ To be detected, a face must be no smaller that 40x40 pixels in an image with 1920X1080 pixels\. Images with dimensions higher than 1920X1080 pixels will need a larger minimum face size proportionally\. 
+ The Maximum images size as raw bytes passed in as parameter to an API is 5 MB\.
+ Amazon Rekognition supports the PNG and JPEG image formats\. That is, the images you provide as input to various API operations, such as `DetectLabels` and `IndexFaces` must be in one of the supported formats\.
+ The Maximum number of faces you can store in a single face collection is 20 million\.
+ The maximum matching faces the search API returns is 4096\.
+ The default Transactions Per Second \(TPS\) limits, per account, for image operations are:  
****    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/rekognition/latest/dg/limits.html)

## Amazon Rekognition Video Stored Video<a name="limits-vstored-video"></a>
+ Amazon Rekognition Video can analyze stored videos up to 8GB in size\.
+ Amazon Rekognition Video supports a maximum of 20 concurrent jobs per account\.
+ The default TPS limits, per account, for video storage operations are:  
****    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/rekognition/latest/dg/limits.html)

## Amazon Rekognition Video Streaming Video<a name="limits-streaming-video"></a>
+ A Kinesis Video input stream can be associated with at most 1 Amazon Rekognition Video stream processor\.
+ A Kinesis Data output stream can be associated with at most 1 Amazon Rekognition Video stream processor\. 
+ The Kinesis Video input stream and Kinesis Data output stream associated with an Amazon Rekognition Video stream processor cannot be shared by multiple processors\.
+ For a given AWS account, the default number of Amazon Rekognition Video stream processors that can simultaneously exist in a single region is 10\. 
+ The default TPS limits, per account, for all streaming video operations are:  
****    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/rekognition/latest/dg/limits.html)