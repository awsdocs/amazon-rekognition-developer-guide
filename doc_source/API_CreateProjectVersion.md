# CreateProjectVersion<a name="API_CreateProjectVersion"></a>

Creates a new version of a model and begins training\. Models are managed as part of an Amazon Rekognition Custom Labels project\. You can specify one training dataset and one testing dataset\. The response from `CreateProjectVersion` is an Amazon Resource Name \(ARN\) for the version of the model\. 

Training takes a while to complete\. You can get the current status by calling [DescribeProjectVersions](API_DescribeProjectVersions.md)\.

Once training has successfully completed, call [DescribeProjectVersions](API_DescribeProjectVersions.md) to get the training results and evaluate the model\. 

After evaluating the model, you start the model by calling [StartProjectVersion](API_StartProjectVersion.md)\.

This operation requires permissions to perform the `rekognition:CreateProjectVersion` action\.

## Request Syntax<a name="API_CreateProjectVersion_RequestSyntax"></a>

```
{
   "[OutputConfig](#rekognition-CreateProjectVersion-request-OutputConfig)": { 
      "[S3Bucket](API_OutputConfig.md#rekognition-Type-OutputConfig-S3Bucket)": "string",
      "[S3KeyPrefix](API_OutputConfig.md#rekognition-Type-OutputConfig-S3KeyPrefix)": "string"
   },
   "[ProjectArn](#rekognition-CreateProjectVersion-request-ProjectArn)": "string",
   "[TestingData](#rekognition-CreateProjectVersion-request-TestingData)": { 
      "[Assets](API_TestingData.md#rekognition-Type-TestingData-Assets)": [ 
         { 
            "[GroundTruthManifest](API_Asset.md#rekognition-Type-Asset-GroundTruthManifest)": { 
               "[S3Object](API_GroundTruthManifest.md#rekognition-Type-GroundTruthManifest-S3Object)": { 
                  "[Bucket](API_S3Object.md#rekognition-Type-S3Object-Bucket)": "string",
                  "[Name](API_S3Object.md#rekognition-Type-S3Object-Name)": "string",
                  "[Version](API_S3Object.md#rekognition-Type-S3Object-Version)": "string"
               }
            }
         }
      ],
      "[AutoCreate](API_TestingData.md#rekognition-Type-TestingData-AutoCreate)": boolean
   },
   "[TrainingData](#rekognition-CreateProjectVersion-request-TrainingData)": { 
      "[Assets](API_TrainingData.md#rekognition-Type-TrainingData-Assets)": [ 
         { 
            "[GroundTruthManifest](API_Asset.md#rekognition-Type-Asset-GroundTruthManifest)": { 
               "[S3Object](API_GroundTruthManifest.md#rekognition-Type-GroundTruthManifest-S3Object)": { 
                  "[Bucket](API_S3Object.md#rekognition-Type-S3Object-Bucket)": "string",
                  "[Name](API_S3Object.md#rekognition-Type-S3Object-Name)": "string",
                  "[Version](API_S3Object.md#rekognition-Type-S3Object-Version)": "string"
               }
            }
         }
      ]
   },
   "[VersionName](#rekognition-CreateProjectVersion-request-VersionName)": "string"
}
```

## Request Parameters<a name="API_CreateProjectVersion_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [OutputConfig](#API_CreateProjectVersion_RequestSyntax) **   <a name="rekognition-CreateProjectVersion-request-OutputConfig"></a>
The Amazon S3 location to store the results of training\.  
Type: [OutputConfig](API_OutputConfig.md) object  
Required: Yes

 ** [ProjectArn](#API_CreateProjectVersion_RequestSyntax) **   <a name="rekognition-CreateProjectVersion-request-ProjectArn"></a>
The ARN of the Amazon Rekognition Custom Labels project that manages the model that you want to train\.  
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`   
Required: Yes

 ** [TestingData](#API_CreateProjectVersion_RequestSyntax) **   <a name="rekognition-CreateProjectVersion-request-TestingData"></a>
The dataset to use for testing\.  
Type: [TestingData](API_TestingData.md) object  
Required: Yes

 ** [TrainingData](#API_CreateProjectVersion_RequestSyntax) **   <a name="rekognition-CreateProjectVersion-request-TrainingData"></a>
The dataset to use for training\.   
Type: [TrainingData](API_TrainingData.md) object  
Required: Yes

 ** [VersionName](#API_CreateProjectVersion_RequestSyntax) **   <a name="rekognition-CreateProjectVersion-request-VersionName"></a>
A name for the version of the model\. This value must be unique\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes

## Response Syntax<a name="API_CreateProjectVersion_ResponseSyntax"></a>

```
{
   "[ProjectVersionArn](#rekognition-CreateProjectVersion-response-ProjectVersionArn)": "string"
}
```

## Response Elements<a name="API_CreateProjectVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [ProjectVersionArn](#API_CreateProjectVersion_ResponseSyntax) **   <a name="rekognition-CreateProjectVersion-response-ProjectVersionArn"></a>
The ARN of the model version that was created\. Use `DescribeProjectVersion` to get the current status of the training operation\.  
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/version\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)` 

## Errors<a name="API_CreateProjectVersion_Errors"></a>

 **AccessDeniedException**   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 **InternalServerError**   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

 **InvalidParameterException**   
Input parameter violated a constraint\. Validate your parameter before calling the API operation again\.  
HTTP Status Code: 400

 **LimitExceededException**   
An Amazon Rekognition service limit was exceeded\. For example, if you start too many Amazon Rekognition Video jobs concurrently, calls to start operations \(`StartLabelDetection`, for example\) will raise a `LimitExceededException` exception \(HTTP status code: 400\) until the number of concurrently running jobs is below the Amazon Rekognition service limit\.   
HTTP Status Code: 400

 **ProvisionedThroughputExceededException**   
The number of requests exceeded your throughput limit\. If you want to increase this limit, contact Amazon Rekognition\.  
HTTP Status Code: 400

 **ResourceInUseException**   
  
HTTP Status Code: 400

 **ResourceNotFoundException**   
The collection specified in the request cannot be found\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_CreateProjectVersion_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/CreateProjectVersion) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/CreateProjectVersion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CreateProjectVersion) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/CreateProjectVersion) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/CreateProjectVersion) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/CreateProjectVersion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/CreateProjectVersion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/CreateProjectVersion) 
+  [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/CreateProjectVersion) 