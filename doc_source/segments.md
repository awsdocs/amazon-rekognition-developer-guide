# Detecting video segments in stored video<a name="segments"></a>

Amazon Rekognition Video provides an API that identifies useful segments of video, such as black frames and end credits\. 

Viewers are watching more content than ever\. In particular, Over\-The\-Top \(OTT\) and Video\-On\-Demand \(VOD\) platforms provide a rich selection of content choices anytime, anywhere, and on any screen\. With proliferating content volumes, media companies are facing challenges in preparing and managing their content\. This is crucial to providing a high\-quality viewing experience and better monetizing content\. Today, companies use large teams of trained human workforces to perform tasks such as the following\.
+ Finding where the opening and end credits are in a piece of content
+ Choosing the right spots to insert advertisements, such as in silent black frame sequences
+ Breaking up videos into smaller clips for better indexing

These manual processes are expensive, slow, and can't scale to keep up with the volume of content that is produced, licensed, and retrieved from archives daily\.

You can use Amazon Rekognition Video to automate operational media analysis tasks using fully managed, purpose\-built video segment detection APIs powered by machine learning \(ML\)\. By using the Amazon Rekognition Video segment APIs, you can easily analyze large volumes of videos and detect markers such as black frames or shot changes\. You get SMPTE \(Society of Motion Picture and Television Engineers\) timecodes, timestamps, and frame numbers from each detection\. No ML experience is required\. 

Amazon Rekognition Video analyzes videos stored in an Amazon Simple Storage Service \(Amazon S3\) bucket\. The SMPTE timecodes that are returned are frame accurate – Amazon Rekognition Video provides the exact frame number of a detected segment of video, and handles various video frame rate formats automatically\. You can use the frame accurate metadata from Amazon Rekognition Video to automate certain tasks completely, or to significantly reduce the review workload of trained human operators, so that they can focus on more creative work\. You can perform tasks such as preparing content, inserting advertisements, and adding "binge\-markers" to content at scale in the cloud\. 

For information about pricing, see [Amazon Rekognition pricing](https://aws.amazon.com/rekognition/pricing/)\.

Amazon Rekognition Video segment detection supports two types of segmentation tasks — [Technical cues](#segment-technical-cue) detection and [Shot detection](#segment-shot-detection)\. 

**Topics**
+ [Technical cues](#segment-technical-cue)
+ [Shot detection](#segment-shot-detection)
+ [About the Amazon Rekognition Video Segment detection API](#segment-api-intro)
+ [Using the Amazon Rekognition Segment API](segment-api.md)
+ [Example: Detecting segments in a stored video](segment-example.md)

## Technical cues<a name="segment-technical-cue"></a>

A *technical cue* identifies black frames, color bars, opening credits, end credits, studio logos, and primary program content in a video\. 

### Black frames<a name="segment-black-frame"></a>

Videos often contain empty black frames with no audio that are used as cues to insert advertisements, or to mark the end of a program segment, such as a scene or opening credits\. With Amazon Rekognition Video, you can detect black frame sequences to automate ad insertion, package content for VOD, and demarcate various program segments or scenes\. Black frames with audio \(such as fade outs or voiceovers\) are considered as content and not returned\. 

### Credits<a name="segment-credits"></a>

Amazon Rekognition Video can automatically identify the exact frames where the opening and closing credits start and end for a movie or TV show\. With this information, you can generate "binge markers" or interactive viewer prompts, such as "Next Episode’"or "Skip Intro," in video on demand \(VOD\) applications\. You can also detect the first and last frame of program content in a video\. Amazon Rekognition Video is trained to handle a wide variety of opening and end credit styles ranging from simple rolling credits to more challenging credits alongside content\. 

### Color bars<a name="segment-color-bar"></a>

Amazon Rekognition Video allows you to detect sections of video that display SMPTE color bars, which are a set of colors displayed in specific patterns to ensure color is calibrated correctly on broadcast monitors, programs, and on cameras\. For more information about SMPTE color bars, see [SMPTE color bar](https://en.wikipedia.org/wiki/SMPTE_color_bars)\. This metadata is useful to prepare content for VOD applications by removing color bar segments from the content, or to detect issues such as loss of broadcast signals in a recording, when color bars are shown continuously as a default signal instead of content\.

### Slates<a name="segment-slates"></a>

Slates are sections of the video, typically near the beginning, that contain text metadata about the episode, studio, video format, audio channels, and more\. Amazon Rekognition Video can identify the start and end of slates, making it easy to use the text metadata or remove the slate when preparing content for final viewing\.

### Studio logos<a name="segment-logos"></a>

Studio logos are sequences that show the logos or emblems of the production studio involved in making the show\. Amazon Rekognition Video can detect these sequences so that users can review them to identify studios\.

### Content<a name="segment-content"></a>

Content is the portions of the TV show or movie that contain the program or related elements\. Black frames, credits, color bars, slates, and studio logos are not considered content\. Amazon Rekognition Video can detect the start and end of each content segment in the video, so you can find the program run time or specific segments\.

Content segments include, but are not limited to, the following:
+ Program scenes between two ad breaks
+ A quick recap of the previous episode at the beginning of the video
+ Bonus post\-credit content 
+ "Textless" content, such as a set of all program scenes that originally contained overlaid text, but where the text has been removed to support translation into other languages\.

After Amazon Rekognition Video finishes detecting all of the content segments, you can apply domain knowledge or send them for human review to further categorize each segment\. For example, if you use videos that always start with a recap, you could categorize the first content segment as a recap\.

The following diagram shows technical cue segments on a show or movie's timeline\. Note the color bars and opening credits, content segments such as the recap and main program, black frames throughout the video, and the end credits\. 

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/technical-cue.png)

## Shot detection<a name="segment-shot-detection"></a>

A shot is a series of interrelated consecutive pictures taken contiguously by a single camera and representing a continuous action in time and space\. With Amazon Rekognition Video, you can detect the start, end, and duration of each shot, as well as a count for all the shots in a piece of content\. You can use shot metadata for tasks such as the following\. 
+ Creating promotional videos using selected shots\.
+ Inserting advertisements in locations that don’t disrupt the viewer's experience, such as the middle of a shot when someone is speaking\. 
+ Generating a set of preview thumbnails that avoid transitional content between shots\.

A shot detection is marked at the exact frame where there is a hard cut to a different camera\. If there is a soft transition from one camera to another, Amazon Rekognition Video omits the transition\. This ensures that shot start and end times don’t include sections without actual content\.

The following diagram illustrates shot detection segments on a strip of film\. Note that each shot is identified by a cut from one camera angle or location to the next\. 

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/shot-detection.png)

## About the Amazon Rekognition Video Segment detection API<a name="segment-api-intro"></a>

To segment a stored video you use the asynchronous [StartSegmentDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartSegmentDetection.html) and [GetSegmentDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetSegmentDetection.html) API operations to start a segmentation job and fetch the results\. Segment detection accepts videos stored in an Amazon S3 bucket and returns a JSON output\. You can choose to detect only technical cues, only shot changes, or both together by configuring the `StartSegmentdetection` API request\. You can also filter detected segments by setting thresholds for a minimum prediction confidence\. For more information, see [Using the Amazon Rekognition Segment API ](segment-api.md)\. For example code, see [Example: Detecting segments in a stored video](segment-example.md)\. 