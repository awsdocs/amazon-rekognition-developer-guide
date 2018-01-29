# Detecting and Analyzing Faces<a name="faces"></a>

Amazon Rekognition can detect faces in images and videos\. This section covers non\-storage operations for analyzing faces\. With Amazon Rekognition you can get information about where faces are detected in an image or video, facial landmarks such as the position of eyes, and detected emotions such as happy or sad\. You can also compare a face in an image with faces detected in another image\. With video analysis, you can track when a face is detected throughout the length of a video\. 

For example, When you provide an image that contains a face as input to [DetectFaces](API_DetectFaces.md), Amazon Rekognition detects the face in the image, analyzes the facial attributes of the face, and then returns a percent confidence score for the face and the facial attributes detected in the image\. 

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/sample-detect-faces.png)

This section provides an examples for both image and video facial analysis\. For more information about using the Amazon Rekognition API, see [Working with Images](images.md) and [Working with Stored Videos](video.md)\.

You can use storage operations to save facial metadata for faces detected in an image\. Later you can search for stored faces in both images and videos\. For example, this enables searching for a specific person in a surveillance video\. For more information, see [Searching Faces in a Collection](collections.md)\.


+ [Detect Faces in an Image](#faces-detect-images)
+ [Compare Faces in Images](#faces-comparefaces)
+ [Detecting Faces in a Stored Video](#faces-video)
+ [Detecting Faces in an Image \(SDK\)](procedure-detecting-faces-in-images.md)
+ [Comparing Faces in Images \(SDK\)](faces-compare-images.md)
+ [Detecting Faces in a Stored Video \(SDK for Java\)](faces-sqs-video.md)

## Detect Faces in an Image<a name="faces-detect-images"></a>

Rekognition Image provides the [DetectFaces](API_DetectFaces.md) operation that looks for key facial features such as eyes, nose, and mouth to detect faces in an input image\. Rekognition Image detects the 100 largest faces in an image\. The operation response returns the following information for each detected face:

+ **Bounding box** – Coordinates of the bounding box surrounding the face\.

+ **Confidence** – Level of confidence that the bounding box contains a face\. 

+ **Facial landmarks** – An array of facial landmarks\. For each landmark, such as the left eye, right eye, and mouth, the response provides the x, y coordinates\.

+ **Facial attributes** – A set of facial attributes, including gender, or whether the face has a beard\. For each such attribute, the response provides a value\. The value can be of different types such as a Boolean \(whether a person is wearing sunglasses\), a string \(whether the person is male or female\), etc\. In addition, for most attributes the response also provides a confidence in the detected value for the attribute\. 

+ **Quality** – Describes the brightness and the sharpness of the face\. For information about ensuring the best possible face detection, see [](image-best-practices.md#recommendations-for-images)\.

+ **Pose** – Describes the rotation of the face inside the image\.

+ **Emotions** – A set of emotions with confidence in the analysis\.

The following is an example response of a `DetectFaces` API call\. 

```
{
   "FaceDetails":[
      {
         "BoundingBox":{
            "Height":0.18000000715255737,
            "Left":0.5555555820465088,
            "Top":0.33666667342185974,
            "Width":0.23999999463558197
         },
         "Confidence":100.0,
         "Landmarks":[
            {
               "Type":"eyeLeft",
               "X":0.6394737362861633,
               "Y":0.40819624066352844
            },
            {
               "Type":"eyeRight",
               "X":0.7266660928726196,
               "Y":0.41039225459098816
            },
            {
               "Type":"nose",
               "X":0.6912462115287781,
               "Y":0.44240960478782654
            },
            {
               "Type":"mouthLeft",
               "X":0.6306198239326477,
               "Y":0.46700039505958557
            },
            {
               "Type":"mouthRight",
               "X":0.7215608954429626,
               "Y":0.47114261984825134
            }
         ],
         "Pose":{
            "Pitch":4.050806522369385,
            "Roll":0.9950747489929199,
            "Yaw":13.693790435791016
         },
         "Quality":{
            "Brightness":37.60169982910156,
            "Sharpness":80.0
         }
      },
      {
         "BoundingBox":{
            "Height":0.16555555164813995,
            "Left":0.3096296191215515,
            "Top":0.7066666483879089,
            "Width":0.22074073553085327
         },
         "Confidence":99.99998474121094,
         "Landmarks":[
            {
               "Type":"eyeLeft",
               "X":0.3767718970775604,
               "Y":0.7863991856575012
            },
            {
               "Type":"eyeRight",
               "X":0.4517287313938141,
               "Y":0.7715709209442139
            },
            {
               "Type":"nose",
               "X":0.42001065611839294,
               "Y":0.8192070126533508
            },
            {
               "Type":"mouthLeft",
               "X":0.3915625810623169,
               "Y":0.8374140858650208
            },
            {
               "Type":"mouthRight",
               "X":0.46825936436653137,
               "Y":0.823401689529419
            }
         ],
         "Pose":{
            "Pitch":-16.320178985595703,
            "Roll":-15.097439765930176,
            "Yaw":-5.771541118621826
         },
         "Quality":{
            "Brightness":31.440860748291016,
            "Sharpness":60.000003814697266
         }
      }
   ],
   "OrientationCorrection":"ROTATE_0"
}
```

Note the following:

+ The `Pose` data describes the rotation of the face detected\. You can use the combination of the `BoundingBox` and `Pose` data to draw the bounding box around faces that your application displays\.

   

+ The `Quality` describes the brightness and the sharpness of the face\. You might find this useful to compare faces across images and find the best face\.

   

+ The `DetectFaces` operation first detects orientation of the input image, before detecting facial features\. The `OrientationCorrection` in the response returns the degrees of rotation detected \(counter\-clockwise direction\)\. Your application can use this value to correct the image orientation when displaying the image\. 

+ The preceding response shows all facial `landmarks` the service can detect, all facial attributes and emotions\. To get all of these in the response, you must specify the `attributes` parameter with value `ALL`\. By default, the `DetectFaces` API returns only the following five facial `landmarks`, `Pose`, and `Quality`\.

  ```
  ...
     "Landmarks": [
         {
             "Y": 0.41730427742004395,
             "X": 0.36835095286369324,
             "Type": "eyeLeft"
         },
         {
             "Y": 0.4281611740589142,
             "X": 0.5960656404495239,
             "Type": "eyeRight"
         },
         {
             "Y": 0.5349795818328857,
             "X": 0.47817257046699524,
             "Type": "nose"
         },
         {
             "Y": 0.5721957683563232,
             "X": 0.352621465921402,
             "Type": "mouthLeft"
         },
         {
             "Y": 0.5792245864868164,
             "X": 0.5936088562011719,
             "Type": "mouthRight"
         }
     ]
  ...
  ```

+ The following illustration shows the relative location of the facial landmarks on the face returned by the `DetectFaces` API operation\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/landmarks-10.png)

The labels on the image map as follows to the [Landmark](API_Landmark.md) data type\. For clarity, The left eye and right eye landmark points are not shown on the image\.


| Label | Landmark | 
| --- | --- | 
|  b\_ll  |  leftEyeBrowLeft  | 
|  b\_lu  |  leftEyeBrowUp  | 
|  b\_lr  |  leftEyeBrowRight  | 
|  e\_ll  |  leftEyeLeft  | 
|  e\_lu  |  leftEyeUp  | 
|  e\_lr  |  leftEyeRight  | 
|  e\_ld  |  leftEyeDown  | 
|  e\_lp  |  leftPupil  | 
|  n\_l  |  noseLeft  | 
|  n  |  nose  | 
|  n\_r  |  noseRight  | 
|  m\_u  |   mouthUp   | 
|  m\_d  |  mouthDown  | 
|  m\_l  |  mouthLeft  | 
|  m\_r  |  mouthRight  | 
|  b\_rl  |  rightEyeBrowLeft  | 
|  b\_ru  |  rightEyeBrowUp  | 
|  b\_rr  |  rightEyeBrowRight  | 
|  e\_rl  |  rightEyeLeft  | 
|  e\_ru  |  rightEyeUp  | 
|  e\_rr  |  rightEyeRight   | 
|  e\_rp  |  rightPupil  | 
|  e\_rd  |  rightEyeDown  | 

## Compare Faces in Images<a name="faces-comparefaces"></a>

To compare a face in the *source* image with each face in the *target* image, use the [CompareFaces](API_CompareFaces.md) operation\. 

**Note**  
If the source image contains more than one face, the service detects the largest face and uses it for comparison\.

To specify the minimum level of confidence in the match that you want returned in the response, use `similarityThreshold` in the request\. For more information, see [CompareFaces](API_CompareFaces.md)\.

The API returns an array of face matches, source face information, image orientation, and an array of unmatched faces\. The following is an example response\.

```
{
    "FaceMatches": [{
        "Face": {
            "BoundingBox": {
                "Width": 0.5521978139877319,
                "Top": 0.1203877404332161,
                "Left": 0.23626373708248138,
                "Height": 0.3126954436302185
            },
            "Confidence": 99.98751068115234,
            "Pose": {
                "Yaw": -82.36799621582031,
                "Roll": -62.13221740722656,
                "Pitch": 0.8652129173278809
            },
            "Quality": {
                "Sharpness": 99.99880981445312,
                "Brightness": 54.49755096435547
            },
            "Landmarks": [{
                    "Y": 0.2996366024017334,
                    "X": 0.41685718297958374,
                    "Type": "eyeLeft"
                },
                {
                    "Y": 0.2658946216106415,
                    "X": 0.4414493441581726,
                    "Type": "eyeRight"
                },
                {
                    "Y": 0.3465650677680969,
                    "X": 0.48636093735694885,
                    "Type": "nose"
                },
                {
                    "Y": 0.30935320258140564,
                    "X": 0.6251809000968933,
                    "Type": "mouthLeft"
                },
                {
                    "Y": 0.26942989230155945,
                    "X": 0.6454493403434753,
                    "Type": "mouthRight"
                }
            ]
        },
        "Similarity": 100.0
    }],
    "SourceImageOrientationCorrection": "ROTATE_90",
    "TargetImageOrientationCorrection": "ROTATE_90",
    "UnmatchedFaces": [{
        "BoundingBox": {
            "Width": 0.4890109896659851,
            "Top": 0.6566604375839233,
            "Left": 0.10989011079072952,
            "Height": 0.278298944234848
        },
        "Confidence": 99.99992370605469,
        "Pose": {
            "Yaw": 51.51519012451172,
            "Roll": -110.32493591308594,
            "Pitch": -2.322134017944336
        },
        "Quality": {
            "Sharpness": 99.99671173095703,
            "Brightness": 57.23163986206055
        },
        "Landmarks": [{
                "Y": 0.8288310766220093,
                "X": 0.3133862614631653,
                "Type": "eyeLeft"
            },
            {
                "Y": 0.7632885575294495,
                "X": 0.28091415762901306,
                "Type": "eyeRight"
            },
            {
                "Y": 0.7417283654212952,
                "X": 0.3631140887737274,
                "Type": "nose"
            },
            {
                "Y": 0.8081989884376526,
                "X": 0.48565614223480225,
                "Type": "mouthLeft"
            },
            {
                "Y": 0.7548204660415649,
                "X": 0.46090251207351685,
                "Type": "mouthRight"
            }
        ]
    }],
    "SourceImageFace": {
        "BoundingBox": {
            "Width": 0.5521978139877319,
            "Top": 0.1203877404332161,
            "Left": 0.23626373708248138,
            "Height": 0.3126954436302185
        },
        "Confidence": 99.98751068115234
    }
}
```

In the response, note the following:

+ **Face match information** – The example shows that one face match was found in the target image\. For that face match, it provides a bounding box and a confidence value \(the level of confidence that Amazon Rekognition has that the bounding box contains a face\)\. The `similarity` score of 99\.99 indicates how similar the faces are\. The face match information also includes an array of landmark locations\.

  If multiple faces match, the `faceMatches` array includes all of the face matches\. 

+ **Source face information** – The response includes information about the face from the source image that was used for comparison, including the bounding box and confidence value\.

+ **Image Orientation** – The response includes information about the orientation of the source and target images\. Amazon Rekognition needs this to display the images and retrieve the correct location of the matched face in the target image\.

+ **Unmatched face match information** – The example shows one face that Amazon Rekognition found in the target image that didn't match the face analyzed in the source image\. For that face, it provides a bounding box and a confidence value, indicating the level of confidence that Amazon Rekognition has that the bounding box contains a face\. The face information also includes an array of landmark locations\.

  If Amazon Rekognition finds mutiple faces that do not match, the `UnmatchedFaces` array includes all of the faces that didn't match\. 

## Detecting Faces in a Stored Video<a name="faces-video"></a>

Rekognition Video can detect faces in videos stored in an Amazon S3 bucket and provide information such as: 

+ The time\(s\) faces are detected in a video\.

+ The location of faces in the video frame at the time they were detected\.

+ Facial landmarks such as the position of the left eye\. 

### Using Rekognition Video Face Operations with Video<a name="video-face-overview"></a>

Rekognition Video face detection in videos is an asynchronous operation\. To start the detection of persons in videos call [StartFaceDetection](API_StartFaceDetection.md)\. Rekognition Video publishes the completion status of the video analysis to an Amazon Simple Notification Service topic\. If the video analysis is succesful, you can call [GetFaceDetection](API_GetFaceDetection.md) to get results of the video analysis\. 

For information about calling the video recognition API operations, see [Calling Rekognition Video Operations](api-video.md)\. For an example, see [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md)\.

`GetFaceDetection` returns an array \(`Faces`\) containing information about the faces detected in the video\. An array element, [FaceDetection](API_FaceDetection.md), exists for each time a face is detected in the video\. The array elements are returned sorted by time, in milliseconds since the start of the video\.  The following example is a partial JSON response from `GetFaceDetection`\.

```
{
    "Faces": [
        {
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
            "Timestamp": 0
        },
        {
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
            "Timestamp": 0
        },
        {
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
            "Timestamp": 0
        }.......

    ],
    "JobStatus": "SUCCEEDED",
    "NextToken": "i7fj5XPV/fwviXqz0eag9Ow332Jd5G8ZGWf7hooirD/6V1qFmjKFOQZ6QPWUiqv29HbyuhMNqQ==",
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

In the response, note the following:

+ **Face information** – The `FaceDetection` array element contains information about the detected face \([FaceDetail](API_FaceDetail.md) and the time the face was detected in the video \(`Timestamp`\)\.

+ **Paging information** – The example shows one page of face detection information\. You can specify how many person elements to return in the `MaxResults` input parameter for `GetFaceDetection`\. If more results than `MaxResults` exist, `GetFaceDetection` returns a token \(`NextToken`\) used to get the next page of results\. For more information, see [](api-video.md#api-video-get)\.

+ **Video information** – The response includes information about the video format \(`VideoMetadata`\) in each page of information returned by `GetFaceDetection`\.