.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.



Amazon Rekognition Documentation .NET Examples
==============================================

These are the .NET examples used in the [Amazon Rekognition developer documentation](https://aws.amazon.com/documentation/rekognition/).

Prerequisites
=============

To build and run these examples, you'll need:


* AWS credentials, either configured in a local AWS credentials file or by setting the
  ``AWS_ACCESS_KEY_ID`` and ``AWS_SECRET_ACCESS_KEY`` environment variables.
* You should also set the *AWS region* within which the operations will be performed. If a region is
  not set, the default region used will be ``us-east-1``.

For information about how to set AWS credentials and the region for use with the AWS SDK for .NET,
see [Configuring Your AWS SDK for .NET Application](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/net-dg-config.html). 

Running the examples
====================
Open the solution corresponding to the service for which you wish to run examples in Visual Studio.

Compile and run the solution.

An IAM user with the following IAM permissions can call every example:
* AmazonRekognitionFullAccess
* AmazonS3ReadOnlyAccess
* AmazonSQSFullAccess

Depending on the AWS operations that you are calling, you can further restrict access. For more 
information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](https://docs.aws.amazon.com/rekognition/latest/dg/api-permissions-reference.html).

**IMPORTANT**

  The examples perform AWS operations for the account and region for which you've specified
  credentials, and you may incur AWS service charges by running them. Please visit the
  [AWS Pricing](https://aws.amazon.com/pricing/) page for details about the charges you can expect for a given service and operation.

  Some of these examples perform *destructive* operations on AWS resources, such as deleting an
  Amazon Rekognition collection. **Be very careful** when running an operation that
  may delete or modify AWS resources in your account. It's best to create separate test-only
  resources when experimenting with these examples.

Many of the examples require configuration before they can be run. For example, to call
DetectLabels, you have to specify the source image. The source code comments and service 
documentation provide further information.
