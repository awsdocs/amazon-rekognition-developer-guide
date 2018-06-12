# Detecting Faces in a Stored Video \(AWS SDK for Java\)<a name="faces-sqs-video"></a>

Amazon Rekognition can detect faces in a video that's stored in an Amazon S3 bucket\. This procedure expands on the code in [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), which uses an Amazon Simple Queue Service \(Amazon SQS\) queue to get the completion status of a video analysis request\. 

## Prerequisites<a name="moderate-images-prerequisites"></a>

To run this procedure, you need to have the AWS SDK for Java installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. 

**To detect faces in a video stored in an Amazon S3 bucket**

1. Perform [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md)\.

1. Add the following code to the project you created in step 1\.

   ```
    //Faces=======================================================================
      
      private static void StartFaces(String bucket, String video) throws Exception{
          
          StartFaceDetectionRequest req = new StartFaceDetectionRequest()
                  .withVideo(new Video()
                          .withS3Object(new S3Object()
                              .withBucket(bucket)
                              .withName(video)))
                  .withNotificationChannel(channel);
                              
                              
          
          StartFaceDetectionResult startLabelDetectionResult = rek.startFaceDetection(req);
          startJobId=startLabelDetectionResult.getJobId();
          
      } 
      
      private static void GetResultsFaces() throws Exception{
          
          int maxResults=10;
          String paginationToken=null;
          GetFaceDetectionResult faceDetectionResult=null;
          
          do{
              if (faceDetectionResult !=null){
                  paginationToken = faceDetectionResult.getNextToken();
              }
          
              faceDetectionResult = rek.getFaceDetection(new GetFaceDetectionRequest()
                   .withJobId(startJobId)
                   .withNextToken(paginationToken)
                   .withMaxResults(maxResults));
          
              VideoMetadata videoMetaData=faceDetectionResult.getVideoMetadata();
                  
              System.out.println("Format: " + videoMetaData.getFormat());
              System.out.println("Codec: " + videoMetaData.getCodec());
              System.out.println("Duration: " + videoMetaData.getDurationMillis());
              System.out.println("FrameRate: " + videoMetaData.getFrameRate());
                  
                  
              //Show faces, confidence and detection times
              List<FaceDetection> faces= faceDetectionResult.getFaces();
           
              for (FaceDetection face: faces) { 
                  long seconds=face.getTimestamp()/1000;
                  System.out.print("Sec: " + Long.toString(seconds) + " ");
                  System.out.println(face.getFace().toString());
                  System.out.println();           
              }
          } while (faceDetectionResult !=null && faceDetectionResult.getNextToken() != null);
            
              
      }
   ```

1. In the function `main`, replace the line 

    `StartLabels("bucket","file");` 

   with

    `StartFaces("bucket","file");` 

   If you've already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace is different\.

1. In the call to `StartFaces`, replace *bucket* and *file* with the Amazon S3 bucket name and file name of the video you want to analyze\.

1. In the function `main`, replace the line 

   `GetResultsLabels();`

   with

   `GetResultsFaces();`

   If you've already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace is different\.

1. Run the code\. Information about the faces that were detected in the video is shown\.

## <a name="getfacedetection-operation-response"></a>

`GetFaceDetection` returns an array \(`Faces`\) that contains information about the faces detected in the video\. An array element, [FaceDetection](API_FaceDetection.md), exists for each time a face is detected in the video\. The array elements returned are sorted by time, in milliseconds since the start of the video\.  The following example is a partial JSON response from `GetFaceDetection`\.

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
+ **Face information** – The `FaceDetection` array element contains information about the detected face \([FaceDetail](API_FaceDetail.md) and the time that the face was detected in the video \(`Timestamp`\)\.
+ **Paging information** – The example shows one page of face detection information\. You can specify how many person elements to return in the `MaxResults` input parameter for `GetFaceDetection`\. If more results than `MaxResults` exist, `GetFaceDetection` returns a token \(`NextToken`\) that's used to get the next page of results\. For more information, see [Getting Amazon Rekognition Video Analysis Results](api-video.md#api-video-get)\.
+ **Video information** – The response includes information about the video format \(`VideoMetadata`\) in each page of information that's returned by `GetFaceDetection`\.