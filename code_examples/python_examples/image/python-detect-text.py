#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

if __name__ == "__main__":

    bucket='bucket'
    photo='inputtext.jpg'

    client=boto3.client('rekognition')

  
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

                        
    textDetections=response['TextDetections']
    print response
   
    for text in textDetections:
            print 'Detected text:' + text['DetectedText']
            print 'Confidence: ' + "{:.2f}".format(text['Confidence']) + "%"
            print 'Id: {}'.format(text['Id'])
            if 'ParentId' in text:
                print 'Parent Id: {}'.format(text['ParentId'])
            print 'Type:' + text['Type']
            print

