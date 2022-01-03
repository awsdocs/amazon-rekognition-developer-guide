# Detect people and objects in a video with Amazon Rekognition using an AWS SDK<a name="example_cross_RekognitionVideoDetection_section"></a>

The following code examples show how to detect people and objects in a video with Amazon Rekognition\.

------
#### [ Java ]

**SDK for Java 2\.x**  
 Shows how to use Amazon Rekognition Java API to create an app to detect faces and objects in videos located in an Amazon Simple Storage Service \(Amazon S3\) bucket\. The app sends the admin an email notification with the results using Amazon Simple Email Service \(Amazon SES\)\.   
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/usecases/video_analyzer_application)\.   

**Services used in this example**
+ Amazon Rekognition
+ Amazon S3
+ Amazon SES

------
#### [ JavaScript ]

**SDK for JavaScript V3**  
 Shows how to use Amazon Rekognition with the AWS SDK for JavaScript to create an app to detect faces and objects in videos located in an Amazon Simple Storage Service \(Amazon S3\) bucket\. The app sends the admin an email notification with the results using Amazon Simple Email Service \(Amazon SES\)\.   
Learn how to:  
+ Create an unauthenticated user using Amazon Cognito\.
+ Analyze images for PPE using Amazon Rekognition\.
+ Verify an email address for Amazon SES\.
+ Send an email notification using Amazon SES\.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cross-services/video-analyzer)\.   

**Services used in this example**
+ Amazon Rekognition
+ Amazon S3
+ Amazon SES

------
#### [ Python ]

**SDK for Python \(Boto3\)**  
 Use Amazon Rekognition to detect faces, objects, and people in videos by starting asynchronous detection jobs\. This example also configures Amazon Rekognition to notify an Amazon Simple Notification Service \(Amazon SNS\) topic when jobs complete and subscribes an Amazon Simple Queue Service \(Amazon SQS\) queue to the topic\. When the queue receives a message about a job, the job is retrieved and the results are output\.   
 This example is best viewed on GitHub\. For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/rekognition)\.   

**Services used in this example**
+ Amazon Rekognition
+ Amazon SNS
+ Amazon SQS

------

For a complete list of AWS SDK developer guides and code examples, including help getting started and information about previous versions, see [Using Rekognition with an AWS SDK](sdk-general-information-section.md)\.