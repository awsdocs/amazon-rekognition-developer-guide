# Example: Detecting segments in a stored video<a name="segment-example"></a>

The following procedure shows how to detect technical cue segments and shot detection segments in a video stored in an Amazon S3 bucket\. The procedure also shows how to filter detected segments based on the confidence that Amazon Rekognition Video has in the accuracy of the detection\.

The example expands on the code in [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md) which uses an Amazon Simple Queue Service queue to get the completion status of a video analysis request\. 

**To detect segments in a video stored in an Amazon S3 bucket \(SDK\)**

1. Perform [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md)\.

1. Add the following to the code that you used in step 1\.

------
#### [ Java ]

   1. Add the following imports\.

      ```
      import com.amazonaws.services.rekognition.model.GetSegmentDetectionRequest;
      import com.amazonaws.services.rekognition.model.GetSegmentDetectionResult;
      import com.amazonaws.services.rekognition.model.SegmentDetection;
      import com.amazonaws.services.rekognition.model.SegmentType;
      import com.amazonaws.services.rekognition.model.SegmentTypeInfo;
      import com.amazonaws.services.rekognition.model.ShotSegment;
      import com.amazonaws.services.rekognition.model.StartSegmentDetectionFilters;
      import com.amazonaws.services.rekognition.model.StartSegmentDetectionRequest;
      import com.amazonaws.services.rekognition.model.StartSegmentDetectionResult;
      import com.amazonaws.services.rekognition.model.StartShotDetectionFilter;
      import com.amazonaws.services.rekognition.model.StartTechnicalCueDetectionFilter;
      import com.amazonaws.services.rekognition.model.TechnicalCueSegment;
      import com.amazonaws.services.rekognition.model.AudioMetadata;
      ```

   1. Add the following code to the class `VideoDetect`\.

      ```
          //Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
          //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
      
      
          private static void StartSegmentDetection(String bucket, String video) throws Exception{
                  
              NotificationChannel channel= new NotificationChannel()
                      .withSNSTopicArn(snsTopicArn)
                      .withRoleArn(roleArn);
      
              float minTechnicalCueConfidence = 80F; 
              float minShotConfidence = 80F; 
                      
              StartSegmentDetectionRequest req = new StartSegmentDetectionRequest()
                      .withVideo(new Video()
                              .withS3Object(new S3Object()
                                      .withBucket(bucket)
                                      .withName(video)))
                      .withSegmentTypes("TECHNICAL_CUE" , "SHOT")
                      .withFilters(new StartSegmentDetectionFilters()
                              .withTechnicalCueFilter(new StartTechnicalCueDetectionFilter()
                                      .withMinSegmentConfidence(minTechnicalCueConfidence))
                              .withShotFilter(new StartShotDetectionFilter()
                                      .withMinSegmentConfidence(minShotConfidence)))
                      .withJobTag("DetectingVideoSegments")
                      .withNotificationChannel(channel);
      
              StartSegmentDetectionResult startLabelDetectionResult = rek.startSegmentDetection(req);
              startJobId=startLabelDetectionResult.getJobId();
              
          }
      
          private static void GetSegmentDetectionResults() throws Exception{
      
              int maxResults=10;
              String paginationToken=null;
              GetSegmentDetectionResult segmentDetectionResult=null;
              Boolean firstTime=true;
              
      
              do {
                  if (segmentDetectionResult !=null){
                      paginationToken = segmentDetectionResult.getNextToken();
                  }
      
                  GetSegmentDetectionRequest segmentDetectionRequest= new GetSegmentDetectionRequest()
                          .withJobId(startJobId)
                          .withMaxResults(maxResults)
                          .withNextToken(paginationToken);
      
                  segmentDetectionResult = rek.getSegmentDetection(segmentDetectionRequest);
                  
                  if(firstTime) {
                      System.out.println("\nStatus\n------");
                      System.out.println(segmentDetectionResult.getJobStatus());
                      System.out.println("\nRequested features\n------------------");
                       for (SegmentTypeInfo requestedFeatures : segmentDetectionResult.getSelectedSegmentTypes()) {
                          System.out.println(requestedFeatures.getType());
                      }
                       int count=1;
                       List<VideoMetadata> videoMetaDataList = segmentDetectionResult.getVideoMetadata();
                       System.out.println("\nVideo Streams\n-------------");
                       for (VideoMetadata videoMetaData: videoMetaDataList) {
                           System.out.println("Stream: " + count++);
                           System.out.println("\tFormat: " + videoMetaData.getFormat());
                           System.out.println("\tCodec: " + videoMetaData.getCodec());
                           System.out.println("\tDuration: " + videoMetaData.getDurationMillis());
                           System.out.println("\tFrameRate: " + videoMetaData.getFrameRate());
                       } 
      
                       
                       List<AudioMetadata> audioMetaDataList = segmentDetectionResult.getAudioMetadata();
                       System.out.println("\nAudio streams\n-------------");
      
                       count=1;
                       for (AudioMetadata audioMetaData: audioMetaDataList) {
                           System.out.println("Stream: " + count++);
                           System.out.println("\tSample Rate: " + audioMetaData.getSampleRate());
                           System.out.println("\tCodec: " + audioMetaData.getCodec());
                           System.out.println("\tDuration: " + audioMetaData.getDurationMillis());
                           System.out.println("\tNumber of Channels: " + audioMetaData.getNumberOfChannels());
                       }
                       System.out.println("\nSegments\n--------");
      
                      firstTime=false;
                  }
      
      
                  //Show segment information
      
                  List<SegmentDetection> detectedSegments= segmentDetectionResult.getSegments();
                  
                  for (SegmentDetection detectedSegment: detectedSegments) { 
                      
                     if (detectedSegment.getType().contains(SegmentType.TECHNICAL_CUE.toString())) {
                          System.out.println("Technical Cue");
                          TechnicalCueSegment segmentCue=detectedSegment.getTechnicalCueSegment();
                          System.out.println("\tType: " + segmentCue.getType()); 
                          System.out.println("\tConfidence: " + segmentCue.getConfidence().toString());
                      }
                     if (detectedSegment.getType().contains(SegmentType.SHOT.toString())) { 
                          System.out.println("Shot");
                          ShotSegment segmentShot=detectedSegment.getShotSegment();
                          System.out.println("\tIndex " + segmentShot.getIndex()); 
                          System.out.println("\tConfidence: " + segmentShot.getConfidence().toString());
                      }
                      long seconds=detectedSegment.getDurationMillis();
                      System.out.println("\tDuration : " + Long.toString(seconds) + " milliseconds");
                      System.out.println("\tStart time code: " + detectedSegment.getStartTimecodeSMPTE());
                      System.out.println("\tEnd time code: " + detectedSegment.getEndTimecodeSMPTE());
                      System.out.println("\tDuration time code: " + detectedSegment.getDurationSMPTE());
                      System.out.println();
                                      
                   } 
                         
              } while (segmentDetectionResult !=null && segmentDetectionResult.getNextToken() != null);
      
          }
      ```

   1. In the function `main`, replace the lines: 

      ```
              StartLabelDetection(bucket, video);
      
              if (GetSQSMessageSuccess()==true)
              	GetLabelDetectionResults();
      ```

      with:

      ```
              StartSegmentDetection(bucket, video);
      
              if (GetSQSMessageSuccess()==true)
              	GetSegmentDetectionResults();
      ```

------
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/VideoDetectSegment.java)\.

   ```
       public static void StartSegmentDetection (RekognitionClient rekClient,
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
   
               StartShotDetectionFilter cueDetectionFilter = StartShotDetectionFilter.builder()
                       .minSegmentConfidence(60F)
                       .build();
   
               StartTechnicalCueDetectionFilter technicalCueDetectionFilter = StartTechnicalCueDetectionFilter.builder()
                       .minSegmentConfidence(60F)
                       .build();
   
               StartSegmentDetectionFilters filters = StartSegmentDetectionFilters.builder()
                       .shotFilter(cueDetectionFilter)
                       .technicalCueFilter(technicalCueDetectionFilter)
                       .build();
   
               StartSegmentDetectionRequest segDetectionRequest = StartSegmentDetectionRequest.builder()
                       .jobTag("DetectingLabels")
                       .notificationChannel(channel)
                       .segmentTypes(SegmentType.TECHNICAL_CUE , SegmentType.SHOT)
                       .video(vidOb)
                       .filters(filters)
                       .build();
   
               StartSegmentDetectionResponse segDetectionResponse = rekClient.startSegmentDetection(segDetectionRequest);
               startJobId = segDetectionResponse.jobId();
   
           } catch(RekognitionException e) {
               e.getMessage();
               System.exit(1);
           }
       }
   
       public static void getSegmentResults(RekognitionClient rekClient) {
   
           try {
               String paginationToken = null;
               GetSegmentDetectionResponse segDetectionResponse = null;
               Boolean finished = false;
               String status = "";
               int yy = 0;
   
               do {
   
                   if (segDetectionResponse != null)
                       paginationToken = segDetectionResponse.nextToken();
   
                   GetSegmentDetectionRequest recognitionRequest = GetSegmentDetectionRequest.builder()
                           .jobId(startJobId)
                           .nextToken(paginationToken)
                           .maxResults(10)
                           .build();
   
                   // Wait until the job succeeds
                   while (!finished) {
   
                       segDetectionResponse = rekClient.getSegmentDetection(recognitionRequest);
                       status = segDetectionResponse.jobStatusAsString();
   
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
                   List<VideoMetadata> videoMetaData = segDetectionResponse.videoMetadata();
   
                   for (VideoMetadata metaData : videoMetaData) {
                       System.out.println("Format: " + metaData.format());
                       System.out.println("Codec: " + metaData.codec());
                       System.out.println("Duration: " + metaData.durationMillis());
                       System.out.println("FrameRate: " + metaData.frameRate());
                       System.out.println("Job");
                   }
   
                   List<SegmentDetection> detectedSegment = segDetectionResponse.segments();
                   String type = detectedSegment.get(0).type().toString();
   
                   if (type.contains(SegmentType.TECHNICAL_CUE.toString())) {
                       System.out.println("Technical Cue");
                       TechnicalCueSegment segmentCue = detectedSegment.get(0).technicalCueSegment();
                       System.out.println("\tType: " + segmentCue.type());
                       System.out.println("\tConfidence: " + segmentCue.confidence().toString());
                   }
                   if (type.contains(SegmentType.SHOT.toString())) {
                       System.out.println("Shot");
                       ShotSegment segmentShot = detectedSegment.get(0).shotSegment();
                       System.out.println("\tIndex " + segmentShot.index());
                       System.out.println("\tConfidence: " + segmentShot.confidence().toString());
                   }
                   long seconds = detectedSegment.get(0).durationMillis();
                   System.out.println("\tDuration : " + Long.toString(seconds) + " milliseconds");
                   System.out.println("\tStart time code: " + detectedSegment.get(0).startTimecodeSMPTE());
                   System.out.println("\tEnd time code: " + detectedSegment.get(0).endTimecodeSMPTE());
                   System.out.println("\tDuration time code: " + detectedSegment.get(0).durationSMPTE());
                   System.out.println();
   
           } while (segDetectionResponse !=null && segDetectionResponse.nextToken() != null);
   
           } catch(RekognitionException | InterruptedException e) {
               System.out.println(e.getMessage());
               System.exit(1);
           }
       }
   ```

------
#### [ Python ]

   1. Add the following code to the class `VideoDetect` that you created in step 1\.

      ```
      #Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
      #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
      
          def StartSegmentDetection(self):
      
              min_Technical_Cue_Confidence = 80.0
              min_Shot_Confidence = 80.0
      
              response=self.rek.start_segment_detection(Video={'S3Object': {'Bucket': self.bucket, 'Name': self.video}},
                  NotificationChannel={'RoleArn': self.roleArn, 'SNSTopicArn': self.snsTopicArn},
                  SegmentTypes=['TECHNICAL_CUE' , 'SHOT'],
                  Filters={'TechnicalCueFilter': {'MinSegmentConfidence':min_Technical_Cue_Confidence},
                      'ShotFilter': {'MinSegmentConfidence': min_Shot_Confidence}})
                 
      
              self.startJobId=response['JobId']
              print('Start Job Id: ' + self.startJobId)
      
          def GetSegmentDetectionResults(self):
              maxResults = 10
              paginationToken = ''
              finished = False
              firstTime = True
      
              while finished == False:
                  response = self.rek.get_segment_detection(JobId=self.startJobId,
                                                      MaxResults=maxResults,
                                                      NextToken=paginationToken)
      
                  if firstTime == True:
                      print('Status\n------\n' + response['JobStatus'])
                      print ('\nRequested Types\n---------------')
                      for selectedSegmentType in response['SelectedSegmentTypes']:
                          print("\tType: " + selectedSegmentType['Type'])
                          print("\t\tModel Version: " + selectedSegmentType['ModelVersion'])
      
                      print()
                      print('\nAudio metadata\n--------------')
                      for audioMetadata in response['AudioMetadata']:
                          print('\tCodec: ' + audioMetadata['Codec'])            
                          print('\tDuration: ' + str(audioMetadata['DurationMillis']))
                          print('\tNumber of Channels: ' + str(audioMetadata['NumberOfChannels']))
                          print('\tSample rate: ' + str(audioMetadata['SampleRate']))
                      print()
                      print ('\nVideo metadata\n--------------')
                      for videoMetadata in response['VideoMetadata']:
                          print('\tCodec: ' + videoMetadata['Codec'])
                          print('\tDuration: ' + str(videoMetadata['DurationMillis']))
                          print('\tFormat: ' + videoMetadata['Format'])
                          print('\tFrame rate: ' + str(videoMetadata['FrameRate'])) 
                          print('\nSegments\n--------')
                      
                      firstTime = False    
      
      
                  for segment in response['Segments']:
      
                      if segment ['Type'] == 'TECHNICAL_CUE':
                          print('Technical Cue')
                          print('\tConfidence: ' + 
                              str(segment['TechnicalCueSegment']['Confidence']))
                          print('\tType: ' + 
                              segment['TechnicalCueSegment']['Type'])  
      
                      if segment ['Type'] == 'SHOT':
                          print ('Shot')
                          print('\tConfidence: ' + 
                              str(segment['ShotSegment']['Confidence']))  
                          print('\tIndex: ' + 
                              str(segment['ShotSegment']['Index']))  
      
                      print('\tDuration (milliseconds): ' + str(segment['DurationMillis']))
                      print('\tStart Timestamp (milliseconds): ' + str(segment['StartTimestampMillis']))
                      print('\tEnd Timestamp (milliseconds): ' + str(segment['EndTimestampMillis']))
                      print('\tStart timecode: ' + segment['StartTimecodeSMPTE'])
                      print('\tEnd timecode: ' + segment['EndTimecodeSMPTE'])
                      print('\tDuration timecode: ' + segment['DurationSMPTE'])
                      print()
                      
                  if 'NextToken' in response:
                      paginationToken = response['NextToken']
                  else:
                      finished = True
      ```

   1. In the function `main`, replace the lines:

      ```
          analyzer.StartLabelDetection()
          if analyzer.GetSQSMessageSuccess()==True:
              analyzer.GetLabelDetectionResults()
      ```

      with:

      ```
          analyzer.StartSegmentDetection()
          if analyzer.GetSQSMessageSuccess()==True:
              analyzer.GetSegmentDetectionResults()
      ```

------
**Note**  
If you've already run a video example other than [Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md), the code to replace might be different\.

1. Run the code\. Information about the segments detected in the input video are displayed\.