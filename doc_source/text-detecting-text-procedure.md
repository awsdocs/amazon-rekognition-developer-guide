# Detecting Text in an Image<a name="text-detecting-text-procedure"></a>

You can provide an input image as an image byte array \(base64\-encoded image bytes\) or as an Amazon S3 object\. In this procedure, you upload a \.jpeg or \.png image to your S3 bucket and specify the file name\. 

## Prerequisites<a name="text-detection-prerequisites"></a>

To detect text in images:

+ You need the AWS Command Line Interface \(AWS CLI\) or AWS SDK for Java\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\.

+ The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. 

## <a name="procedure-detect-text-cli"></a>

**To detect text in an image \(AWS CLI\)**

1. Upload an image that contains text to your S3 bucket\. 

   For instructions, see [Uploading Objects into Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. At the command line, run the following command\. Replace `bucketname` and `input.jpg` with the names of the S3 bucket and image from Step 1\. Replace `region` with the name of the region you are using\. For information about Amazon Rekognition regions and endpoints, see [Regions and Endpoints](http://docs.aws.amazon.com/general/latest/gr/rande.html)\.

   ```
   aws rekognition detect-text \
   --image "S3Object={Bucket=bucketname,Name=input.jpg}" \
   --region region
   ```

1. Choose **Enter**\. You'll see the JSON output for the `DetectText` operation\.

## <a name="procedure-detect-text-cli"></a>

**To detect text in an image \(API\)**

1. Upload an image that contains text to your S3 bucket\. 

   For instructions, see [Uploading Objects into Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. In the AWS SDK for Java, run the following example code\. Replace `bucketname` and `input.jpg` with the names of the S3 bucket and image that you used in Step 1\. Replace `Regions.US_EAST_1` with the name of the region you are using\.

   ```
   package com.amazonaws.samples;
   
   import java.util.List;
   
   import com.amazonaws.AmazonClientException;
   import com.amazonaws.auth.AWSCredentials;
   import com.amazonaws.auth.AWSStaticCredentialsProvider;
   import com.amazonaws.auth.profile.ProfileCredentialsProvider;
   import com.amazonaws.regions.Regions;
   import com.amazonaws.services.rekognition.model.AmazonRekognitionException;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.DetectTextRequest;
   import com.amazonaws.services.rekognition.model.DetectTextResult;
   import com.amazonaws.services.rekognition.model.Image;
   import com.amazonaws.services.rekognition.model.S3Object;
   import com.amazonaws.services.rekognition.model.TextDetection;
   
   
   
   public class TextDetectionInImage {
   
      public static void main(String[] args) throws Exception {
         
     
         String photo = "input.jpg";
         String bucket = "bucketname";
   
         AWSCredentials credentials;
         try {
             credentials = new ProfileCredentialsProvider("AdminUser").getCredentials();
         } catch(Exception e) {
            throw new AmazonClientException("Cannot load the credentials from the credential profiles file. "
             + "Please make sure that your credentials file is at the correct "
             + "location (/Users/userid/.aws/credentials), and is in a valid format.", e);
         }
   
   
         AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder
                 .standard()
                 .withRegion(Regions.US_EAST_1)
                 .withCredentials(new AWSStaticCredentialsProvider(credentials))
                 .build();
         
         
         DetectTextRequest request = new DetectTextRequest()
                 .withImage(new Image()
                 .withS3Object(new S3Object()
                 .withName(photo)
                 .withBucket(bucket)));
       
   
         try {
            DetectTextResult result = rekognitionClient.detectText(request);
            List<TextDetection> textDetections = result.getTextDetections();
   
            System.out.println("Detected lines and words for " + photo);
            for (TextDetection text: textDetections) {
         
                    System.out.println("Detected: " + text.getDetectedText());
                    System.out.println("Confidence: " + text.getConfidence().toString());
                    System.out.println("Id : " + text.getId());
                    System.out.println("Parent Id: " + text.getParentId());
                    System.out.println("Type: " + text.getType());
                    System.out.println();
            }
         } catch(AmazonRekognitionException e) {
            e.printStackTrace();
         }
      }
   }
   ```