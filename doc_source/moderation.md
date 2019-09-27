# Detecting Unsafe Content<a name="moderation"></a>

You can use Amazon Rekognition to determine if an image or stored video contains unsafe content, such as explicit adult content or violent content\.

You can use the image and video moderation APIs in a variety of use cases such as social media, online market places, and professional media\. By using Amazon Rekognition to detect unsafe content, you can reduce the need for human review of unsafe content\.

## Using the Image and Video Moderation APIs<a name="moderation-api"></a>

In the Amazon Rekognition Image API, you can use the [DetectModerationLabels](API_DetectModerationLabels.md) operation to detect unsafe content in images\. You can use the Amazon Rekognition Video API to detect unsafe content asynchronously by using the [StartContentModeration](API_StartContentModeration.md) and [GetContentModeration](API_GetContentModeration.md) operations\.

Amazon Rekognition uses a two\-level hierarchical taxonomy to label categories of unsafe content\. Each top\-level category has a number of second\-level categories\. 

[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/rekognition/latest/dg/moderation.html)

You determine the suitability of content for your application\. For example, images of a suggestive nature might be acceptable, but images containing nudity might not\. To filter images, use the [ModerationLabel](API_ModerationLabel.md) labels array that's returned by `DetectModerationLabels` \(images\) and by `GetContentModeration` \(videos\)\.

You can set the confidence threshold that Amazon Rekognition uses to detect unsafe content by specifying the `MinConfidence` input parameter\. Labels aren't returned for unsafe content that is detected with a lower confidence than `MinConfidence`\.

Specifying a value for `MinConfidence` that is less than 50% is likely to return a high number of false\-positive results\. We recommend that you use a value that is less than 50% only when detection with a lower precision is acceptable\. If you don't specify a value for `MinConfidence`, Amazon Rekognition returns labels for unsafe content that is detected with at least 50% confidence\. 

The `ModerationLabel` array contains labels in the preceding categories, and an estimated confidence in the accuracy of the recognized content\. A top\-level label is returned along with any second\-level labels that were identified\. For example, Amazon Rekognition might return “Explicit Nudity” with a high confidence score as a top\-level label\. That might be enough for your filtering needs\. However, if it's necessary, you can use the confidence score of a second\-level label \(such as "Graphic Male Nudity"\) to obtain more granular filtering\. For an example, see [Detecting Unsafe Images](procedure-moderate-images.md)\.

Amazon Rekognition Image and Amazon Rekognition Video both return the version of the moderation detection model that is used to detect unsafe content \(`ModerationModelVersion`\)\. 

**Note**  
Amazon Rekognition isn't an authority on, and doesn't in any way claim to be an exhaustive filter of, unsafe content\. Additionally, the image and video moderation APIs don't detect whether an image includes illegal content, such as child pornography\.