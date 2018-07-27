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

