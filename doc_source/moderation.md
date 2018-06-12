# Detecting Unsafe Content<a name="moderation"></a>

Amazon Rekognition can determine if an image or video contains explicit or suggestive adult content\. Rekognition Image provides the [DetectModerationLabels](API_DetectModerationLabels.md) operation to detect unsafe content in images\. Rekognition Video can be detect unsafe content asynchronously by using [StartContentModeration](API_StartContentModeration.md) and [GetContentModeration](API_GetContentModeration.md)\.

Amazon Rekognition uses a hierarchical taxonomy to label categories of explicit and suggestive content\. The two top\-level categories are *Explicit Nudity*, and *Suggestive*\. Each top\-level category has a number of second\-level categories\. 

[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/rekognition/latest/dg/moderation.html)

You determine the suitability of an image for your application\. For example, images of a suggestive nature might be acceptable, but images containing nudity might not\. To filter images, use the [ModerationLabel](API_ModerationLabel.md) labels array returned by `DetectModerationLabels` \(images\) and by `GetContentModeration` \(videos\)\.

The `ModerationLabel` array contains labels in the preceding categories and an estimated confidence in the accuracy of the recognized content\. A top\-level label is returned along with any second\-level labels that were identified\. For example, Rekognition may return “Explicit Nudity” with a high confidence score as a top\-level label\. That may be enough for your filtering needs, but if necessary, you can use the confidence score of a second\-level label, such as "Partial Nudity", to obtain more granular filtering\. For an example, see [Detecting Unsafe Images \(API\)](procedure-moderate-images.md)\.

**Note**  
Rekognition Unsafe Image Detection API is not an authority on, or in any way purports to be an exhaustive filter of, explicit and suggestive adult content\. Furthermore, the Unsafe Image Detection API does not detect whether an image includes illegal content \(such as child pornography\) or unnatural adult content\.

**Topics**
+ [Unsafe Image Detection](#moderate-images)
+ [Unsafe Video Detection](#moderate-video)
+ [Detecting Unsafe Images \(API\)](procedure-moderate-images.md)
+ [Detecting Unsafe Stored Videos \(SDK for Java\)](procedure-moderate-videos.md)

## Unsafe Image Detection<a name="moderate-images"></a>

 `DetectModerationLabels` can retrieve input images from an S3 bucket or you can provide them as image bytes\. The following example is the response from a call to `DetectModerationLabels`\.

```
{
"ModerationLabels": [
    {
        "Confidence": 99.24723052978516,
        "ParentName": "",
        "Name": "Explicit Nudity"
    },
    {
        "Confidence": 99.24723052978516,
        "ParentName": "Explicit Nudity",
        "Name": "Graphic Male Nudity"
    },
    {
        "Confidence": 88.25341796875,
        "ParentName": "Explicit Nudity",
        "Name": "Sexual Activity"
    }
]
}
```

The response includes the following:
+ **Unsafe Image Detection information** – The example shows a list of moderation labels for explicit or suggestive content found in the image\. The list includes the top\-level label and each second\-level label detected in the image\.

  **Label** – Each label has a name, an estimation of the confidence that Amazon Rekognition has that the label is accurate, and the name of its parent label\. The parent name for a top\-level label is `""`\.

  **Label confidence** – Each label has a confidence value between 0 and 100 that indicates the percentage confidence that Amazon Rekognition has that the label is correct\. You specify the required confidence level for a label to be returned in the response in the API operation request\.

## Unsafe Video Detection<a name="moderate-video"></a>

To detect suggestive and adult content in a video stored in an Amazon S3 bucket, you use [StartContentModeration](API_StartContentModeration.md) and [GetContentModeration](API_GetContentModeration.md)\. Analyzing videos stored in an Amazon S3 bucket is an asynchronous workflow\. For more information, see [Working with Stored Videos](video.md)\. For an example, see [ Detecting Unsafe Stored Videos \(SDK for Java\)](procedure-moderate-videos.md)\. The following is an example response from `GetContentModeration`\.

```
{
    "JobStatus": "SUCCEEDED",
    "ModerationLabels": [
        {
            "ModerationLabel": {
                "Confidence": 93.02153015136719,
                "Name": "Male Swimwear Or Underwear",
                "ParentName": "Suggestive"
            },
            "Timestamp": 0
        },
        {
            "ModerationLabel": {
                "Confidence": 93.02153015136719,
                "Name": "Suggestive",
                "ParentName": ""
            },
            "Timestamp": 0
        },
        {
            "ModerationLabel": {
                "Confidence": 98.29075622558594,
                "Name": "Male Swimwear Or Underwear",
                "ParentName": "Suggestive"
            },
            "Timestamp": 1000
        },
        {
            "ModerationLabel": {
                "Confidence": 98.29075622558594,
                "Name": "Suggestive",
                "ParentName": ""
            },
            "Timestamp": 1000
        },
        {
            "ModerationLabel": {
                "Confidence": 97.91191101074219,
                "Name": "Male Swimwear Or Underwear",
                "ParentName": "Suggestive"
            },
            "Timestamp": 1999
        }
    ],
    "NextToken": "w5xfYx64+QvCdGTidVVWtczKHe0JAcUFu2tJ1RgDevHRovJ+1xej2GUDfTMWrTVn1nwSMHi9",
    "VideoMetadata": {
        "Codec": "h264",
        "DurationMillis": 3533,
        "Format": "QuickTime / MOV",
        "FrameHeight": 1080,
        "FrameRate": 30,
        "FrameWidth": 1920
    }
}
```

The response from `GetContentModeration` is an array, `ModerationLabels`, of [ContentModerationDetection](API_ContentModerationDetection.md) objects\. The array contains an element for each time a moderation label is detected\. Within a `ContentModerationDetectionObject` object, [ModerationLabel](API_ModerationLabel.md) contains information for a detected item of suggestive or adult content\. `Timestamp` is the time, in milliseconds from the start of the video, when the label was detected\. The labels are organized hierarchically in the same manner as the moderation labels detected by image analysis\. For more information, see [Detecting Unsafe Content](#moderation)\.