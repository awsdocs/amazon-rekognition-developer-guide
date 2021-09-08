# People pathing<a name="persons"></a>

Amazon Rekognition Video can create a track of the path people take in videos and provide information such as: 
+ The location of the person in the video frame at the time their path is tracked\.
+ Facial landmarks such as the position of the left eye, when detected\. 

Amazon Rekognition Video people pathing in stored videos is an asynchronous operation\. To start the pathing of people in videos call [ StartPersonTracking ](API_StartPersonTracking.md)\. Amazon Rekognition Video publishes the completion status of the video analysis to an Amazon Simple Notification Service topic\. If the video analysis is succesful, call [ GetPersonTracking ](API_GetPersonTracking.md) to get results of the video analysis\. For more information about calling Amazon Rekognition Video API operations, see [Calling Amazon Rekognition Video operations](api-video.md)\. 

The following procedure shows how to track the path of people through a video stored in an Amazon S3 bucket\. The example expands on the code in [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md) which uses an Amazon Simple Queue Service queue to get the completion status of a video analysis request\. 

**To detect people in a video stored in an Amazon S3 bucket \(SDK\)**

1. Perform [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md)\.

1. Add the following code to the class `VideoDetect` that you created in step 1\.

------
#### [ Java ]

   ```
          //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
          //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
           //Persons========================================================================
           private static void StartPersonDetection(String bucket, String video) throws Exception{
               
               
               NotificationChannel channel= new NotificationChannel()
                       .withSNSTopicArn(snsTopicArn)
                       .withRoleArn(roleArn);
               
            StartPersonTrackingRequest req = new StartPersonTrackingRequest()
                    .withVideo(new Video()
                            .withS3Object(new S3Object()
                                .withBucket(bucket)
                                .withName(video)))
                    .withNotificationChannel(channel);
                                   
                
               
            StartPersonTrackingResult startPersonDetectionResult = rek.startPersonTracking(req);
            startJobId=startPersonDetectionResult.getJobId();
               
           } 
           
           private static void GetPersonDetectionResults() throws Exception{
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

   In the function `main`, replace the lines: 

   ```
           StartLabelDetection(bucket, video);
   
           if (GetSQSMessageSuccess()==true)
           	GetLabelDetectionResults();
   ```

   with:

   ```
           StartPersonDetection(bucket, video);
   
           if (GetSQSMessageSuccess()==true)
           	GetPersonDetectionResults();
   ```

------
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/VideoPersonDetection.java)\.

   ```
       public static void startPersonLabels(RekognitionClient rekClient,
                                          NotificationChannel channel,
                                          String bucket,
                                          String video) {
           try {
               S3Object s3Obj = S3Object.builder()
                       .bucket(bucket)
                       .name(video)
                       .build();
   
               Video vidOb = Video.builder()
                       .s3Object(s3Obj)
                       .build();
   
               StartPersonTrackingRequest personTrackingRequest = StartPersonTrackingRequest.builder()
                       .jobTag("DetectingLabels")
                       .video(vidOb)
                       .notificationChannel(channel)
                       .build();
   
               StartPersonTrackingResponse labelDetectionResponse = rekClient.startPersonTracking(personTrackingRequest);
               startJobId = labelDetectionResponse.jobId();
   
           } catch(RekognitionException e) {
               System.out.println(e.getMessage());
               System.exit(1);
           }
       }
   
       public static void GetPersonDetectionResults(RekognitionClient rekClient) {
   
           try {
               String paginationToken=null;
               GetPersonTrackingResponse personTrackingResult=null;
               Boolean finished = false;
               String status="";
               int yy=0 ;
   
               do{
                   if (personTrackingResult !=null)
                       paginationToken = personTrackingResult.nextToken();
   
                   GetPersonTrackingRequest recognitionRequest = GetPersonTrackingRequest.builder()
                           .jobId(startJobId)
                           .nextToken(paginationToken)
                           .maxResults(10)
                           .build();
   
                   // Wait until the job succeeds
                   while (!finished) {
   
                       personTrackingResult = rekClient.getPersonTracking(recognitionRequest);
                       status = personTrackingResult.jobStatusAsString();
   
                       if (status.compareTo("SUCCEEDED") == 0)
                           finished = true;
                       else {
                           System.out.println(yy + " status is: " + status);
                           Thread.sleep(1000);
                       }
                       yy++;
                   }
   
                   finished = false;
   
                   // Proceed when the job is done - otherwise VideoMetadata is null
                   VideoMetadata videoMetaData=personTrackingResult.videoMetadata();
   
                   System.out.println("Format: " + videoMetaData.format());
                   System.out.println("Codec: " + videoMetaData.codec());
                   System.out.println("Duration: " + videoMetaData.durationMillis());
                   System.out.println("FrameRate: " + videoMetaData.frameRate());
                   System.out.println("Job");
   
                   List<PersonDetection> detectedPersons= personTrackingResult.persons();
                   for (PersonDetection detectedPerson: detectedPersons) {
   
                       long seconds=detectedPerson.timestamp()/1000;
                       System.out.print("Sec: " + seconds + " ");
                       System.out.println("Person Identifier: "  + detectedPerson.person().index());
                       System.out.println();
                   }
   
               } while (personTrackingResult !=null && personTrackingResult.nextToken() != null);
   
           } catch(RekognitionException | InterruptedException e) {
               System.out.println(e.getMessage());
               System.exit(1);
           }
       }
   ```

------
#### [ Python ]

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
       # ============== People pathing ===============  
       def StartPersonPathing(self):
           response=self.rek.start_person_tracking(Video={'S3Object': {'Bucket': self.bucket, 'Name': self.video}},
               NotificationChannel={'RoleArn': self.roleArn, 'SNSTopicArn': self.snsTopicArn})
   
           self.startJobId=response['JobId']
           print('Start Job Id: ' + self.startJobId)
       
       def GetPersonPathingResults(self):
           maxResults = 10
           paginationToken = ''
           finished = False
   
           while finished == False:
               response = self.rek.get_person_tracking(JobId=self.startJobId,
                                               MaxResults=maxResults,
                                               NextToken=paginationToken)
   
               print('Codec: ' + response['VideoMetadata']['Codec'])
               print('Duration: ' + str(response['VideoMetadata']['DurationMillis']))
               print('Format: ' + response['VideoMetadata']['Format'])
               print('Frame rate: ' + str(response['VideoMetadata']['FrameRate']))
               print()
   
               for personDetection in response['Persons']:
                   print('Index: ' + str(personDetection['Person']['Index']))
                   print('Timestamp: ' + str(personDetection['Timestamp']))
                   print()
   
               if 'NextToken' in response:
                   paginationToken = response['NextToken']
               else:
                   finished = True
   ```

   In the function `main`, replace the lines:

   ```
       analyzer.StartLabelDetection()
       if analyzer.GetSQSMessageSuccess()==True:
           analyzer.GetLabelDetectionResults()
   ```

   with:

   ```
       analyzer.StartPersonPathing()
       if analyzer.GetSQSMessageSuccess()==True:
           analyzer.GetPersonPathingResults()
   ```

------
**Note**  
If you've already run a video example other than [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md), the code to replace might be different\.

1. Run the code\. The unique identifiers for tracked people are shown along with the time, in seconds, the people's paths were tracked\.

## GetPersonTracking operation response<a name="getresultspersons-operation-response"></a>

`GetPersonTracking` returns an array, `Persons`, of [ PersonDetection ](API_PersonDetection.md) objects which contain details about people detected in the video and when their paths are tracked\. 

You can sort `Persons` by using the `SortBy` input parameter\. Specify `TIMESTAMP` to sort the elements by the time people's paths are tracked in the video\. Specify `INDEX` to sort by people tracked in the video\. Within each set of results for a person, the elements are sorted by descending confidence in the accuracy of the path tracking\. By default, `Persons` is returned sorted by `TIMESTAMP`\. The following example is the JSON response from `GetPersonDetection`\. The results are sorted by the time, in milliseconds since the start of the video, that people's paths are tracked in the video\. In the response, note the following:
+ **Person information** – The `PersonDetection` array element contains information about the detected person\. For example, the time the person was detected \(`Timestamp`\), the position of the person in the video frame at the time they were detected \(`BoundingBox`\), and how confident Amazon Rekognition Video is that the person has been correctly detected \(`Confidence`\)\.

  Facial features are not returned at every timestamp for which the person's path is tracked\. Furthermore, in some circumstances a tracked person's body might not be visible, in which case only their face location is returned\.
+ **Paging information** – The example shows one page of person detection information\. You can specify how many person elements to return in the `MaxResults` input parameter for `GetPersonTracking`\. If more results than `MaxResults` exist, `GetPersonTracking` returns a token \(`NextToken`\) used to get the next page of results\. For more information, see [Getting Amazon Rekognition Video analysis results](api-video.md#api-video-get)\.
+ **Index** – A unique identifier for identifying the person throughout the video\. 
+ **Video information** – The response includes information about the video format \(`VideoMetadata`\) in each page of information returned by `GetPersonDetection`\.

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