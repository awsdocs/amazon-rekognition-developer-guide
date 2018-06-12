# Starting Streaming Video Analysis<a name="streaming-video-starting-analysis"></a>

You start analyzing a streaming video by starting a Rekognition Video stream processor and streaming video into Rekognition Video\. A Rekognition Video stream processor allows you to start, stop, and manage stream processors\. You create a stream processor by calling [CreateStreamProcessor](API_CreateStreamProcessor.md)\. The request parameters include the Amazon Resource Names \(ARNs\) for the Kinesis video stream, the Kinesis data stream, and the identifier for the collection that's used to recognize faces in the streaming video\. It also includes the name that you specify for the stream processor\.

You start processing a video by calling the [ StartStreamProcessor APIrequestsStartStreamProcessor  Starts processing a stream processor\. You create a stream processor by calling [CreateStreamProcessor](API_CreateStreamProcessor.md)\. To tell `StartStreamProcessor` which stream processor to start, use the value of the `Name` field specified in the call to `CreateStreamProcessor`\.  Request Syntax  

```
{
   "[Name](#rekognition-StartStreamProcessor-request-Name)": "string"
}
```   Request Parameters  The request accepts the following data in JSON format\.  

 ** [Name](#API_StartStreamProcessor_RequestSyntax) **   <a name="rekognition-StartStreamProcessor-request-Name"></a>
The name of the stream processor to start processing\.  
Type: String  
Length Constraints: Minimum length of 1\. Maximum length of 128\.  
Pattern: `[a-zA-Z0-9_.\-]+`   
Required: Yes    Response Elements  If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body\.   Errors   

 **AccessDeniedException**   
You are not authorized to perform the action\.  
HTTP Status Code: 400 

 **InternalServerError**   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500 

 **InvalidParameterException**   
Input parameter violated a constraint\. Validate your parameter before calling the API operation again\.  
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
HTTP Status Code: 500    See Also   For more information about using this API in one of the language\-specific AWS SDKs, see the following:    [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/StartStreamProcessor)     [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/StartStreamProcessor)     [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StartStreamProcessor)     [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/StartStreamProcessor)     [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/StartStreamProcessor)     [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/StartStreamProcessor)     [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/StartStreamProcessor)     [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/StartStreamProcessor)     [AWS SDK for Ruby V2](https://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/StartStreamProcessor)    ](API_StartStreamProcessor.md) operation\. To get status information for a stream processor, call [DescribeStreamProcessor](API_DescribeStreamProcessor.md)\. Other operations you can call are [StopStreamProcessor](API_StopStreamProcessor.md) to stop a stream processor, and [DeleteStreamProcessor](API_DeleteStreamProcessor.md) to delete a stream processor\. To get a list of stream processors in your account, call [ListStreamProcessors](API_ListStreamProcessors.md)\. 

After the stream processor starts running, you stream the video into Rekognition Video through the Kinesis video stream that you specified in `CreateStreamProcessor`\. Use the Kinesis Video Streams SDK [PutMedia](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_PutMedia.html) operation to deliver video into the Kinesis video stream\. For an example, see [PutMedia API Example](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-putmedia.html)\.

For information about how your application can consume Rekognition Video analysis results, see [Reading Streaming Video Analysis Results](streaming-video-kinesis-output.md)\.

## Creating the Rekognition Video Stream Processor<a name="streaming-video-creating-stream-processor"></a>

Before you can analyze a streaming video, you create a Rekognition Video stream processor \([CreateStreamProcessor](API_CreateStreamProcessor.md)\)\. The stream processor contains information about the Kinesis data stream and the Kinesis video stream\. It also contains the identifier for the collection that contains the faces you want to recognize in the input streaming video\. You also specify a name for the stream processor\. The following is a JSON example for the `CreateStreamProcessor` request\.

```
{
       "Name": "streamProcessorForCam",
       "Input": {
              "KinesisVideoStream": {
                     "Arn": "arn:aws:kinesisvideo:us-east-1:nnnnnnnnnnnn:stream/inputVideo"
              }
       },
       "Output": {
              "KinesisDataStream": {
                     "Arn": "arn:aws:kinesis:us-east-1:nnnnnnnnnnnn:stream/outputData"
              }
       },
       "RoleArn": "arn:aws:iam::nnnnnnnnnnn:role/roleWithKinesisPermission",
       "Settings": {
              "FaceSearch": {
                     "CollectionId": "collection-with-100-faces",
                     "FaceMatchThreshold": 85.5
              }
       }
}
```

The following is an example response from `CreateStreamProcessor`\.

```
{
       “StreamProcessorArn”: “arn:aws:rekognition:us-east-1:987654321098:streamprocessor/streamProcessorForCam”
}
```

## Starting the Rekognition Video Stream Processor<a name="streaming-video-starting-stream-processor"></a>

You start analyzing streaming video by calling [StartStreamProcessor](API_StartStreamProcessor.md) with the stream processor name that you specified in `CreateStreamProcessor`\. The following is a JSON example for the `StartStreamProcessor` request\.

```
{
       "Name": "streamProcessorForCam"
}
```

If the stream processor successfully starts, an HTTP 200 response is returned, along with an empty JSON body\.

## Using Stream Processors<a name="using-stream-processors"></a>

The following example code shows how to call various stream processor operations, such as [CreateStreamProcessor](API_CreateStreamProcessor.md) and [StartStreamProcessor](API_StartStreamProcessor.md)\.

```
package com.amazonaws.rekognition.video.streaming;

import com.amazonaws.services.rekognition.AmazonRekognitionClient;
import com.amazonaws.services.rekognition.model.CreateStreamProcessorRequest;
import com.amazonaws.services.rekognition.model.CreateStreamProcessorResult;
import com.amazonaws.services.rekognition.model.DeleteStreamProcessorRequest;
import com.amazonaws.services.rekognition.model.DeleteStreamProcessorResult;
import com.amazonaws.services.rekognition.model.DescribeStreamProcessorRequest;
import com.amazonaws.services.rekognition.model.DescribeStreamProcessorResult;
import com.amazonaws.services.rekognition.model.FaceSearchSettings;
import com.amazonaws.services.rekognition.model.KinesisDataStream;
import com.amazonaws.services.rekognition.model.KinesisVideoStream;
import com.amazonaws.services.rekognition.model.ListStreamProcessorsRequest;
import com.amazonaws.services.rekognition.model.ListStreamProcessorsResult;
import com.amazonaws.services.rekognition.model.StartStreamProcessorRequest;
import com.amazonaws.services.rekognition.model.StartStreamProcessorResult;
import com.amazonaws.services.rekognition.model.StopStreamProcessorRequest;
import com.amazonaws.services.rekognition.model.StopStreamProcessorResult;
import com.amazonaws.services.rekognition.model.StreamProcessor;
import com.amazonaws.services.rekognition.model.StreamProcessorInput;
import com.amazonaws.services.rekognition.model.StreamProcessorOutput;
import com.amazonaws.services.rekognition.model.StreamProcessorSettings;

public class StreamProcessorSample {

    private String streamProcessorName;
    private String kinesisVideoStreamArn;
    private String kinesisDataStreamArn;
    private String roleArn;
    private String collectionId;
    private float matchThreshold;

    private AmazonRekognitionClient rekognitionClient;

    public void createStreamProcessorSample() {
        KinesisVideoStream kinesisVideoStream = new KinesisVideoStream().withArn(kinesisVideoStreamArn);
        StreamProcessorInput streamProcessorInput =
                new StreamProcessorInput().withKinesisVideoStream(kinesisVideoStream);
        KinesisDataStream kinesisDataStream = new KinesisDataStream().withArn(kinesisDataStreamArn);
        StreamProcessorOutput streamProcessorOutput =
                new StreamProcessorOutput().withKinesisDataStream(kinesisDataStream);
        FaceSearchSettings faceSearchSettings =
                new FaceSearchSettings().withCollectionId(collectionId).withFaceMatchThreshold(matchThreshold);
        StreamProcessorSettings streamProcessorSettings =
                new StreamProcessorSettings().withFaceSearch(faceSearchSettings);

        CreateStreamProcessorResult createStreamProcessorResult = rekognitionClient.createStreamProcessor(
                new CreateStreamProcessorRequest().withInput(streamProcessorInput).withOutput(streamProcessorOutput)
                        .withSettings(streamProcessorSettings).withRoleArn(roleArn).withName(streamProcessorName));
        System.out.println("StreamProcessorArn - " + createStreamProcessorResult.getStreamProcessorArn());
    }

    public void startStreamProcessorSample() {
        StartStreamProcessorResult startStreamProcessorResult =
                rekognitionClient.startStreamProcessor(new StartStreamProcessorRequest().withName(streamProcessorName));
    }

    public void stopStreamProcessorSample() {
        StopStreamProcessorResult stopStreamProcessorResult =
                rekognitionClient.stopStreamProcessor(new StopStreamProcessorRequest().withName(streamProcessorName));
    }

    public void deleteStreamProcessorSample() {
        DeleteStreamProcessorResult deleteStreamProcessorResult = rekognitionClient
                .deleteStreamProcessor(new DeleteStreamProcessorRequest().withName(streamProcessorName));
    }

    public void describeStreamProcessorSample() {
        DescribeStreamProcessorResult describeStreamProcessorResult = rekognitionClient
                .describeStreamProcessor(new DescribeStreamProcessorRequest().withName(streamProcessorName));
        System.out.println("Arn - " + describeStreamProcessorResult.getStreamProcessorArn());
        System.out.println("Input kinesisVideo stream - "
                + describeStreamProcessorResult.getInput().getKinesisVideoStream().getArn());
        System.out.println("Output kinesisData stream - "
                + describeStreamProcessorResult.getOutput().getKinesisDataStream().getArn());
        System.out.println("RoleArn - " + describeStreamProcessorResult.getRoleArn());
        System.out.println(
                "CollectionId - " + describeStreamProcessorResult.getSettings().getFaceSearch().getCollectionId());
        System.out.println("Status - " + describeStreamProcessorResult.getStatus());
        System.out.println("Status message - " + describeStreamProcessorResult.getStatusMessage());
        System.out.println("Creation timestamp - " + describeStreamProcessorResult.getCreationTimestamp());
        System.out.println("Last update timestamp - " + describeStreamProcessorResult.getLastUpdateTimestamp());
    }

    public void listStreamProcessorSample() {
        ListStreamProcessorsResult listStreamProcessorsResult =
                rekognitionClient.listStreamProcessors(new ListStreamProcessorsRequest().withMaxResults(100));
        for (StreamProcessor streamProcessor : listStreamProcessorsResult.getStreamProcessors()) {
            System.out.println("StreamProcessor name - " + streamProcessor.getName());
            System.out.println("Status - " + streamProcessor.getStatus());
        }
    }
}
```

## Streaming Video into Rekognition Video<a name="video-streaming-kinesisvideostreams-stream"></a>

To stream video into Rekognition Video, you use the Amazon Kinesis Video Streams SDK to create and use a Kinesis video stream\. The `PutMedia` operation writes video data *fragments* into a Kinesis video stream that Rekognition Video consumes\. Each video data fragment is typically 2–10 seconds in length and contains a self\-contained sequence of video frames\. Rekognition Video supports H\.264 encoded videos, which can have three types of frames \(I, B, and P\)\. For more information, see [Inter Frame](https://en.wikipedia.org/wiki/Inter_frame)\. The first frame in the fragment must be an I\-frame\. An I\-frame can be decoded independent of any other frame\. 

As video data arrives into the Kinesis video stream, Kinesis Video Streams assigns a unique number to the fragment\. For an example, see [PutMedia API Example](http://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-putmedia.html)\.