# Moderating content<a name="moderation"></a>

You can use Amazon Rekognition to detect content that is inappropriate, unwanted, or offensive\. You can use Rekognition moderation APIs in social media, broadcast media, advertising, and e\-commerce situations to create a safer user experience, provide brand safety assurances to advertisers, and comply with local and global regulations\.

Today, many companies rely entirely on human moderators to review third\-party or user\-generated content, while others simply react to user complaints to take down offensive or inappropriate images, ads, or videos\. However, human moderators alone cannot scale to meet these needs at sufficient quality or speed, which leads to a poor user experience, high costs to achieve scale, or even a loss of brand reputation\. By using Rekognition for image and video moderation, human moderators can review a much smaller set of content, typically 1\-5% of the total volume, already flagged by machine learning\. This enables them to focus on more valuable activities and still achieve comprehensive moderation coverage at a fraction of their existing cost\. To set up human workforces and perform human review tasks, you can use Amazon Augmented AI, which is already integrated with Rekognition\.

**Topics**
+ [Using the image and video moderation APIs](#moderation-api)
+ [Detecting inappropriate images](procedure-moderate-images.md)
+ [Detecting inappropriate stored videos](procedure-moderate-videos.md)
+ [Reviewing inappropriate content with Amazon Augmented AI](a2i-rekognition.md)

## Using the image and video moderation APIs<a name="moderation-api"></a>

In the Amazon Rekognition Image API, you can use the [ DetectModerationLabels ](API_DetectModerationLabels.md) operation to detect inappropriate or offensive content in images\. You can use the Amazon Rekognition Video API to detect inappropriate content asynchronously by using the [ StartContentModeration ](API_StartContentModeration.md) and [ GetContentModeration ](API_GetContentModeration.md) operations\.

Amazon Rekognition uses a two\-level hierarchical taxonomy to label categories of inappropriate or offensive content\. Each top\-level category has a number of second\-level categories\. 

[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/rekognition/latest/dg/moderation.html)

You determine the suitability of content for your application\. For example, images of a suggestive nature might be acceptable, but images containing nudity might not\. To filter images, use the [ ModerationLabel ](API_ModerationLabel.md) labels array that's returned by `DetectModerationLabels` \(images\) and by `GetContentModeration` \(videos\)\.

You can set the confidence threshold that Amazon Rekognition uses to detect inappropriate content by specifying the `MinConfidence` input parameter\. Labels aren't returned for inappropriate content that is detected with a lower confidence than `MinConfidence`\.

Specifying a value for `MinConfidence` that is less than 50% is likely to return a high number of false\-positive results\. We recommend that you use a value that is less than 50% only when detection with a lower precision is acceptable\. If you don't specify a value for `MinConfidence`, Amazon Rekognition returns labels for inappropriate content that is detected with at least 50% confidence\. 

The `ModerationLabel` array contains labels in the preceding categories, and an estimated confidence in the accuracy of the recognized content\. A top\-level label is returned along with any second\-level labels that were identified\. For example, Amazon Rekognition might return “Explicit Nudity” with a high confidence score as a top\-level label\. That might be enough for your filtering needs\. However, if it's necessary, you can use the confidence score of a second\-level label \(such as "Graphic Male Nudity"\) to obtain more granular filtering\. For an example, see [Detecting inappropriate images](procedure-moderate-images.md)\.

Amazon Rekognition Image and Amazon Rekognition Video both return the version of the moderation detection model that is used to detect inappropriate content \(`ModerationModelVersion`\)\. 

**Note**  
Amazon Rekognition isn't an authority on, and doesn't in any way claim to be an exhaustive filter of, inappropriate or offensive content\. Additionally, the image and video moderation APIs don't detect whether an image includes illegal content, such as child pornography\.