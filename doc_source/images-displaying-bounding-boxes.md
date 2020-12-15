# Displaying bounding boxes<a name="images-displaying-bounding-boxes"></a>

Amazon Rekognition Image operations can return bounding boxes coordinates for items that are detected in images\. For example, the [DetectFaces](API_DetectFaces.md) operation returns a bounding box \([BoundingBox](API_BoundingBox.md)\) for each face detected in an image\. You can use the bounding box coordinates to display a box around detected items\. For example, the following image shows a bounding box surrounding a face\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/face.png)

A `BoundingBox` has the following properties:
+ Height – The height of the bounding box as a ratio of the overall image height\.
+ Left – The left coordinate of the bounding box as a ratio of overall image width\.
+ Top – The top coordinate of the bounding box as a ratio of overall image height\.
+ Width – The width of the bounding box as a ratio of the overall image width\.

Each BoundingBox property has a value between 0 and 1\. Each property value is a ratio of the overall image width \(`Left` and `Width`\) or height \(`Height` and `Top`\)\. For example, if the input image is 700 x 200 pixels, and the top\-left coordinate of the bounding box is 350 x 50 pixels, the API returns a `Left` value of 0\.5 \(350/700\) and a `Top` value of 0\.25 \(50/200\)\. 

The following diagram shows the range of an image that each bounding box property covers\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/bounding-box.png)

To display the bounding box with the correct location and size, you have to multiply the BoundingBox values by the image width or height \(depending on the value you want\) to get the pixel values\. You use the pixel values to display the bounding box\. For example, the pixel dimensions of the previous image are 608 width x 588 height\. The bounding box values for the face are: 

```
BoundingBox.Left: 0.3922065
Bounding.Top: 0.15567766
BoundingBox.Width: 0.284666
BoundingBox.Height: 0.2930403
```

The location of the face bounding box in pixels is calculated as follows: 

`Left coordinate = BoundingBox.Left (0.3922065) * image width (608) = 238`

`Top coordinate = BoundingBox.Top (0.15567766) * image height (588) = 91`

`Face width = BoundingBox.Width (0.284666) * image width (608) = 173`

`Face height = BoundingBox.Height (0.2930403) * image height (588) = 172`

You use these values to display a bounding box around the face\.

**Note**  
An image can be orientated in various ways\. Your application might need to rotate the image to display it with the correction orientation\. Bounding box coordinates are affected by the orientation of the image\. You might need to translate the coordinates before you can display a bounding box at the right location\. For more information, see [Getting image orientation and bounding box coordinates](images-orientation.md)\.

The following examples show how to display a bounding box around faces that are detected by calling [DetectFaces](API_DetectFaces.md)\. The examples assume that the images are oriented to 0 degrees\. The examples also show how to download the image from an Amazon S3 bucket\. 

**To display a bounding box**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` and `AmazonS3ReadOnlyAccess` permissions\. For more information, see [Step 1: Set up an AWS account and create an IAM user](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Use the following examples to call the `DetectFaces` operation\. Change the value of `bucket` to the Amazon S3 bucket that contains the image file\. Change the value of `photo` to the file name of an image file \(\.jpg or \.png format\)\.

------
#### [ Java ]

   ```
   //Loads images, detects faces and draws bounding boxes.Determines exif orientation, if necessary.
   package com.amazonaws.samples;
   
   //Import the basic graphics classes.
   import java.awt.*;
   import java.awt.image.BufferedImage;
   import java.util.List;
   import javax.imageio.ImageIO;
   import javax.swing.*;
   
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   
   import com.amazonaws.services.rekognition.model.BoundingBox;
   import com.amazonaws.services.rekognition.model.DetectFacesRequest;
   import com.amazonaws.services.rekognition.model.DetectFacesResult;
   import com.amazonaws.services.rekognition.model.FaceDetail;
   import com.amazonaws.services.rekognition.model.Image;
   import com.amazonaws.services.rekognition.model.S3Object;
   import com.amazonaws.services.s3.AmazonS3;
   import com.amazonaws.services.s3.AmazonS3ClientBuilder;
   import com.amazonaws.services.s3.model.S3ObjectInputStream;
   
   // Calls DetectFaces and displays a bounding box around each detected image.
   public class DisplayFaces extends JPanel {
   
       private static final long serialVersionUID = 1L;
   
       BufferedImage image;
       static int scale;
       DetectFacesResult result;
   
       public DisplayFaces(DetectFacesResult facesResult, BufferedImage bufImage) throws Exception {
           super();
           scale = 1; // increase to shrink image size.
   
           result = facesResult;
           image = bufImage;
   
           
       }
       // Draws the bounding box around the detected faces.
       public void paintComponent(Graphics g) {
           float left = 0;
           float top = 0;
           int height = image.getHeight(this);
           int width = image.getWidth(this);
   
           Graphics2D g2d = (Graphics2D) g; // Create a Java2D version of g.
   
           // Draw the image.
           g2d.drawImage(image, 0, 0, width / scale, height / scale, this);
           g2d.setColor(new Color(0, 212, 0));
   
           // Iterate through faces and display bounding boxes.
           List<FaceDetail> faceDetails = result.getFaceDetails();
           for (FaceDetail face : faceDetails) {
               
               BoundingBox box = face.getBoundingBox();
               left = width * box.getLeft();
               top = height * box.getTop();
               g2d.drawRect(Math.round(left / scale), Math.round(top / scale),
                       Math.round((width * box.getWidth()) / scale), Math.round((height * box.getHeight())) / scale);
               
           }
       }
   
   
       public static void main(String arg[]) throws Exception {
   
           String photo = "photo.png";
           String bucket = "bucket";
           int height = 0;
           int width = 0;
   
           // Get the image from an S3 Bucket
           AmazonS3 s3client = AmazonS3ClientBuilder.defaultClient();
   
           com.amazonaws.services.s3.model.S3Object s3object = s3client.getObject(bucket, photo);
           S3ObjectInputStream inputStream = s3object.getObjectContent();
           BufferedImage image = ImageIO.read(inputStream);
           DetectFacesRequest request = new DetectFacesRequest()
                   .withImage(new Image().withS3Object(new S3Object().withName(photo).withBucket(bucket)));
   
           width = image.getWidth();
           height = image.getHeight();
   
           // Call DetectFaces    
           AmazonRekognition amazonRekognition = AmazonRekognitionClientBuilder.defaultClient();
           DetectFacesResult result = amazonRekognition.detectFaces(request);
           
           //Show the bounding box info for each face.
           List<FaceDetail> faceDetails = result.getFaceDetails();
           for (FaceDetail face : faceDetails) {
   
               BoundingBox box = face.getBoundingBox();
               float left = width * box.getLeft();
               float top = height * box.getTop();
               System.out.println("Face:");
   
               System.out.println("Left: " + String.valueOf((int) left));
               System.out.println("Top: " + String.valueOf((int) top));
               System.out.println("Face Width: " + String.valueOf((int) (width * box.getWidth())));
               System.out.println("Face Height: " + String.valueOf((int) (height * box.getHeight())));
               System.out.println();
   
           }
   
           // Create frame and panel.
           JFrame frame = new JFrame("RotateImage");
           frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
           DisplayFaces panel = new DisplayFaces(result, image);
           panel.setPreferredSize(new Dimension(image.getWidth() / scale, image.getHeight() / scale));
           frame.setContentPane(panel);
           frame.pack();
           frame.setVisible(true);
   
       }
   }
   ```

------
#### [ Python ]

   ```
   import boto3
   import io
   from PIL import Image, ImageDraw, ExifTags, ImageColor
   
   def show_faces(photo,bucket):
        
   
       client=boto3.client('rekognition')
   
       # Load image from S3 bucket
       s3_connection = boto3.resource('s3')
       s3_object = s3_connection.Object(bucket,photo)
       s3_response = s3_object.get()
   
       stream = io.BytesIO(s3_response['Body'].read())
       image=Image.open(stream)
       
       #Call DetectFaces 
       response = client.detect_faces(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
           Attributes=['ALL'])
   
       imgWidth, imgHeight = image.size  
       draw = ImageDraw.Draw(image)  
                       
   
       # calculate and display bounding boxes for each detected face       
       print('Detected faces for ' + photo)    
       for faceDetail in response['FaceDetails']:
           print('The detected face is between ' + str(faceDetail['AgeRange']['Low']) 
                 + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
           
           box = faceDetail['BoundingBox']
           left = imgWidth * box['Left']
           top = imgHeight * box['Top']
           width = imgWidth * box['Width']
           height = imgHeight * box['Height']
                   
   
           print('Left: ' + '{0:.0f}'.format(left))
           print('Top: ' + '{0:.0f}'.format(top))
           print('Face Width: ' + "{0:.0f}".format(width))
           print('Face Height: ' + "{0:.0f}".format(height))
   
           points = (
               (left,top),
               (left + width, top),
               (left + width, top + height),
               (left , top + height),
               (left, top)
   
           )
           draw.line(points, fill='#00d400', width=2)
   
           # Alternatively can draw rectangle. However you can't set line width.
           #draw.rectangle([left,top, left + width, top + height], outline='#00d400') 
   
       image.show()
   
       return len(response['FaceDetails'])
   
   def main():
       bucket="bucket"
       photo="photo"
   
       faces_count=show_faces(photo,bucket)
       print("faces detected: " + str(faces_count))
   
   
   if __name__ == "__main__":
       main()
   ```

------