# Detecting Objects and Scenes<a name="labels"></a>

This section provides information for detecting labels in images and videos with Amazon Rekognition Image and Amazon Rekognition Video\. 

 A label or a tag is an object, scene, or concept found in an image or video based on its contents\. For example, a photo of people on a tropical beach may contain labels such as Person, Water, Sand, Palm Tree, and Swimwear \(objects\), Beach \(scene\), and Outdoors \(concept\)\. Amazon Rekognition Video can also detect activities such as a person skiing or riding a bike\. Amazon Rekognition Image does not detect activities in images\.

Amazon Rekognition Image and Amazon Rekognition Video can return the bounding box for common object labels such as people, cars, furniture, apparel or pets\. Bounding box information isn't returned for less common object labels\. You can use bounding boxes to find the exact locations of objects in an image, count instances of detected objects, or to measure an object's size using bounding box dimensions\. 

Amazon Rekognition Image and Amazon Rekognition Video use a hierarchical taxonomy of ancestor labels to categorize labels\. For example, a person walking across a road might be detected as a *Pedestrian*\. The parent label for *Pedestrian* is *Person*\. Both of these labels are returned in the response\. All ancestor labels are returned and a given label contains a list of its parent and other ancestor labels\. For example, grandparent and great grandparent labels, if they exist\. You can use parent labels to build groups of related labels and to allow querying of similar labels in one or more images\. For example, a query for all *Vehicles* might return a car from one image and a motor bike from another\.

Amazon Rekognition Image and Amazon Rekognition Video both return the version of the label detection model used to detect labels in an image or stored video\.

For example, in the following image, Amazon Rekognition Image is able to detect the presence of a person, a skateboard, parked cars and other information\. Amazon Rekognition Image also returns the bounding box for a detected person, and other detected objects such as cars and wheels\. Amazon Rekognition Video and Amazon Rekognition Image also provide a percentage score for how much confidence Amazon Rekognition has in the accuracy of each detected label\. 

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/detect-scenes.jpg)

**Topics**
+ [Detecting Labels in an Image](labels-detect-labels-image.md)
+ [Detecting Labels in a Video](labels-detecting-labels-video.md)