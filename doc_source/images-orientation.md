# Getting Image Orientation and Bounding Box Coordinates<a name="images-orientation"></a>

Applications that use Amazon Rekognition Image commonly need to display the images that are detected by Amazon Rekognition Image operations and the boxes around detected faces\. To display an image correctly in your application, you need to know the image's orientation and possibly correct it\. For some \.jpg files, the image's orientation is contained in the image's Exchangeable image file format \(Exif\) metadata\. For other \.jpg files and all \.png files, Amazon Rekognition Image operations return the estimated orientation\.

To display a box around a face, you need the coordinates for the face's bounding box\. If the box isn't oriented correctly, you might need to adjust those coordinates\. Amazon Rekognition Image face detection operations return bounding box coordinates for each detected face\. 

The following Amazon Rekognition Image operations return information for correcting an image's orientation and bounding box coordinates: 
+ [CompareFaces](API_CompareFaces.md)
+ [DetectFaces](API_DetectFaces.md)
+ [DetectLabels](API_DetectLabels.md) \(returns only information to correct image orientation\)
+ [IndexFaces](API_IndexFaces.md)
+ [RecognizeCelebrities](API_RecognizeCelebrities.md)

This example shows how to get the following information for your code:
+ The estimated orientation of an image \(if there is no orientation information in Exif metadata\)
+ The bounding box coordinates for the faces detected in an image 
+ Translated bounding box coordinates for bounding boxes that are affected by estimated image orientation

Use the information in this example to ensure that your images are oriented correctly and that bounding boxes are displayed in the correct location in your application\. 

Because the code used to rotate and display images and bounding boxes depends on the language and environment that you use, we don't explain how to display images and bounding boxes in your code, or how to get orientation information from Exif metadata\.

## Finding an Image's Orientation<a name="images-discovering-image-orientation"></a>

To display an image correctly in your application, you might need to rotate it\. The following image is oriented to 0 degrees and is displayed correctly\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/00face.png)

However, the following image is rotated 90 degrees counterclockwise\. To display it correctly, you need to find the orientation of the image and use that information in your code to rotate the image to 0 degrees\. 

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/90face.png)

Some images in \.jpg format contain orientation information in Exif metadata\. If the value of the `OrientationCorrection` field is `null` in the operation's response, the Exif metadata for the image contains the orientation\. In the Exif metadata, you can find the image's orientation in the `orientation` field\. Although Amazon Rekognition Image identifies the presence of image orientation information in Exif metadata, it does not provide access to it\. To access the Exif metadata in an image, use a third\-party library or write your own code\. For more information, see [Exif Version 2\.31](http://www.cipa.jp/std/documents/e/DC-008-Translation-2016-E.pdf)\.

Images in \.png format do not have Exif metadata\. For \.jpg images that don't have Exif metadata and for all \.png images, Amazon Rekognition Image operations return an estimated orientation for the image in the `OrientationCorrection` field\. Estimated orientation is measured counterclockwise and in increments of 90 degrees\. For example, Amazon Rekognition Image returns ROTATE\_0 for an image that is oriented to 0 degrees and ROTATE\_90 for an image that is rotated 90 degrees counterclockwise\.

**Note**  
The `CompareFaces` operation returns the source image orientation in the `SourceImageOrientationCorrection` field and the target image orientation in the `TargetImageOrientationCorrection` field\. 

When you know an image's orientation, you can write code to rotate and correctly display it\.

## Displaying Bounding Boxes<a name="images-displaying-bounding-boxes"></a>

The Amazon Rekognition Image operations that analyze faces in an image also return the coordinates of the bounding boxes that surround the faces\. For more information, see [BoundingBox](API_BoundingBox.md)\. 

To display a bounding box around a face similar to the box shown in the following image in your application, use the bounding box coordinates in your code\. The bounding box coordinates returned by an operation reflect the image's orientation\. If you have to rotate the image to display it correctly, you might need to translate the bounding box coordinates\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/00facebounding.png)

### Displaying Bounding Boxes When Orientation Information Is Not Present in Exif Metadata<a name="images-no-exif-metadata"></a>

If an image doesn't have Exif metadata, or if the `orientation` field in the Exif metadata is not populated, Amazon Rekognition Image operations return the following:
+ An estimated orientation for the image
+ The bounding box coordinates oriented to the estimated orientation

If you need to rotate the image to display it correctly, you also need to rotate the bounding box\.

For example, the following image is oriented at 90 degrees counterclockwise and shows a bounding box around the face\. The bounding box is displayed using the coordinates for the estimated orientation returned from an Amazon Rekognition Image operation\. 

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/90faceboundingbox.png)

When you rotate the image to 0 degrees orientation, you also need to rotate the bounding box by translating the bounding box coordinates\. For example, the following image has been rotated to 0 degrees from 90 degrees counterclockwise\. The bounding box coordinates have not yet been translated, so the bounding box is displayed in the wrong position\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/notranslate.png)

**To rotate and display bounding boxes when orientation isn't present in Exif metadata**

1. Call an Amazon Rekognition Image operation providing an input image with at least one face and with no Exif metadata orientation\. For an example, see [Detecting Faces in an Image](faces-detect-images.md)\.

1. Note the estimated orientation returned in the response's `OrientationCorrection` field\.

1. Rotate the image to 0 degrees orientation by using the estimated orientation you noted in step 2 in your code\.

1. Translate the top and left bounding box coordinates to 0 degrees orientation and convert them to pixel points on the image in your code\. Use the formula in the following list that matches the estimated orientation you noted in step 2\.

   Note the following definitions: 
   + `ROTATE_(n)` is the estimated image orientation returned by an Amazon Rekognition Image operation\.
   + `<face>` represents information about the face that is returned by an Amazon Rekognition Image operation\. For example, the [FaceDetail](API_FaceDetail.md) data type that the [DetectFaces](API_DetectFaces.md) operation returns contains bounding box information for faces detected in the source image\.
   + `image.width` and `image.height` are pixel values for the width and height of the source image\. 
   + The bounding box coordinates are a value between 0 and 1 relative to the image size\. For example, for an image with 0 degree orientation, a `BoundingBox.left` value of 0\.9 puts the left coordinate close to the right side of the image\. To display the box, translate the bounding box coordinate values to pixel points on the image and rotate them to 0 degrees, as shown in each of the following formulas\. For more information, see [BoundingBox](API_BoundingBox.md)\.  
**ROTATE\_0**  
`left = image.width*BoundingBox.Left`  
`top = image.height*BoundingBox.Top`  
**ROTATE\_90**  
`left = image.height * (1 - (<face>.BoundingBox.Top + <face>.BoundingBox.Height))`  
`top = image.width * <face>.BoundingBox.Left`  
**ROTATE\_180**  
`left = image.width - (image.width*(<face>.BoundingBox.Left+<face>.BoundingBox.Width))`  
`top = image.height * (1 - (<face>.BoundingBox.Top + <face>.BoundingBox.Height))`  
**ROTATE\_270**  
`left = image.height * BoundingBox.top`  
`top = image.width * (1 - BoundingBox.Left - BoundingBox.Width)`

1. Using the following formulas, calculate the bounding box's width and height as pixel ranges on the image in your code\.

   The width and height of a bounding box is returned in the `BoundingBox.Width` and `BoundingBox.Height` fields\. The width and height values range between 0 and 1 relative to the image size\. `image.width` and `image.height` are pixel values for the width and height of the source image\.  
****  
`box width = image.width * (<face>.BoundingBox.Width)`  
`box height = image.height * (<face>.BoundingBox.Height)`

1.  Display the bounding box on the rotated image by using the values calculated in steps 4 and 5\.

### Displaying Bounding Boxes When Orientation Information is Present in Exif Metadata<a name="images-exif-metadata"></a>

If an image's orientation is included in Exif metadata, Amazon Rekognition Image operations do the following:
+ Return null in the orientation correction field in the operation's response\. To rotate the image, use the orientation provided in the Exif metadata in your code\.
+ Return bounding box coordinates already oriented to 0 degrees\. To show the bounding box in the correct position, use the coordinates that were returned\. You do not need to translate them\.

## Example: Getting Image Orientation and Bounding Box Coordinates For an Image<a name="images-correcting-image-orientation-java"></a>

The following example shows how to use the AWS SDK for Java to get the estimated orientation of an image and to translate bounding box coordinates for faces detected by the `DetectFaces` operation\.

The example loads an image from the local file system, calls the `DetectFaces` operation, determines the height and width of the image, and calculates the bounding box coordinates of the face for the rotated image\. The example does not show how to process orientation information that is stored in Exif metadata\.

To use this code, replace the value of `photo` with the name and path of an image that is stored locally in either \.png or \.jpg format\.

------
#### [ Java ]

```
package aws.example.rekognition.image;
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
import com.amazonaws.util.IOUtils;
import com.amazonaws.services.rekognition.model.AgeRange;
import com.amazonaws.services.rekognition.model.AmazonRekognitionException;
import com.amazonaws.services.rekognition.model.Attribute;
import com.amazonaws.services.rekognition.model.BoundingBox;
import com.amazonaws.services.rekognition.model.DetectFacesRequest;
import com.amazonaws.services.rekognition.model.DetectFacesResult;
import com.amazonaws.services.rekognition.model.FaceDetail;

public class RotateImage {

public static void main(String[] args) throws Exception {

  String photo = "input.png";

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

  //Call detect faces and show face age and placement

  try{
    DetectFacesRequest request = new DetectFacesRequest()
           .withImage(new Image()
              .withBytes((imageBytes)))
           .withAttributes(Attribute.ALL);


      DetectFacesResult result = amazonRekognition.detectFaces(request);
      System.out.println("Orientation: " + result.getOrientationCorrection() + "\n");
      List <FaceDetail> faceDetails = result.getFaceDetails();

      for (FaceDetail face: faceDetails) {
        System.out.println("Face:");
          ShowBoundingBoxPositions(height,
                  width,
                  face.getBoundingBox(),
                  result.getOrientationCorrection());
          AgeRange ageRange = face.getAgeRange();
          System.out.println("The detected face is estimated to be between "
               + ageRange.getLow().toString() + " and " + ageRange.getHigh().toString()
               + " years old.");
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

This example uses the PIL/Pillow image library to get the image width and height\. For more information, see [Pillow](http://pillow.readthedocs.io/en/3.0.x/index.html#)\. This example preserves exif metadata which you might need elsewhere in your application\. If you choose to not save the exif metadata, the estimated orientation is returned from the call to `DetectFaces`\. 

```
import boto3
import io
from PIL import Image

# Calculate positions from from estimated rotation 
def ShowBoundingBoxPositions(imageHeight, imageWidth, box, rotation): 
    left = 0
    top = 0
      
    if rotation == 'ROTATE_0':
        left = imageWidth * box['Left']
        top = imageHeight * box['Top']
    
    if rotation == 'ROTATE_90':
        left = imageHeight * (1 - (box['Top'] + box['Height']))
        top = imageWidth * box['Left']

    if rotation == 'ROTATE_180':
        left = imageWidth - (imageWidth * (box['Left'] + box['Width']))
        top = imageHeight * (1 - (box['Top'] + box['Height']))

    if rotation == 'ROTATE_270':
        left = imageHeight * box['Top']
        top = imageWidth * (1- box['Left'] - box['Width'] )

    print('Left: ' + '{0:.0f}'.format(left))
    print('Top: ' + '{0:.0f}'.format(top))
    print('Face Width: ' + "{0:.0f}".format(imageWidth * box['Width']))
    print('Face Height: ' + "{0:.0f}".format(imageHeight * box['Height']))


if __name__ == "__main__":

    photo='input.png'
    client=boto3.client('rekognition')
 

    #Get image width and height
    image = Image.open(open(photo,'rb'))
    width, height = image.size

    print ('Image information: ')
    print (photo)
    print ('Image Height: ' + str(height)) 
    print('Image Width: ' + str(width))    


    # call detect faces and show face age and placement
    # if found, preserve exif info
    stream = io.BytesIO()
    if 'exif' in image.info:
        exif=image.info['exif']
        image.save(stream,format=image.format, exif=exif)
    else:
        image.save(stream, format=image.format)    
    image_binary = stream.getvalue()
   
    response = client.detect_faces(Image={'Bytes': image_binary}, Attributes=['ALL'])
    
    print('Detected faces for ' + photo)    
    for faceDetail in response['FaceDetails']:
        print ('Face:')
        if 'OrientationCorrection'  in response:
            print('Orientation: ' + response['OrientationCorrection'])
            ShowBoundingBoxPositions(height, width, faceDetail['BoundingBox'], response['OrientationCorrection'])
            
        else:
            print ('No estimated orientation. Check Exif data')
 
        print('The detected face is estimated to be between ' + str(faceDetail['AgeRange']['Low']) 
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years')
        print()
```

------
#### [ \.NET ]

```
using System;
using System.Collections.Generic;
using System.IO;
using Amazon.Rekognition;
using Amazon.Rekognition.Model;

public class ImageOrientationAndBoundingBox
{
    public static void Example()
    {
        String photo = "photo.jpg";

        AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();

        Image image = new Image();
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

        int height;
        int width;
        // Used to extract original photo width/height
        using (System.Drawing.Bitmap imageBitmap = new System.Drawing.Bitmap(photo))
        {
            height = imageBitmap.Height;
            width = imageBitmap.Width;
        }

        Console.WriteLine("Image Information:");
        Console.WriteLine(photo);
        Console.WriteLine("Image Height: " + height);
        Console.WriteLine("Image Width: " + width);

        try
        {
            DetectFacesRequest detectFacesRequest = new DetectFacesRequest()
            {
                Image = image,
                Attributes = new List<String>() { "ALL" }
            };

            DetectFacesResponse detectFacesResponse = rekognitionClient.DetectFaces(detectFacesRequest);
            foreach (FaceDetail face in detectFacesResponse.FaceDetails)
            {
                Console.WriteLine("Face:");
                ShowBoundingBoxPositions(height, width, 
                    face.BoundingBox, detectFacesResponse.OrientationCorrection);
                Console.WriteLine("BoundingBox: top={0} left={1} width={2} height={3}", face.BoundingBox.Left,
                    face.BoundingBox.Top, face.BoundingBox.Width, face.BoundingBox.Height);
                Console.WriteLine("The detected face is estimated to be between " +
                    face.AgeRange.Low + " and " + face.AgeRange.High + " years old.");
                Console.WriteLine();
            }
        }
        catch (Exception e)
        {
            Console.WriteLine(e.Message);
        }
    }

    public static void ShowBoundingBoxPositions(int imageHeight, int imageWidth, BoundingBox box, String rotation)
    {
        float left = 0;
        float top = 0;

        if (rotation == null)
        {
            Console.WriteLine("No estimated estimated orientation. Check Exif data.");
            return;
        }
        //Calculate face position based on image orientation.
        switch (rotation)
        {
            case "ROTATE_0":
                left = imageWidth * box.Left;
                top = imageHeight * box.Top;
                break;
            case "ROTATE_90":
                left = imageHeight * (1 - (box.Top + box.Height));
                top = imageWidth * box.Left;
                break;
            case "ROTATE_180":
                left = imageWidth - (imageWidth * (box.Left + box.Width));
                top = imageHeight * (1 - (box.Top + box.Height));
                break;
            case "ROTATE_270":
                left = imageHeight * box.Top;
                top = imageWidth * (1 - box.Left - box.Width);
                break;
            default:
                Console.WriteLine("No estimated orientation information. Check Exif data.");
                return;
        }

        //Display face location information.
        Console.WriteLine("Left: " + left);
        Console.WriteLine("Top: " + top);
        Console.WriteLine("Face Width: " + imageWidth * box.Width);
        Console.WriteLine("Face Height: " + imageHeight * box.Height);

    }
}
```

------