# Using Amazon Rekognition for Identity Verification<a name="identity-verification-tutorial"></a>

Amazon Rekognition provides users with several operations that enable the simple creation of identity verification systems\. Amazon Rekognition allows the user to detect faces in an image and then compare any detected faces to other faces by comparing face data\. This face data is stored in server\-side containers called Collections\. By making use of Amazon Rekognition’s face detection, face comparison, and collection management operations, you can create an application with an identity verification solution\.

This tutorial will demonstrate two common workflows for the creation of applications requiring identity verification\.

The first workflow involves the registration of a new user in a collection\. The second workflow involves searching an existing collection for the purposes of logging in a returning user\.

You’ll use the [AWS SDK for Python](https://aws.amazon.com/sdk-for-python/) for this tutorial\. You can also see the AWS Documentation SDK examples [GitHub repo ](https://github.com/awsdocs/aws-doc-sdk-examples)for more Python tutorials\.



**Topics**
+ [Prerequisites](#tutorial-prerequisites)
+ [Creating a Collection](#tutorial-step1)
+ [New User Registration](#tutorial-step1.3.1)
+ [Existing User Login](#tutorial-step1.4)

## Prerequisites<a name="tutorial-prerequisites"></a>

Before you begin this tutorial, you’ll need install Python and complete the steps required to [set up the Python AWS SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)\. Beyond this, ensure that you have:
+ [Created an AWS account and an IAM role](https://docs.aws.amazon.com/rekognition/latest/dg/setting-up.html)
+ [Installed the Python SDK \(Boto3\)](https://aws.amazon.com/sdk-for-python/)
+ [Properly configured your AWS access credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
+ [Created a Amazon Simple Storage Service bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) and uploaded an image you wish to use as an ID for the purposes of Identity Verification\.
+ Have selected a second image to to serve as the target image for identity verification\.

## Creating a Collection<a name="tutorial-step1"></a>

Before you can register a new user in a Collection or search a Collection for a user, you have to have a Collection to work with\. An Amazon Rekognition Collection is a server\-side container used to store information about detected faces\.



### Create the Collection<a name="tutorial-step1.2"></a>

You’ll start by writing a function that creates a Collection for use by your application\. Amazon Rekognition stores information about faces that have been detected in server\-side containers called Collections\. You can search facial information stored in a Collection for known faces\. To store facial information, you first need to create a Collection using the `CreateCollection` operation\.

1. Select a name for the Collection that you would like to create\. In the following code, replace the value of `collection_id` with the name of the Collection you’d like to create, and replace the value of `region` with the name of the region defined in your user credentials\. You can use the `Tags` argument to apply any tags you would like to the collection, although this isn’t required\. The `CreateCollection` operation will return information about the collection you have created, including the Arn of the collection\. Make a note of the Arn that you receive as a result of running the code\.

   ```
   import boto3
   
   def create_collection(collection_id, region):
       client = boto3.client('rekognition', region_name=region)
   
       # Create a collection
       print('Creating collection:' + collection_id)
       response = client.create_collection(CollectionId=collection_id, 
       Tags={"SampleKey1":"SampleValue1"})
       print('Collection ARN: ' + response['CollectionArn'])
       print('Status code: ' + str(response['StatusCode']))
       print('Done...')
   
   collection_id = 'collection-id-name'
   region = "region-name"
   create_collection(collection_id, region)
   ```

1. Save and run the code\. Copy down the collection Arn\.

   Now that the Rekognition Collection has been created, you can store facial information and identifiers in that Collection\. You will also be able to compare faces against the stored information for verification\. 

### <a name="tutorial-step1.3"></a>

## New User Registration<a name="tutorial-step1.3.1"></a>

You’ll want to be able to register new users and add their info to a Collection\. The process of registering a new user typically involves the following steps:    Checking to see if an input image \(typically captured by a camera\) matches a reference image using `CompareFaces`\. In this tutorial, you’ll use a local image as the input/target image and the image in your Amazon S3 bucket as a reference image\.   Search your Collection for a potential match to ensure that the new user isn’t already registered using `SearchFacesByImage`\.   If the user isn’t already in the Collection, register the face found in the input image in your collection using `IndexFaces`\.   Store the input image data and the `FaceID` data in Amazon S3 and DynamoDB, respectively\.   

### Call the `DetectFaces` Operation<a name="tutorial-step1.3.2"></a>

Write the code to check the quality of the face image via the `DetectFaces` operation\. You’ll use the `DetectFaces` operation to determine if an image captured by the camera is suitable for processing by the `SearchFacesByImage` operation\. The image should contain only one face\. You’ll provide a local input image file to the `DetectFaces` operation and receive details for the faces detected in the image\. The following sample code provides the input image to `DetectFaces` and then checks to see if only one face has been detected in the image\.

1. In the following code example, replace `photo` with the name of the target image in which you’d like to detect faces\. You’ll also need to replace the value of `region` with the name of the region associated with your account\.

   ```
   import boto3
   import json
   
   def detect_faces(target_file, region):
   
       client=boto3.client('rekognition', region_name=region)
   
       imageTarget = open(target_file, 'rb')
   
       response = client.detect_faces(Image={'Bytes': imageTarget.read()}, 
       Attributes=['ALL'])
   
       print('Detected faces for ' + photo)
       for faceDetail in response['FaceDetails']:
           print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
                 + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
   
           print('Here are the other attributes:')
           print(json.dumps(faceDetail, indent=4, sort_keys=True))
   
           # Access predictions for individual face details and print them
           print("Gender: " + str(faceDetail['Gender']))
           print("Smile: " + str(faceDetail['Smile']))
           print("Eyeglasses: " + str(faceDetail['Eyeglasses']))
           print("Emotions: " + str(faceDetail['Emotions'][0]))
   
       return len(response['FaceDetails'])
   
   photo = 'photo-name'
   region = 'region-name'
   face_count=detect_faces(photo, region)
   print("Faces detected: " + str(face_count))
   
   if face_count == 1:
       print("Image suitable for use in collection.")
   else:
       print("Please submit an image with only one face.")
   ```

1. Save and run the proceeding code\.

### Call the `CompareFaces` Operation<a name="tutorial-step1.3.3"></a>

Your application will need to be able to register new users in a Collection and confirm the identity of returning users\. You will create the functions used to register a new user first\. You’ll start by using the `CompareFaces` operation to compare a local input/target image of the user and a ID/stored image\. If there is a match between the face detected in both images, you can search through the Collection to see if the user has been registered in it\. 

Start by writing a function that compares an input image to the ID image you have stored in your Amazon S3 bucket\. In the following code example, you will need to provide the input image yourself, which should be captured after using some form of liveness detector\. You will also need to pass the name of an image stored in your Amazon S3 bucket\. 

1. Replace the value of `bucket` with the name of the Amazon S3 bucket containing your source file\. You will also need to replace the value of `source_file` with the name of the source image you are using\. Replace the value of `target_file` with the name of the target file you have provided\. Replace the value of `region` with the name of the `region` defined in your user credentials\.

   You will also want to specify a minimum confidence level in the match that is returned in the response, using the `similarityThreshold` argument\. Detected faces will only be returned in the `FaceMatches` array if the confidence is above this threshold\. Your chosen `similarityThreshold` should reflect the nature of your specific use case\. Any use case involving critical security applications should use 99 as the selected threshold\.

   ```
   import boto3
   
   def compare_faces(bucket, sourceFile, targetFile, region):
       client = boto3.client('rekognition', region_name=region)
   
       imageTarget = open(targetFile, 'rb')
   
       response = client.compare_faces(SimilarityThreshold=99,
                                       SourceImage={'S3Object':{'Bucket':bucket,'Name':sourceFile}},
                                       TargetImage={'Bytes': imageTarget.read()})
   
       for faceMatch in response['FaceMatches']:
           position = faceMatch['Face']['BoundingBox']
           similarity = str(faceMatch['Similarity'])
           print('The face at ' +
                 str(position['Left']) + ' ' +
                 str(position['Top']) +
                 ' matches with ' + similarity + '% confidence')
   
       imageTarget.close()
       return len(response['FaceMatches'])
   
   bucket = 'bucket-name'
   source_file = 'source-file-name'
   target_file = 'target-file-name'
   region = "region-name"
   face_matches = compare_faces(bucket, source_file, target_file, region)
   print("Face matches: " + str(face_matches))
   
   if str(face_matches) == "1":
       print("Face match found.")
   else:
       print("No face match found.")
   ```

1. Save and run the proceeding code\.

   You will be returned a response object containing information about the matched face and the confidence level\.

### Call the `SearchFacesByImage` Operation<a name="tutorial-step1.3.4"></a>

If the confidence level of the `CompareFaces` operation is above your chosen `SimilarityThreshold`, you’ll want to search your Collection for a face that might match the input image\. If a match is found in your collection, that means the user is likely already registered in the Collection and there isn’t a need to register a new user in your Collection\. If there isn’t a match, you can register the new user in your Collection\.

1. Start by writing the code that will invoke the `SearchFacesByImage` operation\. The operation will take in a local image file as an argument and then search your `Collection` for a face that matches the largest detected faces in the provided image\. 

   In the following code example, change the value of `collectionId` to the Collection that you want to search\. Replace the value of `region` with the name of the region associated with your account\. You’ll also need to replace the value of `photo` with the name of the your input file\. You will also want to specify a similarity threshold by replacing the value of `threshold` with a chosen percentile\. 

   ```
   import boto3
   
   collectionId = 'collection-id-name'
   region = "region-name"
   photo = 'photo-name'
   threshold = 99
   maxFaces = 1
   client = boto3.client('rekognition', region_name=region)
   
   # input image should be local file here, not s3 file
   with open(photo, 'rb') as image:
       response = client.search_faces_by_image(CollectionId=collectionId,
       Image={'Bytes': image.read()},
       FaceMatchThreshold=threshold, MaxFaces=maxFaces)
   
   faceMatches = response['FaceMatches']
   print(faceMatches)
   
   for match in faceMatches:
       print('FaceId:' + match['Face']['FaceId'])
       print('ImageId:' + match['Face']['ImageId'])
       print('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
       print('Confidence: ' + str(match['Face']['Confidence']))
   ```

1. Save and run the proceeding code\. If there’s been a match, it means the person recognized in the image is already part of the Collection and there’s no need to go on to the next steps\. In this case, you can just allow the user access to the application\.

### Call the `IndexFaces` Operation<a name="tutorial-step1.3.5"></a>

Assuming that no match was found in the Collection you searched, you will want to add the face of the user to your collection\. You do this by calling the `IndexFaces` operation\. When you call IndexFaces, Amazon Rekognition extracts the facial features of a face identified in your input image, storing the data in the specified collection\.

1. Begin by writing the code to call `IndexFaces`\. Replace the value of `image` with the name of the local file you want to use as an input image for the IndexFaces operation\. You will also need to replace the value of `photo_name` with the desired name for your input image\. Be sure to replace the value of `collection_id` with the ID of the collection you previously created\. Next, replace the value of `region` with the name of the region associated with your account\. You will also want to specify a value for the `MaxFaces` input parameter, which defines the maximum number of faces in an image that should be indexed\. The default value for this parameter is 1\. 

   ```
   import boto3
   
   def add_faces_to_collection(target_file, photo, collection_id, region):
       client = boto3.client('rekognition', region_name=region)
   
       imageTarget = open(target_file, 'rb')
   
       response = client.index_faces(CollectionId=collection_id,
                                     Image={'Bytes': imageTarget.read()},
                                     ExternalImageId=photo,
                                     MaxFaces=1,
                                     QualityFilter="AUTO",
                                     DetectionAttributes=['ALL'])
       print(response)
   
       print('Results for ' + photo)
       print('Faces indexed:')
       for faceRecord in response['FaceRecords']:
           print('  Face ID: ' + faceRecord['Face']['FaceId'])
           print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))
           print('  Image ID: {}'.format(faceRecord['Face']['ImageId']))
           print('  External Image ID: {}'.format(faceRecord['Face']['ExternalImageId']))
           print('  Confidence: {}'.format(faceRecord['Face']['Confidence']))
   
       print('Faces not indexed:')
       for unindexedFace in response['UnindexedFaces']:
           print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
           print(' Reasons:')
           for reason in unindexedFace['Reasons']:
               print('   ' + reason)
       return len(response['FaceRecords'])
   
   image = 'image-file-name'
   collection_id = 'collection-id-name'
   photo_name = 'desired-image-name'
   region = "region-name"
   
   indexed_faces_count = add_faces_to_collection(image, photo_name, collection_id, region)
   print("Faces indexed count: " + str(indexed_faces_count))
   ```

1. Save and run the proceeding code\. Determine if you would like to save any of the data returned by the `IndexFaces` operation, such as the FaceID assigned to the person in the image\. The next section will examine how to save this data\. Copy down the returned `FaceId`, `ImageId`, and `Confidence` values before proceeding\.

### Store Image and FaceID Data in Amazon S3 and Amazon DynamoDB<a name="tutorial-step1.3.6"></a>

Once the Face ID for the input image has been obtained, the image data can be saved in Amazon S3, while the face data and image URL can be entered into a database like DynamoDB\. 

1. Write the code to upload the input image to your Amazon S3 database\. In the code sample that follows, replace the value of `bucket` with the name of the bucket to which you’d like to upload the file, then replace the value of `file_name` with the name of the local file you want to store in your Amazon S3 bucket\. Provide a key name that will identify the file in the Amazon S3 bucket by replacing the value of `key_name` with a name you’d like to give the image file\. The file you want to upload is the same one that was defined in earlier code samples, which is the input file you used for IndexFaces\. Finally, replace the value of `region` with the name of the region associated with your account\.

   ```
   import boto3
   import logging
   from botocore.exceptions import ClientError
   
   # store local file in S3 bucket
   bucket = "bucket-name"
   file_name = "file-name"
   key_name = "key-name"
   region = "region-name"
   s3 = boto3.client('s3', region_name=region)
   # Upload the file
   try:
       response = s3.upload_file(file_name, bucket, key_name)
       print("File upload successful!")
   except ClientError as e:
       logging.error(e)
   ```

1. Save and run the proceeding code sample to upload your input image to Amazon Amazon S3\.

1. You’ll want to save the returned Face ID to a database as well\. This can be done by creating a DynamoDB database table and then uploading the Face ID to that table\. The following code sample creates a DynamoDB table\. Note that you only need to run the code that creates this table once\. In the following code, replace the value of `region` with the value of the region associated with your account\. You will also need to replace the value of `database_name` with the name that you’d like to give the DynamoDB table\.

   ```
   import boto3
   
   # Create DynamoDB database with image URL and face data, face ID
   
   def create_dynamodb_table(table_name, region):
       dynamodb = boto3.client("dynamodb", region_name=region)
   
       table = dynamodb.create_table(
           TableName=table_name,   
           KeySchema=[{
                   'AttributeName': 'FaceID', 'KeyType': 'HASH'  # Partition key  
                   },],        
               AttributeDefinitions=[
               {
                   'AttributeName': 'FaceID', 'AttributeType': 'S'  }, ],        
                   ProvisionedThroughput={
               'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10  }
       )
       print(table)
       return table
   
   region = "region-name"
   database_name = 'database-name'
   dynamodb_table = create_dynamodb_table(database_name, region)
   print("Table status:", dynamodb_table)
   ```

1. Save and run the proceeding code to create your table\.

1. After creating the table, you can upload the returned FaceId to it\. To do this, you’ll establish a connection to the table with the Table function and then use the `put_item` function to upload the data\. 

   In the following code sample, replace the value of `bucket` with the name of the bucket containing the input image you uploaded to Amazon S3\. You’ll also need to replace the value of` file_name` with the name of the input file you uploaded to your Amazon S3 bucket and the value of `key_name` with the key that you previously used to identify the input file\. Finally, replace the value of `region` with the name of the region associated with your account\. These values should match the ones provided in step 1\.

   The `AddDBEntry` stores the FaceId, ImageId, and Confidence values assigned to a face in a collection\. Provide the function below with the values that you saved during Step 2 of the proceeding `IndexFaces` section\.

   ```
   import boto3
   from pprint import pprint
   from decimal import Decimal
   import json
   
   # The local file that was stored in S3 bucket
   bucket = "s3-bucket-name"
   file_name = "file-name"
   key_name = "key-name"
   region = "region-name"
   # Get URL of file
   file_url = "https://s3.amazonaws.com/{}/{}".format(bucket, key_name)
   print(file_url)
   
   # upload face-id, face info, and image url
   def AddDBEntry(file_name, file_url, face_id, image_id, confidence):
       dynamodb = boto3.resource('dynamodb', region_name=region)
       table = dynamodb.Table('FacesDB-4')
       response = table.put_item(
          Item={
               'ExternalImageID': file_name,
               'ImageURL': file_url,
               'FaceID': face_id,
               'ImageID': image_id, 
               'Confidence': json.loads(json.dumps(confidence), parse_float=Decimal)
          }
       )
       return response
   
   # Mock values for face ID, image ID, and confidence - replace them with actual values from your collection results
   dynamodb_resp = AddDBEntry(file_name, file_url, "FACE-ID-HERE",  
       "IMAGE-ID-HERE", confidence-here)
   print("Database entry successful.")
   pprint(dynamodb_resp, sort_dicts=False)
   ```

1.  Save and run the proceeding code sample to store the returned Face ID data in a table\.

## Existing User Login<a name="tutorial-step1.4"></a>

After a user has been registered in a Collection, they can be authenticated upon their return by using the `SearchFacesByImage` operation\. You will need to get an input image and then check the quality of the input image using `DetectFaces`\. This determines if a suitable image has been used before running the `SearchFacesbyImage` operation\.

### Call the DetectFaces Operation<a name="tutorial-step1.4.1"></a>

1. You’ll use the `DetectFaces` operation to check the quality of the face image and determine if an image captured by the camera is suitable for processing by the `SearchFacesByImage` operation\. The input image should contain just one face\. The following code sample takes an input image and provides it to the `DetectFaces` operation\.

   In the following code example, replace the value of `photo` with the name of the local target image and replace the value of `region` with the name of the region associated with your account\.

   ```
   import boto3
   import json
   
   def detect_faces(target_file, region):
   
       client=boto3.client('rekognition', region_name=region)
   
       imageTarget = open(target_file, 'rb')
   
       response = client.detect_faces(Image={'Bytes': imageTarget.read()}, 
       Attributes=['ALL'])
   
       print('Detected faces for ' + photo)
       for faceDetail in response['FaceDetails']:
           print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
                 + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
   
           print('Here are the other attributes:')
           print(json.dumps(faceDetail, indent=4, sort_keys=True))
   
           # Access predictions for individual face details and print them
           print("Gender: " + str(faceDetail['Gender']))
           print("Smile: " + str(faceDetail['Smile']))
           print("Eyeglasses: " + str(faceDetail['Eyeglasses']))
           print("Emotions: " + str(faceDetail['Emotions'][0]))
   
       return len(response['FaceDetails'])
   
   photo = 'photo-name'
   region = 'region-name'
   face_count=detect_faces(photo, region)
   print("Faces detected: " + str(face_count))
   
   if face_count == 1:
       print("Image suitable for use in collection.")
   else:
       print("Please submit an image with only one face.")
   ```

1. Save and run the code\. 

### Call the SearchFacesByImage Operation<a name="tutorial-step1.4.2"></a>

1. Write the code to compare the detected face against the faces in the Collection with the `SearchFacesByImage`\. You'll use the code shown in the proceeding New User Registration section and provide the input image to the `SearchFacesByImage` operation\.

   In the following code example, change the value of `collectionId` to the collection that you want to search\. You will also change the value of `bucket` to the name of an Amazon S3 bucket and the value of `fileName` to an image file in that bucket\. Replace the value of `region` with the name of the region associated with your account\. You will also want to specify a similarity threshold by replacing the value of `threshold` with a chosen percentile\.

   ```
   import boto3
   
   bucket = 'bucket-name'
   collectionId = 'collection-id-name'
   region = "region-name"
   fileName = 'file-name'
   threshold = 70
   maxFaces = 1
   client = boto3.client('rekognition', region_name=region)
   
   # input image should be local file here, not s3 file
   with open(fileName, 'rb') as image:
       response = client.search_faces_by_image(CollectionId=collectionId,
       Image={'Bytes': image.read()},
       FaceMatchThreshold=threshold, MaxFaces=maxFaces)
   ```

1. Save and run the code\. 

### Check for the Returned FaceID and Confidence Level<a name="tutorial-step1.4.3"></a>

You can now check for information on the matched FaceId by printing out response elements like the FaceId, Similarity, and Confidence attributes\.

```
faceMatches = response['FaceMatches']
print(faceMatches)

for match in faceMatches:
    print('FaceId:' + match['Face']['FaceId'])
    print('ImageId:' + match['Face']['ImageId'])
    print('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
    print('Confidence: ' + str(match['Face']['Confidence']))
```