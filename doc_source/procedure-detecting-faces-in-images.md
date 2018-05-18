# Detecting Faces in an Image \(SDK\)<a name="procedure-detecting-faces-in-images"></a>

In this procedure you use the [DetectFaces](API_DetectFaces.md) operation to detect faces in an image \(JPEG or PNG\) that you provide as input\. You can provide the input image as an image byte array \(Base64\-encoded image bytes\) or specify an S3 object\. In this exercise, you upload an image \(JPEG or PNG\) to your S3 bucket and specify the object key name\.

The following examples show how you can use the operation with the AWS CLI, the AWS SDK for Java and the AWS SDK for Python \(Boto\)\. 

For more information, see [Detect Faces in an Image](faces.md#faces-detect-images)\. 

1. Upload an image \(containing one or more faces\) to your S3 bucket\. 

   For instructions, see [Uploading Objects into Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. Use the following example code to call the `DetectFaces` API operation\.
   + Using the AWS CLI

     ```
     aws rekognition detect-faces \
     --image '{"S3Object":{"Bucket":"Bucketname","Name":"s3ObjectKey"}}' \
     --attributes "ALL" \
     --region us-east-1 \
     --profile adminuser
     ```
   + Using the AWS SDK for Java\. This example displays the estimated age range for detected faces and lists the JSON for all detected facial attributes\.

     ```
     import java.util.List;
     import com.amazonaws.AmazonClientException;
     import com.amazonaws.auth.AWSCredentials;
     import com.amazonaws.auth.AWSStaticCredentialsProvider;
     import com.amazonaws.auth.profile.ProfileCredentialsProvider;
     import com.amazonaws.regions.Regions;
     import com.amazonaws.services.rekognition.AmazonRekognition;
     import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
     import com.amazonaws.services.rekognition.model.AgeRange;
     import com.amazonaws.services.rekognition.model.AmazonRekognitionException;
     import com.amazonaws.services.rekognition.model.Attribute;
     import com.amazonaws.services.rekognition.model.DetectFacesRequest;
     import com.amazonaws.services.rekognition.model.DetectFacesResult;
     import com.amazonaws.services.rekognition.model.FaceDetail;
     import com.amazonaws.services.rekognition.model.Image;
     import com.amazonaws.services.rekognition.model.S3Object;
     import com.fasterxml.jackson.databind.ObjectMapper;
     
     
     public class DetectFacesExample {
     
        public static void main(String[] args) throws Exception {
     
           String photo = "photo.jpg";
           String bucket = "S3bucket";
     
           AWSCredentials credentials;
           try {
              credentials = new ProfileCredentialsProvider("AdminUser").getCredentials();
           } catch (Exception e) {
              throw new AmazonClientException("Cannot load the credentials from the credential profiles file. "
                 + "Please make sure that your credentials file is at the correct "
                 + "location (/Users/userid.aws/credentials), and is in a valid format.", e);
           }
     
           AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder
              .standard()
              .withRegion(Regions.US_WEST_2)
              .withCredentials(new AWSStaticCredentialsProvider(credentials))
              .build();
     
           DetectFacesRequest request = new DetectFacesRequest()
              .withImage(new Image()
                 .withS3Object(new S3Object()
                    .withName(photo)
                    .withBucket(bucket)))
              .withAttributes(Attribute.ALL);
           // Replace Attribute.ALL with Attribute.DEFAULT to get default values.
     
           try {
              DetectFacesResult result = rekognitionClient.detectFaces(request);
              List < FaceDetail > faceDetails = result.getFaceDetails();
     
              for (FaceDetail face: faceDetails) {
                 if (request.getAttributes().contains("ALL")) {
                    AgeRange ageRange = face.getAgeRange();
                    System.out.println("The detected face is estimated to be between "
                       + ageRange.getLow().toString() + " and " + ageRange.getHigh().toString()
                       + " years old.");
                    System.out.println("Here's the complete set of attributes:");
                 } else { // non-default attributes have null values.
                    System.out.println("Here's the default set of attributes:");
                 }
     
                 ObjectMapper objectMapper = new ObjectMapper();
                 System.out.println(objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(face));
              }
     
           } catch (AmazonRekognitionException e) {
              e.printStackTrace();
           }
     
        }
     
     }
     ```
   + Using AWS SDK for Python \(Boto\)\. This example displays the estimated age range for detected faces and lists the JSON for all detected facial attributes\.

     ```
     import boto3
     import json
     
     if __name__ == "__main__":
         fileName='input.jpg'
         bucket='bucket'
         client=boto3.client('rekognition','us-east-1')
     
         response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':fileName}},Attributes=['ALL'])
     
         print('Detected faces for ' + fileName)
         for faceDetail in response['FaceDetails']:
             print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
                   + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
             print('Here are the other attributes:')
             print(json.dumps(faceDetail, indent=4, sort_keys=True))
     ```