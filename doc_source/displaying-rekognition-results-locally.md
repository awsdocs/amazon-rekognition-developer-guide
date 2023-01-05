# Displaying Rekognition results with Kinesis Video Streams locally<a name="displaying-rekognition-results-locally"></a>

 You can see the results of Amazon Rekognition Video displayed in your feed from Amazon Kinesis Video Streams using the Amazon Kinesis Video Streams Parser Library’s example tests provided at [KinesisVideo \- Rekognition Examples](https://github.com/aws/amazon-kinesis-video-streams-parser-library#kinesisvideo---rekognition-examples)\. The `KinesisVideoRekognitionIntegrationExample` displays bounding boxes over detected faces and renders the video locally through JFrame\. This process assumes you have successfully connected a media input from a device camera to a Kinesis video stream and started an Amazon Rekognition Stream Processor\. For more information, see [Streaming using a GStreamer plugin](streaming-using-gstreamer-plugin.md)\. 

## Step 1: Installing Kinesis Video Streams Parser Library<a name="step-1-install-parser-library"></a>

 To create a directory and download the Github repository, run the following command: 

```
$ git clone https://github.com/aws/amazon-kinesis-video-streams-parser-library.git
```

 Navigate to the library directory and run the following Maven command to perform a clean installation: 

```
$ mvn clean install
```

## Step 2: Configuring the Kinesis Video Streams and Rekognition integration example test<a name="step-2-configure-kinesis-video-rekognition-example-test"></a>

 Open the `KinesisVideoRekognitionIntegrationExampleTest.java` file\. Remove the `@Ignore` right after the class header\. Populate the data fields with the information from your Amazon Kinesis and Amazon Rekognition resources\. For more information, see [Setting up your Amazon Rekognition Video and Amazon Kinesis resources](setting-up-your-amazon-rekognition-streaming-video-resources.md)\. If you are streaming video to your Kinesis video stream, remove the `inputStream` parameter\. 

 See the following code example: 

```
RekognitionInput rekognitionInput = RekognitionInput.builder()
  .kinesisVideoStreamArn("arn:aws:kinesisvideo:us-east-1:123456789012:stream/rekognition-test-video-stream")
  .kinesisDataStreamArn("arn:aws:kinesis:us-east-1:123456789012:stream/AmazonRekognition-rekognition-test-data-stream")
  .streamingProcessorName("rekognition-test-stream-processor")
  // Refer how to add face collection :
  // https://docs.aws.amazon.com/rekognition/latest/dg/add-faces-to-collection-procedure.html
  .faceCollectionId("rekognition-test-face-collection")
  .iamRoleArn("rekognition-test-IAM-role")
  .matchThreshold(0.95f)
  .build();                
            
KinesisVideoRekognitionIntegrationExample example = KinesisVideoRekognitionIntegrationExample.builder()
  .region(Regions.US_EAST_1)
  .kvsStreamName("rekognition-test-video-stream")
  .kdsStreamName("AmazonRekognition-rekognition-test-data-stream")
  .rekognitionInput(rekognitionInput)
  .credentialsProvider(new ProfileCredentialsProvider())
  // NOTE: Comment out or delete the inputStream parameter if you are streaming video, otherwise
  // the test will use a sample video. 
  //.inputStream(TestResourceUtil.getTestInputStream("bezos_vogels.mkv"))
  .build();
```

## Step 3: Running the Kinesis Video Streams and Rekognition integration example test<a name="step-3-run-kinesis-video-rekognition-example-test"></a>

 Ensure that your Kinesis video stream is receiving media input if you are streaming to it and start analyzing your stream with an Amazon Rekognition Video Stream Processor running\. For more information, see [Overview of Amazon Rekognition Video stream processor operations](streaming-video.md#using-rekognition-video-stream-processor)\. Run the `KinesisVideoRekognitionIntegrationExampleTest` class as a JUnit test\. After a short delay, a new window opens with a video feed from your Kinesis video stream with bounding boxes drawn over detected faces\. 

**Note**  
 The faces in the collection used in this example must have External Image Id \(the file name\) specified in this format in order for bounding box labels to display meaningful text: PersonName1\-Trusted, PersonName2\-Intruder, PersonName3\-Neutral, etc\. The labels can also be color\-coded and are customizable in the FaceType\.java file\. 