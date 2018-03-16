# Detecting Labels in a Video<a name="labels-detecting-labels-video"></a>

Rekognition Video can detect labels, and the time a label is detected, in a video\. For an AWS SDK for Java example, see [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md)\. For an AWS CLI example, see [Analyzing a Video with the AWS Command Line Interface](video-cli-commands.md)\.

Rekognition Video label detection is an asynchronous operation\. To start the detection of labels in a video, call [StartLabelDetection](API_StartLabelDetection.md)\. Rekognition Video publishes the completion status of the video analysis to an Amazon Simple Notification Service topic\. If the video analysis is succesful, call [GetLabelDetection](API_GetLabelDetection.md) to get the detected labels\.

For information about calling Rekognition Video operations, see [Calling Rekognition Video Operations](api-video.md)\. 

`GetLabelDetection` returns an array \(`Labels`\) that contains information about the labels detected in the video\. The array can be sorted either by time or by the label detected by specifying the `SortBy` parameter\. The following example is the JSON response of the `GetLabelDetection`\.

```
{
  "Labels": [{
    "Label": {
      "Confidence": 99.03720092773438,
      "Name": "Speech"
    },
    "Timestamp": 0
  }, {
    "Label": {
      "Confidence": 71.6698989868164,
      "Name": "Pumpkin"
    },
    "Timestamp": 0
  }, {
    "Label": {
      "Confidence": 71.6698989868164,
      "Name": "Squash"
    },
    "Timestamp": 0
  }, {
    "Label": {
      "Confidence": 71.6698989868164,
      "Name": "Vegetable"
    },
    "Timestamp": 0
  }, {
    "Label": {
      "Confidence": 71.44749450683594,
      "Name": "Clothing"
    },
    "Timestamp": 0
  }, {
    "Label": {
      "Confidence": 71.44749450683594,
      "Name": "Overcoat"
    },
    "Timestamp": 0
  }, {
    "Label": {
      "Confidence": 71.44749450683594,
      "Name": "Suit"
    },
    "Timestamp": 0
  }, {
    "Label": {
      "Confidence": 58.84939956665039,
      "Name": "Jar"
    },
    "Timestamp": 0
  }, {
    "Label": {
      "Confidence": 58.84939956665039,
      "Name": "Porcelain"
    },
    "Timestamp": 0
  }, {
    "Label": {
      "Confidence": 58.84939956665039,
      "Name": "Vase"
    },
    "Timestamp": 0
  }],
  "NextToken": "BgPXS37fNUY+Hrd7jYbBoTk1I5LevLm/MV+dhCwbXxoVOgMi0di6xYSeL6/Dztya/Pflx9xxxx==",
  "VideoMetadata": {
    "Codec": "h264",
    "DurationMillis": 67301,
    "Format": "mov,mp4,m4a,3gp,3g2,mj2",
    "FrameHeight": 1080,
    "FrameRate": 29.970029830932617,
    "FrameWidth": 1920
  }
}
```

In the response, note the following:

+ **Sort order** – The array of labels returned is sorted by time\. To sort by label, specify `NAME` in the `SortBy` input parameter for `GetLabelDetection`\. If the label appears multiple times in the video, there will be multiples instances of the \([LabelDetection](API_LabelDetection.md)\) element\. 

+ **Label information** – The `LabelDetection` array element contains a \([Label](API_Label.md)\) object which contains the label name and the confidence Amazon Rekognition has in the accuracy of the detected label\. `Timestamp` is the time, in milliseconds from the start of the video, that the label was detected\.

+ **Paging information** – The example shows one page of label detection information\. You can specify how many `LabelDetection` objects to return in the `MaxResults` input parameter for `GetLabelDetection`\. If more results than `MaxResults` exist, `GetLabelDetection` returns a token \(`NextToken`\) used to get the next page of results\. For more information, see [Getting Rekognition Video Analysis Results](api-video.md#api-video-get)\.

+ **Video information** – The response includes information about the video format \(`VideoMetadata`\) in each page of information returned by `GetLabelDetection`\.