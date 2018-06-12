# Tracking People through a Stored Video \(SDK for Java\)<a name="video-sqs-persons"></a>

The following procedure shows how to track people through a video stored in an Amazon S3 bucket\. The example expands on the code in [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md) which uses an Amazon Simple Queue Service queue to get the completion status of a video analysis request\. 

## Tracking People through a Stored Video \(SDK\)<a name="track-persons-example"></a>

To run these procedures, you need to have the AWS SDK for Java installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. You also need an image file that contains one or more celebrity faces\.

**To detect people in a video stored in an Amazon S3 bucket**

1. Perform [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md)\.

1. Add the following code to the project created in step one\.

   ```
     //Persons========================================================================
      
      private static void StartPersons(String bucket, String video) throws Exception{
          
          int maxResults=10;
          String paginationToken=null;
          
       StartPersonTrackingRequest req = new StartPersonTrackingRequest()
               .withVideo(new Video()
                       .withS3Object(new S3Object()
                           .withBucket(bucket)
                           .withName(video)))
               .withNotificationChannel(channel);
                              
           
          
       StartPersonTrackingResult startPersonDetectionResult = rek.startPersonTracking(req);
       startJobId=startPersonDetectionResult.getJobId();
          
      } 
      
      private static void GetResultsPersons() throws Exception{
          int maxResults=10;
          String paginationToken=null;
          GetPersonTrackingResult personTrackingResult=null;
          
          do{
              if (personTrackingResult !=null){
                  paginationToken = personTrackingResult.getNextToken();
              }
              
              personTrackingResult = rek.getPersonTracking(new GetPersonTrackingRequest()
                   .withJobId(startJobId)
                   .withNextToken(paginationToken)
                   .withSortBy(PersonTrackingSortBy.TIMESTAMP)
                   .withMaxResults(maxResults));
        
              VideoMetadata videoMetaData=personTrackingResult.getVideoMetadata();
                  
              System.out.println("Format: " + videoMetaData.getFormat());
              System.out.println("Codec: " + videoMetaData.getCodec());
              System.out.println("Duration: " + videoMetaData.getDurationMillis());
              System.out.println("FrameRate: " + videoMetaData.getFrameRate());
                  
                  
              //Show persons, confidence and detection times
              List<PersonDetection> detectedPersons= personTrackingResult.getPersons();
           
              for (PersonDetection detectedPerson: detectedPersons) { 
                  
                 long seconds=detectedPerson.getTimestamp()/1000;
                 System.out.print("Sec: " + Long.toString(seconds) + " ");
                 System.out.println("Person Identifier: "  + detectedPerson.getPerson().getIndex());
                    System.out.println();             
              }
          }  while (personTrackingResult !=null && personTrackingResult.getNextToken() != null);
          
      }
   ```

1. In the function `main`, replace the line 

    `StartLabels("bucket","file");` 

   with

    `StartPersons("bucket","file");` 

   If you have already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace will be different\.

1. In the call to `StartPersons`, replace *bucket* and *file* with the Amazon S3 bucket name and file name of the video you want to analyze\.

1. In the function `main`, replace the line 

   `GetResultsLabels();`

   with

   `GetResultsPersons();`

   If you have already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with the AWS SDK for Java](video-analyzing-with-sqs.md), the function name to replace will be different\.

1. Run the code\. The unique identifiers for tracked people are shown along with the time, in seconds, the people were tracked\.

## Operation Response<a name="getresultspersons-operation-response"></a>

`GetPersonTracking` returns an array, `Persons`, of [PersonDetection](API_PersonDetection.md) objects which contain details about tracked people and the times they are tracked in the video\. 

You can sort `Persons` by using the `SortBy` input parameter\. Specify `TIMESTAMP` to sort the elements by the time people are detected in the video\. Specify `INDEX` to sort by people tracked in the video\. Within each set of results for a person, the elements are sorted by descending confidence in the accuracy of the tracking\. By default, `Persons` is returned sorted by `TIMESTAMP`\. The following example is the JSON response from `GetPersonDetection`\. The results are sorted by the time, in milliseconds since the start of the video, people are tracked in the video\.

```
{
    "JobStatus": "SUCCEEDED",
    "NextToken": "AcDymG0fSSoaI6+BBYpka5wVlqttysSPP8VvWcujMDluj1QpFo/vf+mrMoqBGk8eUEiFlllR6g==",
    "Persons": [
        {
            "Person": {
                "BoundingBox": {
                    "Height": 0.8787037134170532,
                    "Left": 0.00572916679084301,
                    "Top": 0.12129629403352737,
                    "Width": 0.21666666865348816
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
                "Index": 0
            },
            "Timestamp": 0
        },
        {
            "Person": {
                "BoundingBox": {
                    "Height": 0.9074074029922485,
                    "Left": 0.24791666865348816,
                    "Top": 0.09259258955717087,
                    "Width": 0.375
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
                "Index": 1
            },
            "Timestamp": 0
        }.....

    ],
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
+ **Person information** – The `PersonDetection` array element contains information about the detected person\. For example, the time the person was detected \(`Timestamp`\), the position of the person in the video frame at the time they were detected \(`BoundingBox`\), and how confident Amazon Rekognition Video is that the person has been correctly detected \(`Confidence`\)\.

  Facial features are not returned at every timestamp for which the person is tracked\. Furthermore, in some circumstances a tracked person's body might not be visible, in which case only their face location is returned\.
+ **Paging information** – The example shows one page of person detection information\. You can specify how many person elements to return in the `MaxResults` input parameter for `GetPersonTracking`\. If more results than `MaxResults` exist, `GetPersonTracking` returns a token \(`NextToken`\) used to get the next page of results\. For more information, see [Getting Amazon Rekognition Video Analysis Results](api-video.md#api-video-get)\.
+ **Index** – A unique identifier for tracking the person throughout the video\. 
+ **Video information** – The response includes information about the video format \(`VideoMetadata`\) in each page of information returned by `GetPersonDetection`\.