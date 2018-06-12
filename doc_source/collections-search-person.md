# Searching for Faces with Rekognition Video<a name="collections-search-person"></a>

You can search a collection for faces that match faces of persons detected in a stored video or a streaming video\. This section covers searching for faces in a stored video\. For information about searching for faces in a streaming video, see [Working with Streaming Videos](streaming-video.md)\.

 The faces you search for must first be indexed into a collection by using [IndexFaces](API_IndexFaces.md)\. For more information see [Adding Faces to a Collection](add-faces-to-collection-procedure.md)\. Rekognition Video face searching follows the same asynchronous workflow as other Rekognition Video operations that analyze videos stored in an Amazon S3 bucket\. For more information, see [Calling Rekognition Video Operations](api-video.md)\. 

To start searching for faces in a stored video, call [StartFaceSearch](API_StartFaceSearch.md)\. After you get the the completion status from the Amazon SNS topic, you call [GetFaceSearch](API_GetFaceSearch.md) to get the search results\. For an example, see [ Searching Stored Videos for Faces \(SDK for Java\)](procedure-person-search-videos.md)\.

The following is an example JSON request for `StartFaceSearch`\.

```
{
    "Video": {
        "S3Object": {
            "Bucket": "bucket",
            "Name": "video.mp4"
        }
    },
    "CollectionId": "VideoFaces",
    "NotificationChannel": {
        "SNSTopicArn": "arn:aws:sns:us-east-1:nnnnnnnnnnnn:xxxxxxx",
        "RoleArn": "arn:aws:iam::nnnnnnnnnnnn:role/xxxxxxxx"
    }
}
```

The request includes the collection to use for the search, the bucket the video is stored in, and the Amazon SNS topic to which Amazon Rekognition publishes the completion status of the search\.

Once you have the completion status from the AWS SNS topic, you get the search results by calling `GetFaceSearch.` The following is an example JSON response from `GetFaceSearch`\.

```
{
    "JobStatus": "SUCCEEDED",
    "NextToken": "IJdbzkZfvBRqj8GPV82BPiZKkLOGCqDIsNZG/gQsEE5faTVK9JHOz/xxxxxxxxxxxxxxx",
    "Persons": [
        {
            "FaceMatches": [
                {
                    "Face": {
                        "BoundingBox": {
                            "Height": 0.527472972869873,
                            "Left": 0.33530598878860474,
                            "Top": 0.2161169946193695,
                            "Width": 0.35503000020980835
                        },
                        "Confidence": 99.90239715576172,
                        "ExternalImageId": "image.PNG",
                        "FaceId": "a2f2e224-bfaa-456c-b360-7c00241e5e2d",
                        "ImageId": "eb57ed44-8d8d-5ec5-90b8-6d190daff4c3"
                    },
                    "Similarity": 98.40909576416016
                }
            ],
            "Person": {
                "BoundingBox": {
                    "Height": 0.8694444298744202,
                    "Left": 0.2473958283662796,
                    "Top": 0.10092592239379883,
                    "Width": 0.49427083134651184
                },
                "Face": {
                    "BoundingBox": {
                        "Height": 0.23000000417232513,
                        "Left": 0.42500001192092896,
                        "Top": 0.16333332657814026,
                        "Width": 0.12937499582767487
                    },
                    "Confidence": 99.97504425048828,
                    "Landmarks": [
                        {
                            "Type": "eyeLeft",
                            "X": 0.46415066719055176,
                            "Y": 0.2572723925113678
                        },
                        {
                            "Type": "eyeRight",
                            "X": 0.5068183541297913,
                            "Y": 0.23705792427062988
                        },
                        {
                            "Type": "nose",
                            "X": 0.49765899777412415,
                            "Y": 0.28383663296699524
                        },
                        {
                            "Type": "mouthLeft",
                            "X": 0.487221896648407,
                            "Y": 0.3452930748462677
                        },
                        {
                            "Type": "mouthRight",
                            "X": 0.5142884850502014,
                            "Y": 0.33167609572410583
                        }
                    ],
                    "Pose": {
                        "Pitch": 15.966927528381348,
                        "Roll": -15.547388076782227,
                        "Yaw": 11.34195613861084
                    },
                    "Quality": {
                        "Brightness": 44.80223083496094,
                        "Sharpness": 99.95819854736328
                    }
                },
                "Index": 0
            },
            "Timestamp": 0
        },
        {
            "Person": {
                "BoundingBox": {
                    "Height": 0.2177777737379074,
                    "Left": 0.7593749761581421,
                    "Top": 0.13333334028720856,
                    "Width": 0.12250000238418579
                },
                "Face": {
                    "BoundingBox": {
                        "Height": 0.2177777737379074,
                        "Left": 0.7593749761581421,
                        "Top": 0.13333334028720856,
                        "Width": 0.12250000238418579
                    },
                    "Confidence": 99.63436889648438,
                    "Landmarks": [
                        {
                            "Type": "eyeLeft",
                            "X": 0.8005779385566711,
                            "Y": 0.20915353298187256
                        },
                        {
                            "Type": "eyeRight",
                            "X": 0.8391435146331787,
                            "Y": 0.21049551665782928
                        },
                        {
                            "Type": "nose",
                            "X": 0.8191410899162292,
                            "Y": 0.2523227035999298
                        },
                        {
                            "Type": "mouthLeft",
                            "X": 0.8093273043632507,
                            "Y": 0.29053622484207153
                        },
                        {
                            "Type": "mouthRight",
                            "X": 0.8366993069648743,
                            "Y": 0.29101791977882385
                        }
                    ],
                    "Pose": {
                        "Pitch": 3.165884017944336,
                        "Roll": 1.4182015657424927,
                        "Yaw": -11.151537895202637
                    },
                    "Quality": {
                        "Brightness": 28.910892486572266,
                        "Sharpness": 97.61507415771484
                    }
                },
                "Index": 1
            },
            "Timestamp": 0
        },
        {
            "Person": {
                "BoundingBox": {
                    "Height": 0.8388888835906982,
                    "Left": 0,
                    "Top": 0.15833333134651184,
                    "Width": 0.2369791716337204
                },
                "Face": {
                    "BoundingBox": {
                        "Height": 0.20000000298023224,
                        "Left": 0.029999999329447746,
                        "Top": 0.2199999988079071,
                        "Width": 0.11249999701976776
                    },
                    "Confidence": 99.85971069335938,
                    "Landmarks": [
                        {
                            "Type": "eyeLeft",
                            "X": 0.06842322647571564,
                            "Y": 0.3010137975215912
                        },
                        {
                            "Type": "eyeRight",
                            "X": 0.10543643683195114,
                            "Y": 0.29697132110595703
                        },
                        {
                            "Type": "nose",
                            "X": 0.09569807350635529,
                            "Y": 0.33701086044311523
                        },
                        {
                            "Type": "mouthLeft",
                            "X": 0.0732642263174057,
                            "Y": 0.3757539987564087
                        },
                        {
                            "Type": "mouthRight",
                            "X": 0.10589495301246643,
                            "Y": 0.3722417950630188
                        }
                    ],
                    "Pose": {
                        "Pitch": -0.5589138865470886,
                        "Roll": -5.1093974113464355,
                        "Yaw": 18.69594955444336
                    },
                    "Quality": {
                        "Brightness": 43.052337646484375,
                        "Sharpness": 99.68138885498047
                    }
                },
                "Index": 2
            },
            "Timestamp": 0
        }......

    ],
    "VideoMetadata": {
        "Codec": "h264",
        "DurationMillis": 67301,
        "Format": "QuickTime / MOV",
        "FrameHeight": 1080,
        "FrameRate": 29.970029830932617,
        "FrameWidth": 1920
    }
}
```

The response includes an array of persons, `Persons`, detected in the video whose face\(s\) matches a face in the input collection\. An array element, [PersonMatch](API_PersonMatch.md), exists for each time the person is matched in the video\. Each `PersonMatch` includes an array of face matches from the input collection, [FaceMatch](API_FaceMatch.md), information about the matched person, [PersonDetail](API_PersonDetail.md), and the time the person was matched in the video\. 
