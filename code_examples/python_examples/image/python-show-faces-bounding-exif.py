#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

#Detect faces in an image. Rotates and diplays image according to estimated orientation, or, if available, EXIF information. 
import boto3
import io
from PIL import Image, ImageDraw, ExifTags

if __name__ == "__main__":

    photo='photo.jpg'

    left = 0
    top = 0
    estimated=False
    rotation='ROTATE_0'

    client=boto3.client('rekognition')

    #open image and get image data from stream.
    image = Image.open(open(photo,'rb'))
    stream = io.BytesIO()
    if 'exif' in image.info:
        exif=image.info['exif']
        image.save(stream,format=image.format, exif=exif)
    else:
        image.save(stream, format=image.format)    
    image_binary = stream.getvalue()
   
    response = client.detect_faces(Image={'Bytes': image_binary}, Attributes=['ALL'])

    #determine orientation based on exif or estimated orientation
    if 'OrientationCorrection'  in response:
        estimated =True
        rotation = response ['OrientationCorrection']
    else:
        estimated=False
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        exif=dict(image._getexif().items())
        if exif[orientation] == 1:
            rotation = 'ROTATE_0'
        if exif[orientation] == 3:
            rotation = 'ROTATE_180'
        elif exif[orientation] == 6:
            rotation='ROTATE_90'
        elif exif[orientation] == 8:
            rotation='ROTATE_270'

    # set up drawing canvas
    if rotation == 'ROTATE_0':
        rotatedImage=image.rotate(0, expand=True)
    if rotation == 'ROTATE_90':
        rotatedImage=image.rotate(270, expand=True) 
    if rotation == 'ROTATE_180':
       rotatedImage=image.rotate(180, expand=True)  
    if rotation == 'ROTATE_270':
        rotatedImage=image.rotate(90, expand=True)  
    width, height = rotatedImage.size  
    draw = ImageDraw.Draw(rotatedImage)  
                    

    # calulate and display bounding boxes for each detected face       
    print('Detected faces for ' + photo)    
    for faceDetail in response['FaceDetails']:
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low']) 
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
        box = faceDetail['BoundingBox']
        if estimated==True:

            if rotation == 'ROTATE_0':
                left = width * box['Left']
                top = height * box['Top']

            if rotation == 'ROTATE_90':
                left = height * (1 - (box['Top'] + box['Height']))
                top = width * box['Left']
         

            if rotation == 'ROTATE_180':
                left = width - (width * (box['Left'] + box['Width']))
                top = height * (1 - (box['Top'] + box['Height']))

            if rotation == 'ROTATE_270':
                left = height * box['Top']
                top = width * (1- box['Left'] - box['Width'] )
        else:
                left = width * box['Left']
                top = height * box['Top']
                

        print('Left: ' + '{0:.0f}'.format(left))
        print('Top: ' + '{0:.0f}'.format(top))
        print('Face Width: ' + "{0:.0f}".format(width * box['Width']))
        print('Face Height: ' + "{0:.0f}".format(height * box['Height']))
        
        draw.rectangle([left,top, left + (width * box['Width']), top +(height * box['Height'])]) 

    rotatedImage.show()

