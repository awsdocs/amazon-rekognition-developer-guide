# CloudWatch metrics for Rekognition<a name="cloudwatch-metricsdim"></a>

This section contains information about the Amazon CloudWatch metrics and the *Operation* dimension available for Amazon Rekognition\.

You can also see an aggregate view of Rekognition metrics from the Rekognition console\. For more information, see [Exercise 4: See aggregated metrics \(console\)](aggregated-metrics.md)\.

## CloudWatch metrics for Rekognition<a name="cloudwatch-metrics"></a>

The following table summarizes the Rekognition metrics\.


| Metric | Description | 
| --- | --- | 
|  SuccessfulRequestCount  |  The number of successful requests\. The response code range for a successful request is 200 to 299\.  Unit: Count Valid statistics: `Sum,Average`  | 
|  ThrottledCount  |  The number of throttled requests\. Rekognition throttles a request when it receives more requests than the limit of transactions per second set for your account\. If the limit set for your account is frequently exceeded, you can request a limit increase\. To request an increase, see [AWS Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)\.  Unit: Count Valid statistics: `Sum,Average`  | 
|  ResponseTime  |  The time in milliseconds for Rekognition to compute the response\.  Units: [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/rekognition/latest/dg/cloudwatch-metricsdim.html) Valid statistics: `Data Samples,Average`  The `ResponseTime` metric is not included in the Rekognition metric pane\.   | 
|  DetectedFaceCount  |  The number of faces detected with the `IndexFaces` or `DetectFaces` operation\. Unit: Count Valid statistics: `Sum,Average`  | 
|  DetectedLabelCount  |  The number of labels detected with the `DetectLabels` operation\. Unit: Count Valid statistics: `Sum,Average`  | 
|  ServerErrorCount  |  The number of server errors\. The response code range for a server error is 500 to 599\. Unit: Count Valid statistics: `Sum, Average`  | 
|  UserErrorCount  |  The number of user errors \(invalid parameters, invalid image, no permission, etc\)\. The response code range for a user error is 400 to 499\. Unit: Count Valid statistics: `Sum,Average`  | 
| MinInferenceUnits | The minimum number of inference units specified during the StartProjectVersion request\.Unit: CountValid statistics: `Average` | 
| MaxInferenceUnits | The maximum number of inference units specified during the StartProjectVersion request\.Unit: CountValid statistics: `Average` | 
|  DesiredInferenceUnits  |  The number of inference units to which Rekognition is scaling up or down\.  Unit: Count Valid statistics: `Average`  | 
|  InServiceInferenceUnits  |  The number of inference units that the model is using\. Unit: Count Valid statistics: `Average` It is recommended that you use the Average statistic to obtain the 1 minute average of how many instances are used\.  | 

## CloudWatch dimension for Rekognition<a name="cloudwatch-dimensions"></a>

To retrieve operation\-specific metrics, use the `Rekognition` namespace and provide an operation dimension\. 

For more information about dimensions, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) in the *Amazon CloudWatch User Guide*\. 

## CloudWatch dimension for Rekognition Custom Labels<a name="cloudwatch-dimensions"></a>

The following table displays the CloudWatch dimensions available for use with Rekognition Custom Labels:


****  

| Dimension | Description | 
| --- | --- | 
| ProjectName | The name of the Rekognition Custom Labels project you created with CreateProject\. | 
| VersionName | The name of the Rekognition Custom Labels project version you created with CreateProjectVersion\. | 

For more information about dimensions, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) in the *Amazon CloudWatch User Guide*\. 