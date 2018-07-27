#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

if __name__ == "__main__":

    bucket='bucket'
    collectionId='MyCollection'
    fileName='input.jpg'
    
    client=boto3.client('rekognition')

    response=client.index_faces

    response=client.index_faces(CollectionId=collectionId,
                                Image={'S3Object':{'Bucket':bucket,'Name':image}},
                                ExternalImageId=fileName,
                                DetectionAttributes=['ALL'])

    print ('Faces in ' + fileName) 							
    for faceRecord in response['FaceRecords']:
         print (faceRecord['Face']['FaceId'])

