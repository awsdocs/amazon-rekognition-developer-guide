# Using the Amazon Rekognition Segment API<a name="segment-api"></a>

Amazon Rekognition Video segment detection in stored videos is an Amazon Rekognition Video asynchronous operation\. The Amazon Rekognition Segment API is a composite API where you choose the type of analysis \(technical cues or shot detection\) from a single API call\. For information about calling asynchronous operations, see [Calling Amazon Rekognition Video operations](api-video.md)\.

**Topics**
+ [Starting segment analysis](#segment-api-start)
+ [Getting segment analysis results](#segment-api-get)

## Starting segment analysis<a name="segment-api-start"></a>

To start the detection of segments in a stored video call [StartSegmentDetection](API_StartSegmentDetection.md)\. The input parameters are the same as other Amazon Rekognition Video operations with the addition of segment type selection and result filtering\. For more information, see [Starting video analysis](api-video.md#api-video-start)\.

The following is example JSON passed by `StartSegmentDetection`\. The request specifies that both technical cue and shot detection segments are detected\. Different filters for the minimum detection confidence are requested for technical cue segments \(90%\) and shot detection segments \(80%\)\.

```
{
    "Video": {
        "S3Object": {
            "Bucket": "test_files",
            "Name": "test_file.mp4"
        },
        "ClientRequestToken": "SegmentDetectionToken",
        "NotificationChannel": {
            "SNSTopicArn": "arn:aws:sns:us-east-1:111122223333:AmazonRekognitionSegmentationTopic",
            "RoleArn": "arn:aws:iam::111122223333:role/RekVideoServiceRole"
        },
        "JobTag": "SegmentingVideo",
        "SegmentTypes": [
            "TECHNICAL_CUE",
            "SHOT"
        ],
        "Filters": {
            "TechnicalCueFilter": {
                "MinSegmentConfidence": 90
            },
            "ShotFilter": {
                "MinSegmentConfidence": 80
            }
        }
    }
}
```

### Choosing a segment type<a name="segment-feature-type"></a>

Use the `SegmentTypes` array input parameter to detect technical cue and/or shot detection segments in the input video\. 
+ TECHNICAL\_CUE — identifies frame\-accurate timestamps for the start, end, and duration of technical cues \(end credits, color bars, and black bars\) detected in a video\. For example, you can use technical cues to find the start of the end credits\. For more information, see [Technical cues](segments.md#segment-technical-cue)\.
+ SHOT — Identifies the start, end, and duration of a shot\. For example, you can use shot detection to identify candidate shots for a final edit of a video\. For more information, see [Shot detection](segments.md#segment-shot-detection)\.

### Filtering the analysis results<a name="w68aac44c27b7c11"></a>

You can use the `Filters` \([StartSegmentDetectionFilters](API_StartSegmentDetectionFilters.md)\) input parameter to specify the minimum detection confidence returned in the response\. Within `Filters`, use `ShotFilter` \([StartShotDetectionFilter](API_StartShotDetectionFilter.md)\) to filter detected shots\. Use `TechnicalCueFilter` \([StartTechnicalCueDetectionFilter](API_StartTechnicalCueDetectionFilter.md)\) to filter technical cues\. 

For example code, see [Example: Detecting segments in a stored video](segment-example.md)\.

## Getting segment analysis results<a name="segment-api-get"></a>

Amazon Rekognition Video publishes the completion status of the video analysis to an Amazon Simple Notification Service topic\. If the video analysis is succesful, call [GetSegmentDetection](API_GetSegmentDetection.md) to get results of the video analysis\. 

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
+ **Audio information** — The response includes audio metadata in an array, `AudioMetadata`, of [AudioMetadata](API_AudioMetadata.md) objects\. There can be multiple audio streams\. Each `AudioMetadata` object contains metadata for a single audio stream\. Audio information in an `AudioMetadata` objects includes the audio codec, the number of audio channels, the duration of the audio stream, and the sample rate\. Audio metadata is returned in each page of information returned by `GetSegmentDetection`\.
+ **Video information** – Currently, Amazon Rekognition Video returns a single [VideoMetadata](API_VideoMetadata.md) object in the `VideoMetadata` array\. The object contains information about the video stream in the input file that Amazon Rekognition Video chose to analyze\. The `VideoMetadata` object includes the video codec, video format and other information\. Video metadata is returned in each page of information returned by `GetSegmentDetection`\.
+ **Paging information** – The example shows one page of segment information\. You can specify how many elements to return in the `MaxResults` input parameter for `GetSegmentDetection`\. If more results than `MaxResults` exist, `GetSegmentDetection` returns a token \(`NextToken`\) used to get the next page of results\. For more information, see [Getting Amazon Rekognition Video analysis results](api-video.md#api-video-get)\.
+ **Request information** – The type of analysis requested in the call to `StartSegmentDetection` is returned in the `SelectedSegmentTypes` field\.

### Segments<a name="segment-api-technical-segments"></a>

Technical cues and shot information detected in a video is returned in an array, `Segments`, of [SegmentDetection](API_SegmentDetection.md) objects\. The array is sorted by the segment types \(TECHNICAL\_CUE or SHOT\) specified in the `SegmentTypes` input parameter of `StartSegmentDetection`\. Within each segment type the array is sorted by timestamp values\. Each `SegmentDetection` object includes information about the type of detected segment \(Technical cue or shot detection\) and general information, such as the start time, end time, and the duration of the segment\. 

Time information is returned in two formats\.
+ 

**Milliseconds**  
The number of milliseconds since the start of the video\. The fields `DurationMillis`, `StartTimestampMillis`, and `EndTimestampMillis` are in millisecond format\.
+ 

**Timecode**  
Amazon Rekognition Video timecodes are in [SMPTE](https://en.wikipedia.org/wiki/SMPTE_timecode) format where each frame of video has a unique timecode value\. The format is *hh:mm:ss:frame*\. For example, a timecode value of 01:05:40:07, would be read as one hour, five minutes, forty seconds and seven frames\. [Drop frame](https://en.wikipedia.org/wiki/SMPTE_timecode#Drop-frame_timecode) rate use cases are supported by Amazon Rekognition Video\. The drop rate timecode format is *hh:mm:ss;frame*\. The fields `DurationSMPTE`, `StartTimecodeSMPTE`, and `EndTimecodeSMPTE` are in timecode format\.

You can use the `SegmentType` field to determine the type of a segment returned by Amazon Rekognition Video\.
+ **Technical Cues** – the `TechnicalCueSegment` field is an [TechnicalCueSegment](API_TechnicalCueSegment.md) object that contains the detection confidence and the type of a technical cue\. The types of technical cue are ColorBars, EndCredits, and BlackFrames\.
+ **Shot** – the `ShotSegment` field is a [ShotSegment](API_ShotSegment.md) object than contains the detection confidence and an identifier for the shot segment within the video\.

 The following example is the JSON response from `GetSegmentDetection`\. 

```
{
    "JobStatus": "SUCCEEDED",
    "VideoMetadata": [
        {
            "Codec": "h264",
            "DurationMillis": 478145,
            "Format": "QuickTime / MOV",
            "FrameRate": 24.0,
            "FrameHeight": 360,
            "FrameWidth": 636
        }
    ],
    "AudioMetadata": [
        {
            "Codec": "aac",
            "DurationMillis": 478214,
            "SampleRate": 44100,
            "NumberOfChannels": 2
        }
    ],
    "Segments": [
        {
            "Type": "TECHNICAL_CUE",
            "StartTimestampMillis": 121666,
            "EndTimestampMillis": 471333,
            "DurationMillis": 349667,
            "StartTimecodeSMPTE": "00:02:01:16",
            "EndTimecodeSMPTE": "00:07:51:08",
            "DurationSMPTE": "00:05:49:16",
            "TechnicalCueSegment": {
                "Type": "EndCredits",
                "Confidence": 84.85398864746094
            }
        },
        {
            "Type": "SHOT",
            "StartTimestampMillis": 0,
            "EndTimestampMillis": 29041,
            "DurationMillis": 29041,
            "StartTimecodeSMPTE": "00:00:00:00",
            "EndTimecodeSMPTE": "00:00:29:01",
            "DurationSMPTE": "00:00:29:01",
            "ShotSegment": {
                "Index": 0,
                "Confidence": 87.50452423095703
            }
        },
        {
            "Type": "SHOT",
            "StartTimestampMillis": 29083,
            "EndTimestampMillis": 225041,
            "DurationMillis": 195958,
            "StartTimecodeSMPTE": "00:00:29:02",
            "EndTimecodeSMPTE": "00:03:45:01",
            "DurationSMPTE": "00:03:15:23",
            "ShotSegment": {
                "Index": 1,
                "Confidence": 85.09957122802734
            }
        },
        {
            "Type": "SHOT",
            "StartTimestampMillis": 225083,
            "EndTimestampMillis": 305375,
            "DurationMillis": 80292,
            "StartTimecodeSMPTE": "00:03:45:02",
            "EndTimecodeSMPTE": "00:05:05:09",
            "DurationSMPTE": "00:01:20:07",
            "ShotSegment": {
                "Index": 2,
                "Confidence": 81.68130493164062
            }
        },
        {
            "Type": "SHOT",
            "StartTimestampMillis": 305416,
            "EndTimestampMillis": 325708,
            "DurationMillis": 20292,
            "StartTimecodeSMPTE": "00:05:05:10",
            "EndTimecodeSMPTE": "00:05:25:17",
            "DurationSMPTE": "00:00:20:07",
            "ShotSegment": {
                "Index": 3,
                "Confidence": 81.68130493164062
            }
        },
        {
            "Type": "SHOT",
            "StartTimestampMillis": 325750,
            "EndTimestampMillis": 355708,
            "DurationMillis": 29958,
            "StartTimecodeSMPTE": "00:05:25:18",
            "EndTimecodeSMPTE": "00:05:55:17",
            "DurationSMPTE": "00:00:29:23",
            "ShotSegment": {
                "Index": 4,
                "Confidence": 84.75640106201172
            }
        },
        {
            "Type": "SHOT",
            "StartTimestampMillis": 355750,
            "EndTimestampMillis": 380375,
            "DurationMillis": 24625,
            "StartTimecodeSMPTE": "00:05:55:18",
            "EndTimecodeSMPTE": "00:06:20:09",
            "DurationSMPTE": "00:00:24:15",
            "ShotSegment": {
                "Index": 5,
                "Confidence": 86.56631469726562
            }
        },
        {
            "Type": "SHOT",
            "StartTimestampMillis": 380416,
            "EndTimestampMillis": 460708,
            "DurationMillis": 80292,
            "StartTimecodeSMPTE": "00:06:20:10",
            "EndTimecodeSMPTE": "00:07:40:17",
            "DurationSMPTE": "00:01:20:07",
            "ShotSegment": {
                "Index": 6,
                "Confidence": 86.56631469726562
            }
        },
        {
            "Type": "SHOT",
            "StartTimestampMillis": 460750,
            "EndTimestampMillis": 470333,
            "DurationMillis": 9583,
            "StartTimecodeSMPTE": "00:07:40:18",
            "EndTimecodeSMPTE": "00:07:50:08",
            "DurationSMPTE": "00:00:09:14",
            "ShotSegment": {
                "Index": 7,
                "Confidence": 91.79395294189453
            }
        },
        {
            "Type": "SHOT",
            "StartTimestampMillis": 470375,
            "EndTimestampMillis": 478125,
            "DurationMillis": 7750,
            "StartTimecodeSMPTE": "00:07:50:09",
            "EndTimecodeSMPTE": "00:07:58:03",
            "DurationSMPTE": "00:00:07:18",
            "ShotSegment": {
                "Index": 8,
                "Confidence": 91.79395294189453
            }
        }
    ],
    "SelectedSegmentTypes": [
        {
            "Type": "SHOT",
            "ModelVersion": "1.0"
        },
        {
            "Type": "TECHNICAL_CUE",
            "ModelVersion": "1.0"
        }
    ]
}
```

For example code, see [Example: Detecting segments in a stored video](segment-example.md)\.