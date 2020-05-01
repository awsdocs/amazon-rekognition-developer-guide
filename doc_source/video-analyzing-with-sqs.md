# Analyzing a Video Stored in an Amazon S3 Bucket with Java or Python \(SDK\)<a name="video-analyzing-with-sqs"></a>

This procedure shows you how to detect labels in a video by using Amazon Rekognition Video label detection operations, a video stored in an Amazon S3 bucket, and an Amazon SNS topic\. The procedure also shows how to use an Amazon SQS queue to get the completion status from the Amazon SNS topic\. For more information, see [Calling Amazon Rekognition Video Operations](api-video.md)\. You aren't restricted to using an Amazon SQS queue\. For example, you can use an AWS Lambda function to get the completion status\. For more information, see [Invoking Lambda functions using Amazon SNS notifications](https://docs.aws.amazon.com/sns/latest/dg/sns-lambda.html)\.

The example code in this procedure shows you how to do the following:

1. Create the Amazon SNS topic\.

1. Create the Amazon SQS queue\.

1. Give Amazon Rekognition Video permission to publish the completion status of a video analysis operation to the Amazon SNS topic\.

1. Subscribe the Amazon SQS queue to the Amazon SNS topic\.

1. Start the video analysis request by calling [StartLabelDetection](API_StartLabelDetection.md)\. 

1. Get the completion status from the Amazon SQS queue\. The example tracks the job identifier \(`JobId`\) that's returned in `StartLabelDetection` and only gets the results for matching job identifiers that are read from the completion status\. This is an important consideration if other applications are using the same queue and topic\. For simplicity, the example deletes jobs that don't match\. Consider adding them to an Amazon SQS dead\-letter queue for further investigation\.

1. Get and display the video analysis results by calling [GetLabelDetection](API_GetLabelDetection.md)\.

## Prerequisites<a name="video-prerequisites"></a>

The example code for this procedure is provided in Java and Python\. You need to have the appropriate AWS SDK installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account that you use must have access permissions to the Amazon Rekognition API\. For more information, see [Actions Defined by Amazon Rekognition](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonrekognition.html#amazonrekognition-actions-as-permissions)\. 

**To Detect Labels in a Video**

1. Configure user access to Amazon Rekognition Video and configure Amazon Rekognition Video access to Amazon SNS\. For more information, see [Configuring Amazon Rekognition Video](api-video-roles.md)\. You don't need to do steps 3, 4, 5, and 6 because the example code creates and configures the Amazon SNS topic and Amazon SQS queue\. 

1. Upload an MOV or MPEG\-4 format video file to an Amazon S3 Bucket\. For test purposes, upload a video that's no longer than 30 seconds in length\.

   For instructions, see [Uploading Objects into Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. Use the following code to detect labels in a video\. 

   In the function `main`:
   + Replace `roleArn` with the ARN of the IAM service role that you created in step 7 of [To configure Amazon Rekognition Video](api-video-roles.md#configure-rekvid-procedure)\.
   + Replace the values of `bucket` and `video` with the bucket and video file name that you specified in step 2\. 

------
#### [ Java ]

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

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   import json
   import sys
   import time
   
   
   
   class VideoDetect:
       jobId = ''
       rek = boto3.client('rekognition')
       sqs = boto3.client('sqs')
       sns = boto3.client('sns')
       
       roleArn = ''
       bucket = ''
       video = ''
       startJobId = ''
   
       sqsQueueUrl = ''
       snsTopicArn = ''
       processType = ''
   
       def __init__(self, role, bucket, video):    
           self.roleArn = role
           self.bucket = bucket
           self.video = video
   
       def GetSQSMessageSuccess(self):
   
           jobFound = False
           succeeded = False
       
           dotLine=0
           while jobFound == False:
               sqsResponse = self.sqs.receive_message(QueueUrl=self.sqsQueueUrl, MessageAttributeNames=['ALL'],
                                             MaxNumberOfMessages=10)
   
               if sqsResponse:
                   
                   if 'Messages' not in sqsResponse:
                       if dotLine<40:
                           print('.', end='')
                           dotLine=dotLine+1
                       else:
                           print()
                           dotLine=0    
                       sys.stdout.flush()
                       time.sleep(5)
                       continue
   
                   for message in sqsResponse['Messages']:
                       notification = json.loads(message['Body'])
                       rekMessage = json.loads(notification['Message'])
                       print(rekMessage['JobId'])
                       print(rekMessage['Status'])
                       if rekMessage['JobId'] == self.startJobId:
                           print('Matching Job Found:' + rekMessage['JobId'])
                           jobFound = True
                           if (rekMessage['Status']=='SUCCEEDED'):
                               succeeded=True
   
                           self.sqs.delete_message(QueueUrl=self.sqsQueueUrl,
                                          ReceiptHandle=message['ReceiptHandle'])
                       else:
                           print("Job didn't match:" +
                                 str(rekMessage['JobId']) + ' : ' + self.startJobId)
                       # Delete the unknown message. Consider sending to dead letter queue
                       self.sqs.delete_message(QueueUrl=self.sqsQueueUrl,
                                      ReceiptHandle=message['ReceiptHandle'])
   
   
           return succeeded
   
       def StartLabelDetection(self):
           response=self.rek.start_label_detection(Video={'S3Object': {'Bucket': self.bucket, 'Name': self.video}},
               NotificationChannel={'RoleArn': self.roleArn, 'SNSTopicArn': self.snsTopicArn})
   
           self.startJobId=response['JobId']
           print('Start Job Id: ' + self.startJobId)
   
   
       def GetLabelDetectionResults(self):
           maxResults = 10
           paginationToken = ''
           finished = False
   
           while finished == False:
               response = self.rek.get_label_detection(JobId=self.startJobId,
                                               MaxResults=maxResults,
                                               NextToken=paginationToken,
                                               SortBy='TIMESTAMP')
   
               print('Codec: ' + response['VideoMetadata']['Codec'])
               print('Duration: ' + str(response['VideoMetadata']['DurationMillis']))
               print('Format: ' + response['VideoMetadata']['Format'])
               print('Frame rate: ' + str(response['VideoMetadata']['FrameRate']))
               print()
   
               for labelDetection in response['Labels']:
                   label=labelDetection['Label']
   
                   print("Timestamp: " + str(labelDetection['Timestamp']))
                   print("   Label: " + label['Name'])
                   print("   Confidence: " +  str(label['Confidence']))
                   print("   Instances:")
                   for instance in label['Instances']:
                       print ("      Confidence: " + str(instance['Confidence']))
                       print ("      Bounding box")
                       print ("        Top: " + str(instance['BoundingBox']['Top']))
                       print ("        Left: " + str(instance['BoundingBox']['Left']))
                       print ("        Width: " +  str(instance['BoundingBox']['Width']))
                       print ("        Height: " +  str(instance['BoundingBox']['Height']))
                       print()
                   print()
                   print ("   Parents:")
                   for parent in label['Parents']:
                       print ("      " + parent['Name'])
                   print ()
   
                   if 'NextToken' in response:
                       paginationToken = response['NextToken']
                   else:
                       finished = True
          
       
       def CreateTopicandQueue(self):
         
           millis = str(int(round(time.time() * 1000)))
   
           #Create SNS topic
           
           snsTopicName="AmazonRekognitionExample" + millis
   
           topicResponse=self.sns.create_topic(Name=snsTopicName)
           self.snsTopicArn = topicResponse['TopicArn']
   
           #create SQS queue
           sqsQueueName="AmazonRekognitionQueue" + millis
           self.sqs.create_queue(QueueName=sqsQueueName)
           self.sqsQueueUrl = self.sqs.get_queue_url(QueueName=sqsQueueName)['QueueUrl']
    
           attribs = self.sqs.get_queue_attributes(QueueUrl=self.sqsQueueUrl,
                                                       AttributeNames=['QueueArn'])['Attributes']
                                           
           sqsQueueArn = attribs['QueueArn']
   
           # Subscribe SQS queue to SNS topic
           self.sns.subscribe(
               TopicArn=self.snsTopicArn,
               Protocol='sqs',
               Endpoint=sqsQueueArn)
   
           #Authorize SNS to write SQS queue 
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
   }}""".format(sqsQueueArn, self.snsTopicArn)
    
           response = self.sqs.set_queue_attributes(
               QueueUrl = self.sqsQueueUrl,
               Attributes = {
                   'Policy' : policy
               })
   
       def DeleteTopicandQueue(self):
           self.sqs.delete_queue(QueueUrl=self.sqsQueueUrl)
           self.sns.delete_topic(TopicArn=self.snsTopicArn)
   
   
   def main():
       roleArn = ''   
       bucket = ''
       video = ''
   
       analyzer=VideoDetect(roleArn, bucket,video)
       analyzer.CreateTopicandQueue()
   
       analyzer.StartLabelDetection()
       if analyzer.GetSQSMessageSuccess()==True:
           analyzer.GetLabelDetectionResults()
       
       analyzer.DeleteTopicandQueue()
   
   
   if __name__ == "__main__":
       main()
   ```

------

1. Build and run the code\. The operation might take a while to finish\. After it's finished, a list of the labels detected in the video is displayed\. For more information, see [Detecting Labels in a Video](labels-detecting-labels-video.md)\.