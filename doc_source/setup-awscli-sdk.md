# Step 2: Set up the AWS CLI and AWS SDKs<a name="setup-awscli-sdk"></a>

The following steps show you how to install the AWS Command Line Interface \(AWS CLI\) and AWS SDKs that the examples in this documentation use\. There are a number of different ways to authenticate AWS SDK calls\. The examples in this guide assume that you're using a default credentials profile for calling AWS CLI commands and AWS SDK API operations\.

For a list of available AWS Regions, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the *Amazon Web Services General Reference*\.

Follow the steps to download and configure the AWS SDKs\.

**To set up the AWS CLI and the AWS SDKs**

1. Download and install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install) and the AWS SDKs that you want to use\. This guide provides examples for the AWS CLI, Java, Python, Ruby, Node\.js, PHP, \.NET, and JavaScript\. For information about installing AWS SDKs, see [Tools for Amazon Web Services](https://aws.amazon.com/tools/)\.

1. Create an access key for the user you created in [Create an IAM user](setting-up.md#setting-up-iam)\.

   1. Sign in to the AWS Management Console and open the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

   1. In the navigation pane, choose **Users**\.

   1. Choose the name of the user you created in [Create an IAM user](setting-up.md#setting-up-iam)\.

   1. Choose the **Security credentials** tab\.

   1. Choose **Create access key**\. Then choose **Download \.csv file** to save the access key ID and secret access key to a CSV file on your computer\. Store the file in a secure location\. You will not have access to the secret access key again after this dialog box closes\. After you have downloaded the CSV file, choose **Close**\. 

1. If you have installed the AWS CLI, you can [configure the credentials and region for most AWS SDKs by entering `aws configure` at the command prompt](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)\. Otherwise, use the following instructions\.

1. On your computer, navigate to your home directory, and create an `.aws` directory\. On Unix\-based systems, such as Linux or macOS, this is in the following location: 

   ```
   ~/.aws
   ```

   On Windows, this is in the following location:

   ```
   %HOMEPATH%\.aws
   ```

1. In the `.aws` directory, create a new file named `credentials`\. 

1. Open the credentials CSV file that you created in step 2 and copy its contents into the `credentials` file using the following format:

   ```
   [default]
   aws_access_key_id = your_access_key_id
   aws_secret_access_key = your_secret_access_key
   ```

   Substitute your access key ID and secret access key for *your\_access\_key\_id* and *your\_secret\_access\_key*\.

1. Save the `Credentials` file and delete the CSV file\.

1. In the `.aws` directory, create a new file named `config`\. 

1. Open the `config` file and enter your region in the following format\.

   ```
   [default]
   region = your_aws_region
   ```

   Substitute your desired AWS Region \(for example, `us-west-2`\) for *your\_aws\_region*\. 
**Note**  
If you don't select a region, then us\-east\-1 will be used by default\. 

1. Save the `config` file\.

## Next step<a name="setting-up-next-step-3"></a>

[Step 3: Getting started using the AWS CLI and AWS SDK API](get-started-exercise.md)