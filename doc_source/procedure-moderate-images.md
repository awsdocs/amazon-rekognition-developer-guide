# Detecting inappropriate images<a name="procedure-moderate-images"></a>

You can use the [ DetectModerationLabels ](API_DetectModerationLabels.md) operation to determine if an image contains inappropriate or offensive content\. For a list of moderation labels in Amazon Rekognition, see [Using the image and video moderation APIs](https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html#moderation-api)\.



## Detecting inappropriate content in an image<a name="moderate-images-sdk"></a>

The image must be in either a \.jpg or a \.png format\. You can provide the input image as an image byte array \(base64\-encoded image bytes\), or specify an Amazon S3 object\. In these procedures, you upload an image \(\.jpg or \.png\) to your S3 bucket\.

To run these procedures, you need to have the AWS CLI or the appropriate AWS SDK installed\. For more information, see [Getting started with Amazon Rekognition](getting-started.md)\. The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Actions Defined by Amazon Rekognition](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonrekognition.html#amazonrekognition-actions-as-permissions)\. 

## <a name="to-detect-moderation-labels-in-an-image"></a>

**To detect moderation labels in an image \(SDK\)**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` and `AmazonS3ReadOnlyAccess` permissions\. For more information, see [Step 1: Set up an AWS account and create an IAM user](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Upload an image to your S3 bucket\. 

   For instructions, see [Uploading Objects into Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. Use the following examples to call the `DetectModerationLabels` operation\.

------
#### [ Java ]

   This example outputs detected inappropriate content label names, confidence levels, and the parent label for detected moderation labels\.

   Replace the values of `bucket` and `photo` with the S3 bucket name and the image file name that you used in step 2\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   package aws.example.rekognition.image;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.AmazonRekognitionException;
   import com.amazonaws.services.rekognition.model.DetectModerationLabelsRequest;
   import com.amazonaws.services.rekognition.model.DetectModerationLabelsResult;
   import com.amazonaws.services.rekognition.model.Image;
   import com.amazonaws.services.rekognition.model.ModerationLabel;
   import com.amazonaws.services.rekognition.model.S3Object;
   
   import java.util.List;
   
   public class DetectModerationLabels
   {
      public static void main(String[] args) throws Exception
      {
         String photo = "input.jpg";
         String bucket = "bucket";
         
         AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
         
         DetectModerationLabelsRequest request = new DetectModerationLabelsRequest()
           .withImage(new Image().withS3Object(new S3Object().withName(photo).withBucket(bucket)))
           .withMinConfidence(60F);
         try
         {
              DetectModerationLabelsResult result = rekognitionClient.detectModerationLabels(request);
              List<ModerationLabel> labels = result.getModerationLabels();
              System.out.println("Detected labels for " + photo);
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

------
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/DetectModerationLabels.java)\.

   ```
       public static void detectModLabels(RekognitionClient rekClient, String sourceImage) {
   
       try {
           InputStream sourceStream = new FileInputStream(sourceImage);
           SdkBytes sourceBytes = SdkBytes.fromInputStream(sourceStream);
   
           Image souImage = Image.builder()
                   .bytes(sourceBytes)
                   .build();
   
           DetectModerationLabelsRequest moderationLabelsRequest = DetectModerationLabelsRequest.builder()
                   .image(souImage)
                   .minConfidence(60F)
                   .build();
   
           DetectModerationLabelsResponse moderationLabelsResponse = rekClient.detectModerationLabels(moderationLabelsRequest);
   
           // Display the results
           List<ModerationLabel> labels = moderationLabelsResponse.moderationLabels();
           System.out.println("Detected labels for image");
   
           for (ModerationLabel label : labels) {
               System.out.println("Label: " + label.name()
                       + "\n Confidence: " + label.confidence().toString() + "%"
                       + "\n Parent:" + label.parentName());
           }
   
       } catch (RekognitionException | FileNotFoundException e) {
           e.printStackTrace();
           System.exit(1);
       }
    }
   ```

------
#### [ AWS CLI ]

   This AWS CLI command displays the JSON output for the `detect-moderation-labels` CLI operation\. 

   Replace `bucket` and `input.jpg` with the S3 bucket name and the image file name that you used in step 2\.

   ```
   aws rekognition detect-moderation-labels \
   --image '{"S3Object":{"Bucket":"bucket","Name":"input.jpg"}}'
   ```

------
#### [ Python ]

   This example outputs detected inappropriate or offensive content label names, confidence levels, and the parent label for detected inappropriate content labels\.

   In the function `main`, replace the values of `bucket` and `photo` with the S3 bucket name and the image file name that you used in step 2\.

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   
   def moderate_image(photo, bucket):
   
       client=boto3.client('rekognition')
   
       response = client.detect_moderation_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
   
       print('Detected labels for ' + photo)    
       for label in response['ModerationLabels']:
           print (label['Name'] + ' : ' + str(label['Confidence']))
           print (label['ParentName'])
       return len(response['ModerationLabels'])
   
   
   
   def main():
       photo='photo'
       bucket='bucket'
       label_count=moderate_image(photo, bucket)
       print("Labels detected: " + str(label_count))
   
   
   if __name__ == "__main__":
       main()
   ```

------
#### [ \.NET ]

   This example outputs detected inappropriate or offensive content label names, confidence levels, and the parent label for detected moderation labels\.

   Replace the values of `bucket` and `photo` with the S3 bucket name and the image file name that you used in step 2\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   using System;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   public class DetectModerationLabels
   {
       public static void Example()
       {
           String photo = "input.jpg";
           String bucket = "bucket";
   
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           DetectModerationLabelsRequest detectModerationLabelsRequest = new DetectModerationLabelsRequest()
           {
               Image = new Image()
               {
                   S3Object = new S3Object()
                   {
                       Name = photo,
                       Bucket = bucket
                   },
               },
               MinConfidence = 60F
           };
   
           try
           {
               DetectModerationLabelsResponse detectModerationLabelsResponse = rekognitionClient.DetectModerationLabels(detectModerationLabelsRequest);
               Console.WriteLine("Detected labels for " + photo);
               foreach (ModerationLabel label in detectModerationLabelsResponse.ModerationLabels)
                   Console.WriteLine("Label: {0}\n Confidence: {1}\n Parent: {2}", 
                       label.Name, label.Confidence, label.ParentName);
           }
           catch (Exception e)
           {
               Console.WriteLine(e.Message);
           }
       }
   }
   ```

------

## DetectModerationLabels operation request<a name="detectmoderation-labels-operation-request"></a>

The input to `DetectModerationLabels` is an image\. In this example JSON input, the source image is loaded from an Amazon S3 bucket\. `MinConfidence` is the minimum confidence that Amazon Rekognition Image must have in the accuracy of the detected label for it to be returned in the response\.

```
{
    "Image": {
        "S3Object": {
            "Bucket": "bucket",
            "Name": "input.jpg"
        }
    },
    "MinConfidence": 60
}
```

## DetectModerationLabels operation response<a name="detectmoderationlabels-operation-response"></a>

 `DetectModerationLabels` can retrieve input images from an S3 bucket, or you can provide them as image bytes\. The following example is the response from a call to `DetectModerationLabels`\.

In the following example JSON response, note the following:
+ **Inappropriate Image Detection information** – The example shows a list of labels for inappropriate or offensive content found in the image\. The list includes the top\-level label and each second\-level label that are detected in the image\.

  **Label** – Each label has a name, an estimation of the confidence that Amazon Rekognition has that the label is accurate, and the name of its parent label\. The parent name for a top\-level label is `""`\.

  **Label confidence** – Each label has a confidence value between 0 and 100 that indicates the percentage confidence that Amazon Rekognition has that the label is correct\. You specify the required confidence level for a label to be returned in the response in the API operation request\.

```
{
"ModerationLabels": [
    {
        "Confidence": 99.24723052978516,
        "ParentName": "",
        "Name": "Explicit Nudity"
    },
    {
        "Confidence": 99.24723052978516,
        "ParentName": "Explicit Nudity",
        "Name": "Graphic Male Nudity"
    },
    {
        "Confidence": 88.25341796875,
        "ParentName": "Explicit Nudity",
        "Name": "Sexual Activity"
    }
]
}
```