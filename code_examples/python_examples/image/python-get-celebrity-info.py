#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

if __name__ == "__main__":

    id="nnnnnnnn"
    
    client=boto3.client('rekognition')

    #Display celebrity info
    print('Getting celebrity info for celebrity: ' + id)
    response=client.get_celebrity_info(Id=id)

    print (response['Name'])  
    print ('Further information (if available):')
    for url in response['Urls']:
        print (url) 
    
