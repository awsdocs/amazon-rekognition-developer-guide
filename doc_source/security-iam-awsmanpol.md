# AWS managed policies for Amazon Rekognition<a name="security-iam-awsmanpol"></a>







To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself\. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need\. To get started quickly, you can use our AWS managed policies\. These policies cover common use cases and are available in your AWS account\. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*\.

AWS services maintain and update AWS managed policies\. You can't change the permissions in AWS managed policies\. Services occasionally add additional permissions to an AWS managed policy to support new features\. This type of update affects all identities \(users, groups, and roles\) where the policy is attached\. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available\. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions\.

Additionally, AWS supports managed policies for job functions that span multiple services\. For example, the **ReadOnlyAccess** AWS managed policy provides read\-only access to all AWS services and resources\. When a service launches a new feature, AWS adds read\-only permissions for new operations and resources\. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*\.









## AWS managed policy: AmazonRekognitionFullAccess<a name="security-iam-awsmanpol-AmazonRekognitionFullAccess"></a>

`AmazonRekognitionFullAccess` grants full access to Amazon Rekognition resources including creating and deleting collections\.

You can attach the `AmazonRekognitionFullAccess` policy to your IAM identities\. 

**Permissions details**

This policy includes the following permissions\.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "rekognition:*"
            ],
            "Resource": "*"
        }
    ]
}
```

## AWS managed policy: AmazonRekognitionReadOnlyAccess<a name="security-iam-awsmanpol-AmazonRekognitionReadOnlyAccess"></a>

`AmazonRekognitionReadOnlyAccess` grants read\-only access to Amazon Rekognition resources\.

You can attach the `AmazonRekognitionReadOnlyAccess` policy to your IAM identities\. 

**Permissions details**

This policy includes the following permissions\.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "rekognition:CompareFaces",
                "rekognition:DetectFaces",
                "rekognition:DetectLabels",
                "rekognition:ListCollections",
                "rekognition:ListFaces",
                "rekognition:SearchFaces",
                "rekognition:SearchFacesByImage",
                "rekognition:DetectText", 
                "rekognition:GetCelebrityInfo",
                "rekognition:RecognizeCelebrities",
                "rekognition:DetectModerationLabels",  
                "rekognition:GetLabelDetection",
                "rekognition:GetFaceDetection",
                "rekognition:GetContentModeration",
                "rekognition:GetPersonTracking",
                "rekognition:GetCelebrityRecognition",
                "rekognition:GetFaceSearch",
                "rekognition:GetTextDetection",
                "rekognition:GetSegmentDetection",
                "rekognition:DescribeStreamProcessor",
                "rekognition:ListStreamProcessors",
                "rekognition:DescribeProjects",
                "rekognition:DescribeProjectVersions",
                "rekognition:DetectCustomLabels",
                "rekognition:DetectProtectiveEquipment",
                "rekognition:ListTagsForResource",
                "rekognition:ListDatasetEntries",
                "rekognition:ListDatasetLabels",
                "rekognition:DescribeDataset"
            ],
            "Resource": "*"
        }
    ]
}
```

## AWS managed policy: AmazonRekognitionServiceRole<a name="security-iam-awsmanpol-AmazonRekognitionServiceRole"></a>

`AmazonRekognitionServiceRole` allows Amazon Rekognition to call Amazon Kinesis Data Streams and Amazon SNS services on your behalf\.

You can attach the `AmazonRekognitionServiceRole` policy to your IAM identities\. 

**Permissions details**

This policy includes the following permissions\.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sns:Publish"
            ],
            "Resource": "arn:aws:sns:*:*:AmazonRekognition*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "kinesis:PutRecord",
                "kinesis:PutRecords"
            ],
            "Resource": "arn:aws:kinesis:*:*:stream/AmazonRekognition*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "kinesisvideo:GetDataEndpoint",
                "kinesisvideo:GetMedia"
            ],
            "Resource": "*"
        }
    ]
}
```

## AWS managed policy: AmazonRekognitionCustomLabelsFullAccess<a name="security-iam-awsmanpol-custom-labels-full-access"></a>

This policy is for Amazon Rekognition Custom Labels; users\. Use the AmazonRekognitionCustomLabelsFullAccess policy to allow users full access to the Amazon Rekognition Custom Labels API and full access to the console buckets created by the Amazon Rekognition Custom Labels console\.  

**Permissions details**

This policy includes the following permissions\.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:ListAllMyBuckets",
                "s3:GetBucketAcl",
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:GetObjectAcl",
                "s3:GetObjectTagging",
                "s3:GetObjectVersion",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::*custom-labels*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "rekognition:CreateProject",
                "rekognition:CreateProjectVersion",
                "rekognition:StartProjectVersion",
                "rekognition:StopProjectVersion",
                "rekognition:DescribeProjects",
                "rekognition:DescribeProjectVersions",
                "rekognition:DetectCustomLabels",
                "rekognition:DeleteProject",
                "rekognition:DeleteProjectVersion"
                "rekognition:TagResource",
                "rekognition:UntagResource",
                "rekognition:ListTagsForResource",
                "rekognition:CreateDataset",
                "rekognition:ListDatasetEntries",
                "rekognition:ListDatasetLabels",
                "rekognition:DescribeDataset",
                "rekognition:UpdateDatasetEntries",
                "rekognition:DistributeDatasetEntries",
                "rekognition:DeleteDataset"

            ],
            "Resource": "*"
        }
    ]
}
```

## Amazon Rekognition updates to AWS managed policies<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for Amazon Rekognition since this service began tracking these changes\. For automatic alerts about changes to this page, subscribe to the RSS feed on the Amazon Rekognition Document history page\.




| Change | Description | Date |  |  |  | 
| --- | --- | --- | --- | --- | --- | 
|  Dataset management update for the following managed policies: [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/rekognition/latest/dg/security-iam-awsmanpol.html)  |  Amazon Rekognition added the following actions to the AmazonRekognitionReadOnlyAccess, AmazonRekognitionFullOnlyAccess, and AmazonRekognitionCustomLabelsFullAccess managed policies [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/rekognition/latest/dg/security-iam-awsmanpol.html)  | November 1, 2021 | 
|  Tagging update for [AWS managed policy: AmazonRekognitionReadOnlyAccess](#security-iam-awsmanpol-AmazonRekognitionReadOnlyAccess) and [AWS managed policy: AmazonRekognitionFullAccess](#security-iam-awsmanpol-AmazonRekognitionFullAccess)  |  Amazon Rekognition added new tagging actions to the AmazonRekognitionFullAccess and AmazonRekognitionReadOnlyAccess policies\.  | April 2, 2021 | 
|  Amazon Rekognition started tracking changes  |  Amazon Rekognition started tracking changes for its AWS managed policies\.  | April 2, 2021 | 