# Amazon Rekognition Resource\-Based Policy Examples<a name="security_iam_resource-based-policy-examples"></a>

Amazon Rekognition Custom Labels uses resource\-based polices, known as *project policies*, to manage copy permissions for a model version\. 

A project policy gives or denies permission to copy a model version from a source project to a destination project\. You need a project policy if the destination project is in a different AWS account or if you want to restrict access within an AWS account, For example, you might want to deny copy permissions to a specific IAM role\. For more information, see [Copying a model](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/md-copy-model-overview.html)\.

## Giving permission to copy a model version<a name="security_iam_resource-based-policy-examples-account"></a>

The following example allows the principal `arn:aws:iam::123456789012:role/Admin` to copy the model version `arn:aws:rekognition:us-east-1:123456789012:project/my_project/version/test_1/1627045542080`\. 

```
{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Effect":"Allow",
      "Principal":{
        "AWS":"arn:aws:iam::123456789012:role/Admin"
      },
      "Action":"rekognition:CopyProjectVersion",
      "Resource":"arn:aws:rekognition:us-east-1:123456789012:project/my_project/version/test_1/1627045542080"
    }
  ]
}
```