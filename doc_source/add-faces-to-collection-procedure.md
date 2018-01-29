# Adding Faces to a Collection<a name="add-faces-to-collection-procedure"></a>

You can use the [IndexFaces](API_IndexFaces.md) operation to detect faces in an image and add them to a collection\. For each face detected, Amazon Rekognition extracts facial features and store the feature information in a database\. In addition, the command stores metadata for each face detected in the specified face collection\. 

The following procedures show how you can use the operation with the AWS CLI, the AWS SDK for Java\. 

For more information, see [Managing Collections](managing-collections.md)\. 

**To add faces to a collection \(AWS CLI\)**

1. Upload an image \(containing one or more faces\) to your S3 bucket\. 

   For instructions, see [Uploading Objects into Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. On the command line, type the following command\. Replace `bucket-name` and `file-name` with the S3 bucket name and image name that you used in step 1\. Replace `collection-id` with the name of the collection you want the face to be stored in\.

   ```
   aws rekognition index-faces \
         --image '{"S3Object":{"Bucket":"bucket-name","Name":"file-name"}}' \
         --collection-id "collection-id" \
         --detection-attributes "ALL" \
         --external-image-id "example-image.jpg" \
         --region us-east-1 \
         --profile adminuser
   ```

1. To run the command, choose **Enter**\. The JSON output for the `IndexFaces` operation is displayed\. 

**To add faces to a collection collection \(AWS SDK for Java\)**

+ To delete a collection, use the following AWS SDK for Java example code\.

  ```
  package com.amazonaws.samples;
  
  import java.util.List;
  import com.amazonaws.AmazonClientException;
  import com.amazonaws.auth.AWSCredentials;
  import com.amazonaws.auth.AWSStaticCredentialsProvider;
  import com.amazonaws.auth.profile.ProfileCredentialsProvider;
  import com.amazonaws.regions.Regions;
  import com.amazonaws.services.rekognition.AmazonRekognition;
  import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
  import com.amazonaws.services.rekognition.model.FaceRecord;
  import com.amazonaws.services.rekognition.model.Image;
  import com.amazonaws.services.rekognition.model.IndexFacesRequest;
  import com.amazonaws.services.rekognition.model.IndexFacesResult;
  import com.amazonaws.services.rekognition.model.S3Object;
  
  public class AddFaces {
     public static final String collectionId = "exampleCollection";
     public static final String bucket = "photo-label-detect";
     public static final String fileName = "filename.jpg";
  
     public static void main(String[] args) throws Exception {
        AWSCredentials credentials;
        try {
           credentials = new ProfileCredentialsProvider("AdminUser").getCredentials();
        } catch (Exception e) {
           throw new AmazonClientException(
              "Cannot load the credentials from the credential profiles file. " +
              "Please make sure that your credentials file is at the correct " +
              "location (/Users/userid/.aws/credentials), and is in valid format.",
              e);
        }
  
  
        AmazonRekognition amazonRekognition = AmazonRekognitionClientBuilder
           .standard()
           .withRegion(Regions.US_WEST_2)
           .withCredentials(new AWSStaticCredentialsProvider(credentials))
           .build();
  
           
        Image image=new Image()
                .withS3Object(new S3Object()
                        .withBucket(bucket)
                        .withName(fileName));
        
        
        
        IndexFacesRequest indexFacesRequest = new IndexFacesRequest()
                .withImage(image)
                .withCollectionId(collectionId)
                .withExternalImageId(fileName)
                .withDetectionAttributes("ALL");
        
        IndexFacesResult indexFacesResult=amazonRekognition.indexFaces(indexFacesRequest);
        
       
        System.out.println(fileName + " added");
        List < FaceRecord > faceRecords = indexFacesResult.getFaceRecords();
        for (FaceRecord faceRecord: faceRecords) {
           System.out.println("Face detected: Faceid is " +
              faceRecord.getFace().getFaceId());
        }
     }
  }
  ```