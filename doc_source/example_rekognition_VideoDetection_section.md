# Detect information in videos using Amazon Rekognition and the AWS SDK<a name="example_rekognition_VideoDetection_section"></a>

The following code examples show how to detect information in videos\.

------
#### [ Java ]

**SDK for Java 2\.x**  
Get celebrity results from a video located in an Amazon S3 bucket\.  

```
    public static  void StartCelebrityDetection(RekognitionClient rekClient,
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

            StartCelebrityRecognitionRequest recognitionRequest = StartCelebrityRecognitionRequest.builder()
                    .jobTag("Celebrities")
                    .notificationChannel(channel)
                    .video(vidOb)
                    .build();

            StartCelebrityRecognitionResponse startCelebrityRecognitionResult = rekClient.startCelebrityRecognition(recognitionRequest);
            startJobId = startCelebrityRecognitionResult.jobId();


        } catch(RekognitionException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }
    }

    public static void GetCelebrityDetectionResults(RekognitionClient rekClient) {

        try {
            String paginationToken=null;
            GetCelebrityRecognitionResponse recognitionResponse = null;
            Boolean finished = false;
            String status="";
            int yy=0 ;

            do{
                if (recognitionResponse !=null)
                    paginationToken = recognitionResponse.nextToken();

                GetCelebrityRecognitionRequest recognitionRequest = GetCelebrityRecognitionRequest.builder()
                            .jobId(startJobId)
                            .nextToken(paginationToken)
                            .sortBy(CelebrityRecognitionSortBy.TIMESTAMP)
                            .maxResults(10)
                            .build();

                // Wait until the job succeeds
                while (!finished) {

                    recognitionResponse = rekClient.getCelebrityRecognition(recognitionRequest);
                    status = recognitionResponse.jobStatusAsString();

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
                VideoMetadata videoMetaData=recognitionResponse.videoMetadata();

                System.out.println("Format: " + videoMetaData.format());
                System.out.println("Codec: " + videoMetaData.codec());
                System.out.println("Duration: " + videoMetaData.durationMillis());
                System.out.println("FrameRate: " + videoMetaData.frameRate());
                System.out.println("Job");

                List<CelebrityRecognition> celebs= recognitionResponse.celebrities();
                for (CelebrityRecognition celeb: celebs) {
                    long seconds=celeb.timestamp()/1000;
                    System.out.print("Sec: " + Long.toString(seconds) + " ");
                    CelebrityDetail details=celeb.celebrity();
                    System.out.println("Name: " + details.name());
                    System.out.println("Id: " + details.id());
                    System.out.println();
                }

            } while (recognitionResponse !=null && recognitionResponse.nextToken() != null);

        } catch(RekognitionException | InterruptedException e) {
            System.out.println(e.getMessage());
            System.exit(1);
    }
  }
```
Detect labels in a video by a label detection operation\.  

```
    public static void startLabels(RekognitionClient rekClient,
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

            StartLabelDetectionRequest labelDetectionRequest = StartLabelDetectionRequest.builder()
                    .jobTag("DetectingLabels")
                    .notificationChannel(channel)
                    .video(vidOb)
                    .minConfidence(50F)
                    .build();

            StartLabelDetectionResponse labelDetectionResponse = rekClient.startLabelDetection(labelDetectionRequest);
            startJobId = labelDetectionResponse.jobId();

            boolean ans = true;
            String status = "";
            int yy = 0;
            while (ans) {

                GetLabelDetectionRequest detectionRequest = GetLabelDetectionRequest.builder()
                        .jobId(startJobId)
                        .maxResults(10)
                        .build();

                GetLabelDetectionResponse result = rekClient.getLabelDetection(detectionRequest);
                status = result.jobStatusAsString();

                if (status.compareTo("SUCCEEDED") == 0)
                    ans = false;
                else
                    System.out.println(yy +" status is: "+status);

                Thread.sleep(1000);
                yy++;
            }

            System.out.println(startJobId +" status is: "+status);
        } catch(RekognitionException | InterruptedException e) {
            e.getMessage();
            System.exit(1);
        }
    }

    public static void getLabelJob(RekognitionClient rekClient,
                                   SqsClient sqs,
                                   String queueUrl) {

        List<Message> messages=null;
        ReceiveMessageRequest messageRequest = ReceiveMessageRequest.builder()
                .queueUrl(queueUrl)
                .build();

        try {
            messages = sqs.receiveMessage(messageRequest).messages();

            if (!messages.isEmpty()) {
                for (Message message: messages) {
                    String notification = message.body();

                    // Get the status and job id from the notification
                    ObjectMapper mapper = new ObjectMapper();
                    JsonNode jsonMessageTree = mapper.readTree(notification);
                    JsonNode messageBodyText = jsonMessageTree.get("Message");
                    ObjectMapper operationResultMapper = new ObjectMapper();
                    JsonNode jsonResultTree = operationResultMapper.readTree(messageBodyText.textValue());
                    JsonNode operationJobId = jsonResultTree.get("JobId");
                    JsonNode operationStatus = jsonResultTree.get("Status");
                    System.out.println("Job found in JSON is " + operationJobId);

                    DeleteMessageRequest deleteMessageRequest = DeleteMessageRequest.builder()
                            .queueUrl(queueUrl)
                            .build();

                    String jobId = operationJobId.textValue();
                    if (startJobId.compareTo(jobId)==0) {

                        System.out.println("Job id: " + operationJobId );
                        System.out.println("Status : " + operationStatus.toString());

                        if (operationStatus.asText().equals("SUCCEEDED"))
                            GetResultsLabels(rekClient);
                        else
                            System.out.println("Video analysis failed");

                        sqs.deleteMessage(deleteMessageRequest);
                    }

                    else{
                        System.out.println("Job received was not job " +  startJobId);
                        sqs.deleteMessage(deleteMessageRequest);
                    }
                }
            }

        } catch(RekognitionException e) {
            e.getMessage();
            System.exit(1);
        } catch (JsonMappingException e) {
            e.printStackTrace();
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Gets the job results by calling GetLabelDetection
    private static void GetResultsLabels(RekognitionClient rekClient) {

        int maxResults=10;
        String paginationToken=null;
        GetLabelDetectionResponse labelDetectionResult=null;

        try {
            do {
                if (labelDetectionResult !=null)
                    paginationToken = labelDetectionResult.nextToken();


                GetLabelDetectionRequest labelDetectionRequest= GetLabelDetectionRequest.builder()
                        .jobId(startJobId)
                        .sortBy(LabelDetectionSortBy.TIMESTAMP)
                        .maxResults(maxResults)
                        .nextToken(paginationToken)
                        .build();

                labelDetectionResult = rekClient.getLabelDetection(labelDetectionRequest);
                VideoMetadata videoMetaData=labelDetectionResult.videoMetadata();

                System.out.println("Format: " + videoMetaData.format());
                System.out.println("Codec: " + videoMetaData.codec());
                System.out.println("Duration: " + videoMetaData.durationMillis());
                System.out.println("FrameRate: " + videoMetaData.frameRate());

                List<LabelDetection> detectedLabels= labelDetectionResult.labels();
                for (LabelDetection detectedLabel: detectedLabels) {
                    long seconds=detectedLabel.timestamp();
                    Label label=detectedLabel.label();
                    System.out.println("Millisecond: " + Long.toString(seconds) + " ");

                    System.out.println("   Label:" + label.name());
                    System.out.println("   Confidence:" + detectedLabel.label().confidence().toString());

                    List<Instance> instances = label.instances();
                    System.out.println("   Instances of " + label.name());

                    if (instances.isEmpty()) {
                        System.out.println("        " + "None");
                    }  else {
                        for (Instance instance : instances) {
                            System.out.println("        Confidence: " + instance.confidence().toString());
                            System.out.println("        Bounding box: " + instance.boundingBox().toString());
                        }
                    }
                    System.out.println("   Parent labels for " + label.name() + ":");
                    List<Parent> parents = label.parents();

                    if (parents.isEmpty()) {
                        System.out.println("        None");
                    } else {
                        for (Parent parent : parents) {
                            System.out.println("   " + parent.name());
                        }
                    }
                    System.out.println();
                }
            } while (labelDetectionResult !=null && labelDetectionResult.nextToken() != null);

        } catch(RekognitionException e) {
            e.getMessage();
            System.exit(1);
        }
    }
```
Detect faces in a video stored in an Amazon S3 bucket\.  

```
    public static void startLabels(RekognitionClient rekClient,
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

            StartLabelDetectionRequest labelDetectionRequest = StartLabelDetectionRequest.builder()
                    .jobTag("DetectingLabels")
                    .notificationChannel(channel)
                    .video(vidOb)
                    .minConfidence(50F)
                    .build();

            StartLabelDetectionResponse labelDetectionResponse = rekClient.startLabelDetection(labelDetectionRequest);
            startJobId = labelDetectionResponse.jobId();

            boolean ans = true;
            String status = "";
            int yy = 0;
            while (ans) {

                GetLabelDetectionRequest detectionRequest = GetLabelDetectionRequest.builder()
                        .jobId(startJobId)
                        .maxResults(10)
                        .build();

                GetLabelDetectionResponse result = rekClient.getLabelDetection(detectionRequest);
                status = result.jobStatusAsString();

                if (status.compareTo("SUCCEEDED") == 0)
                    ans = false;
                else
                    System.out.println(yy +" status is: "+status);

                Thread.sleep(1000);
                yy++;
            }

            System.out.println(startJobId +" status is: "+status);
        } catch(RekognitionException | InterruptedException e) {
            e.getMessage();
            System.exit(1);
        }
    }

    public static void getLabelJob(RekognitionClient rekClient,
                                   SqsClient sqs,
                                   String queueUrl) {

        List<Message> messages=null;
        ReceiveMessageRequest messageRequest = ReceiveMessageRequest.builder()
                .queueUrl(queueUrl)
                .build();

        try {
            messages = sqs.receiveMessage(messageRequest).messages();

            if (!messages.isEmpty()) {
                for (Message message: messages) {
                    String notification = message.body();

                    // Get the status and job id from the notification
                    ObjectMapper mapper = new ObjectMapper();
                    JsonNode jsonMessageTree = mapper.readTree(notification);
                    JsonNode messageBodyText = jsonMessageTree.get("Message");
                    ObjectMapper operationResultMapper = new ObjectMapper();
                    JsonNode jsonResultTree = operationResultMapper.readTree(messageBodyText.textValue());
                    JsonNode operationJobId = jsonResultTree.get("JobId");
                    JsonNode operationStatus = jsonResultTree.get("Status");
                    System.out.println("Job found in JSON is " + operationJobId);

                    DeleteMessageRequest deleteMessageRequest = DeleteMessageRequest.builder()
                            .queueUrl(queueUrl)
                            .build();

                    String jobId = operationJobId.textValue();
                    if (startJobId.compareTo(jobId)==0) {

                        System.out.println("Job id: " + operationJobId );
                        System.out.println("Status : " + operationStatus.toString());

                        if (operationStatus.asText().equals("SUCCEEDED"))
                            GetResultsLabels(rekClient);
                        else
                            System.out.println("Video analysis failed");

                        sqs.deleteMessage(deleteMessageRequest);
                    }

                    else{
                        System.out.println("Job received was not job " +  startJobId);
                        sqs.deleteMessage(deleteMessageRequest);
                    }
                }
            }

        } catch(RekognitionException e) {
            e.getMessage();
            System.exit(1);
        } catch (JsonMappingException e) {
            e.printStackTrace();
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Gets the job results by calling GetLabelDetection
    private static void GetResultsLabels(RekognitionClient rekClient) {

        int maxResults=10;
        String paginationToken=null;
        GetLabelDetectionResponse labelDetectionResult=null;

        try {
            do {
                if (labelDetectionResult !=null)
                    paginationToken = labelDetectionResult.nextToken();


                GetLabelDetectionRequest labelDetectionRequest= GetLabelDetectionRequest.builder()
                        .jobId(startJobId)
                        .sortBy(LabelDetectionSortBy.TIMESTAMP)
                        .maxResults(maxResults)
                        .nextToken(paginationToken)
                        .build();

                labelDetectionResult = rekClient.getLabelDetection(labelDetectionRequest);
                VideoMetadata videoMetaData=labelDetectionResult.videoMetadata();

                System.out.println("Format: " + videoMetaData.format());
                System.out.println("Codec: " + videoMetaData.codec());
                System.out.println("Duration: " + videoMetaData.durationMillis());
                System.out.println("FrameRate: " + videoMetaData.frameRate());

                List<LabelDetection> detectedLabels= labelDetectionResult.labels();
                for (LabelDetection detectedLabel: detectedLabels) {
                    long seconds=detectedLabel.timestamp();
                    Label label=detectedLabel.label();
                    System.out.println("Millisecond: " + Long.toString(seconds) + " ");

                    System.out.println("   Label:" + label.name());
                    System.out.println("   Confidence:" + detectedLabel.label().confidence().toString());

                    List<Instance> instances = label.instances();
                    System.out.println("   Instances of " + label.name());

                    if (instances.isEmpty()) {
                        System.out.println("        " + "None");
                    }  else {
                        for (Instance instance : instances) {
                            System.out.println("        Confidence: " + instance.confidence().toString());
                            System.out.println("        Bounding box: " + instance.boundingBox().toString());
                        }
                    }
                    System.out.println("   Parent labels for " + label.name() + ":");
                    List<Parent> parents = label.parents();

                    if (parents.isEmpty()) {
                        System.out.println("        None");
                    } else {
                        for (Parent parent : parents) {
                            System.out.println("   " + parent.name());
                        }
                    }
                    System.out.println();
                }
            } while (labelDetectionResult !=null && labelDetectionResult.nextToken() != null);

        } catch(RekognitionException e) {
            e.getMessage();
            System.exit(1);
        }
    }
```
Detect inappropriate or offensive content in a video stored in an Amazon S3 bucket\.  

```
    public static void startModerationDetection(RekognitionClient rekClient,
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

            StartContentModerationRequest modDetectionRequest = StartContentModerationRequest.builder()
                    .jobTag("Moderation")
                    .notificationChannel(channel)
                    .video(vidOb)
                    .build();

            StartContentModerationResponse startModDetectionResult = rekClient.startContentModeration(modDetectionRequest);
            startJobId=startModDetectionResult.jobId();

        } catch(RekognitionException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }
    }

    public static void GetModResults(RekognitionClient rekClient) {

        try {
            String paginationToken=null;
            GetContentModerationResponse modDetectionResponse=null;
            Boolean finished = false;
            String status="";
            int yy=0 ;

            do{

                if (modDetectionResponse !=null)
                    paginationToken = modDetectionResponse.nextToken();

                GetContentModerationRequest modRequest = GetContentModerationRequest.builder()
                        .jobId(startJobId)
                        .nextToken(paginationToken)
                        .maxResults(10)
                        .build();

                // Wait until the job succeeds
                while (!finished) {

                    modDetectionResponse = rekClient.getContentModeration(modRequest);
                    status = modDetectionResponse.jobStatusAsString();

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
                VideoMetadata videoMetaData=modDetectionResponse.videoMetadata();

                System.out.println("Format: " + videoMetaData.format());
                System.out.println("Codec: " + videoMetaData.codec());
                System.out.println("Duration: " + videoMetaData.durationMillis());
                System.out.println("FrameRate: " + videoMetaData.frameRate());
                System.out.println("Job");

                List<ContentModerationDetection> mods = modDetectionResponse.moderationLabels();
                for (ContentModerationDetection mod: mods) {
                    long seconds=mod.timestamp()/1000;
                    System.out.print("Mod label: " + seconds + " ");
                    System.out.println(mod.moderationLabel().toString());
                    System.out.println();
                }

            } while (modDetectionResponse !=null && modDetectionResponse.nextToken() != null);

        } catch(RekognitionException | InterruptedException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }
    }
```
Detect technical cue segments and shot detection segments in a video stored in an Amazon S3 bucket\.  

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
Detect text in a video stored in a video stored in an Amazon S3 bucket\.  

```
    public static void startTextLabels(RekognitionClient rekClient,
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

            StartTextDetectionRequest labelDetectionRequest = StartTextDetectionRequest.builder()
                    .jobTag("DetectingLabels")
                    .notificationChannel(channel)
                    .video(vidOb)
                    .build();

            StartTextDetectionResponse labelDetectionResponse = rekClient.startTextDetection(labelDetectionRequest);
            startJobId = labelDetectionResponse.jobId();

        } catch(RekognitionException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }
      }

    public static void GetTextResults(RekognitionClient rekClient) {

        try {
            String paginationToken=null;
            GetTextDetectionResponse textDetectionResponse=null;
            Boolean finished = false;
            String status="";
            int yy=0 ;

            do{
                if (textDetectionResponse !=null)
                    paginationToken = textDetectionResponse.nextToken();

                GetTextDetectionRequest recognitionRequest = GetTextDetectionRequest.builder()
                        .jobId(startJobId)
                        .nextToken(paginationToken)
                        .maxResults(10)
                        .build();

                // Wait until the job succeeds
                while (!finished) {

                    textDetectionResponse = rekClient.getTextDetection(recognitionRequest);
                    status = textDetectionResponse.jobStatusAsString();

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
                VideoMetadata videoMetaData=textDetectionResponse.videoMetadata();

                System.out.println("Format: " + videoMetaData.format());
                System.out.println("Codec: " + videoMetaData.codec());
                System.out.println("Duration: " + videoMetaData.durationMillis());
                System.out.println("FrameRate: " + videoMetaData.frameRate());
                System.out.println("Job");

                List<TextDetectionResult> labels= textDetectionResponse.textDetections();
                for (TextDetectionResult detectedText: labels) {
                    System.out.println("Confidence: " + detectedText.textDetection().confidence().toString());
                    System.out.println("Id : " + detectedText.textDetection().id());
                    System.out.println("Parent Id: " + detectedText.textDetection().parentId());
                    System.out.println("Type: " + detectedText.textDetection().type());
                    System.out.println("Text: " + detectedText.textDetection().detectedText());
                    System.out.println();
                }

            } while (textDetectionResponse !=null && textDetectionResponse.nextToken() != null);

        } catch(RekognitionException | InterruptedException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }
    }
```
Detect people in a video stored in a video stored in an Amazon S3 bucket\.  

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
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/rekognition/#readme)\. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
This is prerelease documentation for a feature in preview release\. It is subject to change\.
Detect faces in a video stored in an Amazon S3 bucket\.  

```
suspend fun startFaceDetection(channelVal: NotificationChannel?, bucketVal: String, videoVal: String) {

        val s3Obj = S3Object {
            bucket = bucketVal
            name = videoVal
        }
        val vidOb = Video {
            s3Object = s3Obj
        }

        val request = StartFaceDetectionRequest {
             jobTag = "Faces"
             faceAttributes = FaceAttributes.All
             notificationChannel = channelVal
             video = vidOb
        }

        RekognitionClient { region = "us-east-1" }.use { rekClient ->
          val startLabelDetectionResult = rekClient.startFaceDetection(request)
          startJobId = startLabelDetectionResult.jobId.toString()
        }
}

suspend fun getFaceResults() {

    var finished = false
    var status: String
    var yy = 0
    RekognitionClient { region = "us-east-1" }.use { rekClient ->
        var response : GetFaceDetectionResponse? = null

        val recognitionRequest = GetFaceDetectionRequest {
            jobId = startJobId
            maxResults = 10
        }

        // Wait until the job succeeds.
        while (!finished) {
            response = rekClient.getFaceDetection(recognitionRequest)
            status = response.jobStatus.toString()
            if (status.compareTo("SUCCEEDED") == 0)
                finished = true
            else {
                println("$yy status is: $status")
                delay(1000)
            }
            yy++
        }

        // Proceed when the job is done - otherwise VideoMetadata is null.
        val videoMetaData = response?.videoMetadata
        println("Format: ${videoMetaData?.format}")
        println("Codec: ${videoMetaData?.codec}")
        println("Duration: ${videoMetaData?.durationMillis}")
        println("FrameRate: ${videoMetaData?.frameRate}")

        // Show face information.
        response?.faces?.forEach { face ->
            println("Age: ${face.face?.ageRange}")
            println("Face: ${face.face?.beard}")
            println("Eye glasses: ${face?.face?.eyeglasses}")
            println("Mustache: ${face.face?.mustache}")
            println("Smile: ${face.face?.smile}")
        }
    }
}
```
Detect inappropriate or offensive content in a video stored in an Amazon S3 bucket\.  

```
suspend fun startModerationDetection(channel: NotificationChannel?, bucketVal: String?, videoVal: String?) {

    val s3Obj = S3Object {
        bucket = bucketVal
        name = videoVal
    }
    val vidOb = Video {
        s3Object = s3Obj
    }
    val request = StartContentModerationRequest {
        jobTag = "Moderation"
        notificationChannel = channel
        video = vidOb
    }

    RekognitionClient { region = "us-east-1" }.use { rekClient ->
        val startModDetectionResult = rekClient.startContentModeration(request)
        startJobId = startModDetectionResult.jobId.toString()
    }
}

suspend fun getModResults() {
    var finished = false
    var status: String
    var yy = 0
    RekognitionClient { region = "us-east-1" }.use { rekClient ->
        var modDetectionResponse: GetContentModerationResponse? = null

        val modRequest = GetContentModerationRequest {
            jobId = startJobId
            maxResults = 10
        }

        // Wait until the job succeeds.
        while (!finished) {
            modDetectionResponse = rekClient.getContentModeration(modRequest)
            status = modDetectionResponse.jobStatus.toString()
            if (status.compareTo("SUCCEEDED") == 0)
                finished = true
            else {
                println("$yy status is: $status")
                delay(1000)
            }
            yy++
        }

        // Proceed when the job is done - otherwise VideoMetadata is null.
        val videoMetaData = modDetectionResponse?.videoMetadata
        println("Format: ${videoMetaData?.format}")
        println("Codec: ${videoMetaData?.codec}")
        println("Duration: ${videoMetaData?.durationMillis}")
        println("FrameRate: ${videoMetaData?.frameRate}")

        modDetectionResponse?.moderationLabels?.forEach { mod ->
            val seconds: Long = mod.timestamp / 1000
            print("Mod label: $seconds ")
            println(mod.moderationLabel)
        }
    }
}
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/example_code/rekognition/#code-examples)\. 

------

For a complete list of AWS SDK developer guides and code examples, including help getting started and information about previous versions, see [Using Rekognition with an AWS SDK](sdk-general-information-section.md)\.