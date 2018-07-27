  Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.



Amazon Rekognition Documentation JavaScript Examples
====================================================


These are the JavaScript examples used in the [Amazon Rekognition developer documentation](https://aws.amazon.com/documentation/rekognition/).



Running the Examples
====================

The JavaScript examples run in a browser script.  For simplicity, the examples uses an anonymous Amazon 
Cognito identity pool to provide unauthenticated access to the Amazon Rekognition Image API. This might
be suitable for your needs. For example, you can use unauthenticated access to provide free,
or trial, access to your website before users sign up. To provide authenticated access, 
use an Amazon Cognito user pool. For more information, see 
[Amazon Cognito User Pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html).  

**IMPORTANT**

   The examples perform AWS operations for the account and region for which you've specified
   credentials, and you may incur AWS service charges by running them. Please visit the [AWS Pricing](https://aws.amazon.com/pricing/) page for details about the charges you can
   expect for a given service and operation.

   Some of these examples perform *destructive* operations on AWS resources, such as deleting an
   Amazon Rekognition collection. **Be very careful** when running an operation that
   may delete or modify AWS resources in your account. It's best to create separate test-only
   resources when experimenting with these examples.

All of the examples require replacing certain configuration values in the source code. These values
are specified as String variables at the beginning of each example, and begin and end with three stars
(for example, "\*\*\* Your Bucket Name \*\*\*"). The source-code comments and developer guide provide
further information.
