# Detect objects in images with Amazon Rekognition using an AWS SDK<a name="example_cross_RekognitionPhotoAnalyzer_section"></a>

The following code examples show how to build an app that uses Amazon Rekognition to detect objects by category in images\.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples)\. Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo\. 

------
#### [ \.NET ]

**AWS SDK for \.NET**  
 Shows how to use Amazon Rekognition \.NET API to create an app that uses Amazon Rekognition to identify objects by category in images located in an Amazon Simple Storage Service \(Amazon S3\) bucket\. The app sends the admin an email notification with the results using Amazon Simple Email Service \(Amazon SES\)\.   
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/cross-service/PhotoAnalyzerApp)\.   

**Services used in this example**
+ Amazon Rekognition
+ Amazon S3
+ Amazon SES

------
#### [ Java ]

**SDK for Java 2\.x**  
 Shows how to use Amazon Rekognition Java API to create an app that uses Amazon Rekognition to identify objects by category in images located in an Amazon Simple Storage Service \(Amazon S3\) bucket\. The app sends the admin an email notification with the results using Amazon Simple Email Service \(Amazon SES\)\.   
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/usecases/creating_photo_analyzer_app)\.   

**Services used in this example**
+ Amazon Rekognition
+ Amazon S3
+ Amazon SES

------
#### [ JavaScript ]

**SDK for JavaScript V3**  
 Shows how to use Amazon Rekognition with the AWS SDK for JavaScript to create an app that uses Amazon Rekognition to identify objects by category in images located in an Amazon Simple Storage Service \(Amazon S3\) bucket\. The app sends the admin an email notification with the results using Amazon Simple Email Service \(Amazon SES\)\.   
Learn how to:  
+ Create an unauthenticated user using Amazon Cognito\.
+ Analyze images for objects using Amazon Rekognition\.
+ Verify an email address for Amazon SES\.
+ Send an email notification using Amazon SES\.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cross-services/photo_analyzer)\.   

**Services used in this example**
+ Amazon Rekognition
+ Amazon S3
+ Amazon SES

------
#### [ Kotlin ]

**SDK for Kotlin**  
This is prerelease documentation for a feature in preview release\. It is subject to change\.
 Shows how to use Amazon Rekognition Kotlin API to create an app that uses Amazon Rekognition to identify objects by category in images located in an Amazon Simple Storage Service \(Amazon S3\) bucket\. The app sends the admin an email notification with the results using Amazon Simple Email Service \(Amazon SES\)\.   
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/usecases/creating_photo_analyzer_app)\.   

**Services used in this example**
+ Amazon Rekognition
+ Amazon S3
+ Amazon SES

------
#### [ Python ]

**SDK for Python \(Boto3\)**  
 Shows you how to use the AWS SDK for Python \(Boto3\) to create a web application that lets you do the following:   
+ Upload photos to an Amazon Simple Storage Service \(Amazon S3\) bucket\.
+ Use Amazon Rekognition to analyze and label the photos\.
+ Use Amazon Simple Email Service \(Amazon SES\) to send email reports of image analysis\.
 This example contains two main components: a webpage written in JavaScript that is built with React, and a REST service written in Python that is built with Flask\-RESTful\.   
You can use the React webpage to:  
+ Display a list of images that are stored in your S3 bucket\.
+ Upload images from your computer to your S3 bucket\.
+ Display images and labels that identify items that are detected in the image\.
+ Get a report of all images in your S3 bucket and send an email of the report\.
The webpage calls the REST service\. The service sends requests to AWS to perform the following actions:   
+ Get and filter the list of images in your S3 bucket\.
+ Upload photos to your S3 bucket\.
+ Use Amazon Rekognition to analyze individual photos and get a list of labels that identify items that are detected in the photo\.
+ Analyze all photos in your S3 bucket and use Amazon SES to email a report\.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/cross_service/photo_analyzer)\.   

**Services used in this example**
+ Amazon Rekognition
+ Amazon S3
+ Amazon SES

------

For a complete list of AWS SDK developer guides and code examples, see [Using Rekognition with an AWS SDK](sdk-general-information-section.md)\. This topic also includes information about getting started and details about previous SDK versions\.