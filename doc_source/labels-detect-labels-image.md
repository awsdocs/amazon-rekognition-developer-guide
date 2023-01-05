# Detecting labels in an image<a name="labels-detect-labels-image"></a>

You can use the [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html) operation to detect labels in an image and retrieve information about an image’s properties\. Image properties include attributes like the color of the foreground and background and the image's sharpness, brightness, and contrast\. You can retrive just the labels in an image, just the properties of the image, or both\. For an example, see [Analyzing images stored in an Amazon S3 bucket](images-s3.md)\.

The following examples use various AWS SDKs and the AWS CLI to call `DetectLabels`\. For information about the `DetectLabels` operation response, see [DetectLabels response](#detectlabels-response)\.

**To detect labels in an image**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` and `AmazonS3ReadOnlyAccess` permissions\. For more information, see [Step 1: Set up an AWS account and create an IAM user](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Upload an image that contains one or more objects—such as trees, houses, and boat—to your S3 bucket\. The image must be in *\.jpg* or *\.png* format\.

   For instructions, see [Uploading Objects into Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/upload-objects.html) in the *Amazon Simple Storage Service User Guide*\.

1. Use the following examples to call the `DetectLabels` operation\.

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
   aws rekognition detect-labels --image '{ "S3Object": { "Bucket": "bucket", "Name": "file" } }' \
   --features GENERAL_LABELS IMAGE_PROPERTIES \
   --settings '{"ImageProperties": {"MaxDominantColors":1}, "GeneralLabels":{"LabelInclusionFilters":["Cat"]}}' \
   --region us-east-1
   ```

------
#### [ Python ]

   This example displays the labels that were detected in the input image\. In the function `main`, replace the values of `bucket` and `photo` with the names of the Amazon S3 bucket and image that you used in Step 2\. 

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
   #Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
      # Add to your Gemfile
      # gem 'aws-sdk-rekognition'
      require 'aws-sdk-rekognition'
      credentials = Aws::Credentials.new(
         ENV['AWS_ACCESS_KEY_ID'],
         ENV['AWS_SECRET_ACCESS_KEY']
      )
      bucket = 'bucket' # the bucket name without s3://
      photo  = 'photo' # the name of file
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
#### [ Node\.js ]

   This example displays a list of labels that were detected in the input image\. Replace the values of `bucket` and `photo` with the names of the Amazon S3 bucket and image that you used in Step 2\. 

   If you are using TypeScript definitions, you may need to use `import AWS from 'aws-sdk'` instead of `const AWS = require('aws-sdk')`, in order to run the program with Node\.js\. You can consult the [AWS SDK for Javascript](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/) for more details\. Depending on how you have your configurations set up, you also may need to specify your region with `AWS.config.update({region:region});`\.

   ```
                                   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   
   // Load the SDK
   var AWS = require('aws-sdk');
   
   const bucket = 'bucket' // the bucketname without s3://
   const photo  = 'photo' // the name of file
   
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
       console.log(err, err.stack); // if an error occurred
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
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/DetectLabels.java)\.

   ```
       public static void detectImageLabels(RekognitionClient rekClient, String sourceImage) {
   
           try {
               InputStream sourceStream = new FileInputStream(sourceImage);
               SdkBytes sourceBytes = SdkBytes.fromInputStream(sourceStream);
   
               // Create an Image object for the source image.
               Image souImage = Image.builder()
                   .bytes(sourceBytes)
                   .build();
   
               DetectLabelsRequest detectLabelsRequest = DetectLabelsRequest.builder()
                   .image(souImage)
                   .maxLabels(10)
                   .build();
   
               DetectLabelsResponse labelsResponse = rekClient.detectLabels(detectLabelsRequest);
               List<Label> labels = labelsResponse.labels();
               System.out.println("Detected labels for the given photo");
               for (Label label: labels) {
                   System.out.println(label.name() + ": " + label.confidence().toString());
               }
   
           } catch (RekognitionException | FileNotFoundException e) {
               System.out.println(e.getMessage());
               System.exit(1);
           }
       }
   ```

------

   

## DetectLabels operation request<a name="detectlabels-request"></a>

The input to `DetectLabel` is an image\. In this example JSON input, the source image is loaded from an Amazon S3 Bucket\. `MaxLabels` is the maximum number of labels to return in the response\. `MinConfidence` is the minimum confidence that Amazon Rekognition Video must have in the accuracy of the detected label for it to be returned in the response\.

Features lets you specify one or more features of the image that you want returned, allowing you to select `GENERAL_LABELS` and `IMAGE_PROPERTIES`\. Including `GENERAL_LABELS` will return the labels detected in the input image, while including `IMAGE_PROPERTIES` will allow you to access image color and quality\. 

Settings lets you filter the returned items for both the `GENERAL_LABELS` and `IMAGE_PROPERTIES` features\. For labels you can use inclusive and exclusive filters\. You can also filter by label specific, individual labels or by label category: 
+ LabelInclusionFilters \- Allows you to specify which labels you want included in the response\.
+ LabelExclusionFilters \- Allows you to specify which labels you want excluded from the response\.
+ LabelCategoryInclusionFilters \- Allows you to specify which label categories you want included in the response\.
+ LabelCategoryExclusionFilters \- Allows you to specify which label categories you want excluded from the response\.

 You can also combine inclusive and exclusive filters according to your needs, excluding some labels or categories and including others\. 

`IMAGE_PROPERTIES` refer to an image’s dominant colors and quality attributes such as sharpness, brightness, and contrast\. When detecting `IMAGE_PROPERTIES` you can specify the maximum number of dominant colors to return \(default is 10\) by using the `MaxDominantColors` parameter\.

```
{
    "Image": {
        "S3Object": {
            "Bucket": "bucket",
            "Name": "input.jpg"
        }
    },
    "MaxLabels": 10,
    "MinConfidence": 75,
    "Features": [ "GENERAL_LABELS", "IMAGE_PROPERTIES" ],
    "Settings": {
        "GeneralLabels": {
            "LabelInclusionFilters": [<Label(s)>],
            "LabelExclusionFilters": [<Label(s)>],
            "LabelCategoryInclusionFilters": [<Category Name(s)>],
            "LabelCategoryExclusionFilters": [<Category Name(s)>] 
        },
        "ImageProperties": {
            "MaxDominantColors":10
        }
    }
}
```

## DetectLabels response<a name="detectlabels-response"></a>

The response from `DetectLabels` is an array of labels detected in the image and the level of confidence by which they were detected\. 

The following is an example response from `DetectLabels`\. The sample response below contains a variety of attributes returned for GENERAL\_LABELS, including:
+ Name \- The name of the detected label\. In this example, the operation detected an object with the label Mobile Phone\.
+ Confidence \- Each label has an associated level of confidence\. In this example, the confidence for the label was 99\.36%\.
+ Parents \- The ancestor labels for a detected label\. In this example, the label Mobile Phone has one parent label named Phone\.
+ Aliases \- Information about possible Aliases for the label\. In this example, the Mobile Phone label has a possible alias of Cell Phone\.
+ Categories \- The label category that the detected label belongs to\. In this example, it is Technology and Computing\.

The response for common object labels includes bounding box information for the location of the label on the input image\. For example, the Person label has an instances array containing two bounding boxes\. These are the locations of two people detected in the image\.

The response also includes attributes regarding IMAGE\_PROPERTIES\. The attributes presented by the IMAGE\_PROPERTIES feature are:
+ Quality \- Information about the Sharpness, Brightness, and Contrast of the input image, scored between 0 to 100\. Quality is reported for the entire image and for the background and foreground of the image, if available\. However, Contrast is only reported for the entire image while Sharpness and Brightness are also reported for Background and Foreground\. 
+  Dominant Color \- An array of the dominant colors in the image\. Each dominant color is described with a simplified color name, a CSS color palette, RGB values, and a hex code\. 
+  Foreground \- Information about the dominant Colors, Sharpness and Brightness of the input image’s foreground\. 
+  Background \- Information about the dominant Colors, Sharpness and Brightness of the input image’s background\. 

 When GENERAL\_LABELS and IMAGE\_PROPERTIES are used together as input parameters, Amazon Rekognition Image will also return the dominant colors of objects with bounding boxes\. 

The field `LabelModelVersion` contains the version number of the detection model used by `DetectLabels`\. 

```
{
   
   "Labels": [
        {
            "Name": "Mobile Phone",
            "Parents": [
              { 
                "Name": "Phone" 
              }
            ],
            "Aliases": [
              {
                "Name": "Cell Phone" 
              }
            ], 
            "Categories": [
              {
                "Name": "Technology and Computing"
              }
            ],
            "Confidence": 99.9364013671875,
            "Instances": [
                {
                    "BoundingBox": {
                        "Width": 0.26779675483703613,
                        "Height": 0.8562285900115967,
                        "Left": 0.3604024350643158,
                        "Top": 0.09245597571134567,
                    }
                    "Confidence": 99.9364013671875,
                    "DominantColors": [
                    {
                "Red": 120,
                "Green": 137,
                "Blue": 132,
                "HexCode": "3A7432",
                "SimplifiedColor": "red", 
                "CssColor": "fuscia",    
                "PixelPercentage": 40.10 
                    }       
                        ],
                }
            ]
        }
    ],
    "ImageProperties": {
        "Quality": {
            "Brightness": 40,
            "Sharpness": 40,
            "Contrast": 24,
        },
        "DominantColors": [
            {
                "Red": 120,
                "Green": 137,
                "Blue": 132,
                "HexCode": "3A7432",
                "SimplifiedColor": "red", 
                "CssColor": "fuscia",    
                "PixelPercentage": 40.10 
            }       
        ],
        "Foreground": {
            "Quality": {
                "Brightness": 40,
                "Sharpness": 40,
            },
            "DominantColors": [                
                {                    
                    "Red": 200,
                    "Green": 137,
                    "Blue": 132,
                    "HexCode": "3A7432",
                    "CSSColor": "",
                    "SimplifiedColor": "red", 
                    "PixelPercentage": 30.70             
                }          
            ],   
        }
        "Background": {
            "Quality": {
                "Brightness": 40,
                "Sharpness": 40,
            },
            "DominantColors": [                
                {                    
                    "Red": 200,
                    "Green": 137,
                    "Blue": 132,
                    "HexCode": "3A7432",
                    "CSSColor": "",
                    "SimplifiedColor": "Red", 
                    "PixelPercentage": 10.20              
                }          
            ],   
        }, 
    },
    "LabelModelVersion": "3.0"
}
```

## Transforming the DetectLabels response<a name="detectlabels-transform-response"></a>

When using the DetectLabels API, you might need the response structure to mimic the older API response structure, where both primary labels and aliases were contained in the same list\. 

The following is an example of the current API response from [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html):

```
"Labels": [
        {
            "Name": "Mobile Phone",
            "Confidence": 99.99717712402344,
            "Instances": [],
            "Parents": [
                { 
                "Name": "Phone" 
                }
             ],
            "Aliases": [
                {
                "Name": "Cell Phone" 
                }
             ]
        }
 ]
```

The following example shows the previous response from the [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html) API:

```
"Labels": [
        {
            "Name": "Mobile Phone",
            "Confidence": 99.99717712402344,
            "Instances": [],
            "Parents": [
                {
                "Name": "Phone" 
                }
             ]
         },
         {
            "Name": "Cell Phone",
            "Confidence": 99.99717712402344,
            "Instances": [],
            "Parents": [
                { 
                "Name": "Phone" 
                }
             ]
         },
]
```

If needed, you can transform the current response to follow the format of the older response\. You can use the following sample code to transform the latest API response to the previous API response structure:

------
#### [ Python ]

The following code sample demonstrates how to transform the current response from the DetectLabels API\. In the code sample below, you can replace the value of *EXAMPLE\_INFERENCE\_OUTPUT* with the output of a DetectLabels operation you have run\.

```
from copy import deepcopy

LABEL_KEY = "Labels"
ALIASES_KEY = "Aliases"
INSTANCE_KEY = "Instances"
NAME_KEY = "Name"

#Latest API response sample
EXAMPLE_INFERENCE_OUTPUT = {
    "Labels": [
        {
            "Name": "Mobile Phone",
            "Confidence": 97.530106,
            "Categories": [
                {
                    "Name": "Technology and Computing"
                }
            ],
            "Aliases": [
                {
                    "Name": "Cell Phone"
                }
            ],
            "Instances":[
                {
                    "BoundingBox":{
                        "Height":0.1549897,
                        "Width":0.07747964,
                        "Top":0.50858885,
                        "Left":0.00018205095
                    },
                    "Confidence":98.401276
                }
            ]
        },
        {
            "Name": "Urban",
            "Confidence": 99.99982,
            "Categories": [
                "Colors and Visual Composition"
            ]
        }
    ]
}

def expand_aliases(inferenceOutputsWithAliases):

    if LABEL_KEY in inferenceOutputsWithAliases:
        expandInferenceOutputs = []
        for primaryLabelDict in inferenceOutputsWithAliases[LABEL_KEY]:
            if ALIASES_KEY in primaryLabelDict:
                for alias in primaryLabelDict[ALIASES_KEY]:
                    aliasLabelDict = deepcopy(primaryLabelDict)
                    aliasLabelDict[NAME_KEY] = alias[NAME_KEY]
                    del aliasLabelDict[ALIASES_KEY]
                    if INSTANCE_KEY in aliasLabelDict:
                        del aliasLabelDict[INSTANCE_KEY]
                    expandInferenceOutputs.append(aliasLabelDict)

        inferenceOutputsWithAliases[LABEL_KEY].extend(expandInferenceOutputs)

    return inferenceOutputsWithAliases


if __name__ == "__main__":

    outputWithExpandAliases = expand_aliases(EXAMPLE_INFERENCE_OUTPUT)
    print(outputWithExpandAliases)
```

Below is an example of the transformed response:

```
#Output example after the transformation
{
    "Labels": [
        {
            "Name": "Mobile Phone",
            "Confidence": 97.530106,
            "Categories": [
                {
                    "Name": "Technology and Computing"
                }
            ],
            "Aliases": [
                {
                    "Name": "Cell Phone"
                }
            ],
            "Instances":[
                {
                    "BoundingBox":{
                        "Height":0.1549897,
                        "Width":0.07747964,
                        "Top":0.50858885,
                        "Left":0.00018205095
                    },
                    "Confidence":98.401276
                }
            ]
        },
        {
            "Name": "Cell Phone",
            "Confidence": 97.530106,
            "Categories": [
                {
                    "Name": "Technology and Computing"
                }
            ],
            "Instances":[]
        },
        {
            "Name": "Urban",
            "Confidence": 99.99982,
            "Categories": [
                "Colors and Visual Composition"
            ]
        }
    ]
}
```

------