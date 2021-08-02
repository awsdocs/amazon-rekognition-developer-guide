# Detecting labels in a video<a name="labels-detecting-labels-video"></a>

Amazon Rekognition Video can detect labels, and the time a label is detected, in a video\. For an SDK code example, see [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md)\. For an AWS CLI example, see [Analyzing a video with the AWS Command Line Interface](video-cli-commands.md)\.

Amazon Rekognition Video label detection is an asynchronous operation\. To start the detection of labels in a video, call [StartLabelDetection](API_StartLabelDetection.md)\. Amazon Rekognition Video publishes the completion status of the video analysis to an Amazon Simple Notification Service topic\. If the video analysis is succesful, call [GetLabelDetection](API_GetLabelDetection.md) to get the detected labels\. For information about calling the video analysis API operations, see [Calling Amazon Rekognition Video operations](api-video.md)\. 

## GetLabelDetection operation response<a name="getlabeldetection-operation-response"></a>

`GetLabelDetection` returns an array \(`Labels`\) that contains information about the labels detected in the video\. The array can be sorted either by time or by the label detected by specifying the `SortBy` parameter\.

The following example is the JSON response of the `GetLabelDetection`\. In the response, note the following:
+ **Sort order** – The array of labels returned is sorted by time\. To sort by label, specify `NAME` in the `SortBy` input parameter for `GetLabelDetection`\. If the label appears multiple times in the video, there will be multiples instances of the \([LabelDetection](API_LabelDetection.md)\) element\. 
+ **Label information** – The `LabelDetection` array element contains a \([Label](API_Label.md)\) object which contains the label name and the confidence Amazon Rekognition has in the accuracy of the detected label\. A `Label` object also includes a hierarchical taxonomy of labels and bounding box information for common labels\. `Timestamp` is the time, in milliseconds from the start of the video, that the label was detected\. 
+ **Paging information** – The example shows one page of label detection information\. You can specify how many `LabelDetection` objects to return in the `MaxResults` input parameter for `GetLabelDetection`\. If more results than `MaxResults` exist, `GetLabelDetection` returns a token \(`NextToken`\) used to get the next page of results\. For more information, see [Getting Amazon Rekognition Video analysis results](api-video.md#api-video-get)\.
+ **Video information** – The response includes information about the video format \(`VideoMetadata`\) in each page of information returned by `GetLabelDetection`\.

```
{
    "Labels": [
        {
            "Timestamp": 0,
            "Label": {
                "Instances": [],
                "Confidence": 60.51791763305664,
                "Parents": [],
                "Name": "Electronics"
            }
        },
        {
            "Timestamp": 0,
            "Label": {
                "Instances": [],
                "Confidence": 99.53411102294922,
                "Parents": [],
                "Name": "Human"
            }
        },
        {
            "Timestamp": 0,
            "Label": {
                "Instances": [
                    {
                        "BoundingBox": {
                            "Width": 0.11109819263219833,
                            "Top": 0.08098889887332916,
                            "Left": 0.8881205320358276,
                            "Height": 0.9073750972747803
                        },
                        "Confidence": 99.5831298828125
                    },
                    {
                        "BoundingBox": {
                            "Width": 0.1268676072359085,
                            "Top": 0.14018426835536957,
                            "Left": 0.0003282368124928324,
                            "Height": 0.7993982434272766
                        },
                        "Confidence": 99.46029663085938
                    }
                ],
                "Confidence": 99.53411102294922,
                "Parents": [],
                "Name": "Person"
            }
        },
        .
        .   
        .

        {
            "Timestamp": 166,
            "Label": {
                "Instances": [],
                "Confidence": 73.6471176147461,
                "Parents": [
                    {
                        "Name": "Clothing"
                    }
                ],
                "Name": "Sleeve"
            }
        }
        
    ],
    "LabelModelVersion": "2.0",
    "JobStatus": "SUCCEEDED",
    "VideoMetadata": {
        "Format": "QuickTime / MOV",
        "FrameRate": 23.976024627685547,
        "Codec": "h264",
        "DurationMillis": 5005,
        "FrameHeight": 674,
        "FrameWidth": 1280
    }
}
```