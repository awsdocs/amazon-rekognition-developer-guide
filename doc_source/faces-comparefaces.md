# Comparing faces in images<a name="faces-comparefaces"></a>

To compare a face in the *source* image with each face in the *target* image, use the [CompareFaces](API_CompareFaces.md) operation\. 

To specify the minimum level of confidence in the match that you want returned in the response, use `similarityThreshold` in the request\. For more information, see [CompareFaces](API_CompareFaces.md)\.

If you provide a source image that contains multiple faces, the service detects the largest face and uses it to compare with each face that's detected in the target image\. 

You can provide the source and target images as an image byte array \(base64\-encoded image bytes\), or specify Amazon S3 objects\. In the AWS CLI example, you upload two JPEG images to your Amazon S3 bucket and specify the object key name\. In the other examples, you load two files from the local file system and input them as image byte arrays\.

**Note**  
CompareFaces uses machine learning algorithms, which are probabilistic\. A false negative is an incorrect prediction that a face in the target image has a low similarity confidence score when compared to the face in the source image\. To reduce the probability of false negatives, we recommend that you compare the target image against multiple source images\. If you plan to use `CompareFaces` to make a decision that impacts an individual's rights, privacy, or access to services, we recommend that you pass the result to a human for review and further validation before taking action\.

**To compare faces**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` and `AmazonS3ReadOnlyAccess` \(AWS CLI example only\) permissions\. For more information, see [Step 1: Set up an AWS account and create an IAM user](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Use the following example code to call the `CompareFaces` operation\.

------
#### [ Java ]

   This example displays information about matching faces in source and target images that are loaded from the local file system\.

   Replace the values of `sourceImage` and `targetImage` with the path and file name of the source and target images\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   package aws.example.rekognition.image;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.Image;
   import com.amazonaws.services.rekognition.model.BoundingBox;
   import com.amazonaws.services.rekognition.model.CompareFacesMatch;
   import com.amazonaws.services.rekognition.model.CompareFacesRequest;
   import com.amazonaws.services.rekognition.model.CompareFacesResult;
   import com.amazonaws.services.rekognition.model.ComparedFace;
   import java.util.List;
   import java.io.File;
   import java.io.FileInputStream;
   import java.io.InputStream;
   import java.nio.ByteBuffer;
   import com.amazonaws.util.IOUtils;
   
   public class CompareFaces {
   
      public static void main(String[] args) throws Exception{
          Float similarityThreshold = 70F;
          String sourceImage = "source.jpg";
          String targetImage = "target.jpg";
          ByteBuffer sourceImageBytes=null;
          ByteBuffer targetImageBytes=null;
   
          AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
   
          //Load source and target images and create input parameters
          try (InputStream inputStream = new FileInputStream(new File(sourceImage))) {
             sourceImageBytes = ByteBuffer.wrap(IOUtils.toByteArray(inputStream));
          }
          catch(Exception e)
          {
              System.out.println("Failed to load source image " + sourceImage);
              System.exit(1);
          }
          try (InputStream inputStream = new FileInputStream(new File(targetImage))) {
              targetImageBytes = ByteBuffer.wrap(IOUtils.toByteArray(inputStream));
          }
          catch(Exception e)
          {
              System.out.println("Failed to load target images: " + targetImage);
              System.exit(1);
          }
   
          Image source=new Image()
               .withBytes(sourceImageBytes);
          Image target=new Image()
               .withBytes(targetImageBytes);
   
          CompareFacesRequest request = new CompareFacesRequest()
                  .withSourceImage(source)
                  .withTargetImage(target)
                  .withSimilarityThreshold(similarityThreshold);
   
          // Call operation
          CompareFacesResult compareFacesResult=rekognitionClient.compareFaces(request);
   
   
          // Display results
          List <CompareFacesMatch> faceDetails = compareFacesResult.getFaceMatches();
          for (CompareFacesMatch match: faceDetails){
            ComparedFace face= match.getFace();
            BoundingBox position = face.getBoundingBox();
            System.out.println("Face at " + position.getLeft().toString()
                  + " " + position.getTop()
                  + " matches with " + match.getSimilarity().toString()
                  + "% confidence.");
   
          }
          List<ComparedFace> uncompared = compareFacesResult.getUnmatchedFaces();
   
          System.out.println("There was " + uncompared.size()
               + " face(s) that did not match");
      }
   }
   ```

------
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/CompareFaces.java)\.

   ```
       public static void compareTwoFaces(RekognitionClient rekClient, Float similarityThreshold, String sourceImage, String targetImage) {
   
           try {
               InputStream sourceStream = new FileInputStream(new File(sourceImage));
               InputStream tarStream = new FileInputStream(new File(targetImage));
   
               SdkBytes sourceBytes = SdkBytes.fromInputStream(sourceStream);
               SdkBytes targetBytes = SdkBytes.fromInputStream(tarStream);
   
               // Create an Image object for the source image
               Image souImage = Image.builder()
                  .bytes(sourceBytes)
                  .build();
   
               Image tarImage = Image.builder()
                       .bytes(targetBytes)
                       .build();
   
               CompareFacesRequest facesRequest = CompareFacesRequest.builder()
                       .sourceImage(souImage)
                       .targetImage(tarImage)
                       .similarityThreshold(similarityThreshold)
                       .build();
   
               // Compare the two images
               CompareFacesResponse compareFacesResult = rekClient.compareFaces(facesRequest);
               List<CompareFacesMatch> faceDetails = compareFacesResult.faceMatches();
               for (CompareFacesMatch match: faceDetails){
                   ComparedFace face= match.face();
                   BoundingBox position = face.boundingBox();
                   System.out.println("Face at " + position.left().toString()
                           + " " + position.top()
                           + " matches with " + face.confidence().toString()
                           + "% confidence.");
   
               }
               List<ComparedFace> uncompared = compareFacesResult.unmatchedFaces();
   
               System.out.println("There was " + uncompared.size()
                       + " face(s) that did not match");
               System.out.println("Source image rotation: " + compareFacesResult.sourceImageOrientationCorrection());
               System.out.println("target image rotation: " + compareFacesResult.targetImageOrientationCorrection());
   
           } catch(RekognitionException | FileNotFoundException e) {
               System.out.println("Failed to load source image " + sourceImage);
               System.exit(1);
           }
   ```

------
#### [ AWS CLI ]

   This example displays the JSON output from the `compare-faces` AWS CLI operation\. 

   Replace `bucket-name` with the name of the Amazon S3 bucket that contains the source and target images\. Replace `source.jpg` and `target.jpg` with the file names for the source and target images\.

   ```
   aws rekognition compare-faces \
   --source-image '{"S3Object":{"Bucket":"bucket-name","Name":"source.jpg"}}' \
   --target-image '{"S3Object":{"Bucket":"bucket-name","Name":"target.jpg"}}'
   ```

------
#### [ Python ]

   This example displays information about matching faces in source and target images that are loaded from the local file system\.

   Replace the values of `source_file` and `target_file` with the path and file name of the source and target images\.

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   
   def compare_faces(sourceFile, targetFile):
   
       client=boto3.client('rekognition')
      
       imageSource=open(sourceFile,'rb')
       imageTarget=open(targetFile,'rb')
   
       response=client.compare_faces(SimilarityThreshold=80,
                                     SourceImage={'Bytes': imageSource.read()},
                                     TargetImage={'Bytes': imageTarget.read()})
       
       for faceMatch in response['FaceMatches']:
           position = faceMatch['Face']['BoundingBox']
           similarity = str(faceMatch['Similarity'])
           print('The face at ' +
                  str(position['Left']) + ' ' +
                  str(position['Top']) +
                  ' matches with ' + similarity + '% confidence')
   
       imageSource.close()
       imageTarget.close()     
       return len(response['FaceMatches'])          
   
   def main():
       source_file='source'
       target_file='target'
       face_matches=compare_faces(source_file, target_file)
       print("Face matches: " + str(face_matches))
   
   
   if __name__ == "__main__":
       main()
   ```

------
#### [ \.NET ]

   This example displays information about matching faces in source and target images that are loaded from the local file system\.

   Replace the values of `sourceImage` and `targetImage` with the path and file name of the source and target images\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   using System;
   using System.IO;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   public class CompareFaces
   {
       public static void Example()
       {
           float similarityThreshold = 70F;
           String sourceImage = "source.jpg";
           String targetImage = "target.jpg";
   
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           Amazon.Rekognition.Model.Image imageSource = new Amazon.Rekognition.Model.Image();
           try
           {
               using (FileStream fs = new FileStream(sourceImage, FileMode.Open, FileAccess.Read))
               {
                   byte[] data = new byte[fs.Length];
                   fs.Read(data, 0, (int)fs.Length);
                   imageSource.Bytes = new MemoryStream(data);
               }
           }
           catch (Exception)
           {
               Console.WriteLine("Failed to load source image: " + sourceImage);
               return;
           }
   
           Amazon.Rekognition.Model.Image imageTarget = new Amazon.Rekognition.Model.Image();
           try
           {
               using (FileStream fs = new FileStream(targetImage, FileMode.Open, FileAccess.Read))
               {
                   byte[] data = new byte[fs.Length];
                   data = new byte[fs.Length];
                   fs.Read(data, 0, (int)fs.Length);
                   imageTarget.Bytes = new MemoryStream(data);
               }
           }
           catch (Exception)
           {
               Console.WriteLine("Failed to load target image: " + targetImage);
               return;
           }
   
           CompareFacesRequest compareFacesRequest = new CompareFacesRequest()
           {
               SourceImage = imageSource,
               TargetImage = imageTarget,
               SimilarityThreshold = similarityThreshold
           };
   
           // Call operation
           CompareFacesResponse compareFacesResponse = rekognitionClient.CompareFaces(compareFacesRequest);
   
           // Display results
           foreach(CompareFacesMatch match in compareFacesResponse.FaceMatches)
           {
               ComparedFace face = match.Face;
               BoundingBox position = face.BoundingBox;
               Console.WriteLine("Face at " + position.Left
                     + " " + position.Top
                     + " matches with " + match.Similarity
                     + "% confidence.");
           }
   
           Console.WriteLine("There was " + compareFacesResponse.UnmatchedFaces.Count + " face(s) that did not match");
   
       }
   }
   ```

------
#### [ Ruby ]

   This example displays information about matching faces in source and target images that are loaded from the local file system\.

   Replace the values of `photo_source` and `photo_target` with the path and file name of the source and target images\.

   ```
     # Add to your Gemfile
      # gem 'aws-sdk-rekognition'
      require 'aws-sdk-rekognition'
      credentials = Aws::Credentials.new(
         ENV['AWS_ACCESS_KEY_ID'],
         ENV['AWS_SECRET_ACCESS_KEY']
      )
      bucket        = 'bucket' # the bucketname without s3://
      photo_source  = 'source.jpg'
      photo_target  = 'target.jpg'
      client   = Aws::Rekognition::Client.new credentials: credentials
      attrs = {
        source_image: {
          s3_object: {
            bucket: bucket,
            name: photo_source
          },
        },
        target_image: {
          s3_object: {
            bucket: bucket,
            name: photo_target
          },
        },
        similarity_threshold: 70
      }
      response = client.compare_faces attrs
      response.face_matches.each do |face_match|
        position   = face_match.face.bounding_box
        similarity = face_match.similarity
        puts "The face at: #{position.left}, #{position.top} matches with #{similarity} % confidence"
      end
   ```

------
#### [ Node\.js ]

   This example displays information about matching faces in source and target images that are loaded from the local file system\.

   Replace the values of `photo_source` and `photo_target` with the path and file name of the source and target images\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   
      const AWS = require('aws-sdk')
      const bucket        = 'bucket' // the bucketname without s3://
      const photo_source  = 'source.jpg'
      const photo_target  = 'target.jpg'
      const config = new AWS.Config({
        accessKeyId: process.env.AWS_ACCESS_KEY_ID,
        secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
        region: process.env.AWS_REGION
      })
      const client = new AWS.Rekognition();
      const params = {
        SourceImage: {
          S3Object: {
            Bucket: bucket,
            Name: photo_source
          },
        },
        TargetImage: {
          S3Object: {
            Bucket: bucket,
            Name: photo_target
          },
        },
        SimilarityThreshold: 70
      }
      client.compareFaces(params, function(err, response) {
        if (err) {
          console.log(err, err.stack); // an error occurred
        } else {
          response.FaceMatches.forEach(data => {
            let position   = data.Face.BoundingBox
            let similarity = data.Similarity
            console.log(`The face at: ${position.Left}, ${position.Top} matches with ${similarity} % confidence`)
          }) // for response.faceDetails
        } // if
      });
   ```

------

## CompareFaces operation request<a name="comparefaces-request"></a>

The input to `CompareFaces` is an image\. In this example, the source and target images are loaded from the local file system\. The `SimilarityThreshold` input parameter specifies the minimum confidence that compared faces must match to be included in the response\. For more information, see [Working with images](images.md)\.

```
{
    "SourceImage": {
        "Bytes": "/9j/4AAQSk2Q==..."
    },
    "TargetImage": {
        "Bytes": "/9j/4O1Q==..."
    },
    "SimilarityThreshold": 70
}
```

## CompareFaces operation response<a name="comparefaces-response"></a>

In the response, you get an array of face matches, source face information, source and target image orientation, and an array of unmatched faces\. For each matching face in the target image, the response provides a similarity score \(how similar the face is to the source face\) and face metadata\. Face metadata includes information such as the bounding box of the matching face and an array of facial landmarks\. The array of unmatched faces includes face metadata\. 

In the following example response, note the following:
+ **Face match information** – The example shows that one face match was found in the target image\. For that face match, it provides a bounding box and a confidence value \(the level of confidence that Amazon Rekognition has that the bounding box contains a face\)\. The `similarity` score of 99\.99 indicates how similar the faces are\. The face match information also includes an array of landmark locations\.

  If multiple faces match, the `faceMatches` array includes all of the face matches\. 
+ **Source face information** – The response includes information about the face from the source image that was used for comparison, including the bounding box and confidence value\.
+ **Unmatched face match information** – The example shows one face that Amazon Rekognition found in the target image that didn't match the face that was analyzed in the source image\. For that face, it provides a bounding box and a confidence value, which indicates the level of confidence that Amazon Rekognition has that the bounding box contains a face\. The face information also includes an array of landmark locations\.

  If Amazon Rekognition finds multiple faces that don't match, the `UnmatchedFaces` array includes all of the faces that didn't match\. 

```
{
    "FaceMatches": [{
        "Face": {
            "BoundingBox": {
                "Width": 0.5521978139877319,
                "Top": 0.1203877404332161,
                "Left": 0.23626373708248138,
                "Height": 0.3126954436302185
            },
            "Confidence": 99.98751068115234,
            "Pose": {
                "Yaw": -82.36799621582031,
                "Roll": -62.13221740722656,
                "Pitch": 0.8652129173278809
            },
            "Quality": {
                "Sharpness": 99.99880981445312,
                "Brightness": 54.49755096435547
            },
            "Landmarks": [{
                    "Y": 0.2996366024017334,
                    "X": 0.41685718297958374,
                    "Type": "eyeLeft"
                },
                {
                    "Y": 0.2658946216106415,
                    "X": 0.4414493441581726,
                    "Type": "eyeRight"
                },
                {
                    "Y": 0.3465650677680969,
                    "X": 0.48636093735694885,
                    "Type": "nose"
                },
                {
                    "Y": 0.30935320258140564,
                    "X": 0.6251809000968933,
                    "Type": "mouthLeft"
                },
                {
                    "Y": 0.26942989230155945,
                    "X": 0.6454493403434753,
                    "Type": "mouthRight"
                }
            ]
        },
        "Similarity": 100.0
    }],
    "SourceImageOrientationCorrection": "ROTATE_90",
    "TargetImageOrientationCorrection": "ROTATE_90",
    "UnmatchedFaces": [{
        "BoundingBox": {
            "Width": 0.4890109896659851,
            "Top": 0.6566604375839233,
            "Left": 0.10989011079072952,
            "Height": 0.278298944234848
        },
        "Confidence": 99.99992370605469,
        "Pose": {
            "Yaw": 51.51519012451172,
            "Roll": -110.32493591308594,
            "Pitch": -2.322134017944336
        },
        "Quality": {
            "Sharpness": 99.99671173095703,
            "Brightness": 57.23163986206055
        },
        "Landmarks": [{
                "Y": 0.8288310766220093,
                "X": 0.3133862614631653,
                "Type": "eyeLeft"
            },
            {
                "Y": 0.7632885575294495,
                "X": 0.28091415762901306,
                "Type": "eyeRight"
            },
            {
                "Y": 0.7417283654212952,
                "X": 0.3631140887737274,
                "Type": "nose"
            },
            {
                "Y": 0.8081989884376526,
                "X": 0.48565614223480225,
                "Type": "mouthLeft"
            },
            {
                "Y": 0.7548204660415649,
                "X": 0.46090251207351685,
                "Type": "mouthRight"
            }
        ]
    }],
    "SourceImageFace": {
        "BoundingBox": {
            "Width": 0.5521978139877319,
            "Top": 0.1203877404332161,
            "Left": 0.23626373708248138,
            "Height": 0.3126954436302185
        },
        "Confidence": 99.98751068115234
    }
}
```