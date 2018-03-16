# NotificationChannel<a name="API_NotificationChannel"></a>

The Amazon Simple Notification Service topic to which Amazon Rekognition publishes the completion status of a video analysis operation\. For more information, see [Calling Rekognition Video Operations](api-video.md)\.

## Contents<a name="API_NotificationChannel_Contents"></a>

 **RoleArn**   <a name="rekognition-Type-NotificationChannel-RoleArn"></a>
The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic\.   
Type: String  
Pattern: `arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`   
Required: Yes

 **SNSTopicArn**   <a name="rekognition-Type-NotificationChannel-SNSTopicArn"></a>
The Amazon SNS topic to which Amazon Rekognition to posts the completion status\.  
Type: String  
Pattern: `(^arn:aws:sns:.*:\w{12}:.+$)`   
Required: Yes

## See Also<a name="API_NotificationChannel_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/NotificationChannel) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/NotificationChannel) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/NotificationChannel) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/NotificationChannel) 