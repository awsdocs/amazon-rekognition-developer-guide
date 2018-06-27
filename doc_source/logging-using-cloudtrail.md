# Logging Amazon Rekognition API Calls with AWS CloudTrail<a name="logging-using-cloudtrail"></a>

Amazon Rekognition is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon Rekognition\. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, Amazon CloudWatch Logs, and Amazon CloudWatch Events\. Amazon Rekognition is also integrated with the **Event history** feature in CloudTrail\. If an API for Amazon Rekognition is supported in **Event history**, you can view the most recent 90 days of events in Amazon Rekognition in the CloudTrail console in **Event history** even if you have not configured any logs in CloudTrail\. Using the information collected by CloudTrail, you can determine the request that was made to Amazon Rekognition, the IP address from which the request was made, who made the request, when it was made, and additional details\. 

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/)\.

## Amazon Rekognition Information in CloudTrail<a name="service-name-info-in-cloudtrail"></a>

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

For more information, see the [CloudTrail userIdentity Element](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html)\.

CloudTrail is enabled on your AWS account when you create the account\. When activity occurs in Amazon Rekognition, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**\. You can view, search, and download the past 90 days of supported activity in your AWS account\. For more information, see [Viewing Events with CloudTrail Event History](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) and [Services Supported by CloudTrail Event History](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-supported-services.html)\. 

 You can create a trail and store your log files in your Amazon S3 bucket for as long as you want, and define Amazon S3 lifecycle rules to archive or delete log files automatically\. By default, your log files are encrypted with Amazon S3 server\-side encryption \(SSE\)\.

To be notified of log file delivery, configure CloudTrail to publish Amazon SNS notifications when new log files are delivered\. For more information, see [Configuring Amazon SNS Notifications for CloudTrail](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)\.

You can also aggregate Amazon Rekognition log files from multiple AWS regions and multiple AWS accounts into a single Amazon S3 bucket\. 

For more information, see [Receiving CloudTrail Log Files from Multiple Regions](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html) and [Receiving CloudTrail Log Files from Multiple Accounts](http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)\.

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
                "arn": "arn:aws:iam::012345678910:user/Alice",
                "accountId": "012345678910",
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
                "collectionArn": "aws:rekognition:us-east-1:012345678910:collection/8fa6aa65-cab4-4d0a-b976-7fd5df63f38a",
                "faceModelVersion": "2.0",
                "statusCode": 200
            },
            "requestID": "1e77d2d5-313f-11e8-8c0e-75c0272f31a4",
            "eventID": "c6da4992-a9a1-4962-93b6-7d0483d95c30",
            "eventType": "AwsApiCall",
            "recipientAccountId": "012345678910"
        },
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "IAMUser",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::012345678910:user/Alice",
                "accountId": "012345678910",
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
            "recipientAccountId": "012345678910"
        },
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "AssumedRole",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:sts::012345678910:assumed-role/Admin/Alice",
                "accountId": "012345678910",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "sessionContext": {
                    "attributes": {
                        "mfaAuthenticated": "false",
                        "creationDate": "2018-03-26T21:48:49Z"
                    },
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "EX_PRINCIPAL_ID",
                        "arn": "arn:aws:iam::012345678910:role/Admin",
                        "accountId": "012345678910",
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
            "recipientAccountId": "012345678910"
        },
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "AssumedRole",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:sts::012345678910:assumed-role/Admin/Alice",
                "accountId": "012345678910",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "sessionContext": {
                    "attributes": {
                        "mfaAuthenticated": "false",
                        "creationDate": "2018-03-26T21:48:49Z"
                    },
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "EX_PRINCIPAL_ID",
                        "arn": "arn:aws:iam::012345678910:role/Admin",
                        "accountId": "012345678910",
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
                "roleArn": "arn:aws:iam::012345678910:role/AmazonRekognition-StreamProcessorRole",
                "settings": {
                    "faceSearch": {
                        "collectionId": "test"
                    }
                },
                "name": "ProcessorName",
                "input": {
                    "kinesisVideoStream": {
                        "arn": "arn:aws:kinesisvideo:us-east-1:012345678910:stream/VideoStream"
                    }
                },
                "output": {
                    "kinesisDataStream": {
                        "arn": "arn:aws:kinesis:us-east-1:012345678910:stream/AmazonRekognition-DataStream"
                    }
                }
            },
            "responseElements": {
                "StreamProcessorArn": "arn:aws:rekognition:us-east-1:012345678910:streamprocessor/ProcessorName"
            },
            "requestID": "e8fb2b3c-3141-11e8-8c0e-75c0272f31a4",
            "eventID": "44ff8f90-fcc2-4740-9e57-0c47610df8e3",
            "eventType": "AwsApiCall",
            "recipientAccountId": "012345678910"
        },
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "AssumedRole",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:sts::012345678910:assumed-role/Admin/Alice",
                "accountId": "012345678910",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "sessionContext": {
                    "attributes": {
                        "mfaAuthenticated": "false",
                        "creationDate": "2018-03-26T21:48:49Z"
                    },
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "EX_PRINCIPAL_ID",
                        "arn": "arn:aws:iam::012345678910:role/Admin",
                        "accountId": "012345678910",
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
            "recipientAccountId": "012345678910"
        },
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "AssumedRole",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:sts::012345678910:assumed-role/Admin/Alice",
                "accountId": "012345678910",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "sessionContext": {
                    "attributes": {
                        "mfaAuthenticated": "false",
                        "creationDate": "2018-03-26T21:48:49Z"
                    },
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "EX_PRINCIPAL_ID",
                        "arn": "arn:aws:iam::012345678910:role/Admin",
                        "accountId": "012345678910",
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
            "recipientAccountId": "012345678910"
        },
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "AssumedRole",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:sts::012345678910:assumed-role/Admin/Alice",
                "accountId": "012345678910",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "sessionContext": {
                    "attributes": {
                        "mfaAuthenticated": "false",
                        "creationDate": "2018-03-26T22:55:22Z"
                    },
                    "sessionIssuer": {
                        "type": "Role",
                        "principalId": "EX_PRINCIPAL_ID",
                        "arn": "arn:aws:iam::012345678910:role/Admin",
                        "accountId": "012345678910",
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
            "recipientAccountId": "012345678910"
        }
    ]
}
```