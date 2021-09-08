# Detecting personal protective equipment<a name="ppe-detection"></a>

Amazon Rekognition can detect Personal Protective Equipment \(PPE\) worn by persons in an image\. You can use this information to improve workplace safety practices\. For example, you can use PPE detection to help determine if workers on a construction site are wearing head covers, or if medical workers are wearing face covers and hand covers\. The following image shows some of the types of PPE that can detected\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/worker-with-bb.png)

To detect PPE in an image you call the [ DetectProtectiveEquipment ](API_DetectProtectiveEquipment.md) API and pass an input image\. The response is a JSON structure that includes the following\.
+ The persons detected in the image\.
+ The parts of a body where where PPE is worn \(face, head, left\-hand, and right\-hand\)\.
+ The types of PPE detected on body parts \(face cover, hand cover, and head cover\)\. 
+ For items of detected PPE, an indicator for whether or not the PPE covers the corresponding body part\.

Bounding boxes are returned for the locations of persons and items of PPE detected in the image\. 

Optionally, you can request a summary of the PPE items and persons detected in an image\. For more information, see [Summarizing PPE detected in an image](#ppe-summarization)\. 

**Note**  
Amazon Rekognition PPE detection doesn't perform facial recognition or facial comparison and can’t identify the detected persons\. 

## Types of PPE<a name="ppe-types"></a>

[ DetectProtectiveEquipment ](API_DetectProtectiveEquipment.md) detects the following types of PPE\. If you want to detect other types of PPE in images, consider using Amazon Rekognition Custom Labels to train a custom model\. For more information, see [Amazon Rekognition Custom Labels](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/what-is.html)\.

### Face cover<a name="ppe-face-cover"></a>

`DetectProtectiveEquipment` can detect common face covers such as surgical, N95, and masks made of cloth\. 

### Hand cover<a name="ppe-hand-cover"></a>

`DetectProtectiveEquipment` can detect hand covers such as surgical gloves and safety gloves\. 

### Head cover<a name="ppe-head-cover"></a>

`DetectProtectiveEquipment` can detect hard hats and helmets\. 

The API indicates that a head, hand, or face cover was detected in an image\. The API doesn't return information about the type of a specific cover\. For example, 'surgical glove' for the type of a hand cover\. 

## PPE detection confidence<a name="ppe-confidence"></a>

Amazon Rekognition makes a prediction about the presence of PPE, persons, and body parts in an image\. The API provides a score \(50\-100\) that indicates how confident Amazon Rekognition is in the accuracy of a prediction\. 

**Note**  
If you plan to use the `DetectProtectiveEquipment` operation to make a decision that impacts an individual's rights, privacy, or access to services we recommend that you pass the result to a human for review and validation before taking action\. 

## Summarizing PPE detected in an image<a name="ppe-summarization"></a>

You can optionally request a summary of the PPE items and persons detected in an image\. You can specify a list of required protective equipment \(face cover, hand cover, or head cover\) and a minimum confidence threshold \(for example, 80%\)\. The response includes a consolidated per\-image identifier \(ID\) summary of persons with the required PPE, persons without the required PPE, and persons where a determination couldn't be made\. 

The summary allows you to quickly answer questions such as *How many persons are not wearing face covers?* or *Is everyone wearing PPE?* Each detected person in the summary has a unique ID\. You can use the ID find out information such as the bounding box location of a person not wearing PPE\. 

**Note**  
The ID is randomly generated on a per\-image analysis basis and is not consistent across images or multiple analyses of the same image\.

You can summarize face covers, head covers, hand covers, or a combination of your choice\. To specify the required types of PPE, see [Specifying summarization requirements](ppe-request-response.md#ppe-summarization-input-parameters)\. You can also specify a minimum confidence level \(50\-100\) that must be met for detections to be included in the summary\. 

 For more information about the summarization response from `DetectProtectiveEquipment`, see [Understanding the DetectProtectiveEquipment response](ppe-request-response.md#detect-protective-equipment-response)\.

## Tutorial: Creating a AWS Lambda function that detects images with PPE<a name="ppe-tutorial-lambda"></a>

You can create an AWS Lambda function that detects personal protective equipment \(PPE\) in images located in an Amazon S3 bucket\. See the [AWS Documentation SDK examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/javav2/usecases/creating_lambda_ppe) for this Java V2 tutorial\.