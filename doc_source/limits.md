# Limits in Amazon Rekognition<a name="limits"></a>

The following is a list of limits in Amazon Rekognition\. For information about limits you can change, see [AWS Service Quotas](https://docs.aws.amazon.com/general/latest/gr/rekognition_region.html#limits_rekognition)\. To change a limit, see [Create Case](https://console.aws.amazon.com/support/v1#/case/create?issueType=service-limit-increase)\.

For information about Transactions Per Second \(TPS\) limits, see [AWS Service Quotas](https://docs.aws.amazon.com/general/latest/gr/rekognition_region.html#limits_rekognition)\.

For Amazon Rekognition Custom Labels limits, see [Limits in Amazon Rekognition Custom Labels](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/limits.html)\.

## Amazon Rekognition Image<a name="limits-image"></a>
+ Maximum image size stored as an Amazon S3 object is limited to 15 MB\. 
+ The minimum image dimensions is 80 pixels for both height and width\. The minimum image dimension for `DetectProtectiveEquipment` is 64 pixels for both height and width\. 
+ The maximum image dimensions for `DetectProtectiveEquipment` is 4096 pixels for both width and height\.
+ To be detected by `DetectProtectiveEquipment`, a person must be no smaller than 100x100 pixels in an image with 800x1300\. Images with dimensions higher than 800x1300 pixels will need a larger minimum person size proportionally\. 
+ To be detected, a face must be no smaller than 40x40 pixels in an image with 1920X1080 pixels\. Images with dimensions higher than 1920X1080 pixels will need a larger minimum face size proportionally\. 
+ The Maximum images size as raw bytes passed in as parameter to an API is 5 MB\. The limit is 4 MB for the `DetectProtectiveEquipment` API\.
+ Amazon Rekognition supports the PNG and JPEG image formats\. That is, the images you provide as input to various API operations, such as `DetectLabels` and `IndexFaces` must be in one of the supported formats\.
+ The Maximum number of faces you can store in a single face collection is 20 million\.
+ The maximum matching faces the search API returns is 4096\.
+ DetectText can detect up to 50 words in an image\.
+ `DetectProtectiveEquipment` can detect Personal Protective Equipment on up to 15 people\.

For best practice information about images and facial comparison, see [Best practices for sensors, input images, and videos](best-practices.md)\.

## Amazon Rekognition Video stored video<a name="limits-vstored-video"></a>
+ Amazon Rekognition Video can analyze stored videos up to 10GB in size\.
+ Amazon Rekognition Video can analyze stored videos up to 6 hours in length\.
+ Amazon Rekognition Video supports a maximum of 20 concurrent jobs per account\.
+ Stored videos must be encoded using the H\.264 codec\. The supported file formats are MPEG\-4 and MOV\.
+ The Time To Live \(TTL\) period for pagination tokens is 24 hours\. Pagination tokens are in the `NextToken` field retured by Get operations such as `GetLabeldetection`\.

## Amazon Rekognition Video streaming video<a name="limits-streaming-video"></a>
+ A Kinesis Video input stream can be associated with at most 1 Amazon Rekognition Video stream processor\.
+ A Kinesis Data output stream can be associated with at most 1 Amazon Rekognition Video stream processor\. 
+ The Kinesis Video input stream and Kinesis Data output stream associated with an Amazon Rekognition Video stream processor cannot be shared by multiple processors\.