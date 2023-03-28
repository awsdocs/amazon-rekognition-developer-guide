# Analyzing a video stored in an Amazon S3 bucket with Java or Python \(SDK\)<a name="video-analyzing-with-sqs"></a>

This procedure shows you how to detect labels in a video by using Amazon Rekognition Video label detection operations, a video stored in an Amazon S3 bucket, and an Amazon SNS topic\. The procedure also shows how to use an Amazon SQS queue to get the completion status from the Amazon SNS topic\. For more information, see [Calling Amazon Rekognition Video operations](api-video.md)\. You aren't restricted to using an Amazon SQS queue\. For example, you can use an AWS Lambda function to get the completion status\. For more information, see [Invoking Lambda functions using Amazon SNS notifications](https://docs.aws.amazon.com/sns/latest/dg/sns-lambda.html)\.

The example code in this procedure shows you how to do the following:

1. Create the Amazon SNS topic\.

1. Create the Amazon SQS queue\.

1. Give Amazon Rekognition Video permission to publish the completion status of a video analysis operation to the Amazon SNS topic\.

1. Subscribe the Amazon SQS queue to the Amazon SNS topic\.

1. Start the video analysis request by calling [StartLabelDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartLabelDetection.html)\. 

1. Get the completion status from the Amazon SQS queue\. The example tracks the job identifier \(`JobId`\) that's returned in `StartLabelDetection` and only gets the results for matching job identifiers that are read from the completion status\. This is an important consideration if other applications are using the same queue and topic\. For simplicity, the example deletes jobs that don't match\. Consider adding them to an Amazon SQS dead\-letter queue for further investigation\.

1. Get and display the video analysis results by calling [GetLabelDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetLabelDetection.html)\.

## Prerequisites<a name="video-prerequisites"></a>

The example code for this procedure is provided in Java and Python\. You need to have the appropriate AWS SDK installed\. For more information, see [Getting started with Amazon Rekognition](getting-started.md)\. The AWS account that you use must have access permissions to the Amazon Rekognition API\. For more information, see [Actions Defined by Amazon Rekognition](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonrekognition.html#amazonrekognition-actions-as-permissions)\. 

**To detect labels in a video**

1. Configure user access to Amazon Rekognition Video and configure Amazon Rekognition Video access to Amazon SNS\. For more information, see [Configuring Amazon Rekognition Video](api-video-roles.md)\. You don't need to do steps 3, 4, 5, and 6 because the example code creates and configures the Amazon SNS topic and Amazon SQS queue\. 

1. Upload an MOV or MPEG\-4 format video file to an Amazon S3 Bucket\. For test purposes, upload a video that's no longer than 30 seconds in length\.

   For instructions, see [Uploading Objects into Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service User Guide*\.

   

1. Use the following code examples to detect labels in a video\. 

------
#### [ Java ]

   In the function `main`:
   + Replace `roleArn` with the ARN of the IAM service role that you created in step 7 of [To configure Amazon Rekognition Video](api-video-roles.md#configure-rekvid-procedure)\.
   + Replace the values of `bucket` and `video` with the bucket and video file name that you specified in step 2\. 

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   package com.amazonaws.samples;
   import com.amazonaws.auth.policy.Policy;
   import com.amazonaws.auth.policy.Condition;
   import com.amazonaws.auth.policy.Principal;
   import com.amazonaws.auth.policy.Resource;
   import com.amazonaws.auth.policy.Statement;
   import com.amazonaws.auth.policy.Statement.Effect;
   import com.amazonaws.auth.policy.actions.SQSActions;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.CelebrityDetail;
   import com.amazonaws.services.rekognition.model.CelebrityRecognition;
   import com.amazonaws.services.rekognition.model.CelebrityRecognitionSortBy;
   import com.amazonaws.services.rekognition.model.ContentModerationDetection;
   import com.amazonaws.services.rekognition.model.ContentModerationSortBy;
   import com.amazonaws.services.rekognition.model.Face;
   import com.amazonaws.services.rekognition.model.FaceDetection;
   import com.amazonaws.services.rekognition.model.FaceMatch;
   import com.amazonaws.services.rekognition.model.FaceSearchSortBy;
   import com.amazonaws.services.rekognition.model.GetCelebrityRecognitionRequest;
   import com.amazonaws.services.rekognition.model.GetCelebrityRecognitionResult;
   import com.amazonaws.services.rekognition.model.GetContentModerationRequest;
   import com.amazonaws.services.rekognition.model.GetContentModerationResult;
   import com.amazonaws.services.rekognition.model.GetFaceDetectionRequest;
   import com.amazonaws.services.rekognition.model.GetFaceDetectionResult;
   import com.amazonaws.services.rekognition.model.GetFaceSearchRequest;
   import com.amazonaws.services.rekognition.model.GetFaceSearchResult;
   import com.amazonaws.services.rekognition.model.GetLabelDetectionRequest;
   import com.amazonaws.services.rekognition.model.GetLabelDetectionResult;
   import com.amazonaws.services.rekognition.model.GetPersonTrackingRequest;
   import com.amazonaws.services.rekognition.model.GetPersonTrackingResult;
   import com.amazonaws.services.rekognition.model.Instance;
   import com.amazonaws.services.rekognition.model.Label;
   import com.amazonaws.services.rekognition.model.LabelDetection;
   import com.amazonaws.services.rekognition.model.LabelDetectionSortBy;
   import com.amazonaws.services.rekognition.model.NotificationChannel;
   import com.amazonaws.services.rekognition.model.Parent;
   import com.amazonaws.services.rekognition.model.PersonDetection;
   import com.amazonaws.services.rekognition.model.PersonMatch;
   import com.amazonaws.services.rekognition.model.PersonTrackingSortBy;
   import com.amazonaws.services.rekognition.model.S3Object;
   import com.amazonaws.services.rekognition.model.StartCelebrityRecognitionRequest;
   import com.amazonaws.services.rekognition.model.StartCelebrityRecognitionResult;
   import com.amazonaws.services.rekognition.model.StartContentModerationRequest;
   import com.amazonaws.services.rekognition.model.StartContentModerationResult;
   import com.amazonaws.services.rekognition.model.StartFaceDetectionRequest;
   import com.amazonaws.services.rekognition.model.StartFaceDetectionResult;
   import com.amazonaws.services.rekognition.model.StartFaceSearchRequest;
   import com.amazonaws.services.rekognition.model.StartFaceSearchResult;
   import com.amazonaws.services.rekognition.model.StartLabelDetectionRequest;
   import com.amazonaws.services.rekognition.model.StartLabelDetectionResult;
   import com.amazonaws.services.rekognition.model.StartPersonTrackingRequest;
   import com.amazonaws.services.rekognition.model.StartPersonTrackingResult;
   import com.amazonaws.services.rekognition.model.Video;
   import com.amazonaws.services.rekognition.model.VideoMetadata;
   import com.amazonaws.services.sns.AmazonSNS;
   import com.amazonaws.services.sns.AmazonSNSClientBuilder;
   import com.amazonaws.services.sns.model.CreateTopicRequest;
   import com.amazonaws.services.sns.model.CreateTopicResult;
   import com.amazonaws.services.sqs.AmazonSQS;
   import com.amazonaws.services.sqs.AmazonSQSClientBuilder;
   import com.amazonaws.services.sqs.model.CreateQueueRequest;
   import com.amazonaws.services.sqs.model.Message;
   import com.amazonaws.services.sqs.model.QueueAttributeName;
   import com.amazonaws.services.sqs.model.SetQueueAttributesRequest;
   import com.fasterxml.jackson.databind.JsonNode;
   import com.fasterxml.jackson.databind.ObjectMapper;
   import java.util.*;
   
   public class VideoDetect {
    
       
       private static String sqsQueueName=null;
       private static String snsTopicName=null;
       private static String snsTopicArn = null;
       private static String roleArn= null;
       private static String sqsQueueUrl = null;
       private static String sqsQueueArn = null;
       private static String startJobId = null;
       private static String bucket = null;
       private static String video = null; 
       private static AmazonSQS sqs=null;
       private static AmazonSNS sns=null;
       private static AmazonRekognition rek = null;
       
       private static NotificationChannel channel= new NotificationChannel()
               .withSNSTopicArn(snsTopicArn)
               .withRoleArn(roleArn);
   
   
       public static void main(String[] args) throws Exception {
           
           video = "";
           bucket = "";
           roleArn= "";
   
           sns = AmazonSNSClientBuilder.defaultClient();
           sqs= AmazonSQSClientBuilder.defaultClient();
           rek = AmazonRekognitionClientBuilder.defaultClient();
     
           CreateTopicandQueue();
           
           //=================================================
           
           StartLabelDetection(bucket, video);
   
           if (GetSQSMessageSuccess()==true)
           	GetLabelDetectionResults();
           
          //=================================================  
           
   
           DeleteTopicandQueue();
           System.out.println("Done!");
          
       }
   
       
       static boolean GetSQSMessageSuccess() throws Exception
       {
       	boolean success=false;
   
      
           System.out.println("Waiting for job: " + startJobId);
           //Poll queue for messages
           List<Message> messages=null;
           int dotLine=0;
           boolean jobFound=false;
   
           //loop until the job status is published. Ignore other messages in queue.
           do{
               messages = sqs.receiveMessage(sqsQueueUrl).getMessages();
               if (dotLine++<40){
                   System.out.print(".");
               }else{
                   System.out.println();
                   dotLine=0;
               }
   
               if (!messages.isEmpty()) {
                   //Loop through messages received.
                   for (Message message: messages) {
                       String notification = message.getBody();
   
                       // Get status and job id from notification.
                       ObjectMapper mapper = new ObjectMapper();
                       JsonNode jsonMessageTree = mapper.readTree(notification);
                       JsonNode messageBodyText = jsonMessageTree.get("Message");
                       ObjectMapper operationResultMapper = new ObjectMapper();
                       JsonNode jsonResultTree = operationResultMapper.readTree(messageBodyText.textValue());
                       JsonNode operationJobId = jsonResultTree.get("JobId");
                       JsonNode operationStatus = jsonResultTree.get("Status");
                       System.out.println("Job found was " + operationJobId);
                       // Found job. Get the results and display.
                       if(operationJobId.asText().equals(startJobId)){
                           jobFound=true;
                           System.out.println("Job id: " + operationJobId );
                           System.out.println("Status : " + operationStatus.toString());
                           if (operationStatus.asText().equals("SUCCEEDED")){
                           	success=true;
                           }
                           else{
                               System.out.println("Video analysis failed");
                           }
   
                           sqs.deleteMessage(sqsQueueUrl,message.getReceiptHandle());
                       }
   
                       else{
                           System.out.println("Job received was not job " +  startJobId);
                           //Delete unknown message. Consider moving message to dead letter queue
                           sqs.deleteMessage(sqsQueueUrl,message.getReceiptHandle());
                       }
                   }
               }
               else {
                   Thread.sleep(5000);
               }
           } while (!jobFound);
   
           System.out.println("Finished processing video");
           return success;
       }
     
   
       private static void StartLabelDetection(String bucket, String video) throws Exception{
       	
           NotificationChannel channel= new NotificationChannel()
                   .withSNSTopicArn(snsTopicArn)
                   .withRoleArn(roleArn);
   
   
           StartLabelDetectionRequest req = new StartLabelDetectionRequest()
                   .withVideo(new Video()
                           .withS3Object(new S3Object()
                                   .withBucket(bucket)
                                   .withName(video)))
                   .withMinConfidence(50F)
                   .withJobTag("DetectingLabels")
                   .withNotificationChannel(channel);
   
           StartLabelDetectionResult startLabelDetectionResult = rek.startLabelDetection(req);
           startJobId=startLabelDetectionResult.getJobId();
           
       }
     
       private static void GetLabelDetectionResults() throws Exception{
   
           int maxResults=10;
           String paginationToken=null;
           GetLabelDetectionResult labelDetectionResult=null;
   
           do {
               if (labelDetectionResult !=null){
                   paginationToken = labelDetectionResult.getNextToken();
               }
   
               GetLabelDetectionRequest labelDetectionRequest= new GetLabelDetectionRequest()
                       .withJobId(startJobId)
                       .withSortBy(LabelDetectionSortBy.TIMESTAMP)
                       .withMaxResults(maxResults)
                       .withNextToken(paginationToken);
   
   
               labelDetectionResult = rek.getLabelDetection(labelDetectionRequest);
   
               VideoMetadata videoMetaData=labelDetectionResult.getVideoMetadata();
   
               System.out.println("Format: " + videoMetaData.getFormat());
               System.out.println("Codec: " + videoMetaData.getCodec());
               System.out.println("Duration: " + videoMetaData.getDurationMillis());
               System.out.println("FrameRate: " + videoMetaData.getFrameRate());
   
   
               //Show labels, confidence and detection times
               List<LabelDetection> detectedLabels= labelDetectionResult.getLabels();
   
               for (LabelDetection detectedLabel: detectedLabels) {
                   long seconds=detectedLabel.getTimestamp();
                   Label label=detectedLabel.getLabel();
                   System.out.println("Millisecond: " + Long.toString(seconds) + " ");
                   
                   System.out.println("   Label:" + label.getName()); 
                   System.out.println("   Confidence:" + detectedLabel.getLabel().getConfidence().toString());
         
                   List<Instance> instances = label.getInstances();
                   System.out.println("   Instances of " + label.getName());
                   if (instances.isEmpty()) {
                       System.out.println("        " + "None");
                   } else {
                       for (Instance instance : instances) {
                           System.out.println("        Confidence: " + instance.getConfidence().toString());
                           System.out.println("        Bounding box: " + instance.getBoundingBox().toString());
                       }
                   }
                   System.out.println("   Parent labels for " + label.getName() + ":");
                   List<Parent> parents = label.getParents();
                   if (parents.isEmpty()) {
                       System.out.println("        None");
                   } else {
                       for (Parent parent : parents) {
                           System.out.println("        " + parent.getName());
                       }
                   }
                   System.out.println();
               }
           } while (labelDetectionResult !=null && labelDetectionResult.getNextToken() != null);
   
       } 
   
       // Creates an SNS topic and SQS queue. The queue is subscribed to the topic. 
       static void CreateTopicandQueue()
       {
           //create a new SNS topic
           snsTopicName="AmazonRekognitionTopic" + Long.toString(System.currentTimeMillis());
           CreateTopicRequest createTopicRequest = new CreateTopicRequest(snsTopicName);
           CreateTopicResult createTopicResult = sns.createTopic(createTopicRequest);
           snsTopicArn=createTopicResult.getTopicArn();
           
           //Create a new SQS Queue
           sqsQueueName="AmazonRekognitionQueue" + Long.toString(System.currentTimeMillis());
           final CreateQueueRequest createQueueRequest = new CreateQueueRequest(sqsQueueName);
           sqsQueueUrl = sqs.createQueue(createQueueRequest).getQueueUrl();
           sqsQueueArn = sqs.getQueueAttributes(sqsQueueUrl, Arrays.asList("QueueArn")).getAttributes().get("QueueArn");
           
           //Subscribe SQS queue to SNS topic
           String sqsSubscriptionArn = sns.subscribe(snsTopicArn, "sqs", sqsQueueArn).getSubscriptionArn();
           
           // Authorize queue
             Policy policy = new Policy().withStatements(
                     new Statement(Effect.Allow)
                     .withPrincipals(Principal.AllUsers)
                     .withActions(SQSActions.SendMessage)
                     .withResources(new Resource(sqsQueueArn))
                     .withConditions(new Condition().withType("ArnEquals").withConditionKey("aws:SourceArn").withValues(snsTopicArn))
                     );
                     
   
             Map queueAttributes = new HashMap();
             queueAttributes.put(QueueAttributeName.Policy.toString(), policy.toJson());
             sqs.setQueueAttributes(new SetQueueAttributesRequest(sqsQueueUrl, queueAttributes)); 
           
   
            System.out.println("Topic arn: " + snsTopicArn);
            System.out.println("Queue arn: " + sqsQueueArn);
            System.out.println("Queue url: " + sqsQueueUrl);
            System.out.println("Queue sub arn: " + sqsSubscriptionArn );
        }
       static void DeleteTopicandQueue()
       {
           if (sqs !=null) {
               sqs.deleteQueue(sqsQueueUrl);
               System.out.println("SQS queue deleted");
           }
           
           if (sns!=null) {
               sns.deleteTopic(snsTopicArn);
               System.out.println("SNS topic deleted");
           }
       }
   }
   ```

------
#### [ Python ]

   In the function `main`:
   + Replace `roleArn` with the ARN of the IAM service role that you created in step 7 of [To configure Amazon Rekognition Video](api-video-roles.md#configure-rekvid-procedure)\.
   + Replace the values of `bucket` and `video` with the bucket and video file name that you specified in step 2\. 
   + You can also include filtration criteria in the settings paramter\. For example, you can use a `LabelsInclusionFilter` or a `LabelsExclusionFilter` alongside a list of desired values\. In the code below, you can uncomment the `Features` and `Settings` section and provide your own values to limit the returned results to just the labels your are interested in\.

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   

   import json
   import sys
   import time

   import boto3


   class VideoDetect:
       job_id = ""
       rek = boto3.client("rekognition")
       sqs = boto3.client("sqs")
       sns = boto3.client("sns")

       role_arn = ""
       bucket = ""
       video = ""
       start_job_id = ""

       sqs_queue_url = ""
       sns_topic_arn = ""
       process_type = ""

       def __init__(self, role, bucket, video):
           self.role_arn = role
           self.bucket = bucket
           self.video = video

       def GetSQSMessageSuccess(self):

           job_found = False
           succeeded = False

           dot_line = 0
           while job_found == False:
               sqs_response = self.sqs.receive_message(
                   QueueUrl=self.sqs_queue_url,
                   MessageAttributeNames=["ALL"],
                   MaxNumberOfMessages=10,
               )

               if sqs_response:

                   if "Messages" not in sqs_response:
                       if dot_line < 40:
                           print(".", end="")
                           dot_line = dot_line + 1
                       else:
                           print()
                           dot_line = 0
                       sys.stdout.flush()
                       time.sleep(5)
                       continue

                   for message in sqs_response["Messages"]:
                       notification = json.loads(message["Body"])
                       rek_message = json.loads(notification["Message"])
                       print(rek_message["JobId"])
                       print(rek_message["Status"])
                       if rek_message["JobId"] == self.start_job_id:
                           print("Matching Job Found:" + rek_message["JobId"])
                           job_found = True
                           if rek_message["Status"] == "SUCCEEDED":
                               succeeded = True

                           self.sqs.delete_message(
                               QueueUrl=self.sqs_queue_url,
                               ReceiptHandle=message["ReceiptHandle"],
                           )
                       else:
                           print(
                               "Job didn't match:"
                               + str(rek_message["JobId"])
                               + " : "
                               + self.start_job_id
                           )
                       # Delete the unknown message. Consider sending to dead letter queue
                       self.sqs.delete_message(
                           QueueUrl=self.sqs_queue_url,
                           ReceiptHandle=message["ReceiptHandle"],
                       )

           return succeeded

       def start_label_detection(self):
           response = self.rek.start_label_detection(
               Video={"S3Object": {"Bucket": self.bucket, "Name": self.video}},
               NotificationChannel={
                   "RoleArn": self.role_arn,
                   "SNSTopicArn": self.sns_topic_arn,
               },
               MinConfidence=90,
               # Filtration options, uncomment and add desired labels to filter returned labels
               # Features=['GENERAL_LABELS'],
               # Settings={
               #'GeneralLabels': {
               #'LabelsInclusionFilter': ['cat','dog']
               # }
           )

           self.start_job_id = response["JobId"]
           print("Start Job Id: " + self.start_job_id)

       def get_label_detection_results(self):
           max_results = 10
           pagination_token = ""
           finished = False

           while not finished:
               response = self.rek.get_label_detection(
                   JobId=self.start_job_id,
                   MaxResults=max_results,
                   NextToken=pagination_token,
                   SortBy="TIMESTAMP",
               )

               print("Codec: " + response["VideoMetadata"]["Codec"])
               print("Duration: " + str(response["VideoMetadata"]["DurationMillis"]))
               print("Format: " + response["VideoMetadata"]["Format"])
               print("Frame rate: " + str(response["VideoMetadata"]["FrameRate"]))
               print()

               for label_detection in response["Labels"]:
                   label = label_detection["Label"]

                   print("Timestamp: " + str(label_detection["Timestamp"]))
                   print("   Label: " + label["Name"])
                   print("   Confidence: " + str(label["Confidence"]))
                   print("   Instances:")
                   for instance in label["Instances"]:
                       print("      Confidence: " + str(instance["Confidence"]))
                       print("      Bounding box")
                       print("        Top: " + str(instance["BoundingBox"]["Top"]))
                       print("        Left: " + str(instance["BoundingBox"]["Left"]))
                       print("        Width: " + str(instance["BoundingBox"]["Width"]))
                       print("        Height: " + str(instance["BoundingBox"]["Height"]))
                       print()
                   print()
                   print("   Parents:")
                   for parent in label["Parents"]:
                       print("      " + parent["Name"])
                   print()

                   if "NextToken" in response:
                       pagination_token = response["NextToken"]
                   else:
                       finished = True

       def create_topic_and_queue(self):

           millis = str(int(round(time.time() * 1000)))

           # Create SNS topic

           sns_topic_name = "AmazonRekognitionExample" + millis

           topic_response = self.sns.create_topic(Name=sns_topic_name)
           self.sns_topic_arn = topic_response["TopicArn"]

           # create SQS queue
           sqs_queue_name = "AmazonRekognitionQueue" + millis
           self.sqs.create_queue(QueueName=sqs_queue_name)
           self.sqs_queue_url = self.sqs.get_queue_url(QueueName=sqs_queue_name)["QueueUrl"]

           attribs = self.sqs.get_queue_attributes(
               QueueUrl=self.sqs_queue_url, AttributeNames=["QueueArn"]
           )["Attributes"]

           sqs_queue_arn = attribs["QueueArn"]

           # Subscribe SQS queue to SNS topic
           self.sns.subscribe(
               TopicArn=self.sns_topic_arn, Protocol="sqs", Endpoint=sqs_queue_arn
           )

           # Authorize SNS to write SQS queue
           policy = """{{
       "Version":"2012-10-17",
       "Statement":[
       {{
           "Sid":"MyPolicy",
           "Effect":"Allow",
           "Principal" : {{"AWS" : "*"}},
           "Action":"SQS:SendMessage",
           "Resource": "{}",
           "Condition":{{
           "ArnEquals":{{
               "aws:SourceArn": "{}"
           }}
           }}
       }}
       ]
   }}""".format(
               sqs_queue_arn, self.sns_topic_arn
           )

           response = self.sqs.set_queue_attributes(
               QueueUrl=self.sqs_queue_url, Attributes={"Policy": policy}
           )

       def delete_topic_and_queue(self):
           self.sqs.delete_queue(QueueUrl=self.sqs_queue_url)
           self.sns.delete_topic(TopicArn=self.sns_topic_arn)


   def main():
       role_arn = ""
       bucket = ""
       video = ""

       analyzer = VideoDetect(role_arn, bucket, video)
       analyzer.create_topic_and_queue()

       analyzer.start_label_detection()
       if analyzer.GetSQSMessageSuccess() == True:
           analyzer.get_label_detection_results()

       analyzer.delete_topic_and_queue()


   if __name__ == "__main__":
       main()
   ```

------
#### [ Node\.Js ]

   In the following sample code:
   + Replace the value of `REGION` with the name of your account's operating region\.
   + Replace the value of `bucket` with the name of the Amazon S3 bucket containing your video file\.
   + Replace the value of `videoName` with the name of the video file in your Amazon S3 bucket\.
   + Replace `roleArn` with the ARN of the IAM service role that you created in step 7 of [To configure Amazon Rekognition Video](api-video-roles.md#configure-rekvid-procedure)\.

   ```
   // snippet-start:[sqs.JavaScript.queues.createQueueV3]
   // Import required AWS SDK clients and commands for Node.js
   import { CreateQueueCommand, GetQueueAttributesCommand, GetQueueUrlCommand, 
     SetQueueAttributesCommand, DeleteQueueCommand, ReceiveMessageCommand, DeleteMessageCommand } from  "@aws-sdk/client-sqs";
   import {CreateTopicCommand, SubscribeCommand, DeleteTopicCommand } from "@aws-sdk/client-sns";
   import  { SQSClient } from "@aws-sdk/client-sqs";
   import  { SNSClient } from "@aws-sdk/client-sns";
   import  { RekognitionClient, StartLabelDetectionCommand, GetLabelDetectionCommand } from "@aws-sdk/client-rekognition";
   import { stdout } from "process";
   
   // Set the AWS Region.
   const REGION = "region-name"; //e.g. "us-east-1"
   // Create SNS service object.
   const sqsClient = new SQSClient({ region: REGION });
   const snsClient = new SNSClient({ region: REGION });
   const rekClient = new RekognitionClient({ region: REGION });
   
   // Set bucket and video variables
   const bucket = "bucket-name";
   const videoName = "video-name";
   const roleArn = "role-arn"
   var startJobId = ""
   
   var ts = Date.now();
   const snsTopicName = "AmazonRekognitionExample" + ts;
   const snsTopicParams = {Name: snsTopicName}
   const sqsQueueName = "AmazonRekognitionQueue-" + ts;
   
   // Set the parameters
   const sqsParams = {
     QueueName: sqsQueueName, //SQS_QUEUE_URL
     Attributes: {
       DelaySeconds: "60", // Number of seconds delay.
       MessageRetentionPeriod: "86400", // Number of seconds delay.
     },
   };
   
   const createTopicandQueue = async () => {
     try {
       // Create SNS topic
       const topicResponse = await snsClient.send(new CreateTopicCommand(snsTopicParams));
       const topicArn = topicResponse.TopicArn
       console.log("Success", topicResponse);
       // Create SQS Queue
       const sqsResponse = await sqsClient.send(new CreateQueueCommand(sqsParams));
       console.log("Success", sqsResponse);
       const sqsQueueCommand = await sqsClient.send(new GetQueueUrlCommand({QueueName: sqsQueueName}))
       const sqsQueueUrl = sqsQueueCommand.QueueUrl
       const attribsResponse = await sqsClient.send(new GetQueueAttributesCommand({QueueUrl: sqsQueueUrl, AttributeNames: ['QueueArn']}))
       const attribs = attribsResponse.Attributes
       console.log(attribs)
       const queueArn = attribs.QueueArn
       // subscribe SQS queue to SNS topic
       const subscribed = await snsClient.send(new SubscribeCommand({TopicArn: topicArn, Protocol:'sqs', Endpoint: queueArn}))
       const policy = {
         Version: "2012-10-17",
         Statement: [
           {
             Sid: "MyPolicy",
             Effect: "Allow",
             Principal: {AWS: "*"},
             Action: "SQS:SendMessage",
             Resource: queueArn,
             Condition: {
               ArnEquals: {
                 'aws:SourceArn': topicArn
               }
             }
           }
         ]
       };
   
       const response = sqsClient.send(new SetQueueAttributesCommand({QueueUrl: sqsQueueUrl, Attributes: {Policy: JSON.stringify(policy)}}))
       console.log(response)
       console.log(sqsQueueUrl, topicArn)
       return [sqsQueueUrl, topicArn]
   
     } catch (err) {
       console.log("Error", err);
     }
   };
   
   const startLabelDetection = async (roleArn, snsTopicArn) => {
     try {
       //Initiate label detection and update value of startJobId with returned Job ID
      const labelDetectionResponse = await rekClient.send(new StartLabelDetectionCommand({Video:{S3Object:{Bucket:bucket, Name:videoName}}, 
         NotificationChannel:{RoleArn: roleArn, SNSTopicArn: snsTopicArn}}));
         startJobId = labelDetectionResponse.JobId
         console.log(`JobID: ${startJobId}`)
         return startJobId
     } catch (err) {
       console.log("Error", err);
     }
   };
   
   const getLabelDetectionResults = async(startJobId) => {
     console.log("Retrieving Label Detection results")
     // Set max results, paginationToken and finished will be updated depending on response values
     var maxResults = 10
     var paginationToken = ''
     var finished = false
   
     // Begin retrieving label detection results
     while (finished == false){
       var response = await rekClient.send(new GetLabelDetectionCommand({JobId: startJobId, MaxResults: maxResults, 
         NextToken: paginationToken, SortBy:'TIMESTAMP'}))
         // Log metadata
         console.log(`Codec: ${response.VideoMetadata.Codec}`)
         console.log(`Duration: ${response.VideoMetadata.DurationMillis}`)
         console.log(`Format: ${response.VideoMetadata.Format}`)
         console.log(`Frame Rate: ${response.VideoMetadata.FrameRate}`)
         console.log()
         // For every detected label, log label, confidence, bounding box, and timestamp
         response.Labels.forEach(labelDetection => {
           var label = labelDetection.Label
           console.log(`Timestamp: ${labelDetection.Timestamp}`)
           console.log(`Label: ${label.Name}`)
           console.log(`Confidence: ${label.Confidence}`)
           console.log("Instances:")
           label.Instances.forEach(instance =>{
             console.log(`Confidence: ${instance.Confidence}`)
             console.log("Bounding Box:")
             console.log(`Top: ${instance.Confidence}`)
             console.log(`Left: ${instance.Confidence}`)
             console.log(`Width: ${instance.Confidence}`)
             console.log(`Height: ${instance.Confidence}`)
             console.log()
           })
         console.log()
         // Log parent if found
         console.log("   Parents:")
         label.Parents.forEach(parent =>{
           console.log(`    ${parent.Name}`)
         })
         console.log()
         // Searh for pagination token, if found, set variable to next token
         if (String(response).includes("NextToken")){
           paginationToken = response.NextToken
   
         }else{
           finished = true
         }
   
         })
     }
   }
   
   // Checks for status of job completion
   const getSQSMessageSuccess = async(sqsQueueUrl, startJobId) => {
     try {
       // Set job found and success status to false initially
       var jobFound = false
       var succeeded = false
       var dotLine = 0
       // while not found, continue to poll for response
       while (jobFound == false){
         var sqsReceivedResponse = await sqsClient.send(new ReceiveMessageCommand({QueueUrl:sqsQueueUrl, 
           MaxNumberOfMessages:'ALL', MaxNumberOfMessages:10}));
         if (sqsReceivedResponse){
           var responseString = JSON.stringify(sqsReceivedResponse)
           if (!responseString.includes('Body')){
             if (dotLine < 40) {
               console.log('.')
               dotLine = dotLine + 1
             }else {
               console.log('')
               dotLine = 0 
             };
             stdout.write('', () => {
               console.log('');
             });
             await new Promise(resolve => setTimeout(resolve, 5000));
             continue
           }
         }
   
         // Once job found, log Job ID and return true if status is succeeded
         for (var message of sqsReceivedResponse.Messages){
           console.log("Retrieved messages:")
           var notification = JSON.parse(message.Body)
           var rekMessage = JSON.parse(notification.Message)
           var messageJobId = rekMessage.JobId
           if (String(rekMessage.JobId).includes(String(startJobId))){
             console.log('Matching job found:')
             console.log(rekMessage.JobId)
             jobFound = true
             console.log(rekMessage.Status)
             if (String(rekMessage.Status).includes(String("SUCCEEDED"))){
               succeeded = true
               console.log("Job processing succeeded.")
               var sqsDeleteMessage = await sqsClient.send(new DeleteMessageCommand({QueueUrl:sqsQueueUrl, ReceiptHandle:message.ReceiptHandle}));
             }
           }else{
             console.log("Provided Job ID did not match returned ID.")
             var sqsDeleteMessage = await sqsClient.send(new DeleteMessageCommand({QueueUrl:sqsQueueUrl, ReceiptHandle:message.ReceiptHandle}));
           }
         }
       }
     return succeeded
     } catch(err) {
       console.log("Error", err);
     }
   };
   
   // Start label detection job, sent status notification, check for success status
   // Retrieve results if status is "SUCEEDED", delete notification queue and topic
   const runLabelDetectionAndGetResults = async () => {
     try {
       const sqsAndTopic = await createTopicandQueue();
       const startLabelDetectionRes = await startLabelDetection(roleArn, sqsAndTopic[1]);
       const getSQSMessageStatus = await getSQSMessageSuccess(sqsAndTopic[0], startLabelDetectionRes)
       console.log(getSQSMessageSuccess)
       if (getSQSMessageSuccess){
         console.log("Retrieving results:")
         const results = await getLabelDetectionResults(startLabelDetectionRes)
       }
       const deleteQueue = await sqsClient.send(new DeleteQueueCommand({QueueUrl: sqsAndTopic[0]}));
       const deleteTopic = await snsClient.send(new DeleteTopicCommand({TopicArn: sqsAndTopic[1]}));
       console.log("Successfully deleted.")
     } catch (err) {
       console.log("Error", err);
     }
   };
   
   runLabelDetectionAndGetResults()
   ```

------
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/VideoDetect.java)\.

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
   
       public static void getLabelJob(RekognitionClient rekClient, SqsClient sqs, String queueUrl) {
   
           List<Message> messages;
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
                       System.out.println("Millisecond: " + seconds + " ");
   
                       System.out.println("   Label:" + label.name());
                       System.out.println("   Confidence:" + detectedLabel.label().confidence().toString());
   
                       List<Instance> instances = label.instances();
                       System.out.println("   Instances of " + label.name());
   
                       if (instances.isEmpty()) {
                           System.out.println("        " + "None");
                       } else {
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

------

1. Build and run the code\. The operation might take a while to finish\. After it's finished, a list of the labels detected in the video is displayed\. For more information, see [Detecting labels in a video](labels-detecting-labels-video.md)\.
