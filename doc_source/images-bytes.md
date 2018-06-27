# Analyzing an Image Loaded from a Local File System<a name="images-bytes"></a>

Amazon Rekognition Image operations can analyze images that are supplied as image bytes or images stored in an Amazon S3 bucket\.

These topics provide examples of supplying image bytes to Amazon Rekognition Image API operations by using a file loaded from a local file system\. You pass image bytes to a Rekognition API operation by using the [Image](API_Image.md) input parameter\. Within `Image`, you specify the `Bytes` property to pass base64\-encoded image bytes\.

Image bytes passed to a Rekognition API operation by using the `Bytes` input parameter must be base64 encoded\. The AWS SDKs that these examples use automatically base64\-encode images\. You don't need to encode image bytes before calling a Rekognition API operation\. For more information, see [Images](images-information.md)\. 

In this example JSON request for `DetectLabels`, the source image bytes are passed in the `Bytes` input parameter\. 

```
{
    "Image": {
        "Bytes": "/9j/4AAQSk....."
    },
    "MaxLabels": 10,
    "MinConfidence": 77
}
```

The following examples use various AWS SDKs and the AWS CLI to call `DetectLabels`\. For information about the `DetectLabels` operation response, see [DetectLabels Response](labels-detect-labels-image.md#detectlabels-response)\.

For a client\-side JavaScript example, see [Using JavaScript](image-bytes-javascript.md)\.

**To detect labels in a local image**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` and `AmazonS3ReadOnlyAccess` permissions\. For more information, see [Step 1: Set Up an AWS Account and Create an IAM User](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Use the following examples to call the `DetectLabels` operation\.

------
#### [ Java ]

   The following Java example shows how to load an image from the local file system and detect labels by using the [detectLabels](http://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/rekognition/AmazonRekognition.html#detectLabels-com.amazonaws.services.rekognition.model.DetectLabelsRequest-) AWS SDK operation\. Change the value of `photo` to the path and file name of an image file \(\.jpg or \.png format\)\.

   ```
   package aws.example.rekognition.image;
   import java.io.File;
   import java.io.FileInputStream;
   import java.io.InputStream;
   import java.nio.ByteBuffer;
   import java.util.List;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.AmazonClientException;
   import com.amazonaws.services.rekognition.model.AmazonRekognitionException;
   import com.amazonaws.services.rekognition.model.DetectLabelsRequest;
   import com.amazonaws.services.rekognition.model.DetectLabelsResult;
   import com.amazonaws.services.rekognition.model.Image;
   import com.amazonaws.services.rekognition.model.Label;
   import com.amazonaws.util.IOUtils;
   
   public class DetectLabelsLocalFile {
       public static void main(String[] args) throws Exception {
       	String photo="input.jpg";
   
   
           ByteBuffer imageBytes;
           try (InputStream inputStream = new FileInputStream(new File(photo))) {
               imageBytes = ByteBuffer.wrap(IOUtils.toByteArray(inputStream));
           }
   
   
           AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
   
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

------
#### [ Python ]

   The following [AWS SDK for Python](https://aws.amazon.com/sdk-for-python/) example shows how to load an image from the local file system and call the [detect\_labels](http://boto3.readthedocs.org/en/latest/reference/services/rekognition.html#Rekognition.Client.detect_labels) operation\. Change the value of `imageFile` to the path and file name of an image file \(\.jpg or \.png format\)\. 

   ```
   import boto3
   
   if __name__ == "__main__":
   
       imageFile='input.jpg'
       client=boto3.client('rekognition')
      
       with open(imageFile, 'rb') as image:
           response = client.detect_labels(Image={'Bytes': image.read()})
           
       print('Detected labels in ' + imageFile)    
       for label in response['Labels']:
           print (label['Name'] + ' : ' + str(label['Confidence']))
   
       print('Done...')
   ```

------
#### [ \.NET ]

   The following example shows how to load an image from the local file system and detect labels by using the `DetectLabels` operation\. Change the value of `photo` to the path and file name of an image file \(\.jpg or \.png format\)\.

   ```
   using System;
   using System.IO;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   public class DetectLabelsLocalfile
   {
       public static void Example()
       {
           String photo = "input.jpg";
   
           Amazon.Rekognition.Model.Image image = new Amazon.Rekognition.Model.Image();
           try
           {
               using (FileStream fs = new FileStream(photo, FileMode.Open, FileAccess.Read))
               {
                   byte[] data = null;
                   data = new byte[fs.Length];
                   fs.Read(data, 0, (int)fs.Length);
                   image.Bytes = new MemoryStream(data);
               }
           }
           catch (Exception)
           {
               Console.WriteLine("Failed to load file " + photo);
               return;
           }
   
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           DetectLabelsRequest detectlabelsRequest = new DetectLabelsRequest()
           {
               Image = image,
               MaxLabels = 10,
               MinConfidence = 77F
           };
   
           try
           {
               DetectLabelsResponse detectLabelsResponse = rekognitionClient.DetectLabels(detectlabelsRequest);
               Console.WriteLine("Detected labels for " + photo);
               foreach (Label label in detectLabelsResponse.Labels)
                   Console.WriteLine("{0}: {1}", label.Name, label.Confidence);
           }
           catch (Exception e)
           {
               Console.WriteLine(e.Message);
           }
       }
   }
   ```

------
#### [ PHP ]

   The following [AWS SDK for PHP](http://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/welcome.html#getting-started) example shows how to load an image from the local file system and call the [DetectFaces](http://docs.aws.amazon.com/aws-sdk-php/v3/api/api-rekognition-2016-06-27.html#detectfaces) API operation\. Change the value of `photo` to the path and file name of an image file \(\.jpg or \.png format\)\. 

   ```
   <?php
       require 'vendor/autoload.php';
   
       use Aws\Rekognition\RekognitionClient;
   
       $options = [
          'region'            => 'us-west-2',
           'version'           => 'latest'
       ];
   
       $rekognition = new RekognitionClient($options);
   	
       #Get local image
       $photo = 'input.jpg';
       $fp_image = fopen($photo, 'r');
       $image = fread($fp_image, filesize($photo));
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

------