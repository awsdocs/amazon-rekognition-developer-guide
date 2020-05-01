# DescribeProjectVersions<a name="API_DescribeProjectVersions"></a>

Lists and describes the models in an Amazon Rekognition Custom Labels project\. You can specify up to 10 model versions in `ProjectVersionArns`\. If you don't specify a value, descriptions for all models are returned\.

This operation requires permissions to perform the `rekognition:DescribeProjectVersions` action\.

## Request Syntax<a name="API_DescribeProjectVersions_RequestSyntax"></a>

```
{
   "[MaxResults](#rekognition-DescribeProjectVersions-request-MaxResults)": number,
   "[NextToken](#rekognition-DescribeProjectVersions-request-NextToken)": "string",
   "[ProjectArn](#rekognition-DescribeProjectVersions-request-ProjectArn)": "string",
   "[VersionNames](#rekognition-DescribeProjectVersions-request-VersionNames)": [ "string" ]
}
```

## Request Parameters<a name="API_DescribeProjectVersions_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [MaxResults](#API_DescribeProjectVersions_RequestSyntax) **   <a name="rekognition-DescribeProjectVersions-request-MaxResults"></a>
The maximum number of results to return per paginated call\. The largest value you can specify is 100\. If you specify a value greater than 100, a ValidationException error occurs\. The default value is 100\.   
Type: Integer  
Valid Range: Minimum value of 1\. Maximum value of 100\.  
Required: No

 ** [NextToken](#API_DescribeProjectVersions_RequestSyntax) **   <a name="rekognition-DescribeProjectVersions-request-NextToken"></a>
If the previous response was incomplete \(because there is more results to retrieve\), Amazon Rekognition Custom Labels returns a pagination token in the response\. You can use this pagination token to retrieve the next set of results\.   
Type: String  
Length Constraints: Maximum length of 1024\.  
Required: No

 ** [ProjectArn](#API_DescribeProjectVersions_RequestSyntax) **   <a name="rekognition-DescribeProjectVersions-request-ProjectArn"></a>
The Amazon Resource Name \(ARN\) of the project that contains the models you want to describe\.  
Type: String  
Length Constraints: Minimum length of 20\. Maximum length of 2048\.  
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`   
Required: Yes

 ** [VersionNames](#API_DescribeProjectVersions_RequestSyntax) **   <a name="rekognition-DescribeProjectVersions-request-VersionNames"></a>
A list of model version names that you want to describe\. You can add up to 10 model version names to the list\. If you don't specify a value, all model descriptions are returned\. A version name is part of a model \(ProjectVersion\) ARN\. For example, `my-model.2020-01-21T09.10.15` is the version name in the following ARN\. `arn:aws:rekognition:us-east-1:123456789012:project/getting-started/version/my-model.2020-01-21T09.10.15/1234567890123`\.  
Type: Array of strings  
Array Members: Minimum number of 1 item\. Maximum number of 10 items\.  
Length Constraints: Minimum length of 1\. Maximum length of 255\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: No

## Response Syntax<a name="API_DescribeProjectVersions_ResponseSyntax"></a>

```
{
   "[NextToken](#rekognition-DescribeProjectVersions-response-NextToken)": "string",
   "[ProjectVersionDescriptions](#rekognition-DescribeProjectVersions-response-ProjectVersionDescriptions)": [ 
      { 
         "[BillableTrainingTimeInSeconds](API_ProjectVersionDescription.md#rekognition-Type-ProjectVersionDescription-BillableTrainingTimeInSeconds)": number,
         "[CreationTimestamp](API_ProjectVersionDescription.md#rekognition-Type-ProjectVersionDescription-CreationTimestamp)": number,
         "[EvaluationResult](API_ProjectVersionDescription.md#rekognition-Type-ProjectVersionDescription-EvaluationResult)": { 
            "[F1Score](API_EvaluationResult.md#rekognition-Type-EvaluationResult-F1Score)": number,
            "[Summary](API_EvaluationResult.md#rekognition-Type-EvaluationResult-Summary)": { 
               "[S3Object](API_Summary.md#rekognition-Type-Summary-S3Object)": { 
                  "[Bucket](API_S3Object.md#rekognition-Type-S3Object-Bucket)": "string",
                  "[Name](API_S3Object.md#rekognition-Type-S3Object-Name)": "string",
                  "[Version](API_S3Object.md#rekognition-Type-S3Object-Version)": "string"
               }
            }
         },
         "[MinInferenceUnits](API_ProjectVersionDescription.md#rekognition-Type-ProjectVersionDescription-MinInferenceUnits)": number,
         "[OutputConfig](API_ProjectVersionDescription.md#rekognition-Type-ProjectVersionDescription-OutputConfig)": { 
            "[S3Bucket](API_OutputConfig.md#rekognition-Type-OutputConfig-S3Bucket)": "string",
            "[S3KeyPrefix](API_OutputConfig.md#rekognition-Type-OutputConfig-S3KeyPrefix)": "string"
         },
         "[ProjectVersionArn](API_ProjectVersionDescription.md#rekognition-Type-ProjectVersionDescription-ProjectVersionArn)": "string",
         "[Status](API_ProjectVersionDescription.md#rekognition-Type-ProjectVersionDescription-Status)": "string",
         "[StatusMessage](API_ProjectVersionDescription.md#rekognition-Type-ProjectVersionDescription-StatusMessage)": "string",
         "[TestingDataResult](API_ProjectVersionDescription.md#rekognition-Type-ProjectVersionDescription-TestingDataResult)": { 
            "[Input](API_TestingDataResult.md#rekognition-Type-TestingDataResult-Input)": { 
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
            "[Output](API_TestingDataResult.md#rekognition-Type-TestingDataResult-Output)": { 
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
            }
         },
         "[TrainingDataResult](API_ProjectVersionDescription.md#rekognition-Type-ProjectVersionDescription-TrainingDataResult)": { 
            "[Input](API_TrainingDataResult.md#rekognition-Type-TrainingDataResult-Input)": { 
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
            "[Output](API_TrainingDataResult.md#rekognition-Type-TrainingDataResult-Output)": { 
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
            }
         },
         "[TrainingEndTimestamp](API_ProjectVersionDescription.md#rekognition-Type-ProjectVersionDescription-TrainingEndTimestamp)": number
      }
   ]
}
```

## Response Elements<a name="API_DescribeProjectVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [NextToken](#API_DescribeProjectVersions_ResponseSyntax) **   <a name="rekognition-DescribeProjectVersions-response-NextToken"></a>
If the previous response was incomplete \(because there is more results to retrieve\), Amazon Rekognition Custom Labels returns a pagination token in the response\. You can use this pagination token to retrieve the next set of results\.   
Type: String  
Length Constraints: Maximum length of 1024\.

 ** [ProjectVersionDescriptions](#API_DescribeProjectVersions_ResponseSyntax) **   <a name="rekognition-DescribeProjectVersions-response-ProjectVersionDescriptions"></a>
A list of model descriptions\. The list is sorted by the creation date and time of the model versions, latest to earliest\.  
Type: Array of [ProjectVersionDescription](API_ProjectVersionDescription.md) objects

## Errors<a name="API_DescribeProjectVersions_Errors"></a>

 **AccessDeniedException**   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 **InternalServerError**   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

 **InvalidPaginationTokenException**   
Pagination token in the request is not valid\.  
HTTP Status Code: 400

 **InvalidParameterException**   
Input parameter violated a constraint\. Validate your parameter before calling the API operation again\.  
HTTP Status Code: 400

 **ProvisionedThroughputExceededException**   
The number of requests exceeded your throughput limit\. If you want to increase this limit, contact Amazon Rekognition\.  
HTTP Status Code: 400

 **ResourceNotFoundException**   
The collection specified in the request cannot be found\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_DescribeProjectVersions_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DescribeProjectVersions) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DescribeProjectVersions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DescribeProjectVersions) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DescribeProjectVersions) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/DescribeProjectVersions) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DescribeProjectVersions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DescribeProjectVersions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DescribeProjectVersions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DescribeProjectVersions) 