# Detecting Unsafe Content<a name="moderation"></a>

Amazon Rekognition can determine if an image or video contains explicit or suggestive adult content\. Amazon Rekognition Image provides the [DetectModerationLabels](API_DetectModerationLabels.md) operation to detect unsafe content in images\. Amazon Rekognition Video can detect unsafe content asynchronously by using [StartContentModeration](API_StartContentModeration.md) and [GetContentModeration](API_GetContentModeration.md)\.

Amazon Rekognition uses a hierarchical taxonomy to label categories of explicit and suggestive content\. The two top\-level categories are *Explicit Nudity*, and *Suggestive*\. Each top\-level category has a number of second\-level categories\. 

[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/rekognition/latest/dg/moderation.html)

You determine the suitability of an image for your application\. For example, images of a suggestive nature might be acceptable, but images containing nudity might not\. To filter images, use the [ModerationLabel](API_ModerationLabel.md) labels array returned by `DetectModerationLabels` \(images\) and by `GetContentModeration` \(videos\)\.

You can set the confidence threshold used by Amazon Rekognition to detect unsafe content by specifying the `MinConfidence` input parameter\. Labels for unsafe content detected with a lower confidence than `MinConfidence` are not returned\.

Specifying a value for `MinConfidence` that is less than 50% is likely to return a high number of false\-positive results\. We recommend you use a value that is less than 50% only when detection with a lower precision is acceptable\. If you don't specify a value for `MinConfidence`, Amazon Rekognition returns labels for unsafe content detected with at least 50% confidence\. 

The `ModerationLabel` array contains labels in the preceding categories and an estimated confidence in the accuracy of the recognized content\. A top\-level label is returned along with any second\-level labels that were identified\. For example, Rekognition may return “Explicit Nudity” with a high confidence score as a top\-level label\. That may be enough for your filtering needs, but if necessary, you can use the confidence score of a second\-level label, such as "Partial Nudity", to obtain more granular filtering\. For an example, see [Detecting Unsafe Images \(API\)](procedure-moderate-images.md)\.

Amazon Rekognition Image and Amazon Rekognition Video both return the version of the moderation detection model used to detect unsafe content \(`ModerationModelVersion`\)\. 

**Note**  
Rekognition Unsafe Image Detection API is not an authority on, or in any way purports to be an exhaustive filter of, explicit and suggestive adult content\. Furthermore, the Unsafe Image Detection API does not detect whether an image includes illegal content \(such as child pornography\) or unnatural adult content\.

**Topics**
+ [Detecting Unsafe Images \(API\)](procedure-moderate-images.md)
+ [Detecting Unsafe Stored Videos](procedure-moderate-videos.md)