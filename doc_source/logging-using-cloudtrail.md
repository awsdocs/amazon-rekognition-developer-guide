# Logging Amazon Rekognition API Calls with AWS CloudTrail<a name="logging-using-cloudtrail"></a>

Amazon Rekognition is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon Rekognition\. CloudTrail captures a subset of API calls for Amazon Rekognition as events, including calls from the Amazon Rekognition console and from code calls to the Amazon Rekognition APIs\. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon Rekognition\. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**\. Using the information collected by CloudTrail, you can determine the request that was made to Amazon Rekognition, the IP address from which the request was made, who made the request, when it was made, and additional details\. 

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/)\.

## Amazon Rekognition Information in CloudTrail<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account\. When supported event activity occurs in Amazon Rekognition, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**\. You can view, search, and download recent events in your AWS account\. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)\. 

For an ongoing record of events in your AWS account, including events for Amazon Rekognition, create a trail\. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket\. By default, when you create a trail in the console, the trail applies to all regions\. The trail logs events from all regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify\. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs\. For more information, see: 
+ [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

Amazon Rekognition supports logging the following actions as events in CloudTrail log files:
+ [CreateCollection](API_CreateCollection.md)
+ [DeleteCollection](API_DeleteCollection.md)
+ [CreateStreamProcessor](API_CreateStreamProcessor.md)
+ [DeleteStreamProcessor](API_DeleteStreamProcessor.md)
+ [DescribeStreamProcessor](API_DescribeStreamProcessor.md)
+ [ListStreamProcessors](API_ListStreamProcessors.md)
+ [ListCollections](API_ListCollections.md)

Every event or log entry contains information about who generated the request\. The identity information helps you determine the following: 
+ Whether the request was made with root or IAM user credentials\.
+ Whether the request was made with temporary security credentials for a role or federated user\.
+ Whether the request was made by another AWS service\.

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html)\.

## Example: Amazon Rekognition Log File Entries<a name="understanding-service-name-entries"></a>

 A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify\. CloudTrail log files contain one or more log entries\. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on\. CloudTrail log files are not an ordered stack trace of the public API calls, so they do not appear in any specific order\.

The following example shows a CloudTrail log entry with actions for the following API: `CreateCollection`, `DeleteCollection`, `CreateStreamProcessor`, `DeleteStreamProcessor`, `DescribeStreamProcessor`, `ListStreamProcessors`, and `ListCollections`\.

```
{
    "Records": [
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "IAMUser",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::111122223333:user/Alice",
                "accountId": "111122223333",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "userName": "Alice"
            },
            "eventTime": "2018-03-26T21:46:22Z",
            "eventSource": "rekognition.amazonaws.com",
            "eventName": "CreateCollection",
            "awsRegion": "us-east-1",
            "sourceIPAddress": "127.0.0.1",
            "userAgent": "aws-internal/3",
            "requestParameters": {
                "collectionId": "8fa6aa65-cab4-4d0a-b976-7fd5df63f38a"
            },
            "responseElements": {
                "collectionArn": "aws:rekognition:us-east-1:111122223333:collection/8fa6aa65-cab4-4d0a-b976-7fd5df63f38a",
                "faceModelVersion": "2.0",
                "statusCode": 200
            },
            "requestID": "1e77d2d5-313f-11e8-8c0e-75c0272f31a4",
            "eventID": "c6da4992-a9a1-4962-93b6-7d0483d95c30",
            "eventType": "AwsApiCall",
            "recipientAccountId": "111122223333"
        },
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "IAMUser",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::111122223333:user/Alice",
                "accountId": "111122223333",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "userName": "Alice"
            },
            "eventTime": "2018-03-26T21:46:25Z",
            "eventSource": "rekognition.amazonaws.com",
            "eventName": "DeleteCollection",
            "awsRegion": "us-east-1",
            "sourceIPAddress": "127.0.0.1",
            "userAgent": "aws-internal/3",
            "requestParameters": {
                "collectionId": "8fa6aa65-cab4-4d0a-b976-7fd5df63f38a"
            },
            "responseElements": {
                "statusCode": 200
            },
            "requestID": "213d5b78-313f-11e8-8c0e-75c0272f31a4",
            "eventID": "3ed4f4c9-22f8-4de4-a051-0d9d0c2faec9",
            "eventType": "AwsApiCall",
            "recipientAccountId": "111122223333"
        },
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "AssumedRole",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Alice",
                "accountId": "111122223333",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "sessionContext": {
                    "attributes": {
                        "mfaAuthenticated": "false",
                        "creationDate": "2018-03-26T21:48:49Z"
                    },
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "EX_PRINCIPAL_ID",
                        "arn": "arn:aws:iam::111122223333:role/Admin",
                        "accountId": "111122223333",
                        "userName": "Admin"
                    }
                }
            },
            "eventTime": "2018-03-26T21:53:09Z",
            "eventSource": "rekognition.amazonaws.com",
            "eventName": "ListCollections",
            "awsRegion": "us-east-1",
            "sourceIPAddress": "127.0.0.1",
            "userAgent": "aws-cli/1.14.63 Python/3.4.7 Linux/3.2.45-0.6.wd.971.49.326.metal1.x86_64 botocore/1.9.16",
            "requestParameters": null,
            "responseElements": null,
            "requestID": "116a57f5-3140-11e8-8c0e-75c0272f31a4",
            "eventID": "94bb5ddd-7836-4fb1-a63e-a782eb009824",
            "eventType": "AwsApiCall",
            "recipientAccountId": "111122223333"
        },
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "AssumedRole",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Alice",
                "accountId": "111122223333",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "sessionContext": {
                    "attributes": {
                        "mfaAuthenticated": "false",
                        "creationDate": "2018-03-26T21:48:49Z"
                    },
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "EX_PRINCIPAL_ID",
                        "arn": "arn:aws:iam::111122223333:role/Admin",
                        "accountId": "111122223333",
                        "userName": "Admin"
                    }
                }
            },
            "eventTime": "2018-03-26T22:06:19Z",
            "eventSource": "rekognition.amazonaws.com",
            "eventName": "CreateStreamProcessor",
            "awsRegion": "us-east-1",
            "sourceIPAddress": "127.0.0.1",
            "userAgent": "aws-cli/1.14.63 Python/3.4.7 Linux/3.2.45-0.6.wd.971.49.326.metal1.x86_64 botocore/1.9.16",
            "requestParameters": {
                "roleArn": "arn:aws:iam::111122223333:role/AmazonRekognition-StreamProcessorRole",
                "settings": {
                    "faceSearch": {
                        "collectionId": "test"
                    }
                },
                "name": "ProcessorName",
                "input": {
                    "kinesisVideoStream": {
                        "arn": "arn:aws:kinesisvideo:us-east-1:111122223333:stream/VideoStream"
                    }
                },
                "output": {
                    "kinesisDataStream": {
                        "arn": "arn:aws:kinesis:us-east-1:111122223333:stream/AmazonRekognition-DataStream"
                    }
                }
            },
            "responseElements": {
                "StreamProcessorArn": "arn:aws:rekognition:us-east-1:111122223333:streamprocessor/ProcessorName"
            },
            "requestID": "e8fb2b3c-3141-11e8-8c0e-75c0272f31a4",
            "eventID": "44ff8f90-fcc2-4740-9e57-0c47610df8e3",
            "eventType": "AwsApiCall",
            "recipientAccountId": "111122223333"
        },
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "AssumedRole",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Alice",
                "accountId": "111122223333",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "sessionContext": {
                    "attributes": {
                        "mfaAuthenticated": "false",
                        "creationDate": "2018-03-26T21:48:49Z"
                    },
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "EX_PRINCIPAL_ID",
                        "arn": "arn:aws:iam::111122223333:role/Admin",
                        "accountId": "111122223333",
                        "userName": "Admin"
                    }
                }
            },
            "eventTime": "2018-03-26T22:09:42Z",
            "eventSource": "rekognition.amazonaws.com",
            "eventName": "DeleteStreamProcessor",
            "awsRegion": "us-east-1",
            "sourceIPAddress": "127.0.0.1",
            "userAgent": "aws-cli/1.14.63 Python/3.4.7 Linux/3.2.45-0.6.wd.971.49.326.metal1.x86_64 botocore/1.9.16",
            "requestParameters": {
                "name": "ProcessorName"
            },
            "responseElements": null,
            "requestID": "624c4c3e-3142-11e8-8c0e-75c0272f31a4",
            "eventID": "27fd784e-fbf3-4163-9f0b-0006c6eed39f",
            "eventType": "AwsApiCall",
            "recipientAccountId": "111122223333"
        },
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "AssumedRole",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Alice",
                "accountId": "111122223333",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "sessionContext": {
                    "attributes": {
                        "mfaAuthenticated": "false",
                        "creationDate": "2018-03-26T21:48:49Z"
                    },
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "EX_PRINCIPAL_ID",
                        "arn": "arn:aws:iam::111122223333:role/Admin",
                        "accountId": "111122223333",
                        "userName": "Admin"
                    }
                }
            },
            "eventTime": "2018-03-26T21:56:14Z",
            "eventSource": "rekognition.amazonaws.com",
            "eventName": "ListStreamProcessors",
            "awsRegion": "us-east-1",
            "sourceIPAddress": "127.0.0.1",
            "userAgent": "aws-cli/1.14.63 Python/3.4.7 Linux/3.2.45-0.6.wd.971.49.326.metal1.x86_64 botocore/1.9.16",
            "requestParameters": null,
            "responseElements": null,
            "requestID": "811735f9-3140-11e8-8c0e-75c0272f31a4",
            "eventID": "5cfc86a6-758c-4fb9-af13-557b04805c4e",
            "eventType": "AwsApiCall",
            "recipientAccountId": "111122223333"
        },
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "AssumedRole",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:sts::111122223333:assumed-role/Admin/Alice",
                "accountId": "111122223333",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "sessionContext": {
                    "attributes": {
                        "mfaAuthenticated": "false",
                        "creationDate": "2018-03-26T22:55:22Z"
                    },
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "EX_PRINCIPAL_ID",
                        "arn": "arn:aws:iam::111122223333:role/Admin",
                        "accountId": "111122223333",
                        "userName": "Admin"
                    }
                }
            },
            "eventTime": "2018-03-26T22:57:38Z",
            "eventSource": "rekognition.amazonaws.com",
            "eventName": "DescribeStreamProcessor",
            "awsRegion": "us-east-1",
            "sourceIPAddress": "127.0.0.1",
            "userAgent": "aws-cli/1.14.63 Python/3.4.7 Linux/3.2.45-0.6.wd.971.49.326.metal1.x86_64 botocore/1.9.16",
            "requestParameters": {
                "name": "ProcessorName"
            },
            "responseElements": null,
            "requestID": "14b2dd34-3149-11e8-8c0e-75c0272f31a4",
            "eventID": "0db3498c-e084-4b30-b5fb-aa0b71ef9b7b",
            "eventType": "AwsApiCall",
            "recipientAccountId": "111122223333"
        }
    ]
}
```