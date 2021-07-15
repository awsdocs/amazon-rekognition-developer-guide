# Detecting personal protective equipment in an image<a name="ppe-procedure-image"></a>

To detect Personal Protective Equipment \(PPE\) on persons in an image, use the [DetectProtectiveEquipment](API_DetectProtectiveEquipment.md) non\-storage API operation\. 

You can provide the input image as an image byte array \(base64\-encoded image bytes\) or as an Amazon S3 object, by using the AWS SDK or the AWS Command Line Interface \(AWS CLI\)\. These examples use an image stored in an Amazon S3 bucket\. For more information, see [Working with images](images.md)\. 

**To detect PPE on persons in an image**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` and `AmazonS3ReadOnlyAccess` permissions\. For more information, see [Step 1: Set up an AWS account and create an IAM user](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Upload an image \(that contains one or more persons wearing PPE\) to your S3 bucket\. 

   For instructions, see [Uploading Objects into Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. Use the following examples to call the `DetectProtectiveEquipment` operation\. For information about displaying bounding boxes in an image, see [Displaying bounding boxes](images-displaying-bounding-boxes.md)\.

------
#### [ Java ]

   This example displays information about the PPE items detected on persons detected in an image\. 

   Change the value of `bucket` to the name of the Amazon S3 bucket that contains your image\. Change the value of `photo` to your image file name\.

   ```
   //Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   package com.amazonaws.samples;
   import com.amazonaws.client.builder.AwsClientBuilder;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.AmazonRekognitionException;
   import com.amazonaws.services.rekognition.model.Image;
   import com.amazonaws.services.rekognition.model.ProtectiveEquipmentBodyPart;
   import com.amazonaws.services.rekognition.model.S3Object;
   import com.amazonaws.services.rekognition.model.ProtectiveEquipmentPerson;
   import com.amazonaws.services.rekognition.model.ProtectiveEquipmentSummarizationAttributes;
   
   import java.util.List;
   import com.amazonaws.services.rekognition.model.BoundingBox;
   import com.amazonaws.services.rekognition.model.DetectProtectiveEquipmentRequest;
   import com.amazonaws.services.rekognition.model.DetectProtectiveEquipmentResult;
   import com.amazonaws.services.rekognition.model.EquipmentDetection;
   
   
   public class DetectPPE {
   
       public static void main(String[] args) throws Exception {
   
           String photo = "photo";
           String bucket = "bucket";
   
   
           AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
           
           ProtectiveEquipmentSummarizationAttributes summaryAttributes = new ProtectiveEquipmentSummarizationAttributes()
                   .withMinConfidence(80F)
                   .withRequiredEquipmentTypes("FACE_COVER", "HAND_COVER", "HEAD_COVER");
                   
           DetectProtectiveEquipmentRequest request = new DetectProtectiveEquipmentRequest()
                   .withImage(new Image()
                           .withS3Object(new S3Object()
                                   .withName(photo).withBucket(bucket)))
                   .withSummarizationAttributes(summaryAttributes);
   
           try {
               System.out.println("Detected PPE for people in image " + photo);
               System.out.println("Detected people\n---------------");
               DetectProtectiveEquipmentResult result = rekognitionClient.detectProtectiveEquipment(request);
   
   
               List <ProtectiveEquipmentPerson> persons = result.getPersons();
   
   
               for (ProtectiveEquipmentPerson person: persons) {
                   System.out.println("ID: " + person.getId());
                   List<ProtectiveEquipmentBodyPart> bodyParts=person.getBodyParts();
                   if (bodyParts.isEmpty()){
                       System.out.println("\tNo body parts detected");
                   } else
                       for (ProtectiveEquipmentBodyPart bodyPart: bodyParts) {
                           System.out.println("\t" + bodyPart.getName() + ". Confidence: " + bodyPart.getConfidence().toString());
   
   
   
                           List<EquipmentDetection> equipmentDetections=bodyPart.getEquipmentDetections();
   
                           if (equipmentDetections.isEmpty()){
                               System.out.println("\t\tNo PPE Detected on " + bodyPart.getName());
   
                           } 
                           else {
                               for (EquipmentDetection item: equipmentDetections) {
                                   System.out.println("\t\tItem: " + item.getType() + ". Confidence: " + item.getConfidence().toString());
                                   System.out.println("\t\tCovers body part: " 
                                           + item.getCoversBodyPart().getValue().toString() + ". Confidence: " + item.getCoversBodyPart().getConfidence().toString());
   
                                   System.out.println("\t\tBounding Box");
                                   BoundingBox box =item.getBoundingBox();
   
                                   System.out.println("\t\tLeft: " +box.getLeft().toString());
                                   System.out.println("\t\tTop: " + box.getTop().toString());
                                   System.out.println("\t\tWidth: " + box.getWidth().toString());
                                   System.out.println("\t\tHeight: " + box.getHeight().toString());
                                   System.out.println("\t\tConfidence: " + item.getConfidence().toString());
                                   System.out.println();
                               }
                           }
   
                       }
               }
               System.out.println("Person ID Summary\n-----------------");
               
               //List<Integer> list=;
               DisplaySummary("With required equipment", result.getSummary().getPersonsWithRequiredEquipment());
               DisplaySummary("Without required equipment", result.getSummary().getPersonsWithoutRequiredEquipment());
               DisplaySummary("Indeterminate", result.getSummary().getPersonsIndeterminate());         
          
               
           } catch(AmazonRekognitionException e) {
               e.printStackTrace();
           }
       }
       static void DisplaySummary(String summaryType,List<Integer> idList)
       {
           System.out.print(summaryType + "\n\tIDs  ");
           if (idList.size()==0) {
               System.out.println("None");
           }
           else {
               int count=0;
               for (Integer id: idList ) { 
                   if (count++ == idList.size()-1) {
                       System.out.println(id.toString());
                   }
                   else {
                       System.out.print(id.toString() + ", ");
                   }
               }
           }
                       
           System.out.println();
           
       
       }
   }
   ```

------
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/DetectPPE.java)\.

   ```
       public static void displayGear(S3Client s3,
                                      RekognitionClient rekClient,
                                      String sourceImage,
                                      String bucketName) {
   
           byte[] data = getObjectBytes (s3, bucketName, sourceImage);
           InputStream is = new ByteArrayInputStream(data);
   
           try {
               ProtectiveEquipmentSummarizationAttributes summarizationAttributes = ProtectiveEquipmentSummarizationAttributes.builder()
                       .minConfidence(80F)
                       .requiredEquipmentTypesWithStrings("FACE_COVER", "HAND_COVER", "HEAD_COVER")
                       .build();
   
               SdkBytes sourceBytes = SdkBytes.fromInputStream(is);
               software.amazon.awssdk.services.rekognition.model.Image souImage = Image.builder()
                       .bytes(sourceBytes)
                       .build();
   
               DetectProtectiveEquipmentRequest request = DetectProtectiveEquipmentRequest.builder()
                       .image(souImage)
                       .summarizationAttributes(summarizationAttributes)
                       .build();
   
               DetectProtectiveEquipmentResponse result = rekClient.detectProtectiveEquipment(request);
               List<ProtectiveEquipmentPerson> persons = result.persons();
   
               for (ProtectiveEquipmentPerson person: persons) {
                   System.out.println("ID: " + person.id());
                   List<ProtectiveEquipmentBodyPart> bodyParts=person.bodyParts();
                   if (bodyParts.isEmpty()){
                       System.out.println("\tNo body parts detected");
                   } else
                       for (ProtectiveEquipmentBodyPart bodyPart: bodyParts) {
                           System.out.println("\t" + bodyPart.name() + ". Confidence: " + bodyPart.confidence().toString());
                           List<EquipmentDetection> equipmentDetections=bodyPart.equipmentDetections();
   
                           if (equipmentDetections.isEmpty()){
                               System.out.println("\t\tNo PPE Detected on " + bodyPart.name());
                           } else {
                               for (EquipmentDetection item: equipmentDetections) {
                                   System.out.println("\t\tItem: " + item.type() + ". Confidence: " + item.confidence().toString());
                                   System.out.println("\t\tCovers body part: "
                                           + item.coversBodyPart().value().toString() + ". Confidence: " + item.coversBodyPart().confidence().toString());
   
                                   System.out.println("\t\tBounding Box");
                                   BoundingBox box =item.boundingBox();
   
                                   System.out.println("\t\tLeft: " +box.left().toString());
                                   System.out.println("\t\tTop: " + box.top().toString());
                                   System.out.println("\t\tWidth: " + box.width().toString());
                                   System.out.println("\t\tHeight: " + box.height().toString());
                                   System.out.println("\t\tConfidence: " + item.confidence().toString());
                                   System.out.println();
                               }
                           }
                       }
               }
               System.out.println("Person ID Summary\n-----------------");
   
               DisplaySummary("With required equipment", result.summary().personsWithRequiredEquipment());
               DisplaySummary("Without required equipment", result.summary().personsWithoutRequiredEquipment());
               DisplaySummary("Indeterminate", result.summary().personsIndeterminate());
   
           } catch (RekognitionException e) {
               e.printStackTrace();
               System.exit(1);
           } catch (Exception e) {
               e.printStackTrace();
           }
       }
   
       public static byte[] getObjectBytes (S3Client s3, String bucketName, String keyName) {
   
           try {
               GetObjectRequest objectRequest = GetObjectRequest
                       .builder()
                       .key(keyName)
                       .bucket(bucketName)
                       .build();
   
               ResponseBytes<GetObjectResponse> objectBytes = s3.getObjectAsBytes(objectRequest);
               byte[] data = objectBytes.asByteArray();
               return data;
   
           } catch (S3Exception e) {
               System.err.println(e.awsErrorDetails().errorMessage());
               System.exit(1);
           }
           return null;
       }
   
       static void DisplaySummary(String summaryType,List<Integer> idList)
       {
           System.out.print(summaryType + "\n\tIDs  ");
           if (idList.size()==0) {
               System.out.println("None");
           }
           else {
               int count=0;
               for (Integer id: idList ) {
                   if (count++ == idList.size()-1) {
                       System.out.println(id.toString());
                   }
                   else {
                       System.out.print(id.toString() + ", ");
                   }
               }
           }
           System.out.println();
       }
   ```

------
#### [ AWS CLI ]

   This AWS CLI command requests a PPE summary and displays the JSON output for the `detect-protective-equipment` CLI operation\. 

   Change `bucketname` to the name of an Amazon S3 bucket that contains an image\. Change `input.jpg` to the name of the image that you want to use\.

   ```
   aws rekognition detect-protective-equipment \
     --image "S3Object={Bucket=bucketname,Name=input.jpg}" \
     --summarization-attributes "MinConfidence=80,RequiredEquipmentTypes=['FACE_COVER','HAND_COVER','HEAD_COVER']"
   ```

   This AWS CLI command displays the JSON output for the `detect-protective-equipment` CLI operation\. 

   Change `bucketname` to the name of an Amazon S3 bucket that contains an image\. Change `input.jpg` to the name of the image that you want to use\.

   ```
   aws rekognition detect-protective-equipment \
     --image "S3Object={Bucket=bucketname,Name=input.jpg}"
   ```

------
#### [ Python ]

   This example displays information about the PPE items detected on persons detected in an image\. 

   Change the value of `bucket` to the name of the Amazon S3 bucket that contains your image\. Change the value of `photo` to your image file name\.

   ```
   #Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   
   def detect_labels(photo, bucket):
   
       client=boto3.client('rekognition')
   
       response = client.detect_protective_equipment(Image={'S3Object':{'Bucket':bucket,'Name':photo}}, 
           SummarizationAttributes={'MinConfidence':80, 'RequiredEquipmentTypes':['FACE_COVER', 'HAND_COVER', 'HEAD_COVER']})
           
    
       print('Detected PPE for people in image ' + photo) 
       print('\nDetected people\n---------------')   
       for person in response['Persons']:
           
           print('Person ID: ' + str(person['Id']))
           print ('Body Parts\n----------')
           body_parts = person['BodyParts']
           if len(body_parts) == 0:
                   print ('No body parts found')
           else:
               for body_part in body_parts:
                   print('\t'+ body_part['Name'] + '\n\t\tConfidence: ' + str(body_part['Confidence']))
                   print('\n\t\tDetected PPE\n\t\t------------')
                   ppe_items = body_part['EquipmentDetections']
                   if len(ppe_items) ==0:
                       print ('\t\tNo PPE detected on ' + body_part['Name'])
                   else:    
                       for ppe_item in ppe_items:
                           print('\t\t' + ppe_item['Type'] + '\n\t\t\tConfidence: ' + str(ppe_item['Confidence'])) 
                           print('\t\tCovers body part: ' + str(ppe_item['CoversBodyPart']['Value']) + '\n\t\t\tConfidence: ' + str(ppe_item['CoversBodyPart']['Confidence']))
                           print('\t\tBounding Box:')
                           print ('\t\t\tTop: ' + str(ppe_item['BoundingBox']['Top']))
                           print ('\t\t\tLeft: ' + str(ppe_item['BoundingBox']['Left']))
                           print ('\t\t\tWidth: ' +  str(ppe_item['BoundingBox']['Width']))
                           print ('\t\t\tHeight: ' +  str(ppe_item['BoundingBox']['Height']))
                           print ('\t\t\tConfidence: ' + str(ppe_item['Confidence']))
               print()
           print()
   
       print('Person ID Summary\n----------------')
       display_summary('With required equipment',response['Summary']['PersonsWithRequiredEquipment'] )
       display_summary('Without required equipment',response['Summary']['PersonsWithoutRequiredEquipment'] )
       display_summary('Indeterminate',response['Summary']['PersonsIndeterminate'] )
      
       print()
       return len(response['Persons'])
   
   #Display summary information for supplied summary.
   def display_summary(summary_type, summary):
       print (summary_type + '\n\tIDs: ',end='')
       if (len(summary)==0):
           print('None')
       else:
           for num, id in enumerate(summary, start=0):
               if num==len(summary)-1:
                   print (id)
               else:
                   print (str(id) + ', ' , end='')
   
   
   
   def main():
       photo='photo'
       bucket='bucket'
       person_count=detect_labels(photo, bucket)
       print("Persons detected: " + str(person_count))
   
   
   if __name__ == "__main__":
       main()
   ```

------