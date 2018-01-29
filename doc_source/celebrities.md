# Recognizing Celebrities<a name="celebrities"></a>

Amazon Rekognition can recognize thousands of celebrities in a wide range of categories, such as entertainment and media, sports, business, and politics\. With Amazon Rekognition you can recognize celebrities in images and in stored videos\. You can also get additional information for recognized celebrities\.


+ [Celebrities in Images](#recognize-celebrities-calling-image)
+ [Celebrities in Video](#recognize-celebrities-calling-video)
+ [Recognizing Celebrities in an Image](celebrities-procedure-image.md)
+ [Recognizing Celebrities in a Stored Video \(SDK for Java\)](celebrities-video-sqs.md)
+ [Getting Information about a Celebrity](get-celebrity-info-procedure.md)

## Celebrities in Images<a name="recognize-celebrities-calling-image"></a>

To recognize celebrities within images and get additional information about recognized celebrities, use the [RecognizeCelebrities](API_RecognizeCelebrities.md) non\-storage API operation\. For example, in social media or news and entertainment industries where information gathering can be time critical, you can use the `RecognizeCelebrities` operation to identify as many as 100 celebrities in an image and return links to celebrity web pages, if they are available\. Amazon Rekognition doesn't remember which image it detected a celebrity in\. Your application must store this information\. For an example, see [Recognizing Celebrities in an Image](celebrities-procedure-image.md)\.

If you haven't stored the additional information for a celebrity returned by `RecognizeCelebrities` and you want to avoid reanalyzing an image to get it, use [GetCelebrityInfo](API_GetCelebrityInfo.md)\. To call `GetCelebrityInfo`, you need the unique identifier that Rekognition assigns to each celebrity\. The identifier is returned as part of the `RecognizeCelebrities` response for each celebrity recognized in an image\. 

If you have a large collection of images to process for celebrity recognition, consider using [AWS Batch](http://docs.aws.amazon.com/batch/latest/userguide/) to process calls to `RecognizeCelebrities` in batches in the background\. When you add a new image to your collection, you can use an AWS Lambda function to recognize celebrities by calling `RecognizeCelebrities` as the image is uploaded into an S3 bucket\.

You provide an input image to `RecognizeCelebrities` either as image bytes or by referencing an image stored in an S3 bucket\. The image must be either a \.png or \.jpg formatted file\. For information about input image recommendations, see [Working with Images](images.md)\. The input image quality \(brightness and sharpness\) is returned by `RecognizeCelebrities`\. 

`RecognizeCelebrities` returns an array of recognized celebrities and an array of unrecognized faces, as shown in the following example: 

```
{
    "CelebrityFaces": [{
        "Face": {
            "BoundingBox": {
                "Height": 0.617123007774353,
                "Left": 0.15641026198863983,
                "Top": 0.10864841192960739,
                "Width": 0.3641025722026825
            },
            "Confidence": 99.99589538574219,
            "Landmarks": [{
                "Type": "eyeLeft",
                "X": 0.2837241291999817,
                "Y": 0.3637104034423828
            }, {
                "Type": "eyeRight",
                "X": 0.4091649055480957,
                "Y": 0.37378931045532227
            }, {
                "Type": "nose",
                "X": 0.35267341136932373,
                "Y": 0.49657556414604187
            }, {
                "Type": "mouthLeft",
                "X": 0.2786353826522827,
                "Y": 0.5455248355865479
            }, {
                "Type": "mouthRight",
                "X": 0.39566439390182495,
                "Y": 0.5597742199897766
            }],
            "Pose": {
                "Pitch": -7.749263763427734,
                "Roll": 2.004552125930786,
                "Yaw": 9.012002944946289
            },
            "Quality": {
                "Brightness": 32.69192123413086,
                "Sharpness": 99.9305191040039
            }
        },
        "Id": "3Ir0du6",
        "MatchConfidence": 98.0,
        "Name": "Jeff Bezos",
        "Urls": ["www.imdb.com/name/nm1757263"]
    }],
    "OrientationCorrection": "ROTATE_0",
    "UnrecognizedFaces": [{
        "BoundingBox": {
            "Height": 0.5345501899719238,
            "Left": 0.48461538553237915,
            "Top": 0.16949152946472168,
            "Width": 0.3153846263885498
        },
        "Confidence": 99.92860412597656,
        "Landmarks": [{
            "Type": "eyeLeft",
            "X": 0.5863404870033264,
            "Y": 0.36940744519233704
        }, {
            "Type": "eyeRight",
            "X": 0.6999204754829407,
            "Y": 0.3769848346710205
        }, {
            "Type": "nose",
            "X": 0.6349524259567261,
            "Y": 0.4804527163505554
        }, {
            "Type": "mouthLeft",
            "X": 0.5872702598571777,
            "Y": 0.5535582304000854
        }, {
            "Type": "mouthRight",
            "X": 0.6952020525932312,
            "Y": 0.5600858926773071
        }],
        "Pose": {
            "Pitch": -7.386096477508545,
            "Roll": 2.304218292236328,
            "Yaw": -6.175624370574951
        },
        "Quality": {
            "Brightness": 37.16635513305664,
            "Sharpness": 99.884521484375
        }
    }]
}
```

The response includes the following:

+ **Recognized celebrities** – `Celebrities` is an array of recognized celebrities\. Each [Celebrity](API_Celebrity.md) object in the array contains the celebrity name and a list of URLs pointing to related content; for example, the celebrity's IMDB link\. Amazon Rekognition returns an [ComparedFace](API_ComparedFace.md) object that your application can use to determine where the celebrity's face is on the image and a unique identifier for the celebrity\. Use the unique identifier to retrieve celebrity information later with the [GetCelebrityInfo](API_GetCelebrityInfo.md) API operation\. 

+ **Unrecognized faces** – `UnrecognizedFaces` is an array of faces that didn't match any known celebrities\. Each [ComparedFace](API_ComparedFace.md) object in the array contains a bounding box \(as well as other information\) that you can use to locate the face in the image\.

+ **Image orientation** – Image orientation information is provided to allow you to correctly display of the image\.

## Celebrities in Video<a name="recognize-celebrities-calling-video"></a>

To recognize celebrities in a video stored in an Amazon S3 bucket, you use [StartCelebrityRecognition](API_StartCelebrityRecognition.md) and [GetCelebrityRecognition](API_GetCelebrityRecognition.md)\. Analyzing videos stored in an Amazon S3 bucket is an asynchronous workflow\. For more information, see [Working with Stored Videos](video.md)\. For an example, see [Recognizing Celebrities in a Stored Video \(SDK for Java\)](celebrities-video-sqs.md)\.

The response from `GetCelebrityRecognition` includes an array, `Celebrities`, of celebrities \([CelebrityRecognition](API_CelebrityRecognition.md)\) recognized in the video and the time\(s\) they were recognized\. The following is an example JSON response\.

```
{
    "Celebrities": [
        {
            "Celebrity": {
                "BoundingBox": {
                    "Height": 0.8842592835426331,
                    "Left": 0,
                    "Top": 0.11574073880910873,
                    "Width": 0.24427083134651184
                },
                "Confidence": 0.699999988079071,
                "Face": {
                    "BoundingBox": {
                        "Height": 0.20555555820465088,
                        "Left": 0.029374999925494194,
                        "Top": 0.22333332896232605,
                        "Width": 0.11562500149011612
                    },
                    "Confidence": 99.89837646484375,
                    "Landmarks": [
                        {
                            "Type": "eyeLeft",
                            "X": 0.06857934594154358,
                            "Y": 0.30842265486717224
                        },
                        {
                            "Type": "eyeRight",
                            "X": 0.10396526008844376,
                            "Y": 0.300625205039978
                        },
                        {
                            "Type": "nose",
                            "X": 0.0966852456331253,
                            "Y": 0.34081998467445374
                        },
                        {
                            "Type": "mouthLeft",
                            "X": 0.075217105448246,
                            "Y": 0.3811396062374115
                        },
                        {
                            "Type": "mouthRight",
                            "X": 0.10744428634643555,
                            "Y": 0.37407416105270386
                        }
                    ],
                    "Pose": {
                        "Pitch": -0.9784082174301147,
                        "Roll": -8.808176040649414,
                        "Yaw": 20.28228759765625
                    },
                    "Quality": {
                        "Brightness": 43.312068939208984,
                        "Sharpness": 99.80813598632812
                    }
                },
                "Id": "XXXXXX",
                "Name": "Celeb A",
                "Urls": []
            },
            "Timestamp": 367
       },......
    ],
    "JobStatus": "SUCCEEDED",
    "NextToken": "XfXnZKiyMOGDhzBzYUhS5puM+g1IgezqFeYpv/H/+5noP/LmM57FitUAwSQ5D6G4AB/PNwolrw==",
    "VideoMetadata": {
        "Codec": "h264",
        "DurationMillis": 67301,
        "FileExtension": "mp4",
        "Format": "QuickTime / MOV",
        "FrameHeight": 1080,
        "FrameRate": 29.970029830932617,
        "FrameWidth": 1920
    }
}
```

The response includes the following:

+ **Recognized celebrities** – `Celebrities` is an array of celebrities and the time\(s\) they are recognized in a video\. A [CelebrityRecognition](API_CelebrityRecognition.md) object exists for each time the celebrity is recognized in the video\. Each `CelebrityRecognition` contains information about a recognized celebrity \([CelebrityDetail](API_CelebrityDetail.md)\) and the time \(`Timestamp`\) the celebrity was recognized in the video\. Timestamp is measured in milliseconds from the start of the video\. 

+ **CelebrityDetail** – Contains information about a recognized celebrity\. It includes the celebrity name \(`Name`\), identifer \(`ID`\), and a list of URLs pointing to related content \(`Urls`\)\. It also includes the bounding box for the celebrity's body, The confidence Rekognition Video has in the accuracy of the recognition, and details about the celebrity's face, [FaceDetail](API_FaceDetail.md)\. If you need to get the related content later, you can use `ID` with [GetCelebrityInfo](API_GetCelebrityInfo.md)\. 

+ **VideoMetadata** – Information about the video that was analyzed\.