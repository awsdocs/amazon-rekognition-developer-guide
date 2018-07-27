#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

if __name__ == "__main__":

    bucket='bucket'
    collectionId='MyCollection'
    threshold = 50
    maxFaces=2
    faceId='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

    client=boto3.client('rekognition')

  
    response=client.search_faces(CollectionId=collectionId,
                                FaceId=faceId,
                                FaceMatchThreshold=threshold,
                                MaxFaces=maxFaces)

                        
    faceMatches=response['FaceMatches']
    print 'Matching faces'
    for match in faceMatches:
            print 'FaceId:' + match['Face']['FaceId']
            print 'Similarity: ' + "{:.2f}".format(match['Similarity']) + "%"
            print

