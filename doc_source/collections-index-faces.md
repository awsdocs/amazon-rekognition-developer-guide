# Storing Faces in a Face Collection<a name="collections-index-faces"></a>

After you create a face collection, you can store faces in it\. Amazon Rekognition provides the `IndexFaces` operation that can detect faces in the input image \(JPEG or PNG\) and adds them to the specified face collection\. For more information about collections, see [Managing Collections](managing-collections.md)\. After you persist faces, you can search the face collection for face matches\.

**Important**  
Amazon Rekognition does not save the actual faces detected\. Instead, the underlying detection algorithm first detects the faces in the input image, extracts facial features for each face, and then stores the feature information in a database\. Then, Amazon Rekognition uses this information in subsequent operations such as searching a face collection for matching faces\. 

For each face, the `IndexFaces` operation persists the following information:

+ **Multidimensional facial features** – `IndexFaces` uses facial analysis to extract multidimensional information about the facial features and stores the information in the face collection\. You cannot access this information directly\. However, Amazon Rekognition uses this information when searching a face collection for face matches\.

   

+ **Metadata** – The metadata for each face includes a bounding box, confidence level \(that the bounding box contains a face\), IDs assigned by Amazon Rekognition \(face ID and image ID\), and an external image ID \(if you provided it\) in the request\. This information is returned to you in response to the `IndexFaces` API call\. For an example, see the `face` element in the following example response\.

  The service returns this metadata in response to the following API calls:

   

  +  `ListFaces` 

  + Search faces operations – The responses for `SearchFaces` and `SearchFacesByImage` return the confidence in the match for each matching face, along with this metadata of the matched face\.

You might want to associate indexed faces with the image they were detected in\. For example, you might want to maintain a client\-side index of images and faces in the images\. To associate faces with an image, specify an image ID in the `ExternalImageId` request parameter\. The image ID can be the file name or another ID that you create\.

In addition to the preceding information that the API persists in the face collection, the API also returns face details that are not persisted in the collection \(see the `faceDetail` element in the following example response\)\. 

**Note**  
`DetectFaces` returns the same information, so you don't need to call both `DetectFaces` and `IndexFaces` for the same image\. 

```
{
    "FaceRecords": [
        {
            "FaceDetail": {
                "BoundingBox": {
                    "Width": 0.6154,
                    "Top": 0.2442,
                    "Left": 0.1765,
                    "Height": 0.4692
                },
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
                ],
                "Pose": {
                    "Yaw": 1.8526556491851807,
                    "Roll": 3.623055934906006,
                    "Pitch": -10.605680465698242
                },
                "Quality": {
                    "Sharpness": 130.0,
                    "Brightness": 49.129302978515625
                },
                "Confidence": 99.99968719482422
            },
            "Face": {
                "BoundingBox": {
                    "Width": 0.6154,
                    "Top": 0.2442,
                    "Left": 0.1765,
                    "Height": 0.4692
                },
                "FaceId": "84de1c86-5059-53f2-a432-34ebb704615d",
                "Confidence": 99.9997,
                "ImageId": "d38ebf91-1a11-58fc-ba42-f978b3f32f60"
            }
        }
    ],
    "OrientationCorrection": "ROTATE_0"
}
```

To get all facial information, specify 'ALL' for the `DetectionAttributes` request parameter\. For example, in the following example response, note the additional information in the `faceDetail` element, which is not persisted on the server:

+ 25 facial landmarks \(compared to only five in the preceding example\)

+ Nine facial attributes \(eyeglasses, beard, etc\) 

+ Emotions \(see the `emotion` element\)

The `face` element provides metadata that is persisted on the server\.

```
{
    "FaceRecords": [
        {
            "FaceDetail": {
                "Confidence": 99.99968719482422,
                "Eyeglasses": {
                    "Confidence": 99.94019317626953,
                    "Value": false
                },
                "Sunglasses": {
                    "Confidence": 99.62261199951172,
                    "Value": false
                },
                "Gender": {
                    "Confidence": 99.92701721191406,
                    "Value": "Male"
                },
                "Pose": {
                    "Yaw": 1.8526556491851807,
                    "Roll": 3.623055934906006,
                    "Pitch": -10.605680465698242
                },
                "Emotions": [
                    {
                        "Confidence": 99.38518524169922,
                        "Type": "HAPPY"
                    },
                    {
                        "Confidence": 1.1799871921539307,
                        "Type": "ANGRY"
                    },
                    {
                        "Confidence": 1.0325908660888672,
                        "Type": "CONFUSED"
                    }
                ],
                "EyesOpen": {
                    "Confidence": 54.15227508544922,
                    "Value": false
                },
                "Quality": {
                    "Sharpness": 130.0,
                    "Brightness": 49.129302978515625
                },
                "BoundingBox": {
                    "Width": 0.6153846383094788,
                    "Top": 0.24423076212406158,
                    "Left": 0.17654477059841156,
                    "Height": 0.4692307710647583
                },
                "Smile": {
                    "Confidence": 99.8236083984375,
                    "Value": true
                },
                "MouthOpen": {
                    "Confidence": 88.39942169189453,
                    "Value": true
                },
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
                    },
                    {
                        "Y": 0.4163532555103302,
                        "X": 0.3697868585586548,
                        "Type": "leftPupil"
                    },
                    {
                        "Y": 0.42626339197158813,
                        "X": 0.6037314534187317,
                        "Type": "rightPupil"
                    },
                    {
                        "Y": 0.38954615592956543,
                        "X": 0.27343833446502686,
                        "Type": "leftEyeBrowLeft"
                    },
                    {
                        "Y": 0.3775958716869354,
                        "X": 0.35098740458488464,
                        "Type": "leftEyeBrowRight"
                    },
                    {
                        "Y": 0.39108505845069885,
                        "X": 0.433648943901062,
                        "Type": "leftEyeBrowUp"
                    },
                    {
                        "Y": 0.3952394127845764,
                        "X": 0.5416828989982605,
                        "Type": "rightEyeBrowLeft"
                    },
                    {
                        "Y": 0.38667190074920654,
                        "X": 0.6171167492866516,
                        "Type": "rightEyeBrowRight"
                    },
                    {
                        "Y": 0.40419116616249084,
                        "X": 0.6827319264411926,
                        "Type": "rightEyeBrowUp"
                    },
                    {
                        "Y": 0.41925403475761414,
                        "X": 0.32195475697517395,
                        "Type": "leftEyeLeft"
                    },
                    {
                        "Y": 0.4225293695926666,
                        "X": 0.41227561235427856,
                        "Type": "leftEyeRight"
                    },
                    {
                        "Y": 0.4096950888633728,
                        "X": 0.3705553412437439,
                        "Type": "leftEyeUp"
                    },
                    {
                        "Y": 0.4213259816169739,
                        "X": 0.36738231778144836,
                        "Type": "leftEyeDown"
                    },
                    {
                        "Y": 0.4294262230396271,
                        "X": 0.5498995184898376,
                        "Type": "rightEyeLeft"
                    },
                    {
                        "Y": 0.4327501356601715,
                        "X": 0.6390777826309204,
                        "Type": "rightEyeRight"
                    },
                    {
                        "Y": 0.42076829075813293,
                        "X": 0.5977370738983154,
                        "Type": "rightEyeUp"
                    },
                    {
                        "Y": 0.4326271116733551,
                        "X": 0.5959710478782654,
                        "Type": "rightEyeDown"
                    },
                    {
                        "Y": 0.5411174893379211,
                        "X": 0.4253743588924408,
                        "Type": "noseLeft"
                    },
                    {
                        "Y": 0.5450678467750549,
                        "X": 0.5309309959411621,
                        "Type": "noseRight"
                    },
                    {
                        "Y": 0.5795656442642212,
                        "X": 0.47389525175094604,
                        "Type": "mouthUp"
                    },
                    {
                        "Y": 0.6466911435127258,
                        "X": 0.47393468022346497,
                        "Type": "mouthDown"
                    }
                ],
                "Mustache": {
                    "Confidence": 99.75302124023438,
                    "Value": false
                },
                "Beard": {
                    "Confidence": 89.82911682128906,
                    "Value": false
                }
            },
            "Face": {
                "BoundingBox": {
                    "Width": 0.6153846383094788,
                    "Top": 0.24423076212406158,
                    "Left": 0.17654477059841156,
                    "Height": 0.4692307710647583
                },
                "FaceId": "407b95a5-f8f7-50c7-bf86-27c9ba5c6931",
                "ExternalImageId": "example-image.jpg",
                "Confidence": 99.99968719482422,
                "ImageId": "af554b0d-fcb2-56e8-9658-69aec6c901be"
            }
        }
    ],
    "OrientationCorrection": "ROTATE_0"
}
```