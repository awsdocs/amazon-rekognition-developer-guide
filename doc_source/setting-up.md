# Step 1: Set Up an AWS Account and Create an IAM User<a name="setting-up"></a>

Before you use Amazon Rekognition for the first time, complete the following tasks:

1. [Sign up for AWS](#setting-up-signup)

1. [Create an IAM User](#setting-up-iam)

## Sign up for AWS<a name="setting-up-signup"></a>

When you sign up for Amazon Web Services \(AWS\), your AWS account is automatically signed up for all services in AWS, including Amazon Rekognition\. You're charged only for the services that you use\.

With Amazon Rekognition, you pay only for the resources you use\.  If you're a new AWS customer, you can get started with Amazon Rekognition for free\. For more information, see [AWS Free Usage Tier](https://aws.amazon.com//free/)\.

If you already have an AWS account, skip to the next task\. If you don't have an AWS account, perform the steps in the following procedure to create one\.

**To create an AWS account**

1. Open [https://aws\.amazon\.com/](https://aws.amazon.com/), and then choose **Create an AWS Account**\.
**Note**  
If you previously signed in to the AWS Management Console using AWS account root user credentials, choose **Sign in to a different account**\. If you previously signed in to the console using IAM credentials, choose **Sign\-in using root account credentials**\. Then choose **Create a new AWS account**\.

1. Follow the online instructions\.

   Part of the sign\-up procedure involves receiving a phone call and entering a verification code using the phone keypad\.

Note your AWS account ID because you'll need it for the next task\.

## Create an IAM User<a name="setting-up-iam"></a>

Services in AWS, such as Amazon Rekognition, require that you provide credentials when you access them\. This is so that the service can determine whether you have permissions to access the resources owned by that service\. The console requires your password\. You can create access keys for your AWS account to access the AWS CLI or API\. However, we don't recommend that you access AWS by using the credentials for your AWS account\. Instead, we recommend that you:
+ Use AWS Identity and Access Management \(IAM\) to create an IAM user\.
+ Add the user to an IAM group with administrative permissions\.

You can then access AWS by using a special URL and that IAM user's credentials\.

If you signed up for AWS, but you haven't created an IAM user for yourself, you can create one by using the IAM console\. Follow the procedure to create an IAM user in your account\.

**To create an IAM user and sign in to the console**

1. Create an IAM user with administrator permissions in your AWS account\. For instructions, see [Creating Your First IAM User and Administrators Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide*\.

1. As the IAM user, sign in to the AWS Management Console by using a special URL\. For more information, [How Users Sign In to Your Account](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_how-users-sign-in.html) in the *IAM User Guide*\.

**Note**  
An IAM user with administrator permissions has unrestricted access to the AWS services in your account\. For information about restricting access to Amazon Rekognition operations, see [Using Identity\-Based Policies \(IAM Policies\) for Amazon Rekognition](using-identity-based-policies.md)\. The code examples in this guide assume that you have a user with the `AmazonRekognitionFullAccess` permissions\. `AmazonS3ReadOnlyAccess` is required for examples that access images or videos that are stored in an Amazon S3 bucket\. The Amazon Rekognition Video stored video code examples also require `AmazonSQSFullAccess` permissions\. Depending on your security requirements, you might want to use an IAM group that's limited to these permissions\. For more information, see [Creating IAM Groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_create.html)\.

For more information about IAM, see the following:
+ [AWS Identity and Access Management \(IAM\)](https://aws.amazon.com/iam/)
+ [Getting Started](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html)
+ [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)

## Next Step<a name="setting-up-next-step-2"></a>

[Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)