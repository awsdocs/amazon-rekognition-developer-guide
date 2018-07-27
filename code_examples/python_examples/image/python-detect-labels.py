#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

if __name__ == "__main__":
    fileName='input.jpg'
    bucket='bucket'
    
    client=boto3.client('rekognition')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':fileName}})

    print('Detected labels for ' + fileName)    
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
 
