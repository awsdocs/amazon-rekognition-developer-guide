# Step 2: Set Up the AWS Command Line Interface \(AWS CLI\)<a name="setup-awscli"></a>

Follow the steps to download and configure the AWS Command Line Interface \(AWS CLI\)\.

**Important**  
You don't need the AWS CLI to perform the steps in the Getting Started exercise\. However, some of the exercises in this guide use the AWS CLI\. You can skip this step and go to [Step 4: Getting Started Using the API](get-started-exercise.md), and then set up the AWS CLI later when you need it\.

**To set up the AWS CLI**

1. Download and configure the AWS CLI\. For instructions, see the following topics in the *AWS Command Line Interface User Guide*: 

   + [Getting Set Up with the AWS Command Line Interface](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html)

   + [Configuring the AWS Command Line Interface](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

1. Add a named profile for the administrator user in the AWS CLI config file\. You use this profile when executing the AWS CLI commands\. For more information about named profiles, see [Named Profiles](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-multiple-profiles) in the *AWS Command Line Interface User Guide*\.

   ```
   [profile adminuser]
   aws_access_key_id = adminuser access key ID
   aws_secret_access_key = adminuser secret access key
   region = aws-region
   ```

   For a list of available AWS regions, see [Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html) in the *Amazon Web Services General Reference*\.

1. Verify the setup by entering the following help command at the command prompt: 

   ```
   aws help
   ```

**Formatting the AWS CLI Examples**  
The AWS CLI examples are formatted for the Linux operating system\. To use the samples with Microsoft Windows, you will need to change the JSON formatting of the `--image` parameter and change the line breaks from backslashes \(\\\) to carets\(^\)\. For more information about JSON formatting, see [Specifying Parameter Values for the AWS Command Line Interface](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html)\. The following is an example AWS CLI command formatted for Microsoft Windows\.

```
aws rekognition detect-labels ^
  --image "{\"S3Object\":{\"Bucket\":\"photo-collection\",\"Name\":\"photo.jpg\"}}" ^
  --region us-west-2
```

You can also provide a shorthand version of the JSON that works on both Microsoft Windows and Linux\.

```
aws rekognition detect-labels --image "S3Object={Bucket=photo-collection,Name=photo.jpg}" --region us-west-2
```

For more information, see [Using Shorthand Syntax with the AWS Command Line Interface](http://docs.aws.amazon.com/cli/latest/userguide/shorthand-syntax.html)\. 

## Next Step<a name="setting-up-next-step-3"></a>

[Step 4: Getting Started Using the API](get-started-exercise.md)