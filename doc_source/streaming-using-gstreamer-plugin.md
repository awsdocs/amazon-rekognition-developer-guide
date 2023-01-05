# Streaming using a GStreamer plugin<a name="streaming-using-gstreamer-plugin"></a>

Amazon Rekognition Video can analyze a live streaming video from a device camera\. To access media input from a device source, you need to install GStreamer\. GStreamer is a third\-party multimedia framework software that connects media sources and processing tools together in workflow pipelines\. You also need to install the [Amazon Kinesis Video Streams Producer Plugin](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp/) for Gstreamer\. This process assumes that you have successfully set up your Amazon Rekognition Video and Amazon Kinesis resources\. For more information, see [Setting up your Amazon Rekognition Video and Amazon Kinesis resources](setting-up-your-amazon-rekognition-streaming-video-resources.md)\.

## Step 1: Install Gstreamer<a name="step-1-install-gstreamer"></a>

 Download and install Gstreamer, a third\-party multi\-media platform software\. You can use a package management software like Homebrew \([Gstreamer on Homebrew](https://formulae.brew.sh/formula/gstreamer)\) or get it directly from the [Freedesktop website](https://gstreamer.freedesktop.org/download/)\. 

 Verify the successful installation of Gstreamer by launching a video feed with a test source from your command line terminal\. 

```
$ gst-launch-1.0 videotestsrc ! autovideosink
```

## Step 2: Install the Kinesis Video Streams Producer plugin<a name="step-2-install-kinesis-video-plugin"></a>

 In this section, you will download the [ Amazon Kinesis Video Streams Producer Library](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp/) and install the Kinesis Video Streams Gstreamer plugin\. 

 Create a directory and clone the source code from the Github repository\. Be sure to include the `--recursive` parameter\. 

```
$ git clone --recursive https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp.git
```

Follow the [instructions provided by the library](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp/blob/master/README.md) to configure and build the project\. Make sure you use the platform\-specific commands for your operating system\. Use the `-DBUILD_GSTREAMER_PLUGIN=ON` parameter when you run `cmake` to install the Kinesis Video Streams Gstreamer plugin\. This project requires the following additional packages that are included in the installation: GCC or Clang, Curl, Openssl and Log4cplus\. If your build fails because of a missing package, verify that the package is installed and in your PATH\. If you encounter a "can’t run C compiled program" error while building, run the build command again\. Sometimes, the correct C compiler is not found\. 

 Verify the installation of the Kinesis Video Streams plugin by running the following command\. 

```
$ gst-inspect-1.0 kvssink
```

 The following information, such as factory and plugin details, should appear: 

```
Factory Details:
  Rank                     primary + 10 (266)
  Long-name                KVS Sink
  Klass                    Sink/Video/Network
  Description              GStreamer AWS KVS plugin
  Author                   AWS KVS <kinesis-video-support@amazon.com>
                
Plugin Details:
  Name                     kvssink
  Description              GStreamer AWS KVS plugin
  Filename                 /Users/YOUR_USER/amazon-kinesis-video-streams-producer-sdk-cpp/build/libgstkvssink.so
  Version                  1.0
  License                  Proprietary
  Source module            kvssinkpackage
  Binary package           GStreamer
  Origin URL               http://gstreamer.net/
  
  ...
```

## Step 3: Run Gstreamer with the Kinesis Video Streams plugin<a name="step-3-run-gstreamer-with-kinesis-video-plugin"></a>

 Before you begin streaming from a device camera to Kinesis Video Streams, you might need to convert the media source to an acceptable codec for Kinesis Video Streams\. To determine the specifications and format capabilities of devices currently connected to your machine, run the following command\.

```
$ gst-device-monitor-1.0
```

 To begin streaming, launch Gstreamer with the following sample command and add your credentials and Amazon Kinesis Video Streams information\. You should use the access keys and region for the IAM service role you created while [giving Amazon Rekognition access to your Kinesis streams](https://docs.aws.amazon.com/rekognition/latest/dg/api-streaming-video-roles.html#api-streaming-video-roles-all-stream)\. For more information on access keys, see [Managing Access Keys for IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the *IAM User Guide*\. Also, you may adjust the video format argument parameters as required by your usage and available from your device\. 

```
$ gst-launch-1.0 autovideosrc device=/dev/video0 ! videoconvert ! video/x-raw,format=I420,width=640,height=480,framerate=30/1 ! 
                x264enc bframes=0 key-int-max=45 bitrate=500 ! video/x-h264,stream-format=avc,alignment=au,profile=baseline ! 
                kvssink stream-name="YOUR_STREAM_NAME" storage-size=512 access-key="YOUR_ACCESS_KEY" secret-key="YOUR_SECRET_ACCESS_KEY" aws-region="YOUR_AWS_REGION"
```

 For more launch commands, see [Example GStreamer Launch Commands](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-gstreamer-plugin.html#examples-gstreamer-plugin-launch)\. 

**Note**  
 If your launch command terminates with a non\-negotiation error, check the output from the Device Monitor and make sure that the `videoconvert` parameter values are valid capabilities of your device\. 

 You will see a video feed from your device camera on your Kinesis video stream after a few seconds\. To begin detecting and matching faces with Amazon Rekognition, start your Amazon Rekognition Video stream processor\. For more information, see [Overview of Amazon Rekognition Video stream processor operations](streaming-video.md#using-rekognition-video-stream-processor)\. 