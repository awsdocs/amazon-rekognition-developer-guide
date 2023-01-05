# Searching stored videos for faces<a name="procedure-person-search-videos"></a>

You can search a collection for faces that match faces of people who are detected in a stored video or a streaming video\. This section covers searching for faces in a stored video\. For information about searching for faces in a streaming video, see [Working with streaming video events](streaming-video.md)\.

The faces that you search for must first be indexed into a collection by using [IndexFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_IndexFaces.html)\. For more information, see [Adding faces to a collection](add-faces-to-collection-procedure.md)\. 

Amazon Rekognition Video face searching follows the same asynchronous workflow as other Amazon Rekognition Video operations that analyze videos stored in an Amazon S3 bucket\. To start searching for faces in a stored video, call [StartFaceSearch](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceSearch.html) and provide the ID of the collection that you want to search\. Amazon Rekognition Video publishes the completion status of the video analysis to an Amazon Simple Notification Service \(Amazon SNS\) topic\. If the video analysis is successful, call [GetFaceSearch](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GeFaceSearch.html) to get the search results\. For more information about starting video analysis and getting the results, see [Calling Amazon Rekognition Video operations](api-video.md)\. 

The following procedure shows how to search a collection for faces that match the faces of people who are detected in a video\. The procedure also shows how to get the tracking data for people who are matched in the video\. The procedure expands on the code in [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md), which uses an Amazon Simple Queue Service \(Amazon SQS\) queue to get the completion status of a video analysis request\. 

**To search a video for matching faces \(SDK\)**

1. [Create a collection](create-collection-procedure.md)\.

1. [Index a face into the collection](add-faces-to-collection-procedure.md)\.

1. Perform [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md)\.

1. Add the following code to the class `VideoDetect` that you created in step 3\.

------
#### [ Java ]

   ```
      //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
      //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
          //Face collection search in video ==================================================================
          private static void StartFaceSearchCollection(String bucket, String video, String collection) throws Exception{
   
           NotificationChannel channel= new NotificationChannel()
                   .withSNSTopicArn(snsTopicArn)
                   .withRoleArn(roleArn);
   
           StartFaceSearchRequest req = new StartFaceSearchRequest()
                   .withCollectionId(collection)
                   .withVideo(new Video()
                           .withS3Object(new S3Object()
                                   .withBucket(bucket)
                                   .withName(video)))
                   .withNotificationChannel(channel);
   
   
   
           StartFaceSearchResult startPersonCollectionSearchResult = rek.startFaceSearch(req);
           startJobId=startPersonCollectionSearchResult.getJobId();
   
       } 
   
       //Face collection search in video ==================================================================
       private static void GetFaceSearchCollectionResults() throws Exception{
   
          GetFaceSearchResult faceSearchResult=null;
          int maxResults=10;
          String paginationToken=null;
   
          do {
   
              if (faceSearchResult !=null){
                  paginationToken = faceSearchResult.getNextToken();
              }
   
   
              faceSearchResult  = rek.getFaceSearch(
                      new GetFaceSearchRequest()
                      .withJobId(startJobId)
                      .withMaxResults(maxResults)
                      .withNextToken(paginationToken)
                      .withSortBy(FaceSearchSortBy.TIMESTAMP)
                      );
   
   
              VideoMetadata videoMetaData=faceSearchResult.getVideoMetadata();
   
              System.out.println("Format: " + videoMetaData.getFormat());
              System.out.println("Codec: " + videoMetaData.getCodec());
              System.out.println("Duration: " + videoMetaData.getDurationMillis());
              System.out.println("FrameRate: " + videoMetaData.getFrameRate());
              System.out.println();      
   
   
              //Show search results
              List<PersonMatch> matches= 
                      faceSearchResult.getPersons();
   
              for (PersonMatch match: matches) { 
                  long milliSeconds=match.getTimestamp();
                  System.out.print("Timestamp: " + Long.toString(milliSeconds));
                  System.out.println(" Person number: " + match.getPerson().getIndex());
                  List <FaceMatch> faceMatches = match.getFaceMatches();
                  if (faceMatches != null) {
                      System.out.println("Matches in collection...");
                      for (FaceMatch faceMatch: faceMatches){
                          Face face=faceMatch.getFace();
                          System.out.println("Face Id: "+ face.getFaceId());
                          System.out.println("Similarity: " + faceMatch.getSimilarity().toString());
                          System.out.println();
                      }
                  }
                  System.out.println();           
              } 
   
              System.out.println(); 
   
          } while (faceSearchResult !=null && faceSearchResult.getNextToken() != null);
   
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
           String collection="collection";
           StartFaceSearchCollection(bucket, video, collection);
   
           if (GetSQSMessageSuccess()==true)
           	GetFaceSearchCollectionResults();
   ```

------
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/VideoDetectFaces.java)\.

   ```
       public static void StartFaceDetection(RekognitionClient rekClient,
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
   
               StartFaceDetectionRequest  faceDetectionRequest = StartFaceDetectionRequest.builder()
                   .jobTag("Faces")
                   .faceAttributes(FaceAttributes.ALL)
                   .notificationChannel(channel)
                   .video(vidOb)
                   .build();
   
               StartFaceDetectionResponse startLabelDetectionResult = rekClient.startFaceDetection(faceDetectionRequest);
               startJobId=startLabelDetectionResult.jobId();
   
           } catch(RekognitionException e) {
               System.out.println(e.getMessage());
               System.exit(1);
           }
       }
   
       public static void GetFaceResults(RekognitionClient rekClient) {
   
           try {
               String paginationToken=null;
               GetFaceDetectionResponse faceDetectionResponse=null;
               boolean finished = false;
               String status;
               int yy=0 ;
   
               do{
                   if (faceDetectionResponse !=null)
                       paginationToken = faceDetectionResponse.nextToken();
   
                   GetFaceDetectionRequest recognitionRequest = GetFaceDetectionRequest.builder()
                       .jobId(startJobId)
                       .nextToken(paginationToken)
                       .maxResults(10)
                       .build();
   
                   // Wait until the job succeeds
                   while (!finished) {
   
                       faceDetectionResponse = rekClient.getFaceDetection(recognitionRequest);
                       status = faceDetectionResponse.jobStatusAsString();
   
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
                   VideoMetadata videoMetaData=faceDetectionResponse.videoMetadata();
                   System.out.println("Format: " + videoMetaData.format());
                   System.out.println("Codec: " + videoMetaData.codec());
                   System.out.println("Duration: " + videoMetaData.durationMillis());
                   System.out.println("FrameRate: " + videoMetaData.frameRate());
                   System.out.println("Job");
   
                   // Show face information
                   List<FaceDetection> faces= faceDetectionResponse.faces();
   
                   for (FaceDetection face: faces) {
                       String age = face.face().ageRange().toString();
                       String smile = face.face().smile().toString();
                       System.out.println("The detected face is estimated to be"
                                   + age + " years old.");
                       System.out.println("There is a smile : "+smile);
                   }
   
               } while (faceDetectionResponse !=null && faceDetectionResponse.nextToken() != null);
   
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
   
       # ============== Face Search ===============
       def StartFaceSearchCollection(self,collection):
           response = self.rek.start_face_search(Video={'S3Object':{'Bucket':self.bucket,'Name':self.video}},
               CollectionId=collection,
               NotificationChannel={'RoleArn':self.roleArn, 'SNSTopicArn':self.snsTopicArn})
           
           self.startJobId=response['JobId']
           
           print('Start Job Id: ' + self.startJobId)
   
   
       def GetFaceSearchCollectionResults(self):
           maxResults = 10
           paginationToken = ''
   
           finished = False
   
           while finished == False:
               response = self.rek.get_face_search(JobId=self.startJobId,
                                           MaxResults=maxResults,
                                           NextToken=paginationToken)
   
               print(response['VideoMetadata']['Codec'])
               print(str(response['VideoMetadata']['DurationMillis']))
               print(response['VideoMetadata']['Format'])
               print(response['VideoMetadata']['FrameRate'])
   
               for personMatch in response['Persons']:
                   print('Person Index: ' + str(personMatch['Person']['Index']))
                   print('Timestamp: ' + str(personMatch['Timestamp']))
   
                   if ('FaceMatches' in personMatch):
                       for faceMatch in personMatch['FaceMatches']:
                           print('Face ID: ' + faceMatch['Face']['FaceId'])
                           print('Similarity: ' + str(faceMatch['Similarity']))
                   print()
               if 'NextToken' in response:
                   paginationToken = response['NextToken']
               else:
                   finished = True
               print()
   ```

   In the function `main`, replace the lines:

   ```
       analyzer.StartLabelDetection()
       if analyzer.GetSQSMessageSuccess()==True:
           analyzer.GetLabelDetectionResults()
   ```

   with:

   ```
       collection='tests'
       analyzer.StartFaceSearchCollection(collection)
       
       if analyzer.GetSQSMessageSuccess()==True:
           analyzer.GetFaceSearchCollectionResults()
   ```

------

   If you've already run a video example other than [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md), the code to replace might be different\.

1. Change the value of `collection` to the name of the collection you created in step 1\.

1. Run the code\. A list of people in the video whose faces match those in the input collection is displayed\. The tracking data for each matched person is also displayed\.

## GetFaceSearch operation response<a name="searchfacesvideo-operation-response"></a>

The following is an example JSON response from `GetFaceSearch`\.

The response includes an array of people \(`Persons`\) detected in the video whose faces match a face in the input collection\. An array element, [PersonMatch](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_PersonMatch.html), exists for each time the person is matched in the video\. Each `PersonMatch` includes an array of face matches from the input collection, [FaceMatch](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_FaceMatch.html), information about the matched person, [PersonDetail](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_PersonDetail.html), and the time the person was matched in the video\. 

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