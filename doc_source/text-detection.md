# Detecting Text<a name="text-detection"></a>

Amazon Rekognition Text in Image can detect text in images and convert it into machine\-readable text\. You can use the machine\-readable text to implement solutions such as:
+ Visual search\. For example, retrieving and displaying images that contain the same text\.
+ Content insights\. For example, providing insights into themes that occur in text recognized in extracted video frames\. Your application can search recognized text for relevant content, such as news, sport scores, athlete numbers, and captions\.
+ Navigation\. For example, developing a speech enabled mobile app for visually impaired people that recognizes the names of restaurants, shops, or street signs\. 
+ Public safety and transportation support\. For example, detecting car licence plate numbers from traffic camera images\. 
+ Filtering\. For example, filtering out personally identifiable information from images\. 

[DetectText](API_DetectText.md) detects text in \.jpeg or \.png format images and supports most fonts including highly stylized ones\. After detecting text, `DetectText` creates a representation of detected words and lines of text and shows the relationship between them\. The `DetectText` API also tells you where the text is on an image\.

Consider the following image: 

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/text.png)

The blue boxes represent information about the detected text and location of the text that the `DetectText` operation returns\. To be detected, text must be within \+/\- 30 degrees orientation of the horizontal axis\. `DetectText` categorizes recognized text as either a word or a line of text\.

A *word* is one or more ISO basic latin script characters that are not separated by spaces\. `DetectText` can detect up to 50 words in an image\.

A *line* is a string of equally spaced words\. A line isn't necessarily a complete sentence\. For example, a driver's license number is detected as a line\. A line ends when there is no aligned text after it\. Also, a line ends when there is a large gap between words, relative to the length of the words\. This means, depending on the gap between words, Amazon Rekognition may detect multiple lines in text aligned in the same direction\. Periods don't represent the end of a line\. If a sentence spans multiple lines, the `DetectText` operation returns multiple lines\.

Amazon Rekognition can also detect numbers and common symbols such as @, /, $,%, \-, \_, \+, \*, and \#\.

****

## Calling the DetectText Operation<a name="text-calling-detecttext"></a>

In the `DetectText` operation, you supply an input image either as a byte64\-encoded byte array or as an image stored in an Amazon S3 bucket\. For an example, see [Detecting Text in an Image](text-detecting-text-procedure.md)\. 

The `DetectText` operation analyses the image and returns an array, TextDetections, where each element \(`[TextDetection](API_TextDetection.md)`\) represents a line or word detected in the image\. For each element, `DetectText` returns the following information: 
+ The detected text \(`DetectedText`\)
+ The relationships between words and lines \(`Id` and `ParentId`\)
+ The location of text on the image \(`Geometry`\)
+ The confidence Amazon Rekognition has in the accuracy of the detected text and bounding box \(`Confidence`\)
+ The type of the detected text \(`Type`\)

### Detected Text<a name="text-detected-text"></a>

Each `TextDetection` element contains recognized text \(words or lines\) in the `DetectedText` field\. Returned text might include characters that makes a word unrecognizable\. For example, *C@t* instead of *Cat*\. To determine whether a `TextDetection` element represents a line of text or a word, use the `Type` field\.

Each `TextDetection` element includes a percentage value that represents the degree of confidence that Amazon Rekognition has in the accuracy of the detected text and of the bounding box surrounding the text\. 

### Word and Line Relationships<a name="text-ids"></a>

Each `TextDetection` element has an identifier field, `Id`\. The `Id` shows the word's position in a line\. If the element is a word, the parent identifier field, `ParentId`, identifies the line where the word was detected\. The `ParentId` for a line is null\. For example, the line "but keep" in the preceding image has the following the `Id` and `ParentId` values: 


|  Text  |  ID  |  Parent ID  | 
| --- | --- | --- | 
|  but keep  |  3  |   | 
|  but  |  8  |  3  | 
|  keep  |  9  |  3  | 

### Text Location on an Image<a name="text-location"></a>

To determine where the recognized text is on an image, use the bounding box \([Geometry](API_Geometry.md)\) information returned by `DetectText`\. The `Geometry` object contains two types of bounding box information for detected lines and words:
+ An axis\-aligned coarse rectangular outline in a [BoundingBox](API_BoundingBox.md) object
+ A finer\-grained polygon made up of multiple X and Y coordinates in a [Point](API_Point.md) array

The bounding box and polygon coordinates show where the text is located on the source image\. The coordinate values are a ratio of the overall image size\. For more information, see [BoundingBox](API_BoundingBox.md)\. 

## Operation Response<a name="text-response"></a>

The following JSON response from the `DetectText` operation shows the words and lines detected in the preceding image\.

```
{
    "TextDetections": [
        {
            "Confidence": 90.54900360107422,
            "DetectedText": "IT'S",
            "Geometry": {
                "BoundingBox": {
                    "Height": 0.10317354649305344,
                    "Left": 0.6677391529083252,
                    "Top": 0.17569075524806976,
                    "Width": 0.15113449096679688
                },
                "Polygon": [
                    {
                        "X": 0.6677391529083252,
                        "Y": 0.17569075524806976
                    },
                    {
                        "X": 0.8188736438751221,
                        "Y": 0.17574213445186615
                    },
                    {
                        "X": 0.8188582062721252,
                        "Y": 0.278915673494339
                    },
                    {
                        "X": 0.6677237153053284,
                        "Y": 0.2788642942905426
                    }
                ]
            },
            "Id": 0,
            "Type": "LINE"
        },
        {
            "Confidence": 59.411651611328125,
            "DetectedText": "I",
            "Geometry": {
                "BoundingBox": {
                    "Height": 0.05955825746059418,
                    "Left": 0.2763049304485321,
                    "Top": 0.394121915102005,
                    "Width": 0.026684552431106567
                },
                "Polygon": [
                    {
                        "X": 0.2763049304485321,
                        "Y": 0.394121915102005
                    },
                    {
                        "X": 0.30298948287963867,
                        "Y": 0.3932435214519501
                    },
                    {
                        "X": 0.30385109782218933,
                        "Y": 0.45280176401138306
                    },
                    {
                        "X": 0.27716654539108276,
                        "Y": 0.453680157661438
                    }
                ]
            },
            "Id": 1,
            "Type": "LINE"
        },
        {
            "Confidence": 92.76634979248047,
            "DetectedText": "MONDAY",
            "Geometry": {
                "BoundingBox": {
                    "Height": 0.11997425556182861,
                    "Left": 0.5545867085456848,
                    "Top": 0.34920141100883484,
                    "Width": 0.39841532707214355
                },
                "Polygon": [
                    {
                        "X": 0.5545867085456848,
                        "Y": 0.34920141100883484
                    },
                    {
                        "X": 0.9530020356178284,
                        "Y": 0.3471102714538574
                    },
                    {
                        "X": 0.9532787799835205,
                        "Y": 0.46708452701568604
                    },
                    {
                        "X": 0.554863452911377,
                        "Y": 0.46917566657066345
                    }
                ]
            },
            "Id": 2,
            "Type": "LINE"
        },
        {
            "Confidence": 96.7636489868164,
            "DetectedText": "but keep",
            "Geometry": {
                "BoundingBox": {
                    "Height": 0.0756164938211441,
                    "Left": 0.634815514087677,
                    "Top": 0.5181083083152771,
                    "Width": 0.20877975225448608
                },
                "Polygon": [
                    {
                        "X": 0.634815514087677,
                        "Y": 0.5181083083152771
                    },
                    {
                        "X": 0.8435952663421631,
                        "Y": 0.52589350938797
                    },
                    {
                        "X": 0.8423560857772827,
                        "Y": 0.6015099883079529
                    },
                    {
                        "X": 0.6335763335227966,
                        "Y": 0.59372478723526
                    }
                ]
            },
            "Id": 3,
            "Type": "LINE"
        },
        {
            "Confidence": 99.47185516357422,
            "DetectedText": "Smiling",
            "Geometry": {
                "BoundingBox": {
                    "Height": 0.2814019024372101,
                    "Left": 0.48475268483161926,
                    "Top": 0.6823741793632507,
                    "Width": 0.47539761662483215
                },
                "Polygon": [
                    {
                        "X": 0.48475268483161926,
                        "Y": 0.6823741793632507
                    },
                    {
                        "X": 0.9601503014564514,
                        "Y": 0.587857186794281
                    },
                    {
                        "X": 0.9847385287284851,
                        "Y": 0.8692590594291687
                    },
                    {
                        "X": 0.5093409419059753,
                        "Y": 0.9637760519981384
                    }
                ]
            },
            "Id": 4,
            "Type": "LINE"
        },
        {
            "Confidence": 90.54900360107422,
            "DetectedText": "IT'S",
            "Geometry": {
                "BoundingBox": {
                    "Height": 0.10387301445007324,
                    "Left": 0.6685508489608765,
                    "Top": 0.17597118020057678,
                    "Width": 0.14985692501068115
                },
                "Polygon": [
                    {
                        "X": 0.6677391529083252,
                        "Y": 0.17569075524806976
                    },
                    {
                        "X": 0.8188736438751221,
                        "Y": 0.17574213445186615
                    },
                    {
                        "X": 0.8188582062721252,
                        "Y": 0.278915673494339
                    },
                    {
                        "X": 0.6677237153053284,
                        "Y": 0.2788642942905426
                    }
                ]
            },
            "Id": 5,
            "ParentId": 0,
            "Type": "WORD"
        },
        {
            "Confidence": 92.76634979248047,
            "DetectedText": "MONDAY",
            "Geometry": {
                "BoundingBox": {
                    "Height": 0.11929994821548462,
                    "Left": 0.5540683269500732,
                    "Top": 0.34858056902885437,
                    "Width": 0.3998897075653076
                },
                "Polygon": [
                    {
                        "X": 0.5545867085456848,
                        "Y": 0.34920141100883484
                    },
                    {
                        "X": 0.9530020356178284,
                        "Y": 0.3471102714538574
                    },
                    {
                        "X": 0.9532787799835205,
                        "Y": 0.46708452701568604
                    },
                    {
                        "X": 0.554863452911377,
                        "Y": 0.46917566657066345
                    }
                ]
            },
            "Id": 7,
            "ParentId": 2,
            "Type": "WORD"
        },
        {
            "Confidence": 59.411651611328125,
            "DetectedText": "I",
            "Geometry": {
                "BoundingBox": {
                    "Height": 0.05981886386871338,
                    "Left": 0.2779299318790436,
                    "Top": 0.3935416042804718,
                    "Width": 0.02624112367630005
                },
                "Polygon": [
                    {
                        "X": 0.2763049304485321,
                        "Y": 0.394121915102005
                    },
                    {
                        "X": 0.30298948287963867,
                        "Y": 0.3932435214519501
                    },
                    {
                        "X": 0.30385109782218933,
                        "Y": 0.45280176401138306
                    },
                    {
                        "X": 0.27716654539108276,
                        "Y": 0.453680157661438
                    }
                ]
            },
            "Id": 6,
            "ParentId": 1,
            "Type": "WORD"
        },
        {
            "Confidence": 95.33189392089844,
            "DetectedText": "but",
            "Geometry": {
                "BoundingBox": {
                    "Height": 0.06849122047424316,
                    "Left": 0.6350157260894775,
                    "Top": 0.5214487314224243,
                    "Width": 0.08413040637969971
                },
                "Polygon": [
                    {
                        "X": 0.6347596645355225,
                        "Y": 0.5215170383453369
                    },
                    {
                        "X": 0.719483494758606,
                        "Y": 0.5212655067443848
                    },
                    {
                        "X": 0.7195737957954407,
                        "Y": 0.5904868841171265
                    },
                    {
                        "X": 0.6348499655723572,
                        "Y": 0.5907384157180786
                    }
                ]
            },
            "Id": 8,
            "ParentId": 3,
            "Type": "WORD"
        },
        {
            "Confidence": 98.1954116821289,
            "DetectedText": "keep",
            "Geometry": {
                "BoundingBox": {
                    "Height": 0.07207882404327393,
                    "Left": 0.7295929789543152,
                    "Top": 0.5265749096870422,
                    "Width": 0.11196041107177734
                },
                "Polygon": [
                    {
                        "X": 0.7290706038475037,
                        "Y": 0.5251666903495789
                    },
                    {
                        "X": 0.842876672744751,
                        "Y": 0.5268880724906921
                    },
                    {
                        "X": 0.8423973917961121,
                        "Y": 0.5989891886711121
                    },
                    {
                        "X": 0.7285913228988647,
                        "Y": 0.5972678065299988
                    }
                ]
            },
            "Id": 9,
            "ParentId": 3,
            "Type": "WORD"
        },
        {
            "Confidence": 99.47185516357422,
            "DetectedText": "Smiling",
            "Geometry": {
                "BoundingBox": {
                    "Height": 0.3739858865737915,
                    "Left": 0.48920923471450806,
                    "Top": 0.5900818109512329,
                    "Width": 0.5097314119338989
                },
                "Polygon": [
                    {
                        "X": 0.48475268483161926,
                        "Y": 0.6823741793632507
                    },
                    {
                        "X": 0.9601503014564514,
                        "Y": 0.587857186794281
                    },
                    {
                        "X": 0.9847385287284851,
                        "Y": 0.8692590594291687
                    },
                    {
                        "X": 0.5093409419059753,
                        "Y": 0.9637760519981384
                    }
                ]
            },
            "Id": 10,
            "ParentId": 4,
            "Type": "WORD"
        }
    ]
}
```