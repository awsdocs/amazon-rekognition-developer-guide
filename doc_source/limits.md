# Guidelines and quotas in Amazon Rekognition<a name="limits"></a>

The following sections provide guidelines and quotas when using Amazon Rekognition\. There are two kinds of quotas\. *Set quotas* such as maximum image size cannot be changed\. *Default quotas* listed on the [AWS Service Quotas](https://docs.aws.amazon.com/general/latest/gr/rekognition.html#limits_rekognition) page can be changed by following the procedure described in the [Default quotas](#changeable-quotas) section\.

**Topics**
+ [Supported regions](#supported-regions)
+ [Set quotas](#quotas)
+ [Default quotas](#changeable-quotas)

## Supported regions<a name="supported-regions"></a>

For a list of AWS Regions where Amazon Rekognition is available, see [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rekognition.html) in the *Amazon Web Services General Reference*\.

## Set quotas<a name="quotas"></a>

The following is a list of limits in Amazon Rekognition that cannot be changed\. For information about limits you can change, such as Transactions Per Second \(TPS\) limits, see [Default quotas](#changeable-quotas)\. 

For Amazon Rekognition Custom Labels limits, see [Guidelines and Quotas in Amazon Rekognition Custom Labels](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/limits.html)\.

### Amazon Rekognition Image<a name="limits-image"></a>
+ Maximum image size stored as an Amazon S3 object is limited to 15 MB\. 
+ The minimum image dimensions is 80 pixels for both height and width\. The minimum image dimension for `DetectProtectiveEquipment` is 64 pixels for both height and width\. 
+ The maximum image dimensions for `DetectProtectiveEquipment` is 4096 pixels for both width and height\.
+ To be detected by `DetectProtectiveEquipment`, a person must be no smaller than 100x100 pixels in an image with 800x1300\. Images with dimensions higher than 800x1300 pixels will need a larger minimum person size proportionally\. 
+ To be detected, a face must be no smaller than 40x40 pixels in an image with 1920X1080 pixels\. Images with dimensions higher than 1920X1080 pixels will need a larger minimum face size proportionally\. 
+ The Maximum images size as raw bytes passed in as parameter to an API is 5 MB\. The limit is 4 MB for the `DetectProtectiveEquipment` API\.
+ Amazon Rekognition supports the PNG and JPEG image formats\. That is, the images you provide as input to various API operations, such as `DetectLabels` and `IndexFaces` must be in one of the supported formats\.
+ The Maximum number of faces you can store in a single face collection is 20 million\.
+ The maximum matching faces the search API returns is 4096\.
+ DetectText can detect up to 100 words in an image\.
+ `DetectProtectiveEquipment` can detect Personal Protective Equipment on up to 15 people\.

For best practice information about images and facial comparison, see [Best practices for sensors, input images, and videos](best-practices.md)\.

### Amazon Rekognition Video stored video<a name="limits-vstored-video"></a>
+ Amazon Rekognition Video can analyze stored videos up to 10GB in size\.
+ Amazon Rekognition Video can analyze stored videos up to 6 hours in length\.
+ Amazon Rekognition Video supports a maximum of 20 concurrent jobs per account\.
+ Stored videos must be encoded using the H\.264 codec\. The supported file formats are MPEG\-4 and MOV\.
+ Any Amazon Rekognition Video API that analyzes audio data only supports AAC audio codecs\.
+ The Time To Live \(TTL\) period for pagination tokens is 24 hours\. Pagination tokens are in the `NextToken` field retured by Get operations such as `GetLabeldetection`\.

### Amazon Rekognition Video streaming video<a name="limits-streaming-video"></a>
+ A Kinesis Video input stream can be associated with at most 1 Amazon Rekognition Video stream processor\.
+ A Kinesis Data output stream can be associated with at most 1 Amazon Rekognition Video stream processor\. 
+ The Kinesis Video input stream and Kinesis Data output stream associated with an Amazon Rekognition Video stream processor cannot be shared by multiple processors\.
+ Any Amazon Rekognition Video API that analyzes audio data only supports ACC audio codecs\.

## Default quotas<a name="changeable-quotas"></a>

A list of default quotas can be found at [AWS Service Quotas](https://docs.aws.amazon.com/general/latest/gr/rekognition.html#limits_rekognition)\. These limits are defaults and can be changed\. To request a limit increase, you create a case\. To see your current quota limits \(applied quota values\), see [Amazon Rekognition Service Quotas](https://us-west-2.console.aws.amazon.com/servicequotas/home/services/rekognition/quotas)\. To view your TPS utilization history for [Amazon Rekognition Image APIs](https://docs.aws.amazon.com/rekognition/latest/dg/API_Reference.html), see the [Amazon Rekognition Service Quotas page](https://us-west-2.console.aws.amazon.com/servicequotas/home/services/rekognition/quotas) and choose a specific API operation to see the history for that operation\. 

**Topics**
+ [Calculate TPS quota change](#quotas-calculating)
+ [Best practices for TPS quotas](#quotas-best-practices)
+ [Create a case to change TPS quotas](#quotas-create-case)

### Calculate TPS quota change<a name="quotas-calculating"></a>

What is the new limit you are requesting? Transactions Per Second \(TPS\) are most relevant at the peak of an expected workload\. It is important to understand the max concurrent API calls at the peak of a workload and time for responses \(5 \- 15 seconds\)\. Please note, 5 seconds should be the minimum\. Below are two examples:
+ Example 1: The max concurrent Face Authentication \(CompareFaces API\) users I expect at the beginning of my busiest hour is 1000\. These responses will be spread over a period of 10 seconds\. Therefore, the TPS required is 100 \(1000/10\) for the CompareFaces API in my relevant region\.
+ Example 2: The max concurrent Object Detection \(DetectLabels API\) calls that are expected at the beginning of my busiest hour is 250\. These responses will be spread over a period of 5 seconds\. Therefore, the TPS required is 50 \(250/5\) for the DetectLabels API in my relevant region\.

### Best practices for TPS quotas<a name="quotas-best-practices"></a>

Recommended best practices for Transactions Per Second \(TPS\) include smoothening spiky traffic, configuring retries, and configuring exponential backoff and jitter\.

1. Smooth spiky traffic\. Spiky traffic affects throughput\. To get maximum throughput for the allotted transactions per second \(TPS\), use a queueing serverless architecture or another mechanism to “smooth” traffic so it is more consistent\. For code samples and references for serverless large\-scale image and video processing with Rekognition, see [Large scale image and video processing with Amazon Rekognition](https://github.com/aws-samples/amazon-rekognition-serverless-large-scale-image-and-video-processing)\. 

1. Configure retries\. Follow the guidelines at [Error handling](error-handling.md) to configure retries for the errors that allow them\.

1. Configure exponential backoff and jitter\. Configuring exponential backoff and jitter as you configure retries allows you to improve the achievable throughput\. See [Error retries and exponential backoff in AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html)\.

### Create a case to change TPS quotas<a name="quotas-create-case"></a>

To create a case, go to [Create Case](https://console.aws.amazon.com/support/v1#/case/create?issueType=service-limit-increase) and answer the following questions: 
+ Have you implemented the [Best practices for TPS quotas](#quotas-best-practices) for smoothening your traffic spikes and configuring retries, exponential backoff, and jitter? 
+ Have you calculated the TPS quota change you need? If not, see [Calculate TPS quota change](#quotas-calculating)\.
+ Have you checked your TPS usage history to more accurately predict your future needs? To view your TPS usage history, see the [Amazon Rekognition Service Quotas page](https://us-west-2.console.aws.amazon.com/servicequotas/home/services/rekognition/quotas)\.
+ What is your use case?
+ What APIs do you plan to use?
+ What regions do you plan to use these APIs in?
+ Are you able to spread the load across multiple regions?
+ How many images do you process daily?
+ How long do you expect to sustain this volume \(Is it a one\-time spike or ongoing\)?
+ How are you blocked by the default limit? Review the following exception table to confirm the scenario that you are encountering\.    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/rekognition/latest/dg/limits.html)

  For a detailed understanding of the error codes, see [Error handling](error-handling.md)\.

**Note**  
These limits depend on the region you are in\. Making a case to change a limit affects the API operation you request, in the region you request it\. Other API operations and regions are not affected\.