# Step 3: Getting Started Using the AWS CLI and AWS SDK API<a name="get-started-exercise"></a>

After you've set up the AWS CLI and AWS SDKs that you want to use, you can build applications that use Amazon Rekognition\. The following topics show you how to get started with Amazon Rekognition Image and Amazon Rekognition Video\.
+ [Working with Images](images.md)
+ [Working with Stored Videos](video.md)
+ [Working with Streaming Videos](streaming-video.md)

## Formatting the AWS CLI Examples<a name="format-cli"></a>

The AWS CLI examples in this guide are formatted for the Linux operating system\. To use the samples with Microsoft Windows, you need to change the JSON formatting of the `--image` parameter, and change the line breaks from backslashes \(\\\) to carets \(^\)\. For more information about JSON formatting, see [Specifying Parameter Values for the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html)\. The following is an example AWS CLI command that's formatted for Microsoft Windows\.

```
aws rekognition detect-labels ^
  --image "{\"S3Object\":{\"Bucket\":\"photo-collection\",\"Name\":\"photo.jpg\"}}" ^
  --region us-west-2
```

You can also provide a shorthand version of the JSON that works on both Microsoft Windows and Linux\.

```
aws rekognition detect-labels --image "S3Object={Bucket=photo-collection,Name=photo.jpg}" --region us-west-2
```

For more information, see [Using Shorthand Syntax with the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/shorthand-syntax.html)\. 

## Next Step<a name="setting-up-next-step-4"></a>

[Step 4: Getting Started Using the Amazon Rekognition Console](getting-started-console.md)