# Detecting Faces in an Image<a name="faces-detect-images"></a>

Amazon Rekognition Image provides the [DetectFaces](API_DetectFaces.md) operation that looks for key facial features such as eyes, nose, and mouth to detect faces in an input image\. Amazon Rekognition Image detects the 100 largest faces in an image\.

You can provide the input image as an image byte array \(base64\-encoded image bytes\), or specify an Amazon S3 object\. In this procedure, you upload an image \(JPEG or PNG\) to your S3 bucket and specify the object key name\.

**To detect faces in an image**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` and `AmazonS3ReadOnlyAccess` permissions\. For more information, see [Step 1: Set Up an AWS Account and Create an IAM User](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Upload an image \(that contains one or more faces\) to your S3 bucket\. 

   For instructions, see [Uploading Objects into Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. Use the following examples to call `DetectFaces`\.

------
#### [ Java ]

   This example displays the estimated age range for detected faces, and lists the JSON for all detected facial attributes\. Change the value of `photo` to the image file name\. Change the value of `bucket` to the Amazon S3 bucket where the image is stored\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   package aws.example.rekognition.image;
   
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.AmazonRekognitionException;
   import com.amazonaws.services.rekognition.model.Image;
   import com.amazonaws.services.rekognition.model.S3Object;
   import com.amazonaws.services.rekognition.model.AgeRange;
   import com.amazonaws.services.rekognition.model.Attribute;
   import com.amazonaws.services.rekognition.model.DetectFacesRequest;
   import com.amazonaws.services.rekognition.model.DetectFacesResult;
   import com.amazonaws.services.rekognition.model.FaceDetail;
   import com.fasterxml.jackson.databind.ObjectMapper;
   import java.util.List;
   
   
   public class DetectFaces {
      
      
      public static void main(String[] args) throws Exception {
   
         String photo = "input.jpg";
         String bucket = "bucket";
   
         AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
   
   
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

------
#### [ AWS CLI ]

   This example displays the JSON output from the `detect-faces` AWS CLI operation\. Replace `file` with the name of an image file\. Replace `bucket` with the name of the Amazon S3 bucket that contains the image file\.

   ```
   aws rekognition detect-faces \
   --image '{"S3Object":{"Bucket":"bucket","Name":"file"}}' \
   --attributes "ALL"
   ```

------
#### [ Python ]

   This example displays the estimated age range for detected faces, and lists the JSON for all detected facial attributes\. Change the value of `photo` to the image file name\. Change the value of `bucket` to the Amazon S3 bucket where the image is stored\.

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   import json
   
   if __name__ == "__main__":
       photo='input.jpg'
       bucket='bucket'
       client=boto3.client('rekognition')
   
       response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo}},Attributes=['ALL'])
   
       print('Detected faces for ' + photo)    
       for faceDetail in response['FaceDetails']:
           print('The detected face is between ' + str(faceDetail['AgeRange']['Low']) 
                 + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
           print('Here are the other attributes:')
           print(json.dumps(faceDetail, indent=4, sort_keys=True))
   ```

------
#### [ \.NET ]

   This example displays the estimated age range for detected faces, and lists the JSON for all detected facial attributes\. Change the value of `photo` to the image file name\. Change the value of `bucket` to the Amazon S3 bucket where the image is stored\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   using System;
   using System.Collections.Generic;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   public class DetectFaces
   {
       public static void Example()
       {
           String photo = "input.jpg";
           String bucket = "bucket";
   
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           DetectFacesRequest detectFacesRequest = new DetectFacesRequest()
           {
               Image = new Image()
               {
                   S3Object = new S3Object()
                   {
                       Name = photo,
                       Bucket = bucket
                   },
               },
               // Attributes can be "ALL" or "DEFAULT". 
               // "DEFAULT": BoundingBox, Confidence, Landmarks, Pose, and Quality.
               // "ALL": See https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Rekognition/TFaceDetail.html
               Attributes = new List<String>() { "ALL" }
           };
   
           try
           {
               DetectFacesResponse detectFacesResponse = rekognitionClient.DetectFaces(detectFacesRequest);
               bool hasAll = detectFacesRequest.Attributes.Contains("ALL");
               foreach(FaceDetail face in detectFacesResponse.FaceDetails)
               {
                   Console.WriteLine("BoundingBox: top={0} left={1} width={2} height={3}", face.BoundingBox.Left,
                       face.BoundingBox.Top, face.BoundingBox.Width, face.BoundingBox.Height);
                   Console.WriteLine("Confidence: {0}\nLandmarks: {1}\nPose: pitch={2} roll={3} yaw={4}\nQuality: {5}",
                       face.Confidence, face.Landmarks.Count, face.Pose.Pitch,
                       face.Pose.Roll, face.Pose.Yaw, face.Quality);
                   if (hasAll)
                       Console.WriteLine("The detected face is estimated to be between " +
                           face.AgeRange.Low + " and " + face.AgeRange.High + " years old.");
               }
           }
           catch (Exception e)
           {
               Console.WriteLine(e.Message);
           }
       }
   }
   ```

------

## DetectFaces Operation Request<a name="detectfaces-request"></a>

The input to `DetectFaces` is an image\. In this example, the image is loaded from an Amazon S3 bucket\. The `Attributes` parameter specifies that all facial attributes should be returned\. For more information, see [Working with Images](images.md)\.

```
{
    "Image": {
        "S3Object": {
            "Bucket": "bucket",
            "Name": "input.jpg"
        }
    },
    "Attributes": [
        "ALL"
    ]
}
```

## DetectFaces Operation Response<a name="detectfaces-response"></a>

 `DetectFaces` returns the following information for each detected face:
+ **Bounding box** – The coordinates of the bounding box that surrounds the face\. For more information, see [Getting Image Orientation and Bounding Box Coordinates](images-orientation.md)\.
+ **Confidence** – The level of confidence that the bounding box contains a face\. 
+ **Facial landmarks** – An array of facial landmarks\. For each landmark \(such as the left eye, right eye, and mouth\), the response provides the x and y coordinates\.
+ **Facial attributes** – A set of facial attributes, including gender, or whether the face has a beard\. For each such attribute, the response provides a value\. The value can be of different types, such as a Boolean type \(whether a person is wearing sunglasses\) or a string \(whether the person is male or female\)\. In addition, for most attributes, the response also provides a confidence in the detected value for the attribute\. 
+ **Quality** – Describes the brightness and the sharpness of the face\. For information about ensuring the best possible face detection, see [Recommendations for Facial Recognition Input Images](image-best-practices.md#recommendations-for-images)\.
+ **Pose** – Describes the rotation of the face inside the image\.
+ **Emotions** – A set of emotions with confidence in the analysis\.

The following is an example response of a `DetectFaces` API call\. 

```
{
    "FaceDetails": [
        {
            "AgeRange": {
                "High": 36,
                "Low": 19
            },
            "Beard": {
                "Confidence": 99.99388122558594,
                "Value": false
            },
            "BoundingBox": {
                "Height": 0.35353535413742065,
                "Left": 0.10707070678472519,
                "Top": 0.12777778506278992,
                "Width": 0.47138047218322754
            },
            "Confidence": 99.99736785888672,
            "Emotions": [
                {
                    "Confidence": 89.59288024902344,
                    "Type": "HAPPY"
                },
                {
                    "Confidence": 5.3619384765625,
                    "Type": "CALM"
                },
                {
                    "Confidence": 4.1074934005737305,
                    "Type": "ANGRY"
                }
            ],
            "Eyeglasses": {
                "Confidence": 99.96102142333984,
                "Value": false
            },
            "EyesOpen": {
                "Confidence": 99.97982788085938,
                "Value": true
            },
            "Gender": {
                "Confidence": 100,
                "Value": "Female"
            },
            "Landmarks": [
                {
                    "Type": "eyeLeft",
                    "X": 0.23772846162319183,
                    "Y": 0.2778792679309845
                },
                {
                    "Type": "eyeRight",
                    "X": 0.3944779932498932,
                    "Y": 0.2527812421321869
                },
                {
                    "Type": "nose",
                    "X": 0.28617316484451294,
                    "Y": 0.3367626965045929
                },
                {
                    "Type": "mouthLeft",
                    "X": 0.288897842168808,
                    "Y": 0.4019121527671814
                },
                {
                    "Type": "mouthRight",
                    "X": 0.41363197565078735,
                    "Y": 0.38766127824783325
                },
                {
                    "Type": "leftPupil",
                    "X": 0.25244733691215515,
                    "Y": 0.27739065885543823
                },
                {
                    "Type": "rightPupil",
                    "X": 0.4029206931591034,
                    "Y": 0.24940147995948792
                },
                {
                    "Type": "leftEyeBrowLeft",
                    "X": 0.17436790466308594,
                    "Y": 0.24362699687480927
                },
                {
                    "Type": "leftEyeBrowUp",
                    "X": 0.21201953291893005,
                    "Y": 0.2338741421699524
                },
                {
                    "Type": "leftEyeBrowRight",
                    "X": 0.2513192892074585,
                    "Y": 0.24069637060165405
                },
                {
                    "Type": "rightEyeBrowLeft",
                    "X": 0.32193484902381897,
                    "Y": 0.21918891370296478
                },
                {
                    "Type": "rightEyeBrowUp",
                    "X": 0.38548189401626587,
                    "Y": 0.19604144990444183
                },
                {
                    "Type": "rightEyeBrowRight",
                    "X": 0.45430734753608704,
                    "Y": 0.2027731090784073
                },
                {
                    "Type": "leftEyeLeft",
                    "X": 0.20944036543369293,
                    "Y": 0.28281378746032715
                },
                {
                    "Type": "leftEyeRight",
                    "X": 0.2710888683795929,
                    "Y": 0.2738289535045624
                },
                {
                    "Type": "leftEyeUp",
                    "X": 0.2339935451745987,
                    "Y": 0.2687133252620697
                },
                {
                    "Type": "leftEyeDown",
                    "X": 0.23892717063426971,
                    "Y": 0.28660306334495544
                },
                {
                    "Type": "rightEyeLeft",
                    "X": 0.36334219574928284,
                    "Y": 0.2598327100276947
                },
                {
                    "Type": "rightEyeRight",
                    "X": 0.4293186664581299,
                    "Y": 0.249033123254776
                },
                {
                    "Type": "rightEyeUp",
                    "X": 0.39038628339767456,
                    "Y": 0.2431529313325882
                },
                {
                    "Type": "rightEyeDown",
                    "X": 0.3967171609401703,
                    "Y": 0.26075780391693115
                },
                {
                    "Type": "noseLeft",
                    "X": 0.28841185569763184,
                    "Y": 0.3598580062389374
                },
                {
                    "Type": "noseRight",
                    "X": 0.3451237976551056,
                    "Y": 0.3516968786716461
                },
                {
                    "Type": "mouthUp",
                    "X": 0.3349839448928833,
                    "Y": 0.38809144496917725
                },
                {
                    "Type": "mouthDown",
                    "X": 0.3422594964504242,
                    "Y": 0.41868656873703003
                }
            ],
            "MouthOpen": {
                "Confidence": 99.97990417480469,
                "Value": false
            },
            "Mustache": {
                "Confidence": 99.97885131835938,
                "Value": false
            },
            "Pose": {
                "Pitch": 1.0711474418640137,
                "Roll": -10.933034896850586,
                "Yaw": -25.838171005249023
            },
            "Quality": {
                "Brightness": 43.86729431152344,
                "Sharpness": 99.95819854736328
            },
            "Smile": {
                "Confidence": 96.89310455322266,
                "Value": true
            },
            "Sunglasses": {
                "Confidence": 80.4033432006836,
                "Value": false
            }
        }
    ]
}
```

Note the following:
+ The `Pose` data describes the rotation of the face detected\. You can use the combination of the `BoundingBox` and `Pose` data to draw the bounding box around faces that your application displays\.
+ The `Quality` describes the brightness and the sharpness of the face\. You might find this useful to compare faces across images and find the best face\.
+ The `DetectFaces` operation first detects orientation of the input image, before detecting facial features\. The `OrientationCorrection` in the response returns the degrees of rotation detected \(counter\-clockwise direction\)\. Your application can use this value to correct the image orientation when displaying the image\. 
+ The preceding response shows all facial `landmarks` the service can detect, all facial attributes and emotions\. To get all of these in the response, you must specify the `attributes` parameter with value `ALL`\. By default, the `DetectFaces` API returns only the following five facial attributes: `BoundingBox`, `Confidence`, `Pose`, `Quality` and `landmarks`\. The default landmarks returned are: `eyeLeft`, `eyeRight`, `nose`, `mouthLeft`, and `mouthRight`\. 
+ The following illustration shows the relative location of the facial landmarks \(`Landmarks`\) on the face that are returned by the `DetectFaces` API operation\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/landmarks-10.png)

The labels on the image map to the [Landmark](API_Landmark.md) data type as shown in the following table\. For clarity, the left eye and right eye landmark points aren't shown on the image\.


| Label | Landmark | 
| --- | --- | 
|  b\_ll  |  leftEyeBrowLeft  | 
|  b\_lu  |  leftEyeBrowUp  | 
|  b\_lr  |  leftEyeBrowRight  | 
|  e\_ll  |  leftEyeLeft  | 
|  e\_lu  |  leftEyeUp  | 
|  e\_lr  |  leftEyeRight  | 
|  e\_ld  |  leftEyeDown  | 
|  e\_lp  |  leftPupil  | 
|  n\_l  |  noseLeft  | 
|  n  |  nose  | 
|  n\_r  |  noseRight  | 
|  m\_u  |   mouthUp   | 
|  m\_d  |  mouthDown  | 
|  m\_l  |  mouthLeft  | 
|  m\_r  |  mouthRight  | 
|  b\_rl  |  rightEyeBrowLeft  | 
|  b\_ru  |  rightEyeBrowUp  | 
|  b\_rr  |  rightEyeBrowRight  | 
|  e\_rl  |  rightEyeLeft  | 
|  e\_ru  |  rightEyeUp  | 
|  e\_rr  |  rightEyeRight   | 
|  e\_rp  |  rightPupil  | 
|  e\_rd  |  rightEyeDown  | 