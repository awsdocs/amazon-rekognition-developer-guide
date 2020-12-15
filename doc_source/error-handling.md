# Error handling<a name="error-handling"></a>

 This section describes runtime errors and how to handle them\. It also describes error messages and codes that are specific to Amazon Rekognition\.

**Topics**
+ [Error components](#error-handling.Components)
+ [Error messages and codes](#error-handling.MessagesAndCodes)
+ [Error handling in your application](#error-handling.Handling)

## Error components<a name="error-handling.Components"></a>

When your program sends a request, Amazon Rekognition attempts to process it\. If the request is successful, Amazon Rekognition returns an HTTP success status code \(`200 OK`\), along with the results from the requested operation\.

If the request is unsuccessful, Amazon Rekognition returns an error\. Each error has three components: 
+ An HTTP status code \(such as `400`\)\.
+ An exception name \(such as `InvalidS3ObjectException`\)\.
+ An error message \(such as `Unable to get object metadata from S3. Check object key, region and/or access permissions.`\)\.

The AWS SDKs take care of propagating errors to your application, so that you can take appropriate action\. For example, in a Java program, you can write `try-catch` logic to handle a `ResourceNotFoundException`\.

If you're not using an AWS SDK, you need to parse the content of the low\-level response from Amazon Rekognition\. The following is an example of such a response:

```
HTTP/1.1 400 Bad Request
Content-Type: application/x-amz-json-1.1
Date: Sat, 25 May 2019 00:28:25 GMT
x-amzn-RequestId: 03507c9b-7e84-11e9-9ad1-854a4567eb71
Content-Length: 222
Connection: keep-alive

{"__type":"InvalidS3ObjectException","Code":"InvalidS3ObjectException","Logref":"5022229e-7e48-11e9-9ad1-854a4567eb71","Message":"Unable to get object metadata from S3. Check object key, region and/or access permissions."}
```

## Error messages and codes<a name="error-handling.MessagesAndCodes"></a>

The following is a list of exceptions that Amazon Rekognition returns, grouped by HTTP status code\. If *OK to retry?* is *Yes*, you can submit the same request again\. If *OK to retry?* is *No*, you need to fix the problem on the client side before you submit a new request\.

### HTTP status code 400<a name="error-handling.MessagesAndCodes.http400"></a>

An HTTP `400` status code indicates a problem with your request\. Some examples of problems are authentication failure, required parameters that are missing, or exceeding an operation's provisioned throughput\. You have to fix the issue in your application before submitting the request again\.

**AccessDeniedException **  
Message: *An error occurred \(AccessDeniedException\) when calling the <Operation> operation: User: <User ARN> is not authorized to perform: <Operation> on resource: <Resource ARN>\.*  
You aren't authorized to perform the action\. Use the Amazon Resource Name \(ARN\) of an authorized user or IAM role to perform the operation\.  
OK to retry? No

**GroupFacesInProgressException **  
Message: *Failed to schedule GroupFaces job\. There is an existing group faces job for this collection\.*  
Retry the operation after the existing job finishes\.  
OK to retry? No

**IdempotentParameterMismatchException **  
Message: *The ClientRequestToken: <Token> you have supplied is already in use\.*  
A ClientRequestToken input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation\.  
OK to retry? No

**ImageTooLargeException **  
Message: *Image size is too large\.*  
The input image size exceeds the allowed limit\. If you are calling [DetectProtectiveEquipment](API_DetectProtectiveEquipment.md), the image size or resolution exceeds the allowed limit\. For more information, see [Limits in Amazon Rekognition](limits.md)\.  
OK to retry? No

**InvalidImageFormatException **  
Message: *Request has invalid image format\.*  
The provided image format isn't supported\. Use a supported image format \(\.JPEG and \.PNG\)\. For more information, see [Limits in Amazon Rekognition](limits.md)\.  
OK to retry? No

**InvalidPaginationTokenException **  
Messages  
+ *Invalid Token*
+ *Invalid Pagination Token*
The pagination token in the request isn't valid\. The token might have expired\.   
OK to retry? No 

**InvalidParameterException **  
Message: *Request has invalid parameters\.*  
An input parameter violated a constraint\. Validate your parameters before calling the API operation again\.  
OK to retry? No

**InvalidS3ObjectException **  
Messages:  
+ *Request has invalid S3 object\.*
+ *Unable to get object metadata from S3\. Check object key, region and/or access permissions\.*
Amazon Rekognition is unable to access the S3 object that was specified in the request\. For more information, see [Configure Access to S3: AWS S3 Managing Access](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html)\. For troubleshooting information, see [Troubleshooting Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/troubleshooting.html)\.  
OK to retry? No

**LimitExceededException **  
Messages:  
+ *Stream processor limit exceeded for account, limit \- <Current Limit>\.*
+ *<Number of Open Jobs> open Jobs for User <User ARN> Maximum limit: <Maximum Limit>*
An Amazon Rekognition service limit was exceeded\. For example, if you start too many Amazon Rekognition Video jobs concurrently, calls to start operations, such as `StartLabelDetection`, raise a `LimitExceededException` exception \(HTTP status code: 400\) until the number of concurrently running jobs is below the Amazon Rekognition service limit\.  
OK to retry? No

**ProvisionedThroughputExceededException **  
Messages:  
+ *Provisioned Rate exceeded\.*
+ *S3 download limit exceeded\.*
The number of requests exceeded your throughput limit\. For more information, see [Amazon Rekognition Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_rekognition)\.  
To request a limit increase, contact [AWS Support](https://aws.amazon.com/support)\.  
OK to retry? Yes

**ResourceAlreadyExistsException **  
Message: *The collection id: <Collection Id> already exists\.*  
 A collection with the specified ID already exists\.  
OK to retry? No

**ResourceInUseException **  
Messages:  
+ *Stream processor name already in use\.*
+ *Specified resource is in use\.*
+ *Processor not available for stopping stream\.*
+ *Cannot delete stream processor\.*
Retry when the resource is available\.  
OK to retry? No

**ResourceNotFoundException **  
Message: Various messages depending on the API call\.  
The specified resource doesn't exist\.  
OK to retry? No

**ThrottlingException **  
Message: *Slow down; sudden increase in rate of requests\.*  
Your rate of request increase is too fast\. Slow down your request rate and gradually increase it\. We recommend that you back off exponentially and retry\. By default, the AWS SDKs use automatic retry logic and exponential backoff\. For more information, see [Error Retries and Exponential Backoff in AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html) and [Exponential Backoff and Jitter](http://www.awsarchitectureblog.com/2015/03/backoff.html)\.   
OK to retry? Yes

**VideoTooLargeException **  
Message: *Video size in bytes: <Video Size> is more than the maximum limit of: <Max Size> bytes\.*  
The file size or duration of the supplied media is too large\. For more information, see [Limits in Amazon Rekognition](limits.md)\.  
OK to retry? No

### HTTP status code 5xx<a name="error-handling.MessagesAndCodes.http5xx"></a>

An HTTP `5xx` status code indicates a problem that must be resolved by AWS\. This might be a transient error\. If it is, you can retry your request until it succeeds\. Otherwise, go to the [AWS Service Health Dashboard](http://status.aws.amazon.com/) to see if there are any operational issues with the service\.

**InternalServerError \(HTTP 500\) **  
Message: *Internal server error*  
Amazon Rekognition experienced a service issue\. Try your call again\. You should back off exponentially and retry\. By default, the AWS SDKs use automatic retry logic and exponential backoff\. For more information, see [Error Retries and Exponential Backoff in AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html) and [Exponential Backoff and Jitter](http://www.awsarchitectureblog.com/2015/03/backoff.html)\.  
OK to retry? Yes

**ThrottlingException \(HTTP 500\)**  
Message: *Service Unavailable*  
Amazon Rekognition is temporarily unable to process the request\. Try your call again\. We recommend that you back off exponentially and retry\. By default, the AWS SDKs use automatic retry logic and exponential backoff\. For more information, see [Error Retries and Exponential Backoff in AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html) and [Exponential Backoff and Jitter](http://www.awsarchitectureblog.com/2015/03/backoff.html)\.   
OK to retry? Yes

## Error handling in your application<a name="error-handling.Handling"></a>

For your application to run smoothly, you need to add logic to catch errors and respond to them\. Typical approaches include using `try-catch` blocks or `if-then` statements\.

The AWS SDKs perform their own retries and error checking\. If you encounter an error while using one of the AWS SDKs, the error code and description can help you troubleshoot it\. 

You should also see a `Request ID` in the response\. The `Request ID` can be helpful if you need to work with AWS Support to diagnose an issue\.

The following Java code snippet attempts to detect objects in an image and performs rudimentary error handling\. \(In this case, it informs the user that the request failed\.\) 

```
try {
    DetectLabelsResult result = rekognitionClient.detectLabels(request);
    List <Label> labels = result.getLabels();

    System.out.println("Detected labels for " + photo);
    for (Label label: labels) {
        System.out.println(label.getName() + ": " + label.getConfidence().toString());
    }
} 
catch(AmazonRekognitionException e) {
    System.err.println("Could not complete operation");
    System.err.println("Error Message:  " + e.getMessage());
    System.err.println("HTTP Status:    " + e.getStatusCode());
    System.err.println("AWS Error Code: " + e.getErrorCode());
    System.err.println("Error Type:     " + e.getErrorType());
    System.err.println("Request ID:     " + e.getRequestId());
}
catch (AmazonClientException ace) {
    System.err.println("Internal error occurred communicating with Rekognition");
    System.out.println("Error Message:  " + ace.getMessage());
}
```

In this code snippet, the `try-catch` construct handles two different kinds of exceptions:
+ `AmazonRekognitionException` –This exception occurs if the client request was correctly transmitted to Amazon Rekognition, but Amazon Rekognition couldn't process the request and returned an error response instead\.
+ `AmazonClientException` – This exception occurs if the client couldn't get a response from a service, or if the client couldn't parse the response from a service\.