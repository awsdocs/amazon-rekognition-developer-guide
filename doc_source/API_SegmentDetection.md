# SegmentDetection<a name="API_SegmentDetection"></a>

A technical cue or shot detection segment detected in a video\. An array of `SegmentDetection` objects containing all segments detected in a stored video is returned by [GetSegmentDetection](API_GetSegmentDetection.md)\. 

## Contents<a name="API_SegmentDetection_Contents"></a>

 **DurationMillis**   <a name="rekognition-Type-SegmentDetection-DurationMillis"></a>
The duration of the detected segment in milliseconds\.   
Type: Long  
Valid Range: Minimum value of 0\.  
Required: No

 **DurationSMPTE**   <a name="rekognition-Type-SegmentDetection-DurationSMPTE"></a>
The duration of the timecode for the detected segment in SMPTE format\.  
Type: String  
Required: No

 **EndTimecodeSMPTE**   <a name="rekognition-Type-SegmentDetection-EndTimecodeSMPTE"></a>
The frame\-accurate SMPTE timecode, from the start of a video, for the end of a detected segment\. `EndTimecode` is in *HH:MM:SS:fr* format \(and *;fr* for drop frame\-rates\)\.  
Type: String  
Required: No

 **EndTimestampMillis**   <a name="rekognition-Type-SegmentDetection-EndTimestampMillis"></a>
The end time of the detected segment, in milliseconds, from the start of the video\. This value is rounded down\.  
Type: Long  
Required: No

 **ShotSegment**   <a name="rekognition-Type-SegmentDetection-ShotSegment"></a>
If the segment is a shot detection, contains information about the shot detection\.  
Type: [ShotSegment](API_ShotSegment.md) object  
Required: No

 **StartTimecodeSMPTE**   <a name="rekognition-Type-SegmentDetection-StartTimecodeSMPTE"></a>
The frame\-accurate SMPTE timecode, from the start of a video, for the start of a detected segment\. `StartTimecode` is in *HH:MM:SS:fr* format \(and *;fr* for drop frame\-rates\)\.   
Type: String  
Required: No

 **StartTimestampMillis**   <a name="rekognition-Type-SegmentDetection-StartTimestampMillis"></a>
The start time of the detected segment in milliseconds from the start of the video\. This value is rounded down\. For example, if the actual timestamp is 100\.6667 milliseconds, Amazon Rekognition Video returns a value of 100 millis\.  
Type: Long  
Required: No

 **TechnicalCueSegment**   <a name="rekognition-Type-SegmentDetection-TechnicalCueSegment"></a>
If the segment is a technical cue, contains information about the technical cue\.  
Type: [TechnicalCueSegment](API_TechnicalCueSegment.md) object  
Required: No

 **Type**   <a name="rekognition-Type-SegmentDetection-Type"></a>
The type of the segment\. Valid values are `TECHNICAL_CUE` and `SHOT`\.  
Type: String  
Valid Values:` TECHNICAL_CUE | SHOT`   
Required: No

## See Also<a name="API_SegmentDetection_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/SegmentDetection) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/SegmentDetection) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/SegmentDetection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/SegmentDetection) 