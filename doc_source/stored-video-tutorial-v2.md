# Tutorial: Creating AWS video analyzer applications<a name="stored-video-tutorial-v2"></a>

You can create a Java web application that analyzes videos for label detection by using the AWS SDK for Java version 2\. The application created in this AWS tutorial lets you upload a video \(MP4 file\) to an Amazon S3 bucket\. Then the appliction uses the Amazon Rekognition service to analyze the video\. The results are used to populate a data model and then a report is generated and emailed to a specific user by using the Amazon Simple Email Service\.

The following illustration shows a report that is generated after the application completes analyzing the video\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/v2-video-tutorial-table.png)

In this tutorial, you create a Spring Boot application that invokes various AWS services\. The Spring Boot APIs are used to build a model, different views, and a controller\. For more information, see [Spring Boot](https://spring.io/projects/spring-boot)\.

This service uses the following AWS services:
+ Amazon Rekognition
+ [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
+ [Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html)
+ [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)

The AWS services included in this tutorial are included in the AWS Free Tier\. We recommend that you terminate all of the resources you create in the tutorial when you are finished with them to avoid being charged\.

## Prerequisites<a name="stored-video-tutorial-prerequisites"></a>

Before you begin, you need to complete the steps in [Setting Up the AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup.html)\. Then make sure that you have the following: 
+ Java 1\.8 JDK\.
+ Maven 3\.6 or later\.
+ An Amazon S3 bucket named **video\[somevalue\]**\. Be sure to use this bucket name in your Amazon S3 Java code\. For more information, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)\.
+ An IAM role\. You need this for the **VideoDetectFaces** class that you will create\. For more information, see [Configuring Amazon Rekognition Video](https://docs.aws.amazon.com/rekognition/latest/dg/api-video-roles.html)\.
+ A valid Amazon SNS topic\. You need this for the **VideoDetectFaces** class that you will create\. For more information, see [Configuring Amazon Rekognition Video](https://docs.aws.amazon.com/rekognition/latest/dg/api-video-roles.html)\.

## Procedure<a name="stored-video-tutorial-procedure"></a>

In the course of the tutorial, you do the following:

1. Create a project

1. Add the POM dependencies to your project

1. Create the Java classes

1. Create the HTML files

1. Create the script files

1. Package the project into a JAR file

1. Deploy the application to AWS Elastic Beanstalk

To proceed with the tutorial, follow the detailed instructions in the [AWS Documentation SDK examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/javav2/usecases/video_analyzer_application)\.