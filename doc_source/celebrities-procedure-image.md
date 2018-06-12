# Recognizing Celebrities in an Image<a name="celebrities-procedure-image"></a>

To recognize celebrities within images and get additional information about recognized celebrities, use the [RecognizeCelebrities](API_RecognizeCelebrities.md) non\-storage API operation\. For example, in social media or news and entertainment industries where information gathering can be time critical, you can use the `RecognizeCelebrities` operation to identify as many as 100 celebrities in an image, and return links to celebrity webpages, if they're available\. Amazon Rekognition doesn't remember which image it detected a celebrity in\. Your application must store this information\. 

If you haven't stored the additional information for a celebrity that's returned by `RecognizeCelebrities` and you want to avoid reanalyzing an image to get it, use [GetCelebrityInfo](API_GetCelebrityInfo.md)\. To call `GetCelebrityInfo`, you need the unique identifier that Amazon Rekognition assigns to each celebrity\. The identifier is returned as part of the `RecognizeCelebrities` response for each celebrity recognized in an image\. 

If you have a large collection of images to process for celebrity recognition, consider using [AWS Batch](http://docs.aws.amazon.com/batch/latest/userguide/) to process calls to `RecognizeCelebrities` in batches in the background\. When you add a new image to your collection, you can use an AWS Lambda function to recognize celebrities by calling `RecognizeCelebrities` as the image is uploaded into an S3 bucket\.

## Calling RecognizeCelebrities<a name="recognize-image-example"></a>

You can provide the input image as an image byte array \(base64\-encoded image bytes\) or as an Amazon S3 object, by using either the AWS Command Line Interface \(AWS CLI\) or the AWS SDK\. In the AWS CLI procedure, you upload an image in \.jpg or \.png format to an S3 bucket\. In the AWS SDK for Java procedure, you use an image that's loaded from your local file system\. For information about input image recommendations, see [Working with Images](images.md)\. 

To run this procedure, you need an image file that contains one or more celebrity faces\.

**To recognize celebrities in an image**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` and `AmazonS3ReadOnlyAccess` permissions\. For more information, see [Step 1: Set Up an AWS Account and Create an IAM User](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Use the following examples to call the `RecognizeCelebrities` operation\.

------
#### [ Java ]

   This example displays information about the celebrities that are detected in an image\. 

   Change the value of `photo` to the path and file name of an image file that contains one or more celebrity faces\.

   ```
   
   package aws.example.rekognition.image;
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
   import java.util.List;
   
   
   public class CelebritiesInImage {
   
      public static void main(String[] args) {
         String photo = "moviestars.jpg";
   
         AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
   
         ByteBuffer imageBytes=null;
         try (InputStream inputStream = new FileInputStream(new File(photo))) {
            imageBytes = ByteBuffer.wrap(IOUtils.toByteArray(inputStream));
         }
         catch(Exception e)
         {
             System.out.println("Failed to load file " + photo);
             System.exit(1);
         }
   
   
         RecognizeCelebritiesRequest request = new RecognizeCelebritiesRequest()
            .withImage(new Image()
            .withBytes(imageBytes));
   
         System.out.println("Looking for celebrities in image " + photo + "\n");
   
         RecognizeCelebritiesResult result=rekognitionClient.recognizeCelebrities(request);
   
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

------
#### [ AWS CLI ]

   This AWS CLI command displays the JSON output for the `recognize-celebrities` CLI operation\. 

   Change `bucketname` to the name of an Amazon S3 bucket that contains an image\. Change `input.jpg` to the file name of an image that contains one or more celebrity faces\.

   ```
   aws rekognition recognize-celebrities \
     --image "S3Object={Bucket=bucketname,Name=input.jpg}"
   ```

------
#### [ Python ]

   This example displays information about the celebrities that are detected in an image\. 

   Change the value of `photo` to the path and file name of an image file that contains one or more celebrity faces\.

   ```
   
   import boto3
   import json
   
   if __name__ == "__main__":
       photo='moviestars.jpg'
       
       client=boto3.client('rekognition')
   
       with open(photo, 'rb') as image:
           response = client.recognize_celebrities(Image={'Bytes': image.read()})
   
       print('Detected faces for ' + photo)    
       for celebrity in response['CelebrityFaces']:
           print ('Name: ' + celebrity['Name'])
           print ('Id: ' + celebrity['Id'])
           print ('Position:')
           print ('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
           print ('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
           print ('Info:')
           for url in celebrity['Urls']:
               print ('   ' + url)
           print
   ```

------
#### [ \.NET ]

   This example displays information about the celebrities that are detected in an image\. 

   Change the value of `photo` to the path and file name of an image file that contains one or more celebrity faces \(\.jpg or \.png format\)\.

   ```
   using System;
   using System.IO;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   public class CelebritiesInImage
   {
       public static void Example()
       {
           String photo = "moviestars.jpg";
   
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           RecognizeCelebritiesRequest recognizeCelebritiesRequest = new RecognizeCelebritiesRequest();
   
           Amazon.Rekognition.Model.Image img = new Amazon.Rekognition.Model.Image();
           byte[] data = null;
           try
           {
               using (FileStream fs = new FileStream(photo, FileMode.Open, FileAccess.Read))
               {
                   data = new byte[fs.Length];
                   fs.Read(data, 0, (int)fs.Length);
               }
           }
           catch(Exception)
           {
               Console.WriteLine("Failed to load file " + photo);
               return;
           }
   
           img.Bytes = new MemoryStream(data);
           recognizeCelebritiesRequest.Image = img;
   
           Console.WriteLine("Looking for celebrities in image " + photo + "\n");
   
           RecognizeCelebritiesResponse recognizeCelebritiesResponse = rekognitionClient.RecognizeCelebrities(recognizeCelebritiesRequest);
   
           Console.WriteLine(recognizeCelebritiesResponse.CelebrityFaces.Count + " celebrity(s) were recognized.\n");
           foreach (Celebrity celebrity in recognizeCelebritiesResponse.CelebrityFaces)
           {
               Console.WriteLine("Celebrity recognized: " + celebrity.Name);
               Console.WriteLine("Celebrity ID: " + celebrity.Id);
               BoundingBox boundingBox = celebrity.Face.BoundingBox;
               Console.WriteLine("position: " +
                  boundingBox.Left + " " + boundingBox.Top);
               Console.WriteLine("Further information (if available):");
               foreach (String url in celebrity.Urls)
                   Console.WriteLine(url);
           }
           Console.WriteLine(recognizeCelebritiesResponse.UnrecognizedFaces.Count + " face(s) were unrecognized.");
       }
   }
   ```

------

1. Record the value of one of the celebrity IDs that are displayed\. You'll need it in [Getting Information About a Celebrity](get-celebrity-info-procedure.md)\.

## RecognizeCelebrities Operation Request<a name="recognizecelebrities-request"></a>

The input to `RecognizeCelebrities` is an image\. In this example, the image is passed as image bytes\. For more information, see [Working with Images](images.md)\.

```
{
    "Image": {
        "Bytes": "/AoSiyvFpm....."
    }
}
```

## RecognizeCelebrities Operation Response<a name="recognizecelebrities-response"></a>

The following is example JSON input and output for `RecognizeCelebrities`\. 

`RecognizeCelebrities` returns an array of recognized celebrities and an array of unrecognized faces\. In the example, note the following:
+ **Recognized celebrities** – `Celebrities` is an array of recognized celebrities\. Each [Celebrity](API_Celebrity.md) object in the array contains the celebrity name and a list of URLs pointing to related content—for example, the celebrity's IMDB link\. Amazon Rekognition returns an [ComparedFace](API_ComparedFace.md) object that your application can use to determine where the celebrity's face is on the image and a unique identifier for the celebrity\. Use the unique identifier to retrieve celebrity information later with the [GetCelebrityInfo](API_GetCelebrityInfo.md) API operation\. 
+ **Unrecognized faces** – `UnrecognizedFaces` is an array of faces that didn't match any known celebrities\. Each [ComparedFace](API_ComparedFace.md) object in the array contains a bounding box \(as well as other information\) that you can use to locate the face in the image\.
+ **Image orientation** – `OrientationCorrection` is image orientation information that you can use to correctly display the image\. For more information, see [Getting Image Orientation and Bounding Box Coordinates](images-orientation.md)\.

```
{
    "CelebrityFaces": [{
        "Face": {
            "BoundingBox": {
                "Height": 0.617123007774353,
                "Left": 0.15641026198863983,
                "Top": 0.10864841192960739,
                "Width": 0.3641025722026825
            },
            "Confidence": 99.99589538574219,
            "Landmarks": [{
                "Type": "eyeLeft",
                "X": 0.2837241291999817,
                "Y": 0.3637104034423828
            }, {
                "Type": "eyeRight",
                "X": 0.4091649055480957,
                "Y": 0.37378931045532227
            }, {
                "Type": "nose",
                "X": 0.35267341136932373,
                "Y": 0.49657556414604187
            }, {
                "Type": "mouthLeft",
                "X": 0.2786353826522827,
                "Y": 0.5455248355865479
            }, {
                "Type": "mouthRight",
                "X": 0.39566439390182495,
                "Y": 0.5597742199897766
            }],
            "Pose": {
                "Pitch": -7.749263763427734,
                "Roll": 2.004552125930786,
                "Yaw": 9.012002944946289
            },
            "Quality": {
                "Brightness": 32.69192123413086,
                "Sharpness": 99.9305191040039
            }
        },
        "Id": "3Ir0du6",
        "MatchConfidence": 98.0,
        "Name": "Jeff Bezos",
        "Urls": ["www.imdb.com/name/nm1757263"]
    }],
    "OrientationCorrection": "ROTATE_0",
    "UnrecognizedFaces": [{
        "BoundingBox": {
            "Height": 0.5345501899719238,
            "Left": 0.48461538553237915,
            "Top": 0.16949152946472168,
            "Width": 0.3153846263885498
        },
        "Confidence": 99.92860412597656,
        "Landmarks": [{
            "Type": "eyeLeft",
            "X": 0.5863404870033264,
            "Y": 0.36940744519233704
        }, {
            "Type": "eyeRight",
            "X": 0.6999204754829407,
            "Y": 0.3769848346710205
        }, {
            "Type": "nose",
            "X": 0.6349524259567261,
            "Y": 0.4804527163505554
        }, {
            "Type": "mouthLeft",
            "X": 0.5872702598571777,
            "Y": 0.5535582304000854
        }, {
            "Type": "mouthRight",
            "X": 0.6952020525932312,
            "Y": 0.5600858926773071
        }],
        "Pose": {
            "Pitch": -7.386096477508545,
            "Roll": 2.304218292236328,
            "Yaw": -6.175624370574951
        },
        "Quality": {
            "Brightness": 37.16635513305664,
            "Sharpness": 99.884521484375
        }
    }]
}
```