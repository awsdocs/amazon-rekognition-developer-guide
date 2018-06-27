# Using Identity\-Based Policies \(IAM Policies\) for Amazon Rekognition<a name="using-identity-based-policies"></a>

This topic provides examples of identity\-based policies that demonstrate how an account administrator can attach permissions policies to IAM identities \(that is, users, groups, and roles\) and thereby grant permissions to perform operations on Amazon Rekognition resources\.

**Important**  
We recommend that you first review the introductory topics that explain the basic concepts and options available to manage access to your Amazon Rekognition resources\. For more information, see [Overview of Managing Access Permissions to Your Amazon Rekognition Resources](access-control-overview.md)\. 

**Topics**
+ [Permissions Required to Use the Amazon Rekognition Console](#console-permissions)
+ [AWS Managed \(Predefined\) Policies for Amazon Rekognition](#access-policy-aws-managed-policies)
+ [Customer Managed Policy Examples](#access-policy-customer-managed-examples)

The following shows an example of a permissions policy\.

```
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
                "rekognition:SearchFacesByImage"
            ],
            "Resource": "*"
        }
    ]
```

This policy example grants a user read\-only access to resources using a limited set of Amazon Rekognition operations\.

For a table showing all of the Amazon Rekognition API operations and the resources that they apply to, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. 

## Permissions Required to Use the Amazon Rekognition Console<a name="console-permissions"></a>

Amazon Rekognition does not require any additional permissions when working with the Amazon Rekognition console\.

## AWS Managed \(Predefined\) Policies for Amazon Rekognition<a name="access-policy-aws-managed-policies"></a>

AWS addresses many common use cases by providing standalone IAM policies that are created and administered by AWS\. These AWS managed policies grant necessary permissions for common use cases so that you can avoid having to investigate what permissions are needed\. For more information, see [AWS Managed Policies](http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*\. 

The following AWS managed policies, which you can attach to users in your account, are specific to Amazon Rekognition:
+ **AmazonRekognitionFullAccess** – Grants full access to Amazon Rekognition resources including creating and deleting collections\.
+ **AmazonRekognitionReadOnlyAccess** – Grants read\-only access to Amazon Rekognition resources\.
+ **AmazonRekognitionServiceRole** – Allows Amazon Rekognition to call Amazon Kinesis Data Streams and Amazon SNS services on your behalf\.

**Note**  
You can review these permissions policies by signing in to the IAM console and searching for specific policies there\.  
These policies work when you are using AWS SDKs or the AWS CLI\.

You can also create your own custom IAM policies to allow permissions for Amazon Rekognition actions and resources\. You can attach these custom policies to the IAM users or groups that require those permissions\. 

## Customer Managed Policy Examples<a name="access-policy-customer-managed-examples"></a>

In this section, you can find example user policies that grant permissions for various Amazon Rekognition actions\. These policies work when you are using AWS SDKs or the AWS CLI\. When you are using the console, you need to grant additional permissions specific to the console, which is discussed in [Permissions Required to Use the Amazon Rekognition Console](#console-permissions)\.

**Topics**
+ [Example 1: Allow a User Read\-Only Access to Resources](#access-policy-customer-managed-first-example)
+ [Example 2: Allow a User Full Access to Resources](#access-policy-customer-managed-second-example)

### Example 1: Allow a User Read\-Only Access to Resources<a name="access-policy-customer-managed-first-example"></a>

The following example grants read\-only access to Amazon Rekognition resources\. 

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
                "rekognition:DescribeStreamProcessor",
                "rekognition:ListStreamProcessors"
            ],
            "Resource": "*"
        }
    ]
}
```

### Example 2: Allow a User Full Access to Resources<a name="access-policy-customer-managed-second-example"></a>

The following example grants full access to Amazon Rekognition resources\.

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