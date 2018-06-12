# Step 4: Getting Started Using the API<a name="get-started-exercise"></a>

In this exercise you use the [DetectLabels](API_DetectLabels.md) API operation to detect objects, concepts, and scenes in an image \(JPEG or PNG\) that you provide as input\. You can provide the input image as an image byte array \(base64\-encoded image bytes\) or specify an S3 object\. In this exercise you upload a JPEG image to your Amazon S3 bucket and specify the object key name\.

The following examples show how you can use the operation with the AWS CLI, the AWS SDK for Java and the AWS SDK for Python \(Boto\)\. 

1. Upload an image \(containing one or more objects, such as trees, houses, and boat etc\.\) to your S3 bucket\. The exercise assumes a \.jpg image\. If you use \.png, update the code accordingly\.

   For instructions, see [Uploading Objects into Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. Use the following example code to call the `DetectLabels` operation\.
   + Using the AWS CLI
**Note**  
The command specifies the `adminuser` profile that you set up in [Step 2: Set Up the AWS Command Line Interface \(AWS CLI\)](setup-awscli.md)\. Then, the AWS CLI command uses the credentials associated with the adminuser profile to sign and authenticate the request\. If you don't provide this profile, the default profile is assumed\.

     ```
     aws rekognition detect-labels \
     --image '{"S3Object":{"Bucket":"bucketname","Name":"object.jpg"}}' \
     --region us-east-1 \
     --profile adminuser
     ```
   + Using the AWS SDK for Java\.

     ```
     import com.amazonaws.services.rekognition.AmazonRekognition;
     import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
     import com.amazonaws.AmazonClientException;
     import com.amazonaws.auth.AWSCredentials;
     import com.amazonaws.auth.AWSStaticCredentialsProvider;
     import com.amazonaws.auth.profile.ProfileCredentialsProvider;
     import com.amazonaws.regions.Regions;
     import com.amazonaws.services.rekognition.model.AmazonRekognitionException;
     import com.amazonaws.services.rekognition.model.DetectLabelsRequest;
     import com.amazonaws.services.rekognition.model.DetectLabelsResult;
     import com.amazonaws.services.rekognition.model.Image;
     import com.amazonaws.services.rekognition.model.Label;
     import com.amazonaws.services.rekognition.model.S3Object;
     import java.util.List;
     
     public class DetectLabelsExample {
     
        public static void main(String[] args) throws Exception {
     
           String photo = "photo.jpg";
           String bucket = "S3bucket";
     
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
         	         .withRegion(Regions.US_WEST_2)
         	         .withCredentials(new AWSStaticCredentialsProvider(credentials))
         	         .build();
     
           DetectLabelsRequest request = new DetectLabelsRequest()
         		  .withImage(new Image()
         		  .withS3Object(new S3Object()
         		  .withName(photo).withBucket(bucket)))
         		  .withMaxLabels(10)
         		  .withMinConfidence(75F);
     
           try {
              DetectLabelsResult result = rekognitionClient.detectLabels(request);
              List <Label> labels = result.getLabels();
     
              System.out.println("Detected labels for " + photo);
              for (Label label: labels) {
                 System.out.println(label.getName() + ": " + label.getConfidence().toString());
              }
           } catch(AmazonRekognitionException e) {
              e.printStackTrace();
           }
        }
     }
     ```
   + Using AWS SDK for Python \(Boto\)\.

     ```
     
     import boto3
     
     if __name__ == "__main__":
         fileName='input.jpg'
         bucket='rekognition-examples-bucket'
         
         client=boto3.client('rekognition','us-west-2')
     
         response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':fileName}})
     
         print('Detected labels for ' + fileName)    
         for label in response['Labels']:
             print (label['Name'] + ' : ' + str(label['Confidence']))
     ```