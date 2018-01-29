# Analysing an Image Loaded from a Local File System<a name="images-bytes"></a>

Rekognition Image operations can analyze images supplied as images bytes or images stored in an S3 bucket\.

This topics provides AWS SDK examples of supplying image bytes to Rekognition Image API operations by using a file loaded from a local file system\. A Rekognition API operation can analyse an image provided as base64 encoded image bytes or it can analyze an image retrieved from an Amazon S3 bucket\. You pass an image to a Rekognition API operation by using the [Image](API_Image.md) input parameter\. Within `Image` you specify the `Bytes` property to pass base64 encoded image bytes or you specify the [S3Object](API_S3Object.md) object property to reference an image stored in an S3 bucket\.

Image bytes passed to a Rekognition API operation using the `Bytes` input parameter must be base64 encoded\. The following common AWS SDKs automatically base64 encode images and you do not need to encode image bytes prior to calling a Rekognition API operation\.

+ Java

+ JavaScript

+ Python

+ PHP

If you are using another AWS SDK and get an image format error when calling a Rekognition API operation, try base64 encoding the image bytes before passing them to a Rekognition API operation\.

**Note**  
The image does not need to be base64 encoded if you pass an image stored in an `S3Object` instead of image bytes\.

 If you use HTTP to call Rekognition Image operations, the image bytes must be a base64\-encoded string\. For more information, see [Working with Images](images.md)\.

If you use the AWS CLI to call Amazon Rekognition operations, passing image bytes is not supported\.

 The following examples show how to load images from the local file system and supply the image bytes to a Rekognition operation\. 


+ [Supplying Images: Using the Local File System and Java](#images-bytes-java)
+ [Supplying Images: Using the Local File System and Python](#images-bytes-python)
+ [Supplying Images: Using the Local File System and PHP](#images-bytes-php)

## Supplying Images: Using the Local File System and Java<a name="images-bytes-java"></a>

The following Java example shows how to load an image from the local file system and detect labels using the [detectLabels](http://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/rekognition/AmazonRekognition.html#detectLabels-com.amazonaws.services.rekognition.model.DetectLabelsRequest-) AWS SDK operation\.

```
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.nio.ByteBuffer;
import java.util.List;
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
import com.amazonaws.util.IOUtils;

public class DetectLabelsExampleImageBytes {
    public static void main(String[] args) throws Exception {
    	String photo="/path/inputimage.jpg";

        AWSCredentials credentials;
        try {
            credentials = new ProfileCredentialsProvider("AdminUser").getCredentials();
        } catch (Exception e) {
            throw new AmazonClientException("Cannot load the credentials from the credential profiles file. "
                    + "Please make sure that your credentials file is at the correct "
                    + "location (/Usersuserid.aws/credentials), and is in a valid format.", e);
        }
        ByteBuffer imageBytes;
        try (InputStream inputStream = new FileInputStream(new File(photo))) {
            imageBytes = ByteBuffer.wrap(IOUtils.toByteArray(inputStream));
        }


        AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder
          		.standard()
          		.withRegion(Regions.US_WEST_2)
        		.withCredentials(new AWSStaticCredentialsProvider(credentials))
        		.build();

        DetectLabelsRequest request = new DetectLabelsRequest()
                .withImage(new Image()
                        .withBytes(imageBytes))
                .withMaxLabels(10)
                .withMinConfidence(77F);

        try {

            DetectLabelsResult result = rekognitionClient.detectLabels(request);
            List <Label> labels = result.getLabels();

            System.out.println("Detected labels for " + photo);
            for (Label label: labels) {
               System.out.println(label.getName() + ": " + label.getConfidence().toString());
            }

        } catch (AmazonRekognitionException e) {
            e.printStackTrace();
        }

    }
}
```

## Supplying Images: Using the Local File System and Python<a name="images-bytes-python"></a>

The following [AWS SDK for Python](https://aws.amazon.com/sdk-for-python/) example shows how to load an image from the local file system and call the [detect\_labels](http://boto3.readthedocs.org/en/latest/reference/services/rekognition.html#Rekognition.Client.detect_labels) operation\. 

```
import boto3

if __name__ == "__main__":

    imageFile='input.jpg'
    client=boto3.client('rekognition','us-west-2')
   
    with open(imageFile, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        
    print('Detected labels in ' + imageFile)    
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))

    print('Done...')
```

## Supplying Images: Using the Local File System and PHP<a name="images-bytes-php"></a>

The following [AWS SDK for PHP](http://docs.aws.amazon.com/aws-sdk-php/v3/guide/index.html#getting-started) example shows how to load an image from the local file system and call the [DetectFaces](http://docs.aws.amazon.com/aws-sdk-php/v3/api/api-rekognition-2016-06-27.html#detectfaces) API operation\. 

```
<?php
    require 'path/vendor/autoload.php';

    use Aws\Rekognition\RekognitionClient;

    $options = [
        'region'            => 'us-west-2',
        'version'           => '2016-06-27',
    ];

    $rekognition = new RekognitionClient($options);

    #Get local image
    $fp_image = fopen('test.png', 'r');
    $image = fread($fp_image, filesize('test.png'));
    fclose($fp_image);


    # Call DetectFaces
    $result = $rekognition->DetectFaces(array(
       'Image' => array(
          'Bytes' => $image,
       ),
       'Attributes' => array('ALL')
       )
    );

    # Display info for each detected person
    print 'People: Image position and estimated age' . PHP_EOL;
    for ($n=0;$n<sizeof($result['FaceDetails']); $n++){

      print 'Position: ' . $result['FaceDetails'][$n]['BoundingBox']['Left'] . " "
      . $result['FaceDetails'][$n]['BoundingBox']['Top']
      . PHP_EOL
      . 'Age (low): '.$result['FaceDetails'][$n]['AgeRange']['Low']
      .  PHP_EOL
      . 'Age (high): ' . $result['FaceDetails'][$n]['AgeRange']['High']
      .  PHP_EOL . PHP_EOL;
    }
?>
```