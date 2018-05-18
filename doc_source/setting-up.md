# Step 1: Set Up an AWS Account and Create an Administrator User<a name="setting-up"></a>

Before you use Amazon Rekognition for the first time, complete the following tasks:

1. [Sign up for AWS](#setting-up-signup)

1. [Create an IAM User](#setting-up-iam)

## Sign up for AWS<a name="setting-up-signup"></a>

When you sign up for Amazon Web Services \(AWS\), your AWS account is automatically signed up for all services in AWS, including Amazon Rekognition\. You are charged only for the services that you use\.

With Amazon Rekognition, you pay only for the resources you use\.  If you are a new AWS customer, you can get started with Amazon Rekognition for free\. For more information, see [AWS Free Usage Tier](https://aws.amazon.com//free/)\.

If you already have an AWS account, skip to the next task\. If you don't have an AWS account, perform the steps in the following procedure to create one\.

**To create an AWS account**

1. Open [https://aws\.amazon\.com/](https://aws.amazon.com/), and then choose **Create an AWS Account**\.
**Note**  
This might be unavailable in your browser if you previously signed into the AWS Management Console\. In that case, choose **Sign in to a different account**, and then choose **Create a new AWS account**\.

1. Follow the online instructions\.

   Part of the sign\-up procedure involves receiving a phone call and entering a PIN using the phone keypad\.

Note your AWS account ID because you'll need it for the next task\.

## Create an IAM User<a name="setting-up-iam"></a>

Services in AWS, such as Amazon Rekognition, require that you provide credentials when you access them so that the service can determine whether you have permissions to access the resources owned by that service\. The console requires your password\. You can create access keys for your AWS account to access the AWS CLI or API\. However, we don't recommend that you access AWS using the credentials for your AWS account\. Instead, we recommend that you use AWS Identity and Access Management \(IAM\)\. Create an IAM user, add the user to an IAM group with administrative permissions, and then grant administrative permissions to the IAM user that you created\. You can then access AWS using a special URL and that IAM user's credentials\.

If you signed up for AWS, but you haven't created an IAM user for yourself, you can create one using the IAM console\.

The Getting Started exercises in this guide assume that you have a user \(`adminuser`\) with administrator privileges\. Follow the procedure to create `adminuser` in your account\.

**To create an administrator user and sign in to the console**

1. Create an administrator user called `adminuser` in your AWS account\. For instructions, see [Creating Your First IAM User and Administrators Group](http://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide*\.

1. A user can sign in to the AWS Management Console using a special URL\. For more information, [How Users Sign In to Your Account](http://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_how-users-sign-in.html) in the *IAM User Guide*\.

For more information about IAM, see the following:
+ [AWS Identity and Access Management \(IAM\)](https://aws.amazon.com/iam/)
+ [Getting Started](http://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html)
+ [IAM User Guide](http://docs.aws.amazon.com/IAM/latest/UserGuide/)

## Next Step<a name="setting-up-next-step-2"></a>

[Step 2: Set Up the AWS Command Line Interface \(AWS CLI\)](setup-awscli.md)