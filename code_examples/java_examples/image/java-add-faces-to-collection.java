//Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
//PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

package aws.example.rekognition.image;
import com.amazonaws.services.rekognition.AmazonRekognition;
import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
import com.amazonaws.services.rekognition.model.FaceRecord;
import com.amazonaws.services.rekognition.model.Image;
import com.amazonaws.services.rekognition.model.IndexFacesRequest;
import com.amazonaws.services.rekognition.model.IndexFacesResult;
import com.amazonaws.services.rekognition.model.S3Object;
import java.util.List;


public class AddFacesToCollection {
   public static final String collectionId = "MyCollection";
   public static final String bucket = "bucket";
   public static final String photo = "input.jpg";

   public static void main(String[] args) throws Exception {

      AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();

         
      Image image=new Image()
              .withS3Object(new S3Object()
                      .withBucket(bucket)
                      .withName(photo));
      
      
      
      IndexFacesRequest indexFacesRequest = new IndexFacesRequest()
              .withImage(image)
              .withCollectionId(collectionId)
              .withExternalImageId(photo)
              .withDetectionAttributes("ALL");
      
      IndexFacesResult indexFacesResult=rekognitionClient.indexFaces(indexFacesRequest);
      
     
      System.out.println(photo + " added");
      List < FaceRecord > faceRecords = indexFacesResult.getFaceRecords();
      for (FaceRecord faceRecord: faceRecords) {
         System.out.println("Face detected: Faceid is " +
            faceRecord.getFace().getFaceId());
      }
   } 
}
      
    

    

