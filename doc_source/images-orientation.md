# Getting image orientation and bounding box coordinates<a name="images-orientation"></a>

Applications that use Amazon Rekognition Image commonly need to display the images that are detected by Amazon Rekognition Image operations and the boxes around detected faces\. To display an image correctly in your application, you need to know the image's orientation\. You might need to correct this orientation\. For some \.jpg files, the image's orientation is contained in the image's Exchangeable image file format \(Exif\) metadata\. 

To display a box around a face, you need the coordinates for the face's bounding box\. If the box isn't oriented correctly, you might need to adjust those coordinates\. Amazon Rekognition Image face detection operations return bounding box coordinates for each detected face, but it doesn't estimate coordinates for \.jpg files without Exif metadata\.

The following examples show how to get the bounding box coordinates for the faces detected in an image\.

Use the information in this example to ensure that your images are oriented correctly and that bounding boxes are displayed in the correct location in your application\. 

Because the code used to rotate and display images and bounding boxes depends on the language and environment that you use, we don't explain how to display images and bounding boxes in your code, or how to get orientation information from Exif metadata\.



## Finding an image's orientation<a name="images-discovering-image-orientation"></a>

To display an image correctly in your application, you might need to rotate it\. The following image is oriented to 0 degrees and is displayed correctly\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/00face.png)

However, the following image is rotated 90 degrees counterclockwise\. To display it correctly, you need to find the orientation of the image and use that information in your code to rotate the image to 0 degrees\. 

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/90face.png)

Some images in \.jpg format contain orientation information in Exif metadata\. If available, the Exif metadata for the image contains the orientation\. In the Exif metadata, you can find the image's orientation in the `orientation` field\. Although Amazon Rekognition Image identifies the presence of image orientation information in Exif metadata, it does not provide access to it\. To access the Exif metadata in an image, use a third\-party library or write your own code\. For more information, see [Exif Version 2\.32](http://cipa.jp/std/documents/download_e.html?DC-008-Translation-2019-E)\.

 



When you know an image's orientation, you can write code to rotate and correctly display it\.

## Displaying bounding boxes<a name="images-bounding-boxes"></a>

The Amazon Rekognition Image operations that analyze faces in an image also return the coordinates of the bounding boxes that surround the faces\. For more information, see [ BoundingBox ](API_BoundingBox.md)\. 

To display a bounding box around a face, similar to the box shown in the following image, in your application, use the bounding box coordinates in your code\. The bounding box coordinates returned by an operation reflect the image's orientation\. If you have to rotate the image to display it correctly, you might need to translate the bounding box coordinates\.



![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/00facebounding.png)



### Displaying bounding boxes when orientation information is present in Exif metadata<a name="images-exif-metadata"></a>

If an image's orientation is included in Exif metadata, Amazon Rekognition Image operations do the following:
+ Return null in the orientation correction field in the operation's response\. To rotate the image, use the orientation provided in the Exif metadata in your code\.
+ Return bounding box coordinates already oriented to 0 degrees\. To show the bounding box in the correct position, use the coordinates that were returned\. You do not need to translate them\.

## Example: Getting image orientation and bounding box coordinates for an image<a name="images-correcting-image-orientation-java"></a>

The following examples show how to use the AWS SDK to get the Exif image orientation data and the bounding box coordinates for celebrities detected by the `RecognizeCelebrities` operation\.

**Note**  
Support for estimating image orientation using the the `OrientationCorrection` field has ceased as of August 2021\. Any returned values for this field included in an API response will always be NULL\.

------
#### [ Java ]

This example loads an image from the local file system, calls the `RecognizeCelebrities` operation, determines the height and width of the image, and calculates the bounding box coordinates of the face for the rotated image\. The example does not show how to process orientation information that is stored in Exif metadata\.

In the function `main`, replace the value of `photo` with the name and path of an image that is stored locally in either \.png or \.jpg format\.

```
//Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
//PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

package com.amazonaws.samples;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.nio.ByteBuffer;
import java.util.List;
import javax.imageio.ImageIO;
import com.amazonaws.services.rekognition.AmazonRekognition;
import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
import com.amazonaws.services.rekognition.model.Image;
import com.amazonaws.services.rekognition.model.RecognizeCelebritiesRequest;
import com.amazonaws.services.rekognition.model.RecognizeCelebritiesResult;
import com.amazonaws.util.IOUtils;
import com.amazonaws.services.rekognition.model.AmazonRekognitionException;
import com.amazonaws.services.rekognition.model.BoundingBox;
import com.amazonaws.services.rekognition.model.Celebrity;
import com.amazonaws.services.rekognition.model.ComparedFace;

public class RotateImage {

public static void main(String[] args) throws Exception {

  String photo = "photo.png";

  //Get Rekognition client
 AmazonRekognition amazonRekognition = AmazonRekognitionClientBuilder.defaultClient();


  // Load image
  ByteBuffer imageBytes=null;
  BufferedImage image = null;

  try (InputStream inputStream = new FileInputStream(new File(photo))) {
     imageBytes = ByteBuffer.wrap(IOUtils.toByteArray(inputStream));

  }
  catch(Exception e)
  {
      System.out.println("Failed to load file " + photo);
      System.exit(1);
  }

  //Get image width and height
  InputStream imageBytesStream;
  imageBytesStream = new ByteArrayInputStream(imageBytes.array());

  ByteArrayOutputStream baos = new ByteArrayOutputStream();
  image=ImageIO.read(imageBytesStream);
  ImageIO.write(image, "jpg", baos);

  int height = image.getHeight();
  int width = image.getWidth();

  System.out.println("Image Information:");
  System.out.println(photo);
  System.out.println("Image Height: " + Integer.toString(height));
  System.out.println("Image Width: " + Integer.toString(width));

  //Call GetCelebrities

  try{
    RecognizeCelebritiesRequest request = new RecognizeCelebritiesRequest()
           .withImage(new Image()
              .withBytes((imageBytes)));


      RecognizeCelebritiesResult result = amazonRekognition.recognizeCelebrities(request);
      // The returned value of OrientationCorrection will always be null
      System.out.println("Orientation: " + result.getOrientationCorrection() + "\n");
      List <Celebrity> celebs = result.getCelebrityFaces();

      for (Celebrity celebrity: celebs) {
          System.out.println("Celebrity recognized: " + celebrity.getName());
          System.out.println("Celebrity ID: " + celebrity.getId());
          ComparedFace  face = celebrity.getFace()
;             ShowBoundingBoxPositions(height,
                  width,
                  face.getBoundingBox(),
                  result.getOrientationCorrection());
                 
            System.out.println();
       }

   } catch (AmazonRekognitionException e) {
      e.printStackTrace();
   }

}


public static void ShowBoundingBoxPositions(int imageHeight, int imageWidth, BoundingBox box, String rotation) {

  float left = 0;
  float top = 0;
   
  if(rotation==null){
      System.out.println("No estimated estimated orientation. Check Exif data.");
      return;
  }
  //Calculate face position based on image orientation.
  switch (rotation) {
     case "ROTATE_0":
        left = imageWidth * box.getLeft();
        top = imageHeight * box.getTop();
        break;
     case "ROTATE_90":
        left = imageHeight * (1 - (box.getTop() + box.getHeight()));
        top = imageWidth * box.getLeft();
        break;
     case "ROTATE_180":
        left = imageWidth - (imageWidth * (box.getLeft() + box.getWidth()));
        top = imageHeight * (1 - (box.getTop() + box.getHeight()));
        break;
     case "ROTATE_270":
        left = imageHeight * box.getTop();
        top = imageWidth * (1 - box.getLeft() - box.getWidth());
        break;
     default:
        System.out.println("No estimated orientation information. Check Exif data.");
        return;
  }

  //Display face location information.
  System.out.println("Left: " + String.valueOf((int) left));
  System.out.println("Top: " + String.valueOf((int) top));
  System.out.println("Face Width: " + String.valueOf((int)(imageWidth * box.getWidth())));
  System.out.println("Face Height: " + String.valueOf((int)(imageHeight * box.getHeight())));

  }
}
```

------
#### [ Python ]

This example uses the PIL/Pillow image library to get the image width and height\. For more information, see [Pillow](https://pillow.readthedocs.io/en/stable/)\. This example preserves exif metadata which you might need elsewhere in your application\.

In the function `main`, replace the value of `photo` with the name and path of an image that is stored locally in either \.png or \.jpg format\.

```
#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import io
from PIL import Image


# Calculate positions from from estimated rotation
def show_bounding_box_positions(imageHeight, imageWidth, box):
    left = 0
    top = 0

    print('Left: ' + '{0:.0f}'.format(left))
    print('Top: ' + '{0:.0f}'.format(top))
    print('Face Width: ' + "{0:.0f}".format(imageWidth * box['Width']))
    print('Face Height: ' + "{0:.0f}".format(imageHeight * box['Height']))


def celebrity_image_information(photo):
    client = boto3.client('rekognition')

    # Get image width and height
    image = Image.open(open(photo, 'rb'))
    width, height = image.size

    print('Image information: ')
    print(photo)
    print('Image Height: ' + str(height))
    print('Image Width: ' + str(width))

    # call detect faces and show face age and placement
    # if found, preserve exif info
    stream = io.BytesIO()
    if 'exif' in image.info:
        exif = image.info['exif']
        image.save(stream, format=image.format, exif=exif)
    else:
        image.save(stream, format=image.format)
    image_binary = stream.getvalue()

    response = client.recognize_celebrities(Image={'Bytes': image_binary})

    print()
    print('Detected celebrities for ' + photo)

    for celebrity in response['CelebrityFaces']:
        print('Name: ' + celebrity['Name'])
        print('Id: ' + celebrity['Id'])

        # Value of "orientation correction" will always be null
        if 'OrientationCorrection' in response:
            show_bounding_box_positions(height, width, celebrity['Face']['BoundingBox'])

        print()
    return len(response['CelebrityFaces'])


def main():
    photo = 'photo'

    celebrity_count = celebrity_image_information(photo)
    print("celebrities detected: " + str(celebrity_count))


if __name__ == "__main__":
    main()
```

------
#### [ Java V2 ]

This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/RotateImage.java)\.

```
    public static void recognizeAllCelebrities(RekognitionClient rekClient, String sourceImage) {

        try {
            BufferedImage image = null;
            InputStream sourceStream = new FileInputStream(sourceImage);
            SdkBytes sourceBytes = SdkBytes.fromInputStream(sourceStream);

            image = ImageIO.read(sourceBytes.asInputStream());
            int height = image.getHeight();
            int width = image.getWidth();

            Image souImage = Image.builder()
                    .bytes(sourceBytes)
                    .build();

            RecognizeCelebritiesRequest request = RecognizeCelebritiesRequest.builder()
                    .image(souImage)
                    .build();

            RecognizeCelebritiesResponse result = rekClient.recognizeCelebrities(request) ;

            List<Celebrity> celebs=result.celebrityFaces();
            System.out.println(celebs.size() + " celebrity(s) were recognized.\n");

            for (Celebrity celebrity: celebs) {
                System.out.println("Celebrity recognized: " + celebrity.name());
                System.out.println("Celebrity ID: " + celebrity.id());
                ComparedFace  face = celebrity.face();
                ShowBoundingBoxPositions(height,
                        width,
                        face.boundingBox(),
                        result.orientationCorrectionAsString());
            }

        } catch (RekognitionException | FileNotFoundException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void ShowBoundingBoxPositions(int imageHeight, int imageWidth, BoundingBox box, String rotation) {

        float left = 0;
        float top = 0;

        if(rotation==null){
            System.out.println("No estimated estimated orientation.");
            return;
        }
        // Calculate face position based on the image orientation
        switch (rotation) {
            case "ROTATE_0":
                left = imageWidth * box.left();
                top = imageHeight * box.top();
                break;
            case "ROTATE_90":
                left = imageHeight * (1 - (box.top() + box.height()));
                top = imageWidth * box.left();
                break;
            case "ROTATE_180":
                left = imageWidth - (imageWidth * (box.left() + box.width()));
                top = imageHeight * (1 - (box.top() + box.height()));
                break;
            case "ROTATE_270":
                left = imageHeight * box.top();
                top = imageWidth * (1 - box.left() - box.width());
                break;
            default:
                System.out.println("No estimated orientation information. Check Exif data.");
                return;
        }

        System.out.println("Left: " + (int) left);
        System.out.println("Top: " + (int) top);
        System.out.println("Face Width: " + (int) (imageWidth * box.width()));
        System.out.println("Face Height: " + (int) (imageHeight * box.height()));
    }
```

------