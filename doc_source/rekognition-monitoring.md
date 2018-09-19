# Monitoring Rekognition<a name="rekognition-monitoring"></a>

With CloudWatch, you can get metrics for individual Rekognition operations or global Rekognition metrics for your account, You can use metrics to track the health of your Rekognition\-based solution and set up alarms to notify you when one or more metrics fall outside a defined threshold\. For example, you can see metrics for the number of server errors that have occurred, or metrics for the number of faces that have been detected\. You can also see metrics for the number of times a specific Rekognition operation has succeeded\. To see metrics, you can use [Amazon CloudWatch](https://console.aws.amazon.com/cloudwatch/), [Amazon AWS Command Line Interface](https://docs.aws.amazon.com/AmazonCloudWatch/latest/cli/), or the [CloudWatch API](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/)\.

You can also see aggregated metrics, for a chosen period of time, by using the Rekognition console\. For more information, see [Exercise 4: See Aggregated Metrics \(Console\)](aggregated-metrics.md)\.

## Using CloudWatch Metrics for Rekognition<a name="using-metrics"></a>

To use metrics, you must specify the following information:
+ The metric dimension, or no dimension\. A *dimension* is a name\-value pair that helps you to uniquely identify a metric\. Rekognition has one dimension, named *Operation*\. It provides metrics for a specific operation\. If you do not specify a dimension, the metric is scoped to all Rekognition operations within your account\.
+ The metric name, such as `UserErrorCount`\.

You can get monitoring data for Rekognition using the AWS Management Console, the AWS CLI, or the CloudWatch API\. You can also use the CloudWatch API through one of the Amazon AWS Software Development Kits \(SDKs\) or the CloudWatch API tools\. The console displays a series of graphs based on the raw data from the CloudWatch API\. Depending on your needs, you might prefer to use either the graphs displayed in the console or retrieved from the API\.

### <a name="how-do-i"></a>

The following list shows some common uses for the metrics\. These are suggestions to get you started, not a comprehensive list\.


| How Do I? | Relevant Metrics | 
| --- | --- | 
|  How do I track the numbers of faces recognized?  |  Monitor the `Sum` statistic of the `DetectedFaceCount` metric\.  | 
|  How do I know if my application has reached the maximum number of requests per second?  |  Monitor the `Sum` statistic of the `ThrottledCount` metric\.  | 
|  How can I monitor the request errors?  |  Use the `Sum` statistic of the `UserErrorCount` metric\.  | 
|  How can I find the total number of requests?  |  Use the `ResponseTime` and `Data Samples` statistic of the `ResponseTime` metric\. This includes any request that results in an error\. If you want to see only successful operation calls, use the `SuccessfulRequestCount` metric\.  | 
|  How can I monitor the latency of `Rekognition` operation calls?  |  Use the `ResponseTime` metric\.  | 
|  How can I monitor how many times `IndexFaces` successfully added faces to Rekognition collections?  |  Monitor the `Sum` statistic with the `SuccessfulRequestCount` metric and `IndexFaces` operation\. Use the `Operation` dimension to select the operation and metric\.  | 

You must have the appropriate CloudWatch permissions to monitor Rekognition with CloudWatch\. For more information, see [Authentication and Access Control for Amazon CloudWatch](https://docs.aws.amazon.com//AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html)\.

## Access Rekognition Metrics<a name="how-to-access"></a>

The following examples show how to access Rekognition metrics using the CloudWatch console, the AWS CLI, and the CloudWatch API\.

**To view metrics \(console\)**

1. Open the CloudWatch console at [https://console\.aws\.amazon\.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch)\.

1. Choose **Metrics**, choose the **All Metrics** tab, and then choose **Rekognition**\.

1. Choose **Metrics with no dimensions**, and then choose a metric\. 

   For example, choose the **DetectedFace** metric to measure how many faces have been detected\.

1. Choose a value for the date range\. The metric count displayed in the graph\. 

**To view metrics successful `DetectFaces` operation calls have been made over a period of time \(CLI\)\.**
+ Open the AWS CLI and enter the following command:

  `aws cloudwatch get-metric-statistics --metric-name SuccessfulRequestCount --start-time 2017-1-1T19:46:20 --end-time 2017-1-6T19:46:57 --period 3600 --namespace AWS/Rekognition --statistics Sum --dimensions Name=Operation,Value=DetectFaces --region us-west-2` 

  This example shows the successful `DetectFaces` operation calls made over a period of time\. For more information, see [get\-metric\-statistics](https://docs.aws.amazon.com/cli/latest/reference/get-metric-statistics.html)\.

**To access metrics \(CloudWatch API\)**
+  Call `[GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html)`\. For more information, see the [Amazon CloudWatch API Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/)\. 

## Create an Alarm<a name="alarms"></a>

You can create a CloudWatch alarm that sends an Amazon Simple Notification Service \(Amazon SNS\) message when the alarm changes state\. An alarm watches a single metric over a time period you specify, and performs one or more actions based on the value of the metric relative to a given threshold over a number of time periods\. The action is a notification sent to an Amazon SNS topic or an Auto Scaling policy\.

Alarms invoke actions for sustained state changes only\. CloudWatch alarms do not invoke actions simply because they are in a particular state\. The state must have changed and been maintained for a specified number of time periods\. 

**To set an alarm \(console\)**

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console\.aws\.amazon\.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/)\.

1. Choose **Create Alarm**\. This launches the **Create Alarm Wizard**\. 

1. In the **Metrics with no dimensions** metric list, choose **Rekognition Metrics**, and then choose a metric\.

   For example, choose **DetectedFaceCount** to set an alarm for a maximum number of detected faces\.

1. In the **Time Range** area, select a date range value that includes face detection operations that you have called\. Choose **Next**

1. Fill in the **Name** and **Description**\. For **Whenever**, choose **>=**, and enter a maximum value of your choice\.

1. If you want CloudWatch to send you email when the alarm state is reached, for **Whenever this alarm:**, choose ** State is ALARM**\. To send alarms to an existing Amazon SNS topic, for **Send notification to:**, choose an existing SNS topic\. To set the name and email addresses for a new email subscription list, choose **Create topic** CloudWatch saves the list and displays it in the field so you can use it to set future alarms\. 
**Note**  
If you use **Create topic** to create a new Amazon SNS topic, the email addresses must be verified before the intended recipients receive notifications\. Amazon SNS sends email only when the alarm enters an alarm state\. If this alarm state change happens before the email addresses are verified, intended recipients do not receive a notification\.

1. Preview the alarm in the **Alarm Preview** section\. Choose **Create Alarm**\. 

**To set an alarm \(AWS CLI\)**
+ Open the AWS CLI and enter the following command\. Change value of the `alarm-actions` parameter to reference an Amazon SNS topic that you previously created\. 

  `aws cloudwatch put-metric-alarm --alarm-name UserErrors --alarm-description "Alarm when more than 10 user errors occur" --metric-name UserErrorCount --namespace AWS/Rekognition --statistic Average --period 300 --threshold 10 --comparison-operator GreaterThanThreshold --evaluation-periods 2 --alarm-actions arn:aws:sns:us-west-2:111111111111:UserError --unit Count`

  This example shows how to create an alarm for when more than 10 user errors occur within 5 minutes\. For more information, see [put\-metric\-alarm](https://docs.aws.amazon.com/cli/latest/reference/put-metric-alarm.html)\.

**To set an alarm \(CloudWatch API\)**
+ Call `[PutMetricAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html)`\. For more information, see *[Amazon CloudWatch API Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/)*\.