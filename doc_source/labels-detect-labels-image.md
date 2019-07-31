# Detecting Labels in an Image<a name="labels-detect-labels-image"></a>

You can use the [DetectLabels](API_DetectLabels.md) operation to detect labels in an image\. For an example, see [Analyzing Images Stored in an Amazon S3 Bucket](images-s3.md)\.

The following examples use various AWS SDKs and the AWS CLI to call `DetectLabels`\. For information about the `DetectLabels` operation response, see [DetectLabels Response](#detectlabels-response)\.

**To detect labels in an image**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` and `AmazonS3ReadOnlyAccess` permissions\. For more information, see [Step 1: Set Up an AWS Account and Create an IAM User](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Upload an image that contains one or more objects—such as trees, houses, and boat—to your S3 bucket\. The image must be in *\.jpg* or *\.png* format\.

   For instructions, see [Uploading Objects into Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. Use the following examples to call the `DetectLabels` operation\.

------
#### [ Ruby ]
   ```
    # Add to your Gemfile
    # gem 'aws-sdk-rekognition'

    require 'aws-sdk-rekognition'

    credentials = Aws::Credentials.new(
       ENV['AWS_ACCESS_KEY_ID'],
       ENV['AWS_SECRET_ACCESS_KEY']
    )

    bucket = 'mybucket' # the bucketname without s3://
    photo  = 'photo.png'# the name of file

    client   = Aws::Rekognition::Client.new credentials: credentials

    attrs = {
      image: {
        s3_object: {
          bucket: bucket,
          name: photo
        },
      },
      max_labels: 10
    }
    response = client.detect_labels attrs

    puts "Detected labels for: #{photo}"

    response.labels.each do |label|
      puts "Label:      #{label.name}"
      puts "Confidence: #{label.confidence}"
      puts "Instances:"
      label['instances'].each do |instance|
        box = instance['bounding_box']
        puts "  Bounding box:"
        puts "    Top:        #{box.top}"
        puts "    Left:       #{box.left}"
        puts "    Width:      #{box.width}"
        puts "    Height:     #{box.height}"
        puts "  Confidence: #{instance.confidence}"
      end
      puts "Parents:"
      label.parents.each do |parent|
        puts "  #{parent.name}"
      end
      puts "------------"
      puts ""
    end

   ```
------
#### [ Java ]

   This example displays a list of labels that were detected in the input image\. Replace the values of `bucket` and `photo` with the names of the Amazon S3 bucket and image that you used in step 2\. 

   ```
   package com.amazonaws.samples;
   import java.util.List;
   
   import com.amazonaws.services.rekognition.model.BoundingBox;
   import com.amazonaws.services.rekognition.model.DetectLabelsRequest;
   import com.amazonaws.services.rekognition.model.DetectLabelsResult;
   import com.amazonaws.services.rekognition.model.Image;
   import com.amazonaws.services.rekognition.model.Instance;
   import com.amazonaws.services.rekognition.model.Label;
   import com.amazonaws.services.rekognition.model.Parent;
   import com.amazonaws.services.rekognition.model.S3Object;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.AmazonRekognitionException;
   
   public class DetectLabels {
   
       public static void main(String[] args) throws Exception {
   
           String photo = "photo";
           String bucket = "bucket";
   
           AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
   
           DetectLabelsRequest request = new DetectLabelsRequest()
                   .withImage(new Image().withS3Object(new S3Object().withName(photo).withBucket(bucket)))
                   .withMaxLabels(10).withMinConfidence(75F);
   
           try {
               DetectLabelsResult result = rekognitionClient.detectLabels(request);
               List<Label> labels = result.getLabels();
   
               System.out.println("Detected labels for " + photo + "\n");
               for (Label label : labels) {
                   System.out.println("Label: " + label.getName());
                   System.out.println("Confidence: " + label.getConfidence().toString() + "\n");
   
                   List<Instance> instances = label.getInstances();
                   System.out.println("Instances of " + label.getName());
                   if (instances.isEmpty()) {
                       System.out.println("  " + "None");
                   } else {
                       for (Instance instance : instances) {
                           System.out.println("  Confidence: " + instance.getConfidence().toString());
                           System.out.println("  Bounding box: " + instance.getBoundingBox().toString());
                       }
                   }
                   System.out.println("Parent labels for " + label.getName() + ":");
                   List<Parent> parents = label.getParents();
                   if (parents.isEmpty()) {
                       System.out.println("  None");
                   } else {
                       for (Parent parent : parents) {
                           System.out.println("  " + parent.getName());
                       }
                   }
                   System.out.println("--------------------");
                   System.out.println();
                  
               }
           } catch (AmazonRekognitionException e) {
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
   
   if __name__ == "__main__":
   
       bucket='bucket'
       photo='photo.jpg'
   
   
       
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
#### [ NodeJS ]
   ```
    // Add to your package.json
    // npm install aws-sdk --save-dev

    const AWS = require('aws-sdk')

    const bucket = 'mybucket' // the bucketname without s3://
    const photo  = 'photo.png' // the name of file

    const config = new AWS.Config({
      accessKeyId: process.env.AWS_ACCESS_KEY_ID,
      secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
      region: process.env.AWS_REGION
    })

    const client = new AWS.Rekognition();
    const params = {
      Image: {
        S3Object: {
          Bucket: bucket,
          Name: photo
        },
      },
      MaxLabels: 10
    }
    client.detectLabels(params, function(err, response) {
      if (err) {
        console.log(err, err.stack); // an error occurred
      } else {
        console.log(`Detected labels for: ${photo}`)

        response.Labels.forEach(label => {
          console.log(`Label:      ${label.Name}`)
          console.log(`Confidence: ${label.Confidence}`)
          console.log("Instances:")
          label.Instances.forEach(instance => {
            let box = instance.BoundingBox
            console.log("  Bounding box:")
            console.log(`    Top:        ${box.Top}`)
            console.log(`    Left:       ${box.Left}`)
            console.log(`    Width:      ${box.Width}`)
            console.log(`    Height:     ${box.Height}`)
            console.log(`  Confidence: ${instance.Confidence}`)
          })
          console.log("Parents:")
          label.Parents.forEach(parent => {
            console.log(`  ${parent.Name}`)
          })
          console.log("------------")
          console.log("")
        }) // for response.labels
      } // if
    });

   ```
------

## DetectLabels Operation Request<a name="detectlabels-request"></a>

The input to `DetectLabel` is an image\. In this example JSON input, the source image is loaded from an Amazon S3 Bucket\. `MaxLabels` is the maximum number of labels to return in the response\. `MinConfidence` is the minimum confidence that Amazon Rekognition Image must have in the accuracy of the detected label for it to be returned in the response\.

```
{
    "Image": {
        "S3Object": {
            "Bucket": "bucket",
            "Name": "input.jpg"
        }
    },
    "MaxLabels": 10,
    "MinConfidence": 75
}
```

## DetectLabels Response<a name="detectlabels-response"></a>

The reponse from `DetectLabels` is an array of labels detected in the image and the level of confidence by which they were detected\. 

The following is an example response from `DetectLabels`\.

The response shows that the operation detected multiple labels including Person, Pedestrian, Vehicle, and Car\. Each label has an associated level of confidence\. For example, the detection algorithm is 99\.99962% confident that the image contains a person\.

The response also includes the ancestor labels for a label in the `Parents` array\. For example, the label Pedestrian has a parent label named Person\. 

The response for common object labels includes bounding box information for the location of the label on the input image\. For example, the Person label has an instances array containing two bounding boxes\. These are the locations of two people detected in the image\.

The field `LabelModelVersion` contains the version number of the detection model used by`DetectLabels`\. 

```
{
            
    LabelModelVersion": 2.0,
    Labels: [
        {
            Name: Person,
            Confidence: 99.99962,
            Instances: [
                {
                    BoundingBox: {
                        Width: 0.19360729,
                        Height: 0.27422005,
                        Left: 0.43734854,
                        Top: 0.35072067
                    },
                    Confidence: 99.99962
                },
                {
                    BoundingBox: {
                        Width: 0.038017172,
                        Height: 0.06597328,
                        Left: 0.9155802,
                        Top: 0.5010884
                    },
                    Confidence: 91.415535
                }
            ],
            Parents: [
                
            ]
        },
        {
            Name: Pedestrian,
            Confidence: 99.48226,
            Instances: [
                
            ],
            Parents: [
                {
                    Name: Person
                }
            ]
        },
        {
            Name: Tarmac,
            Confidence: 99.385605,
            Instances: [
                
            ],
            Parents: [
                
            ]
        },
        {
            Name: Path,
            Confidence: 98.70715,
            Instances: [
                
            ],
            Parents: [
                
            ]
        },
        {
            Name: Road,
            Confidence: 98.11571,
            Instances: [
                
            ],
            Parents: [
                
            ]
        },
        {
            Name: Urban,
            Confidence: 96.2798,
            Instances: [
                
            ],
            Parents: [
                
            ]
        },
        {
            Name: City,
            Confidence: 96.2798,
            Instances: [
                
            ],
            Parents: [
                {
                    Name: Urban
                }
            ]
        },
        {
            Name: Vehicle,
            Confidence: 94.803375,
            Instances: [
                
            ],
            Parents: [
                
            ]
        },
        {
            Name: Car,
            Confidence: 94.803375,
            Instances: [
                {
                    BoundingBox: {
                        Width: 0.101054385,
                        Height: 0.122262456,
                        Left: 0.5743986,
                        Top: 0.53436863
                    },
                    Confidence: 58.146957
                },
                {
                    BoundingBox: {
                        Width: 0.110863954,
                        Height: 0.10271988,
                        Left: 0.10355594,
                        Top: 0.5354845
                    },
                    Confidence: 70.77716
                },
                {
                    BoundingBox: {
                        Width: 0.056389667,
                        Height: 0.171637,
                        Left: 0.942777,
                        Top: 0.52358043
                    },
                    Confidence: 57.8401
                },
                {
                    BoundingBox: {
                        Width: 0.046953984,
                        Height: 0.18796417,
                        Left: 0.0031801604,
                        Top: 0.50652236
                    },
                    Confidence: 48.009228
                },
                {
                    BoundingBox: {
                        Width: 0.060038604,
                        Height: 0.06737709,
                        Left: 0.22409998,
                        Top: 0.54413414
                    },
                    Confidence: 56.240288
                },
                {
                    BoundingBox: {
                        Width: 0.040678814,
                        Height: 0.03428703,
                        Left: 0.31641594,
                        Top: 0.5566274
                    },
                    Confidence: 53.59637
                },
                {
                    BoundingBox: {
                        Width: 0.02848697,
                        Height: 0.19150497,
                        Left: 0.0,
                        Top: 0.5107087
                    },
                    Confidence: 54.186676
                },
                {
                    BoundingBox: {
                        Width: 0.06254628,
                        Height: 0.053911515,
                        Left: 0.4608306,
                        Top: 0.5573825
                    },
                    Confidence: 58.661976
                },
                {
                    BoundingBox: {
                        Width: 0.04341105,
                        Height: 0.08935959,
                        Left: 0.18293385,
                        Top: 0.539492
                    },
                    Confidence: 52.312466
                },
                {
                    BoundingBox: {
                        Width: 0.031183116,
                        Height: 0.0398999,
                        Left: 0.2853088,
                        Top: 0.55793667
                    },
                    Confidence: 51.869164
                },
                {
                    BoundingBox: {
                        Width: 0.03111379,
                        Height: 0.056484755,
                        Left: 0.2580395,
                        Top: 0.550482
                    },
                    Confidence: 45.591652
                },
                {
                    BoundingBox: {
                        Width: 0.10616336,
                        Height: 0.1852818,
                        Left: 0.0037978808,
                        Top: 0.5039217
                    },
                    Confidence: 94.34959
                },
                {
                    BoundingBox: {
                        Width: 0.14233612,
                        Height: 0.15528248,
                        Left: 0.6494813,
                        Top: 0.5333096
                    },
                    Confidence: 88.45155
                },
                {
                    BoundingBox: {
                        Width: 0.08586375,
                        Height: 0.0855043,
                        Left: 0.5128013,
                        Top: 0.5438793
                    },
                    Confidence: 45.12628
                },
                {
                    BoundingBox: {
                        Width: 0.24299885,
                        Height: 0.21577217,
                        Left: 0.7309805,
                        Top: 0.52518845
                    },
                    Confidence: 94.146774
                }
            ],
            Parents: [
                {
                    Name: Vehicle
                }
            ]
        },
        {
            Name: Downtown,
            Confidence: 91.13891,
            Instances: [
                
            ],
            Parents: [
                {
                    Name: Urban
                },
                {
                    Name: City
                }
            ]
        }
    ],
    
}
```
