# Understanding the personal protective equipment detection API<a name="ppe-request-response"></a>

The following information describes the [DetectProtectiveEquipment](API_DetectProtectiveEquipment.md) API\. For example code, see [Detecting personal protective equipment in an image](ppe-procedure-image.md)\.

## Supplying an image<a name="detect-protective-equipment-request"></a>

You can provide the input image \(JPG or PNG format\) either as image bytes or reference an image stored in an Amazon S3 bucket\. 

We recommend using images where the person's face is facing the camera\.

If your input image isn't rotated to 0 degrees orientation, we recommend rotating it to 0 degrees orientation before submitting it to `DetectProtectiveEquipment`\. Images in JPG format might contain orientation information in Exchangeable image file format \(Exif\) metadata\. You can use this information to write code that rotates your image\. For more information, see [Exif version 2\.32](http://cipa.jp/std/documents/download_e.html?DC-008-Translation-2019-E)\. PNG format images don't contain image orientation information\. 

 To pass an image from an Amazon S3 bucket, use an IAM user with at least ``AmazonS3ReadOnlyAccess priviliges\. Use an IAM user user with `AmazonRekognitionFullAccess` priviliges to call `DetectProtectiveEquipment.` 

In the following example input JSON, the image is passed in an Amazon S3 bucket\. For more information, see [Working with images](images.md)\. The example requests a summary of all PPE types \(head cover, hand cover, and face cover\) with a minimum detection confidence \(`MinConfidence`\) of 80%\. You should specify a `MinConfidence` value that is between 50\-100% as `DetectProtectiveEquipment` returns predictions only where the detection confidence is between 50% \- 100%\. If you specify a value that is less than 50%, the results are the same specifying a value of 50%\. For more information, see [Specifying summarization requirements](#ppe-summarization-input-parameters)\.  

```
{
    "Image": {
        "S3Object": {
            "Bucket": "bucket",
            "Name": "worker.jpg"
        }
    },
    "SummarizationAttributes": {
        "MinConfidence": 80,
        "RequiredEquipmentTypes": [
            "FACE_COVER",
            "HAND_COVER",
            "HEAD_COVER"
        ]
    }
}
```

If you have a large collection of images to process, consider using [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/) to process calls to `DetectProtectiveEquipment` in batches in the background\. 

### Specifying summarization requirements<a name="ppe-summarization-input-parameters"></a>

You can optionally use the `SummarizationAttributes` \([ProtectiveEquipmentSummarizationAttributes](API_ProtectiveEquipmentSummarizationAttributes.md)\) input parameter to request summary information for the types of PPE detected in an image\.

To specify the types of PPE to summarize, use the `RequiredEquipmentTypes` array field\. In the array, include one or more of `FACE_COVER`, `HAND_COVER` or `HEAD_COVER`\. 

Use the `MinConfidence` field to specify a minimum detection confidence \(50\-100\)\. The summary doesn't include Persons, body parts, body part coverage, and items of PPE, detected with a confidence lower than `MinConfidence`\.

For information about the summary response from `DetectProtectiveEquipment`, see [Understanding the DetectProtectiveEquipment response](#detect-protective-equipment-response)\. 



## Understanding the DetectProtectiveEquipment response<a name="detect-protective-equipment-response"></a>

`DetectProtectiveEquipment` returns an array of persons detected in the input image\. For each person, information about detected body parts and detected items of PPE is returned\. The JSON for the following image of a worker wearing a head cover, hand cover, and a face cover is as follows\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/worker-with-bb.png)

In the JSON, note the following\.
+ **Detected Persons** – `Persons` is an array of persons detected on the image \(including persons not wearing PPE\)\. `DetectProtectiveEquipment` can detect PPE on up to 15 persons detected in an image\. Each [ProtectiveEquipmentPerson](API_ProtectiveEquipmentPerson.md) object in the array contains a person ID, a bounding box for the person, detected body parts, and detected items of PPE\. The value of `Confidence` in `ProtectiveEquipmentPerson` indicates the percentage confidence that Amazon Rekognition has that the bounding box contains a person\.
+ **Body Parts** – `BodyParts` is an array of body parts \([ProtectiveEquipmentBodyPart](API_ProtectiveEquipmentBodyPart.md)\) detected on a person \(including body parts not covered by PPE\)\. Each `ProtectiveEquipmentBodyPart` includes the name \(`Name`\) of the detected body part\. `DetectProtectEquipment` can detect face, head, left\-hand, and right\-hand body parts\. The `Confidence` field in `ProtectiveEquipmentBodyPart` indicates the percentage confidence that Amazon Rekognition has in the detection accuracy of the body part\. 
+ **PPE Items** – The array `EquipmentDetections` in an `ProtectiveEquipmentBodyPart` object contains an array of detected PPE items\. Each [EquipmentDetection](API_EquipmentDetection.md) object contains the following fields\. 
  +  `Type` – The type of the detected PPE\.
  + `BoundingBox` – a bounding box around the detected PPE\.
  + `Confidence` – The confidence Amazon Rekognition has that the bounding box contains the detected PPE\.
  + `CoversBodyPart` – Indicates if the detected PPE is on the corresponding body part\.

  The [CoversBodyPart](API_CoversBodyPart.md) field `Value` is a boolean value that indicates if the detected PPE is on the corresponding body part\. The field `Confidence` indicates the confidence in the prediction\. You can use `CoversBodyPart` to filter out cases where the detected PPE is in the image, but not actually on the person\. 
**Note**  
`CoversBodyPart` doesn't indicate, or imply, that the person is adequately protected by the protective equipment or that the protective equipment itself is properly worn\. 
+ **Summary Information** – `Summary` contains the summary information specified in the `SummarizationAttributes` input parameter\. For more information, see [Specifying summarization requirements](#ppe-summarization-input-parameters)\.

  `Summary` is an object of type [ProtectiveEquipmentSummary](API_ProtectiveEquipmentSummary.md) which contains the following information\.
  + `PersonsWithRequiredEquipment` – An array of the IDs of persons where each person meets the following criteria\.
    + The person is wearing all of the PPE specified in the `SummarizationAttributes` input parameter\. 
    + The `Confidence` for the person \(`ProtectiveEquipmentPerson`\), body part \(`ProtectiveEquipmentBodyPart`\), protective equipment \(`EquipmentDetection`\) is equal to or greater than the specified minimum confidence threshold \(`MinConfidence`\)\.
    + The value of `CoversBodyPart` for all items of PPE is true\. 
  + `PersonsWithoutRequiredEquipment` – An array of the IDs of persons that meet one of the following criteria\. 
    + The `Confidence` value for the person \(`ProtectiveEquipmentPerson`\), body part \(`ProtectiveEquipmentBodyPart`\), and body part coverage \(`CoversBodyPart`\) are greater than the specified minimum confidence threshold \(`MinConfidence`\), but the person is missing one or more specified PPE \(`SummarizationAttributes`\)\.
    + The value of `CoversBodyPart` is false for any specified PPE \(`SummarizationAttributes`\) that has a `Confidence` value greater than the specified minimum confidence threshold \(`MinConfidence`\)\. The person also has all the specified PPE \(`SummarizationAttributes`\) and the `Confidence` values for person \(`ProtectiveEquipmentPerson`\), body part \(`ProtectiveEquipmentBodyPart`\), and protective equipment \(`EquipmentDetection`\) are greater than or equal to the minimum confidence threshold \(`MinConfidence`\.
  + `PersonsIndeterminate` – An array of the IDs of persons detected where the `Confidence` value for the person \(`ProtectiveEquipmentPerson`\), body part \(`ProtectiveEquipmentBodyPart`\), protective equipment \(`EquipmentDetection`\), or `CoversBodyPart` boolean is lower than specified minimum confidence threshold \(`MinConfidence`\)\. 

  Use the array size to get a count for a particular summary\. For example, the size of `PersonsWithRequiredEquipment` tells you the number of people detected as wearing the specified type of PPE\.

  You can use the person ID to find out further information about a person, such as the bounding box location of the person\. The person ID maps to the ID field of a `ProtectiveEquipmentPerson`\) object returned in `Persons` \(array of`ProtectiveEquipmentPerson`\)\. You can then get the Bounding box and other information from the corresponding `ProtectiveEquipmentPerson` object\. 

```
 {
    "ProtectiveEquipmentModelVersion": "1.0",
    "Persons": [
        {
            "BodyParts": [
                {
                    "Name": "FACE",
                    "Confidence": 99.99861145019531,
                    "EquipmentDetections": [
                        {
                            "BoundingBox": {
                                "Width": 0.14528800547122955,
                                "Height": 0.14956723153591156,
                                "Left": 0.4363413453102112,
                                "Top": 0.34203192591667175
                            },
                            "Confidence": 99.90001678466797,
                            "Type": "FACE_COVER",
                            "CoversBodyPart": {
                                "Confidence": 98.0676498413086,
                                "Value": true
                            }
                        }
                    ]
                },
                {
                    "Name": "LEFT_HAND",
                    "Confidence": 96.9786376953125,
                    "EquipmentDetections": [
                        {
                            "BoundingBox": {
                                "Width": 0.14495663344860077,
                                "Height": 0.12936046719551086,
                                "Left": 0.5114737153053284,
                                "Top": 0.5744519829750061
                            },
                            "Confidence": 83.72270965576172,
                            "Type": "HAND_COVER",
                            "CoversBodyPart": {
                                "Confidence": 96.9288558959961,
                                "Value": true
                            }
                        }
                    ]
                },
                {
                    "Name": "RIGHT_HAND",
                    "Confidence": 99.82939147949219,
                    "EquipmentDetections": [
                        {
                            "BoundingBox": {
                                "Width": 0.20971858501434326,
                                "Height": 0.20528452098369598,
                                "Left": 0.2711356580257416,
                                "Top": 0.6750612258911133
                            },
                            "Confidence": 95.70789337158203,
                            "Type": "HAND_COVER",
                            "CoversBodyPart": {
                                "Confidence": 99.85433197021484,
                                "Value": true
                            }
                        }
                    ]
                },
                {
                    "Name": "HEAD",
                    "Confidence": 99.9999008178711,
                    "EquipmentDetections": [
                        {
                            "BoundingBox": {
                                "Width": 0.24350935220718384,
                                "Height": 0.34623199701309204,
                                "Left": 0.43011072278022766,
                                "Top": 0.01103297434747219
                            },
                            "Confidence": 83.88762664794922,
                            "Type": "HEAD_COVER",
                            "CoversBodyPart": {
                                "Confidence": 99.96485900878906,
                                "Value": true
                            }
                        }
                    ]
                }
            ],
            "BoundingBox": {
                "Width": 0.7403100728988647,
                "Height": 0.9412225484848022,
                "Left": 0.02214839495718479,
                "Top": 0.03134796395897865
            },
            "Confidence": 99.98855590820312,
            "Id": 0
        }
    ],
    "Summary": {
        "PersonsWithRequiredEquipment": [
            0
        ],
        "PersonsWithoutRequiredEquipment": [],
        "PersonsIndeterminate": []
    }
}
```