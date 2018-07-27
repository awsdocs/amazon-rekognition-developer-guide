#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import json

if __name__ == "__main__":
    photo='moviestars.jpg'
    
    client=boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.recognize_celebrities(Image={'Bytes': image.read()})

    print('Detected faces for ' + photo)    
    for celebrity in response['CelebrityFaces']:
        print 'Name: ' + celebrity['Name']
        print 'Id: ' + celebrity['Id']
        print 'Position:'
        print '   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height'])
        print '   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top'])
        print 'Info'
        for url in celebrity['Urls']:
            print '   ' + url
        print

        
