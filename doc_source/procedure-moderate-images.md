# Detecting Unsafe Images \(API\)<a name="procedure-moderate-images"></a>

You can use the [DetectModerationLabels](API_DetectModerationLabels.md) operation to determine if an image contains explicit or suggestive adult content\. The image must be in either a \.jpg or a \.png format\. You can provide the input image as an image byte array \(base64\-encoded image bytes\) or specify an S3 object\. In these procedures you upload an image \(\.jpg or \.png\) to your S3 bucket\.

## Prerequisites<a name="moderate-images-prerequisites"></a>

To run these procedures, you need to have the AWS CLI and AWS SDK for Java installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. 

## <a name="to-detect-moderation-labels-in-an-image-cli"></a>

**To detect moderation labels in an image \(AWS CLI\)**

1. Upload an image to your S3 bucket\. 

   For instructions, see [Uploading Objects into Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. On the command line, type the following command\. Replace `bucketname` and `input.jpg` with the S3 bucket name and image name that you used in step 1\.

   ```
   aws rekognition detect-moderation-labels \ 
   --image '{"S3Object":{"Bucket":"bucketname","Name":"input.jpg"}}' \
   --region us-east-1 \
   --profile adminuser
   ```

1. To run the command, choose **Enter**\. The JSON output for the `DetectModerationLabels` API operation is displayed\.

## <a name="to-detect-moderation-labels-in-an-image-api"></a>

**To detect moderation labels in an image \(API\)**

1. Upload an image to your S3 bucket\. 

   For instructions, see [Uploading Objects into Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. To detect moderation labels in an image, use the following AWS SDK for Java example code\. Replace `bucketname` and `input.jpg` with the S3 bucket name and the image file name that you used in step 1\.

   ```
     import com.amazonaws.services.rekognition.AmazonRekognition;
     import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
     import com.amazonaws.AmazonClientException;
     import com.amazonaws.auth.AWSCredentials;
     import com.amazonaws.auth.AWSStaticCredentialsProvider;
     import com.amazonaws.auth.profile.ProfileCredentialsProvider;
     import com.amazonaws.regions.Regions;
     import com.amazonaws.services.rekognition.model.AmazonRekognitionException;
     import com.amazonaws.services.rekognition.model.DetectModerationLabelsRequest;
     import com.amazonaws.services.rekognition.model.DetectModerationLabelsResult;
     import com.amazonaws.services.rekognition.model.Image;
     import com.amazonaws.services.rekognition.model.ModerationLabel;
     import com.amazonaws.services.rekognition.model.S3Object;
   
     import java.util.List;
   
     public class DetectModerationLabelsExample
     {
        public static void main(String[] args) throws Exception
        {
           String image = "input.jpg";
           String bucket = "bucketname";
           AWSCredentials credentials;
           try
           {
               credentials = new ProfileCredentialsProvider("AdminUser").getCredentials();
           }
           catch (Exception e)
           {
              throw new AmazonClientException("Cannot load the credentials from the credential profiles file. "
                         + "Please make sure that your credentials file is at the correct "
                         + "location (/Users/userid/.aws/credentials), and is in valid format.", e);
           }
           AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.standard()
                 .withRegion(Regions.US_WEST_2)
                 .withCredentials(new AWSStaticCredentialsProvider(credentials)).build();
   
           DetectModerationLabelsRequest request = new DetectModerationLabelsRequest()
             .withImage(new Image().withS3Object(new S3Object().withName(image).withBucket(bucket)))
             .withMinConfidence(60F);
           try
           {
                DetectModerationLabelsResult result = rekognitionClient.detectModerationLabels(request);
                List<ModerationLabel> labels = result.getModerationLabels();
                System.out.println("Detected labels for " + image);
                for (ModerationLabel label : labels)
                {
                   System.out.println("Label: " + label.getName()
                    + "\n Confidence: " + label.getConfidence().toString() + "%"
                    + "\n Parent:" + label.getParentName());
               }
            }
            catch (AmazonRekognitionException e)
            {
              e.printStackTrace();
            }
         }
     }
   ```

1. Run the sample code\. The output lists the label name, confidence and parent label for each detected label\.