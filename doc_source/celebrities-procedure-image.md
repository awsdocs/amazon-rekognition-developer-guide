# Recognizing Celebrities in an Image<a name="celebrities-procedure-image"></a>

You can use the [RecognizeCelebrities](API_RecognizeCelebrities.md) operation to recognize celebrities in an image that you supply\. You can provide the input image as an image byte array \(base64\-encoded image bytes\) or as an S3 object, using either the AWS command line interface \(AWS CLI\) or the AWS SDK for Java\. In the AWS CLI procedure, you upload an image in \.jpg or \.png format to an S3 bucket\. In the AWS SDK for Java procedure, you use an image loaded from your local file system\.

## Prerequisites<a name="recognize-celebrities-prerequisites"></a>

To run this procedure, you need to have the AWS CLI and AWS SDK for Java installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\. You also need an image file that contains one or more celebrity faces\.

## <a name="to-recognize-celebrities-in-an-image-cli"></a>

**To recognize celebrities in an image \(AWS CLI\)**

1. Upload an image that contains one or more celebrity faces to your S3 bucket\. 

   For instructions, see [Uploading Objects into Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. On the command line, type the following command\. Replace `bucketname` and `input.jpg` with the S3 bucket name and image name that you used in step 1\.

   ```
   aws rekognition recognize-celebrities \
     --image "S3Object={Bucket=bucketname,Name=input.jpg}"
   ```

1. To run the command, choose **Enter**\. The JSON output for the `RecognizeCelebrities` API operation is displayed\.

1. Record the value of one of the celebrity IDs that are displayed\. You'll need it in [Getting Information about a Celebrity](get-celebrity-info-procedure.md)\.

## <a name="to-recognize-celebrities-in-an-image-api"></a>

**To recognize celebrities in an image \(API\)**

1. To recognize celebrities in an image, use the following AWS SDK for Java example code\. Replace `input.jpg` with the name and location of a locally stored \.jpg image file that contains one or more celebrity faces\.

   ```
      import java.util.List;
      import com.amazonaws.AmazonClientException;
      import com.amazonaws.auth.AWSCredentials;
      import com.amazonaws.auth.AWSStaticCredentialsProvider;
      import com.amazonaws.auth.profile.ProfileCredentialsProvider;
      import com.amazonaws.regions.Regions;
      import com.amazonaws.services.rekognition.AmazonRekognition;
      import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
      import com.amazonaws.services.rekognition.model.Image;
      import com.amazonaws.services.rekognition.model.BoundingBox;
      import com.amazonaws.services.rekognition.model.Celebrity;
      import com.amazonaws.services.rekognition.model.RecognizeCelebritiesRequest;
      import com.amazonaws.services.rekognition.model.RecognizeCelebritiesResult;
      import java.io.File;
      import java.io.FileInputStream;
      import java.io.InputStream;
      import java.nio.ByteBuffer;
      import com.amazonaws.util.IOUtils;
   
      public class Celebs {
   
         public static void main(String[] args) {
            String photo = "input.jpg";
            AWSCredentials credentials;
            try {
               credentials = new ProfileCredentialsProvider("AdminUser").getCredentials();
            } catch (Exception e) {
               throw new AmazonClientException("Cannot load the credentials from the credential profiles file. "
                  + "Please make sure that your credentials file is at the correct "
                  + "location (/Users/<userid>/.aws/credentials), and is in valid format.", e);
            }
   
            ByteBuffer imageBytes=null;
            try (InputStream inputStream = new FileInputStream(new File(photo))) {
               imageBytes = ByteBuffer.wrap(IOUtils.toByteArray(inputStream));
            }
            catch(Exception e)
            {
                System.out.println("Failed to load file " + photo);
                System.exit(1);
            }
   
            AmazonRekognition amazonRekognition = AmazonRekognitionClientBuilder
               .standard()
               .withRegion(Regions.US_WEST_2)
               .withCredentials(new AWSStaticCredentialsProvider(credentials))
               .build();
   
            RecognizeCelebritiesRequest request = new RecognizeCelebritiesRequest()
               .withImage(new Image()
               .withBytes(imageBytes));
   
            System.out.println("Looking for celebrities in image " + photo + "\n");
   
            RecognizeCelebritiesResult result=amazonRekognition.recognizeCelebrities(request);
   
            //Display recognized celebrity information
            List<Celebrity> celebs=result.getCelebrityFaces();
            System.out.println(celebs.size() + " celebrity(s) were recognized.\n");
   
            for (Celebrity celebrity: celebs) {
                System.out.println("Celebrity recognized: " + celebrity.getName());
                System.out.println("Celebrity ID: " + celebrity.getId());
                BoundingBox boundingBox=celebrity.getFace().getBoundingBox();
                System.out.println("position: " +
                   boundingBox.getLeft().toString() + " " +
                   boundingBox.getTop().toString());
                System.out.println("Further information (if available):");
                for (String url: celebrity.getUrls()){
                   System.out.println(url);
                }
                System.out.println();
             }
             System.out.println(result.getUnrecognizedFaces().size() + " face(s) were unrecognized.");
         }
      }
   ```

1. Run the sample code\. The output lists the names of celebrities that were recognized, the celebrity IDs, the location of the celebrities' faces on the image, and links to further information\. The output also tells how many faces weren't recognized\.

1. Record one of the celebrity IDs\. You'll need it in [Getting Information about a Celebrity](get-celebrity-info-procedure.md)\.