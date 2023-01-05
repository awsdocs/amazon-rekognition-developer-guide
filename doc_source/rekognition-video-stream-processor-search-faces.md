# Searching faces in a streaming video<a name="rekognition-video-stream-processor-search-faces"></a>

Amazon Rekognition Video can search faces in a collection that match faces that are detected in a streaming video\. For more information about collections, see [Searching faces in a collection](collections.md)\.

**Topics**
+ [Creating the Amazon Rekognition Video face search stream processor](#streaming-video-creating-stream-processor)
+ [Starting the Amazon Rekognition Video face search stream processor](#streaming-video-starting-stream-processor)
+ [Using stream processors for face searching \(Java V2 example\)](#using-stream-processors-v2)
+ [Using stream processors for face searching \(Java V1 example\)](#using-stream-processors)
+ [Reading streaming video analysis results](streaming-video-kinesis-output.md)
+ [Reference: Kinesis face recognition record](streaming-video-kinesis-output-reference.md)

The following diagram shows how Amazon Rekognition Video detects and recognizes faces in a streaming video\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/VideoRekognitionStream.png)

## Creating the Amazon Rekognition Video face search stream processor<a name="streaming-video-creating-stream-processor"></a>

Before you can analyze a streaming video, you create an Amazon Rekognition Video stream processor \([CreateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html)\)\. The stream processor contains information about the Kinesis data stream and the Kinesis video stream\. It also contains the identifier for the collection that contains the faces you want to recognize in the input streaming video\. You also specify a name for the stream processor\. The following is a JSON example for the `CreateStreamProcessor` request\.

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
       “StreamProcessorArn”: “arn:aws:rekognition:us-east-1:nnnnnnnnnnnn:streamprocessor/streamProcessorForCam”
}
```

## Starting the Amazon Rekognition Video face search stream processor<a name="streaming-video-starting-stream-processor"></a>

You start analyzing streaming video by calling [StartStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartStreamProcessor.html) with the stream processor name that you specified in `CreateStreamProcessor`\. The following is a JSON example for the `StartStreamProcessor` request\.

```
{
       "Name": "streamProcessorForCam"
}
```

If the stream processor successfully starts, an HTTP 200 response is returned, along with an empty JSON body\.

## Using stream processors for face searching \(Java V2 example\)<a name="using-stream-processors-v2"></a>

The following example code shows how to call various stream processor operations, such as [CreateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html) and [StartStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartStreamProcessor.html), using the AWS SDK for Java version 2\.

This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/CreateStreamProcessor.java)\.

```
    public static void listStreamProcessors(RekognitionClient rekClient) {

        ListStreamProcessorsRequest request = ListStreamProcessorsRequest.builder()
            .maxResults(15)
            .build();

        ListStreamProcessorsResponse listStreamProcessorsResult = rekClient.listStreamProcessors(request);
        for (StreamProcessor streamProcessor : listStreamProcessorsResult.streamProcessors()) {
            System.out.println("StreamProcessor name - " + streamProcessor.name());
            System.out.println("Status - " + streamProcessor.status());
        }
    }

    private static void describeStreamProcessor(RekognitionClient rekClient, String StreamProcessorName) {

        DescribeStreamProcessorRequest streamProcessorRequest = DescribeStreamProcessorRequest.builder()
            .name(StreamProcessorName)
            .build();

        DescribeStreamProcessorResponse describeStreamProcessorResult = rekClient.describeStreamProcessor(streamProcessorRequest);
        System.out.println("Arn - " + describeStreamProcessorResult.streamProcessorArn());
        System.out.println("Input kinesisVideo stream - "
              + describeStreamProcessorResult.input().kinesisVideoStream().arn());
        System.out.println("Output kinesisData stream - "
              + describeStreamProcessorResult.output().kinesisDataStream().arn());
        System.out.println("RoleArn - " + describeStreamProcessorResult.roleArn());
        System.out.println(
              "CollectionId - " + describeStreamProcessorResult.settings().faceSearch().collectionId());
        System.out.println("Status - " + describeStreamProcessorResult.status());
        System.out.println("Status message - " + describeStreamProcessorResult.statusMessage());
        System.out.println("Creation timestamp - " + describeStreamProcessorResult.creationTimestamp());
        System.out.println("Last update timestamp - " + describeStreamProcessorResult.lastUpdateTimestamp());
    }

    private static void startSpecificStreamProcessor(RekognitionClient rekClient, String StreamProcessorName) {
        try {
            StartStreamProcessorRequest streamProcessorRequest = StartStreamProcessorRequest.builder()
                .name(StreamProcessorName)
                .build();

            rekClient.startStreamProcessor(streamProcessorRequest);
            System.out.println("Stream Processor " + StreamProcessorName + " started.");

        } catch (RekognitionException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }
    }

    private static void processCollection(RekognitionClient rekClient, String StreamProcessorName, String kinInputStream, String kinOutputStream, String collectionName, String role ) {

        try {
            KinesisVideoStream videoStream = KinesisVideoStream.builder()
                .arn(kinInputStream)
                .build();

            KinesisDataStream dataStream = KinesisDataStream.builder()
                .arn(kinOutputStream)
                .build();

            StreamProcessorOutput processorOutput = StreamProcessorOutput.builder()
                .kinesisDataStream(dataStream)
                .build();

            StreamProcessorInput processorInput = StreamProcessorInput.builder()
                .kinesisVideoStream(videoStream)
                .build();

            FaceSearchSettings searchSettings = FaceSearchSettings.builder()
                .faceMatchThreshold(75f)
                .collectionId(collectionName)
                .build() ;

            StreamProcessorSettings processorSettings = StreamProcessorSettings.builder()
                .faceSearch(searchSettings)
                .build();

            CreateStreamProcessorRequest processorRequest = CreateStreamProcessorRequest.builder()
                .name(StreamProcessorName)
                .input(processorInput)
                .output(processorOutput)
                .roleArn(role)
                .settings(processorSettings)
                .build();

            CreateStreamProcessorResponse response = rekClient.createStreamProcessor(processorRequest);
            System.out.println("The ARN for the newly create stream processor is "+response.streamProcessorArn());

        } catch (RekognitionException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }
    }

    private static void deleteSpecificStreamProcessor(RekognitionClient rekClient, String StreamProcessorName) {

        rekClient.stopStreamProcessor(a->a.name(StreamProcessorName));
        rekClient.deleteStreamProcessor(a->a.name(StreamProcessorName));
        System.out.println("Stream Processor " + StreamProcessorName + " deleted.");
    }
```

## Using stream processors for face searching \(Java V1 example\)<a name="using-stream-processors"></a>

The following example code shows how to call various stream processor operations, such as [CreateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html) and [StartStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartStreamProcessor.html), using Java V1\. The example includes a stream processor manager class \(StreamManager\) that provides methods to call stream processor operations\. The starter class \(Starter\) creates a StreamManager object and calls various operations\. 

**To configure the example:**

1. Set the values of the Starter class member fields to your desired values\.

1. In the Starter class function `main`, uncomment the desired function call\.

### Starter class<a name="streaming-started"></a>

```
//Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
//PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

// Starter class. Use to create a StreamManager class
// and call stream processor operations.
package com.amazonaws.samples;
import com.amazonaws.samples.*;

public class Starter {

	public static void main(String[] args) {
		
		
    	String streamProcessorName="Stream Processor Name";
    	String kinesisVideoStreamArn="Kinesis Video Stream Arn";
    	String kinesisDataStreamArn="Kinesis Data Stream Arn";
    	String roleArn="Role Arn";
    	String collectionId="Collection ID";
    	Float matchThreshold=50F;

		try {
			StreamManager sm= new StreamManager(streamProcessorName,
					kinesisVideoStreamArn,
					kinesisDataStreamArn,
					roleArn,
					collectionId,
					matchThreshold);
			//sm.createStreamProcessor();
			//sm.startStreamProcessor();
			//sm.deleteStreamProcessor();
			//sm.deleteStreamProcessor();
			//sm.stopStreamProcessor();
			//sm.listStreamProcessors();
			//sm.describeStreamProcessor();
		}
		catch(Exception e){
			System.out.println(e.getMessage());
		}
	}
}
```

### StreamManager class<a name="streaming-manager"></a>

```
//Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
//PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

// Stream manager class. Provides methods for calling
// Stream Processor operations.
package com.amazonaws.samples;

import com.amazonaws.services.rekognition.AmazonRekognition;
import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
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

public class StreamManager {

    private String streamProcessorName;
    private String kinesisVideoStreamArn;
    private String kinesisDataStreamArn;
    private String roleArn;
    private String collectionId;
    private float matchThreshold;

    private AmazonRekognition rekognitionClient;
    

    public StreamManager(String spName,
    		String kvStreamArn,
    		String kdStreamArn,
    		String iamRoleArn,
    		String collId,
    		Float threshold){
    	streamProcessorName=spName;
    	kinesisVideoStreamArn=kvStreamArn;
    	kinesisDataStreamArn=kdStreamArn;
    	roleArn=iamRoleArn;
    	collectionId=collId;
    	matchThreshold=threshold;
    	rekognitionClient=AmazonRekognitionClientBuilder.defaultClient();
    	
    }
    
    public void createStreamProcessor() {
    	//Setup input parameters
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

        //Create the stream processor
        CreateStreamProcessorResult createStreamProcessorResult = rekognitionClient.createStreamProcessor(
                new CreateStreamProcessorRequest().withInput(streamProcessorInput).withOutput(streamProcessorOutput)
                        .withSettings(streamProcessorSettings).withRoleArn(roleArn).withName(streamProcessorName));

        //Display result
        System.out.println("Stream Processor " + streamProcessorName + " created.");
        System.out.println("StreamProcessorArn - " + createStreamProcessorResult.getStreamProcessorArn());
    }

    public void startStreamProcessor() {
        StartStreamProcessorResult startStreamProcessorResult =
                rekognitionClient.startStreamProcessor(new StartStreamProcessorRequest().withName(streamProcessorName));
        System.out.println("Stream Processor " + streamProcessorName + " started.");
    }

    public void stopStreamProcessor() {
        StopStreamProcessorResult stopStreamProcessorResult =
                rekognitionClient.stopStreamProcessor(new StopStreamProcessorRequest().withName(streamProcessorName));
        System.out.println("Stream Processor " + streamProcessorName + " stopped.");
    }

    public void deleteStreamProcessor() {
        DeleteStreamProcessorResult deleteStreamProcessorResult = rekognitionClient
                .deleteStreamProcessor(new DeleteStreamProcessorRequest().withName(streamProcessorName));
        System.out.println("Stream Processor " + streamProcessorName + " deleted.");
    }

    public void describeStreamProcessor() {
        DescribeStreamProcessorResult describeStreamProcessorResult = rekognitionClient
                .describeStreamProcessor(new DescribeStreamProcessorRequest().withName(streamProcessorName));

        //Display various stream processor attributes.
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

    public void listStreamProcessors() {
        ListStreamProcessorsResult listStreamProcessorsResult =
                rekognitionClient.listStreamProcessors(new ListStreamProcessorsRequest().withMaxResults(100));

        //List all stream processors (and state) returned from Rekognition
        for (StreamProcessor streamProcessor : listStreamProcessorsResult.getStreamProcessors()) {
            System.out.println("StreamProcessor name - " + streamProcessor.getName());
            System.out.println("Status - " + streamProcessor.getStatus());
        }
    }
}
```