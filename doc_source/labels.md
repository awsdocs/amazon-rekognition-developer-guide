# Detecting labels<a name="labels"></a>

This section provides information for detecting labels in images and videos with Amazon Rekognition Image and Amazon Rekognition Video\. 

 A label or a tag is an object, scene, action, or concept found in an image or video based on its contents\. For example, a photo of people on a tropical beach may contain labels such as Palm Tree \(object\), Beach \(scene\), Running \(action\), and Outdoors \(concept\)\. 

To download the full list of labels and object bounding boxes supported by Amazon Rekognition, click [here](https://d2t0jkte1sxko6.cloudfront.net/ed0429e3-38ec-439d-8f31-51e2381d91cc/AmazonRekognitionLabels_v2.0.zip)\.

**Note**  
Amazon Rekognition makes gender binary \(man, woman, girl, etc\.\) predictions based on the physical appearance of a person in a particular image\. This kind of prediction is not designed to categorize a person’s gender identity, and you shouldn't use Amazon Rekognition to make such a determination\. For example, a male actor wearing a long\-haired wig and earrings for a role might be predicted as female\.  
Using Amazon Rekognition to make gender binary predictions is best suited for use cases where aggregate gender distribution statistics need to be analyzed without identifying specific users\. For example, the percentage of users who are women compared to men on a social media platform\.  
We don't recommend using gender binary predictions to make decisions that impact an individual's rights, privacy, or access to services\.

Amazon Rekognition returns labels in English\. You can use [Amazon Translate](https://aws.amazon.com/translate/) to translate English labels into [other languages](https://docs.aws.amazon.com/translate/latest/dg/what-is.html#language-pairs)\.

## Bounding boxes and parent labels<a name="labels-details"></a>

Amazon Rekognition Image and Amazon Rekognition Video can return the bounding box for common object labels such as cars, furniture, apparel or pets\. Bounding box information isn't returned for less common object labels\. You can use bounding boxes to find the exact locations of objects in an image, count instances of detected objects, or to measure an object's size using bounding box dimensions\. 

Amazon Rekognition Image and Amazon Rekognition Video use a hierarchical taxonomy of ancestor labels to categorize labels\. For example, a person walking across a road might be detected as a *Pedestrian*\. The parent label for *Pedestrian* is *Person*\. Both of these labels are returned in the response\. All ancestor labels are returned and a given label contains a list of its parent and other ancestor labels\. For example, grandparent and great grandparent labels, if they exist\. You can use parent labels to build groups of related labels and to allow querying of similar labels in one or more images\. For example, a query for all *Vehicles* might return a car from one image and a motor bike from another\.

Amazon Rekognition Image and Amazon Rekognition Video both return the version of the label detection model used to detect labels in an image or stored video\.

For example, in the following image, Amazon Rekognition Image is able to detect the presence of a person, a skateboard, parked cars and other information\. Amazon Rekognition Image also returns the bounding box for a detected person, and other detected objects such as cars and wheels\. Amazon Rekognition Video and Amazon Rekognition Image also provide a percentage score for how much confidence Amazon Rekognition has in the accuracy of each detected label\. 

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/detect-scenes.jpg)

**Topics**