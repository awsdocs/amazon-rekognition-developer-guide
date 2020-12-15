# Detecting video segments in stored video<a name="segments"></a>

Amazon Rekognition Video provides an easy to use API that identifies useful segments of video such as color bars and end credits\. 

Viewers are watching more content than ever\. In particular, Over\-The\-Top \(OTT\) and Video\-On\-Demand \(VOD\) platforms provide a rich selection of content choices anytime, anywhere, and on any screen\. With proliferating content volumes, media companies are facing challenges in preparing and managing their content\. This is crucial to providing a high\-quality viewing experience and better monetizing content\. Today, companies use large teams of trained human workforces to perform tasks such as the following\.
+ Finding where the end credits begin in a piece of content\.
+ Choosing the right spots to insert advertisments\.
+ Breaking up videos into smaller clips for better indexing\.

These manual processes are expensive, slow, and cannot scale to keep up with the volume of content being produced, licensed, and retrieved from archives daily\.

Amazon Rekognition Video makes it easy to automate these operational media analysis tasks by providing fully managed, purpose\-built APIs powered by Machine Learning \(ML\)\. By using the Amazon Rekognition Video segment APIs, you can easily analyze large volumes of videos and detect markers such as black frames or shot changes\. You get SMPTE \(Society of Motion Picture and Television Engineers\) timecodes and timestamps for each detection\. No machine learning experience is required\. Amazon Rekognition analyzes videos stored in an Amazon S3 bucket\. SMPTE timecodes returned by Amazon Rekognition Video are frame accurate – Amazon Rekognition Video provides the exact frame number of a detected segment of video, and handles various video frame rate formats\. You can use the frame accurate metadata from Amazon Rekognition Video, to automate certain tasks completely, or significantly reduce the review workload of trained human operators, so that they can focus on more creative work\. This enables you to perform tasks such as preparing content, inserting advertisements, and adding ‘binge\-markers’ to content at scale in the cloud\. 

For information about pricing, see [Amazon Rekognition pricing](https://aws.amazon.com/rekognition/pricing/)\.

Amazon Rekognition Video supports two types of segmentation tasks — [Technical cues](#segment-technical-cue) Detection and [Shot detection](#segment-shot-detection)\. 

**Topics**
+ [Technical cues](#segment-technical-cue)
+ [Shot detection](#segment-shot-detection)
+ [About the Amazon Rekognition Video API](#segment-api-intro)
+ [Using the Amazon Rekognition Segment API](segment-api.md)
+ [Example: Detecting segments in a stored video](segment-example.md)

## Technical cues<a name="segment-technical-cue"></a>

A technical cue identifies black frames, color bars, and end credits in a video\. 

### Black frames<a name="segment-black-frame"></a>

Videos often contain a short duration of empty black frames with no audio that are used as cues to insert advertisements, or to demarcate the end of a program segment such as a scene or the opening credits\. With Amazon Rekognition Video, you can detect such black frame sequences to automate ad insertion, package content for VOD, and demarcate various program segments or scenes\. Black frames with audio \(such as fade outs or voiceovers\) are considered as content and not returned\. 

### End credits<a name="segment-end-credits"></a>

Amazon Rekognition Video helps you automatically identify the exact frames where the closing credits start and end for a movie or TV show\. With this information, you can generate markers for interactive viewer prompts such as ‘Next Episode’ in VOD applications, or find out the last frame of program content in a video\. Amazon Rekognition Video is trained to handle a wide variety of end credit styles ranging from simple rolling credits to more challenging credits alongside content, and excludes opening credits automatically\. 

### Color bars<a name="segment-color-bar"></a>

Amazon Rekognition Video allows you to detect sections of video that display SMPTE color bars, which are a set of colors displayed in specific patterns to ensure color is calibrated correctly on broadcast monitors, programs, and on cameras\. For more information about SMPTE color bars, see [SMPTE color bar](https://en.wikipedia.org/wiki/SMPTE_color_bars)\. This metadata is useful to prepare content for VOD applications by removing color bar segments from the content, or to detect issues such as loss of broadcast signals in a recording, when color bars are shown continuously as a default signal instead of content\.

The following diagram illustrates technical cue segments on the timeline of a show or movie\. Note the color bars at the beginning, the black frames throughout the video, and the end credits at the end\. 

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/technical-cue.png)

## Shot detection<a name="segment-shot-detection"></a>

A shot is a series of interrelated consecutive pictures taken contiguously by a single camera and representing a continuous action in time and space\. With Amazon Rekognition Video, you can detect the start, end, and duration of each shot, as well as a count for all the shots in a piece of content\. You can use shot metadata for tasks such as the following\. 
+ Creating promotional videos using selected shots\.
+ Inserting advertisements in locations that don’t disrupt the viewer's experience, such as the middle of a shot when someone is speaking\. 
+ Generating a set of preview thumbnails that avoid transitional content between shots\.

A shot detection is marked at the exact frame where there is a hard cut to a different camera\. If there is a soft transition from one camera to another, Amazon Rekognition Video omits the transition\. This ensures that shot start and end times don’t include sections without actual content\.

The following diagram illustrates shot detection segments on a strip of film\. Note that each shot is identified by a cut from one camera angle or location to the next\. 

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/shot-detection.png)

## About the Amazon Rekognition Video API<a name="segment-api-intro"></a>

To segment a stored video you use the asynchronous [StartSegmentDetection](API_StartSegmentDetection.md) and [GetSegmentDetection](API_GetSegmentDetection.md) APIs to start a segmentation job and fetch the results\. Segment detection accepts videos stored in an Amazon S3 bucket and returns a JSON output\. You can can choose to detect only technical cues, only shot changes, or both together by configuring the `StartSegmentdetection` API request\. You can also filter detected segments by setting thresholds for a minimum prediction confidence\. For more information, see [Using the Amazon Rekognition Segment API ](segment-api.md)\. For example code, see [Example: Detecting segments in a stored video](segment-example.md)\. 