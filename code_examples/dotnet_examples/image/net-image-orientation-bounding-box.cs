//Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
//PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

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