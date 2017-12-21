# Overview of Managing Access Permissions to Your Amazon Rekognition Resources<a name="access-control-overview"></a>

Every AWS resource is owned by an AWS account, and permissions to create or access a resource are governed by permissions policies\. An account administrator can attach permissions policies to IAM identities \(that is, users, groups, and roles\), and some services \(such as AWS Lambda\) also support attaching permissions policies to resources\. 

**Note**  
An *account administrator* \(or administrator user\) is a user with administrator privileges\. For more information, see [IAM Best Practices](http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*\.

When granting permissions, you decide who is getting the permissions, the resources they get permissions for, and the specific actions that you want to allow on those resources\.


+ [Amazon Rekognition Resources and Operations](#access-control-resources)
+ [Understanding Resource Ownership](#access-control-resource-ownership)
+ [Managing Access to Resources](#manage-access-overview)
+ [Specifying Policy Elements: Actions, Effects, and Principals](#specify-policy-elements)
+ [Specifying Conditions in a Policy](#specifying-conditions-overview)

## Amazon Rekognition Resources and Operations<a name="access-control-resources"></a>

In Amazon Rekognition, there are resource types for *a collection* and *a streamprocessor*\. In a policy, you use an Amazon Resource Name \(ARN\) to identify the resource that the policy applies to\.

These resources have unique Amazon Resource Names \(ARNs\) associated with them, as shown in the following table\. 


****  

| Resource Type | ARN Format | 
| --- | --- | 
| Collection ARN | arn:aws:rekognition:region:account\-id:collection/collection\-id | 
| Stream Processor ARN | arn:aws:rekognition:region:account\-id:streamprocessor/stream\-processor\-name | 

Amazon Rekognition provides a set of operations to work with Amazon Rekognition resources\. For a list of available operations, see Amazon Rekognition [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\.

## Understanding Resource Ownership<a name="access-control-resource-ownership"></a>

The AWS account owns the resources that are created in the account, regardless of who created the resources\. Specifically, the resource owner is the AWS account of the [principal entity](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) \(that is, the root account or an IAM user\) that authenticates the resource creation request\. The following examples illustrate how this works:

+ If you use the root account credentials of your AWS account to create a collection, your AWS account is the owner of the resource \(in Amazon Rekognition, the resource is a collection\)\.

+ If you create an IAM user in your AWS account and grant permissions to create a collection to that user, the user can create a collection\. However, your AWS account, to which the user belongs, owns the collection resource\.

## Managing Access to Resources<a name="manage-access-overview"></a>

A *permissions policy* describes who has access to what\. The following section explains the available options for creating permissions policies\.

**Note**  
This section discusses using IAM in the context of Amazon Rekognition\. It doesn't provide detailed information about the IAM service\. For complete IAM documentation, see [What Is IAM?](http://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) in the *IAM User Guide*\. For information about IAM policy syntax and descriptions, see [AWS IAM Policy Reference](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the *IAM User Guide*\.

Policies attached to an IAM identity are referred to as *identity\-based* policies \(IAM polices\) and policies attached to a resource are referred to as *resource\-based* policies\. Amazon Rekognition supports identity\-based policies\. 


+ [Identity\-Based Policies \(IAM Policies\)](#manage-access-iam-policies)
+ [Resource\-Based Policies](#manage-access-resource-policies)

### Identity\-Based Policies \(IAM Policies\)<a name="manage-access-iam-policies"></a>

You can attach policies to IAM identities\. For example, you can do the following:

+ **Attach a permissions policy to a user or a group in your account** – To grant a user permissions to create an Amazon Rekognition resource, such as a collection, you can attach a permissions policy to a user or group that the user belongs to\.

+ **Attach a permissions policy to a role \(grant cross\-account permissions\)** – You can attach an identity\-based permissions policy to an IAM role to grant cross\-account permissions\. For example, the administrator in account A can create a role to grant cross\-account permissions to another AWS account \(for example, account B\) or an AWS service as follows:

  1. Account A administrator creates an IAM role and attaches a permissions policy to the role that grants permissions on resources in account A\.

  1. Account A administrator attaches a trust policy to the role identifying account B as the principal who can assume the role\. 

  1. Account B administrator can then delegate permissions to assume the role to any users in account B\. Doing this allows users in account B to create or access resources in account A\. The principal in the trust policy can also be an AWS service principal if you want to grant an AWS service permissions to assume the role\.

  For more information about using IAM to delegate permissions, see [Access Management](http://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*\.

The following is an example policy that lists all collections\.

```
"Version": "2012-10-17",
             "Statement": [
        {
            "Sid": "AllowsListCollectionAction",
            "Effect": "Allow",
            "Action": [
                "rekognition:ListCollections"
            ],
            "Resource": "*"
        }
    ]
}
```

For more information about using identity\-based policies with Amazon Rekognition, see [Using Identity\-Based Policies \(IAM Policies\) for Amazon Rekognition](using-identity-based-policies.md)\. For more information about users, groups, roles, and permissions, see [Identities \(Users, Groups, and Roles\)](http://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the *IAM User Guide*\. 

### Resource\-Based Policies<a name="manage-access-resource-policies"></a>

Other services, such as Amazon S3, also support resource\-based permissions policies\. For example, you can attach a policy to an S3 bucket to manage access permissions to that bucket\. Amazon Rekognition doesn't support resource\-based policies\.

To access images stored in an Amazon S3 bucket, you must have permission to access object in the S3 bucket\. With this permission, Amazon Rekognition can download images from the S3 bucket\. The following example policy allows the user to perform the `s3:GetObject` action on the S3 bucket named Tests3bucket\.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::Tests3bucket"
            ]
        }
    ]
}
```

To use an S3 bucket with versioning enabled, add the `s3:GetObjectVersion` action, as shown in the following example\.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": [
                "arn:aws:s3:::Tests3bucket"
            ]
        }
    ]
```

## Specifying Policy Elements: Actions, Effects, and Principals<a name="specify-policy-elements"></a>

For each Amazon Rekognition resource, the service defines a set of API operations\. To grant permissions for these API operations, Amazon Rekognition defines a set of actions that you can specify in a policy\. Some API operations can require permissions for more than one action in order to perform the API operation\. For more information about resources and API operations, see [Amazon Rekognition Resources and Operations](#access-control-resources) and Amazon Rekognition [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\.

The following are the most basic policy elements:

+ **Resource** – You use an Amazon Resource Name \(ARN\) to identify the resource that the policy applies to\. For more information, see [Amazon Rekognition Resources and Operations](#access-control-resources)\.

+ **Action** – You use action keywords to identify resource operations that you want to allow or deny\. For example, you can use `ListCollections` to list collections\.

+ **Effect** – You specify the effect, either allow or deny, when the user requests the specific action\. If you don't explicitly grant access to \(allow\) a resource, access is implicitly denied\. You can also explicitly deny access to a resource, which you might do to make sure that a user cannot access it, even if a different policy grants access\.

+ **Principal** – In identity\-based policies \(IAM policies\), the user that the policy is attached to is the implicit principal\. For resource\-based policies, you specify the user, account, service, or other entity that you want to receive permissions \(applies to resource\-based policies only\)\. Amazon Rekognition doesn't support resource\-based policies\.

To learn more about IAM policy syntax and descriptions, see [AWS IAM Policy Reference](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the *IAM User Guide*\.

For a table showing all of the Amazon Rekognition API operations and the resources that they apply to, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\.

## Specifying Conditions in a Policy<a name="specifying-conditions-overview"></a>

When you grant permissions, you can use the access policy language to specify the conditions when a policy should take effect\. For example, you might want a policy to be applied only after a specific date\. For more information about specifying conditions in a policy language, see [Condition](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#Condition) in the *IAM User Guide*\.

To express conditions, you use predefined condition keys\. There are no condition keys specific to Amazon Rekognition\. However, there are AWS\-wide condition keys that you can use as appropriate\. For a complete list of AWS\-wide keys, see [Available Keys for Conditions](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys) in the *IAM User Guide*\.