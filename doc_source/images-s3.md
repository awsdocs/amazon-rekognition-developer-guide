# Analyzing Images Stored in an Amazon S3 Bucket<a name="images-s3"></a>

Amazon Rekognition Image can analyze images that are stored in an Amazon S3 bucket or images that are supplied as image bytes\.

In this topic, you use the [DetectLabels](API_DetectLabels.md) API operation to detect objects, concepts, and scenes in an image \(JPEG or PNG\) that's stored in an Amazon S3 bucket\. You pass an image to an Amazon Rekognition Image API operation by using the [Image](API_Image.md) input parameter\. Within `Image`, you specify the [S3Object](API_S3Object.md) object property to reference an image stored in an S3 bucket\. Image bytes for images stored in Amazon S3 buckets don't need to be base64 encoded\. For more information, see [Images](images-information.md)\. 

The region for the S3 bucket containing the S3 object must match the region you use for Amazon Rekognition Image operations\. 

In this example JSON request for `DetectLabels`, the source image \(`input.jpg`\) is loaded from an Amazon S3 bucket named `MyBucket`\.

```
{
    "Image": {
        "S3Object": {
            "Bucket": "MyBucket",
            "Name": "input.jpg"
        }
    },
    "MaxLabels": 10,
    "MinConfidence": 75
}
```

The following examples use various AWS SDKs and the AWS CLI to call `DetectLabels`\. For information about the `DetectLabels` operation response, see [DetectLabels Response](labels-detect-labels-image.md#detectlabels-response)\.

**To detect labels in an image**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` and `AmazonS3ReadOnlyAccess` permissions\. For more information, see [Step 1: Set Up an AWS Account and Create an IAM User](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Upload an image that contains one or more objects—such as trees, houses, and boat—to your S3 bucket\. The image must be in *\.jpg* or *\.png* format\.

   For instructions, see [Uploading Objects into Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. Use the following examples to call the `DetectLabels` operation\.

------
#### [ Java ]

   This example displays a list of labels that were detected in the input image\. Replace the values of `bucket` and `photo` with the names of the Amazon S3 bucket and image that you used in step 2\. 

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   package com.amazonaws.samples;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.AmazonRekognitionException;
   import com.amazonaws.services.rekognition.model.DetectLabelsRequest;
   import com.amazonaws.services.rekognition.model.DetectLabelsResult;
   import com.amazonaws.services.rekognition.model.Image;
   import com.amazonaws.services.rekognition.model.Label;
   import com.amazonaws.services.rekognition.model.S3Object;
   import java.util.List;
   
   public class DetectLabels {
   
      public static void main(String[] args) throws Exception {
   
         String photo = "input.jpg";
         String bucket = "bucket";
   
   
         AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
   
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

------
#### [ AWS CLI ]

   This example displays the JSON output from the `detect-labels` CLI operation\. Replace the values of `bucket` and `photo` with the names of the Amazon S3 bucket and image that you used in Step 2\. 

   ```
   aws rekognition detect-labels \
   --image '{"S3Object":{"Bucket":"bucket","Name":"file"}}'
   ```

------
#### [ Python ]

   This example displays the labels that were detected in the input image\. Replace the values of `bucket` and `photo` with the names of the Amazon S3 bucket and image that you used in Step 2\. 

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   
   def detect_labels(photo, bucket):
   
       client=boto3.client('rekognition')
   
       response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
           MaxLabels=10)
   
       print('Detected labels for ' + photo) 
       print()   
       for label in response['Labels']:
           print ("Label: " + label['Name'])
           print ("Confidence: " + str(label['Confidence']))
           print ("Instances:")
           for instance in label['Instances']:
               print ("  Bounding box")
               print ("    Top: " + str(instance['BoundingBox']['Top']))
               print ("    Left: " + str(instance['BoundingBox']['Left']))
               print ("    Width: " +  str(instance['BoundingBox']['Width']))
               print ("    Height: " +  str(instance['BoundingBox']['Height']))
               print ("  Confidence: " + str(instance['Confidence']))
               print()
   
           print ("Parents:")
           for parent in label['Parents']:
               print ("   " + parent['Name'])
           print ("----------")
           print ()
       return len(response['Labels'])
   
   
   def main():
       photo=''
       bucket=''
       label_count=detect_labels(photo, bucket)
       print("Labels detected: " + str(label_count))
   
   
   if __name__ == "__main__":
       main()
   ```

------
#### [ \.NET ]

   This example displays a list of labels that were detected in the input image\. Replace the values of `bucket` and `photo` with the names of the Amazon S3 bucket and image that you used in Step 2\. 

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   using System;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   public class DetectLabels
   {
       public static void Example()
       {
           String photo = "input.jpg";
           String bucket = "bucket";
   
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           DetectLabelsRequest detectlabelsRequest = new DetectLabelsRequest()
           {
               Image = new Image()
               {
                   S3Object = new S3Object()
                   {
                       Name = photo,
                       Bucket = bucket
                   },
               },
               MaxLabels = 10,
               MinConfidence = 75F
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
#### [ Ruby ]

   This example displays a list of labels that were detected in the input image\. Replace the values of `bucket` and `photo` with the names of the Amazon S3 bucket and image that you used in Step 2\. 

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
      # Add to your Gemfile
      # gem 'aws-sdk-rekognition'
      require 'aws-sdk-rekognition'
      credentials = Aws::Credentials.new(
         ENV['AWS_ACCESS_KEY_ID'],
         ENV['AWS_SECRET_ACCESS_KEY']
      )
      bucket = 'bucket' # the bucketname without s3://
      photo  = 'photo'# the name of file
      client   = Aws::Rekognition::Client.new credentials: credentials
      attrs = {
        image: {
          s3_object: {
            bucket: bucket,
            name: photo
          },
        },
        attributes: ['ALL']
      }
      response = client.detect_faces attrs
      puts "Detected faces for: #{photo}"
      response.face_details.each do |face_detail|
        low  = face_detail.age_range.low
        high = face_detail.age_range.high
        puts "The detected face is between: #{low} and #{high} years old"
        puts "All other attributes:"
        puts "  bounding_box.width:     #{face_detail.bounding_box.width}"
        puts "  bounding_box.height:    #{face_detail.bounding_box.height}"
        puts "  bounding_box.left:      #{face_detail.bounding_box.left}"
        puts "  bounding_box.top:       #{face_detail.bounding_box.top}"
        puts "  age.range.low:          #{face_detail.age_range.low}"
        puts "  age.range.high:         #{face_detail.age_range.high}"
        puts "  smile.value:            #{face_detail.smile.value}"
        puts "  smile.confidence:       #{face_detail.smile.confidence}"
        puts "  eyeglasses.value:       #{face_detail.eyeglasses.value}"
        puts "  eyeglasses.confidence:  #{face_detail.eyeglasses.confidence}"
        puts "  sunglasses.value:       #{face_detail.sunglasses.value}"
        puts "  sunglasses.confidence:  #{face_detail.sunglasses.confidence}"
        puts "  gender.value:           #{face_detail.gender.value}"
        puts "  gender.confidence:      #{face_detail.gender.confidence}"
        puts "  beard.value:            #{face_detail.beard.value}"
        puts "  beard.confidence:       #{face_detail.beard.confidence}"
        puts "  mustache.value:         #{face_detail.mustache.value}"
        puts "  mustache.confidence:    #{face_detail.mustache.confidence}"
        puts "  eyes_open.value:        #{face_detail.eyes_open.value}"
        puts "  eyes_open.confidence:   #{face_detail.eyes_open.confidence}"
        puts "  mout_open.value:        #{face_detail.mouth_open.value}"
        puts "  mout_open.confidence:   #{face_detail.mouth_open.confidence}"
        puts "  emotions[0].type:       #{face_detail.emotions[0].type}"
        puts "  emotions[0].confidence: #{face_detail.emotions[0].confidence}"
        puts "  landmarks[0].type:      #{face_detail.landmarks[0].type}"
        puts "  landmarks[0].x:         #{face_detail.landmarks[0].x}"
        puts "  landmarks[0].y:         #{face_detail.landmarks[0].y}"
        puts "  pose.roll:              #{face_detail.pose.roll}"
        puts "  pose.yaw:               #{face_detail.pose.yaw}"
        puts "  pose.pitch:             #{face_detail.pose.pitch}"
        puts "  quality.brightness:     #{face_detail.quality.brightness}"
        puts "  quality.sharpness:      #{face_detail.quality.sharpness}"
        puts "  confidence:             #{face_detail.confidence}"
        puts "------------"
        puts ""
      end
   ```

------