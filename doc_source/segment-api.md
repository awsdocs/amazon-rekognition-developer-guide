# Using the Amazon Rekognition Segment API<a name="segment-api"></a>

Amazon Rekognition Video segment detection in stored videos is an Amazon Rekognition Video asynchronous operation\. The Amazon Rekognition Segment API is a composite API where you choose the type of analysis \(technical cues or shot detection\) from a single API call\. For information about calling asynchronous operations, see [Calling Amazon Rekognition Video operations](api-video.md)\.

**Topics**
+ [Starting segment analysis](#segment-api-start)
+ [Getting segment analysis results](#segment-api-get)

## Starting segment analysis<a name="segment-api-start"></a>

To start the detection of segments in a stored video call [ StartSegmentDetection ](API_StartSegmentDetection.md)\. The input parameters are the same as other Amazon Rekognition Video operations with the addition of segment type selection and result filtering\. For more information, see [Starting video analysis](api-video.md#api-video-start)\.

The following is example JSON passed by `StartSegmentDetection`\. The request specifies that both technical cue and shot detection segments are detected\. Different filters for the minimum detection confidence are requested for technical cue segments \(90%\) and shot detection segments \(80%\)\.

```
{
  "Video": {
    "S3Object": {
      "Bucket": "test_files",
      "Name": "test_file.mp4"
    }
    "SegmentTypes":["TECHNICAL_CUES", "SHOT"]
    "Filters": {
      "TechnicalCueFilter": {
         "MinSegmentConfidence": 90,
         "BlackFrame" : {
            "MaxPixelThreshold": 0.1,
            "MinCoveragePercentage": 95     
         }
      },
      "ShotFilter" : {
          "MinSegmentConfidence": 60
      }
  }
}
```

### Choosing a segment type<a name="segment-feature-type"></a>

Use the `SegmentTypes` array input parameter to detect technical cue and/or shot detection segments in the input video\. 
+ TECHNICAL\_CUE — identifies frame\-accurate timestamps for the start, end, and duration of technical cues \(black frames, color bars, opening credits, end credits, studio logos, and primary program content\) detected in a video\. For example, you can use technical cues to find the start of the end credits\. For more information, see [Technical cues](segments.md#segment-technical-cue)\.
+ SHOT — Identifies the start, end, and duration of a shot\. For example, you can use shot detection to identify candidate shots for a final edit of a video\. For more information, see [Shot detection](segments.md#segment-shot-detection)\.

### Filtering the analysis results<a name="w93aac44c29b7c11"></a>

You can use the `Filters` \([ StartSegmentDetectionFilters ](API_StartSegmentDetectionFilters.md)\) input parameter to specify the minimum detection confidence returned in the response\. Within `Filters`, use `ShotFilter` \([ StartShotDetectionFilter ](API_StartShotDetectionFilter.md)\) to filter detected shots\. Use `TechnicalCueFilter` \([ StartTechnicalCueDetectionFilter ](API_StartTechnicalCueDetectionFilter.md)\) to filter technical cues\. 

For example code, see [Example: Detecting segments in a stored video](segment-example.md)\.

## Getting segment analysis results<a name="segment-api-get"></a>

Amazon Rekognition Video publishes the completion status of the video analysis to an Amazon Simple Notification Service topic\. If the video analysis is successful, call [ GetSegmentDetection ](API_GetSegmentDetection.md) to get results of the video analysis\. 

The following is an example `GetSegmentDetection` request\. The `JobId` is the job identifier returned from the call to `StartSegmentDetection`\. For information about the other input parameters, see [Getting Amazon Rekognition Video analysis results](api-video.md#api-video-get)\. 

```
{
    "JobId": "270c1cc5e1d0ea2fbc59d97cb69a72a5495da75851976b14a1784ca90fc180e3",
    "MaxResults": 10,
    "NextToken": "XfXnZKiyMOGDhzBzYUhS5puM+g1IgezqFeYpv/H/+5noP/LmM57FitUAwSQ5D6G4AB/PNwolrw=="
}
```

`GetSegmentDetection` returns results for the requested analysis and general information about the stored video\. 

### General information<a name="segment-api-general"></a>

`GetSegmentDection` returns the following general information\.
+ **Audio information** — The response includes audio metadata in an array, `AudioMetadata`, of [ AudioMetadata ](API_AudioMetadata.md) objects\. There can be multiple audio streams\. Each `AudioMetadata` object contains metadata for a single audio stream\. Audio information in an `AudioMetadata` objects includes the audio codec, the number of audio channels, the duration of the audio stream, and the sample rate\. Audio metadata is returned in each page of information returned by `GetSegmentDetection`\.
+ **Video information** – Currently, Amazon Rekognition Video returns a single [ VideoMetadata ](API_VideoMetadata.md) object in the `VideoMetadata` array\. The object contains information about the video stream in the input file that Amazon Rekognition Video chose to analyze\. The `VideoMetadata` object includes the video codec, video format and other information\. Video metadata is returned in each page of information returned by `GetSegmentDetection`\.
+ **Paging information** – The example shows one page of segment information\. You can specify how many elements to return in the `MaxResults` input parameter for `GetSegmentDetection`\. If more results than `MaxResults` exist, `GetSegmentDetection` returns a token \(`NextToken`\) used to get the next page of results\. For more information, see [Getting Amazon Rekognition Video analysis results](api-video.md#api-video-get)\.
+ **Request information** – The type of analysis requested in the call to `StartSegmentDetection` is returned in the `SelectedSegmentTypes` field\.

### Segments<a name="segment-api-technical-segments"></a>

Technical cues and shot information detected in a video is returned in an array, `Segments`, of [ SegmentDetection ](API_SegmentDetection.md) objects\. The array is sorted by the segment types \(TECHNICAL\_CUE or SHOT\) specified in the `SegmentTypes` input parameter of `StartSegmentDetection`\. Within each segment type the array is sorted by timestamp values\. Each `SegmentDetection` object includes information about the type of detected segment \(Technical cue or shot detection\) and general information, such as the start time, end time, and the duration of the segment\. 

Time information is returned in three formats\.
+ 

**Milliseconds**  
The number of milliseconds since the start of the video\. The fields `DurationMillis`, `StartTimestampMillis`, and `EndTimestampMillis` are in millisecond format\.
+ 

**Timecode**  
Amazon Rekognition Video timecodes are in [SMPTE](https://en.wikipedia.org/wiki/SMPTE_timecode) format where each frame of video has a unique timecode value\. The format is *hh:mm:ss:frame*\. For example, a timecode value of 01:05:40:07, would be read as one hour, five minutes, forty seconds and seven frames\. [Drop frame](https://en.wikipedia.org/wiki/SMPTE_timecode#Drop-frame_timecode) rate use cases are supported by Amazon Rekognition Video\. The drop rate timecode format is *hh:mm:ss;frame*\. The fields `DurationSMPTE`, `StartTimecodeSMPTE`, and `EndTimecodeSMPTE` are in timecode format\.
+ 

**Frame Counters**  
The duration of each video segment is also expressed with the number of frames\. The field `StartFrameNumber` gives the frame number at the start of a video segment, and `EndFrameNumber` gives the frame number at the end of a video segment\. `DurationFrames` gives the total number of frames in a video segment\. These values are calculated using a frame index that starts with 0\.

You can use the `SegmentType` field to determine the type of a segment returned by Amazon Rekognition Video\.
+ **Technical Cues** – the `TechnicalCueSegment` field is an [ TechnicalCueSegment ](API_TechnicalCueSegment.md) object that contains the detection confidence and the type of a technical cue\. The types of technical cue are `ColorBars`, `EndCredits`, `BlackFrames`, `OpeningCredits`, `StudioLogo`, `Slate`, and `Content`\.
+ **Shot** – the `ShotSegment` field is a [ ShotSegment ](API_ShotSegment.md) object than contains the detection confidence and an identifier for the shot segment within the video\.

 The following example is the JSON response from `GetSegmentDetection`\. 

```
{
    "SelectedSegmentTypes": [
        {
            "ModelVersion": "2.0",
            "Type": "SHOT"
        },
        {
            "ModelVersion": "2.0",
            "Type": "TECHNICAL_CUE"
        }
    ],
    "Segments": [
        {
            "DurationFrames": 299,
            "DurationSMPTE": "00:00:09;29",
            "StartFrameNumber": 0,
            "EndFrameNumber": 299,
            "EndTimecodeSMPTE": "00:00:09;29",
            "EndTimestampMillis": 9976,
            "StartTimestampMillis": 0,
            "DurationMillis": 9976,
            "StartTimecodeSMPTE": "00:00:00;00",
            "Type": "TECHNICAL_CUE",
            "TechnicalCueSegment": {
                "Confidence": 90.45006561279297,
                "Type": "BlackFrames"
            }
        },
        {
            "DurationFrames": 150,
            "DurationSMPTE": "00:00:05;00",
            "StartFrameNumber": 299,
            "EndFrameNumber": 449,
            "EndTimecodeSMPTE": "00:00:14;29",
            "EndTimestampMillis": 14981,
            "StartTimestampMillis": 9976,
            "DurationMillis": 5005,
            "StartTimecodeSMPTE": "00:00:09;29",
            "Type": "TECHNICAL_CUE",
            "TechnicalCueSegment": {
                "Confidence": 100.0,
                "Type": "Content"
            }
        },
        {
            "DurationFrames": 299,
            "ShotSegment": {
                "Index": 0,
                "Confidence": 99.9982681274414
            },
            "DurationSMPTE": "00:00:09;29",
            "StartFrameNumber": 0,
            "EndFrameNumber": 299,
            "EndTimecodeSMPTE": "00:00:09;29",
            "EndTimestampMillis": 9976,
            "StartTimestampMillis": 0,
            "DurationMillis": 9976,
            "StartTimecodeSMPTE": "00:00:00;00",
            "Type": "SHOT"
        },
        {
            "DurationFrames": 149,
            "ShotSegment": {
                "Index": 1,
                "Confidence": 99.9982681274414
            },
            "DurationSMPTE": "00:00:04;29",
            "StartFrameNumber": 300,
            "EndFrameNumber": 449,
            "EndTimecodeSMPTE": "00:00:14;29",
            "EndTimestampMillis": 14981,
            "StartTimestampMillis": 10010,
            "DurationMillis": 4971,
            "StartTimecodeSMPTE": "00:00:10;00",
            "Type": "SHOT"
        }
    ],
    "JobStatus": "SUCCEEDED",
    "VideoMetadata": [
        {
            "Format": "QuickTime / MOV",
            "FrameRate": 29.970029830932617,
            "Codec": "h264",
            "DurationMillis": 15015,
            "FrameHeight": 1080,
            "FrameWidth": 1920,
            "ColorRange": "LIMITED"

        }
    ],
    "AudioMetadata": [
        {
            "NumberOfChannels": 1,
            "SampleRate": 48000,
            "Codec": "aac",
            "DurationMillis": 15007
        }
    ]
}
```

For example code, see [Example: Detecting segments in a stored video](segment-example.md)\.