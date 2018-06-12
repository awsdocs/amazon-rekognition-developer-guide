# Comparing Faces in Images \(SDK\)<a name="faces-compare-images"></a>

In this procedure you use the [CompareFaces](API_CompareFaces.md) operation to compare a face in the *source* image with each face detected in the *target* image\.

If you provide a source image containing multiple faces, the service detects the largest face and uses it to compare with each face detected in the target image\. 

In the response you get an array of face matches, source face information, source and target image orientation, and an array of unmatched faces\. For each matching face in the target image, the response provides a similarity score \(how similar the face is to the source face\) and face metadata such as the bounding box of the matching face and an array of facial landmarks\. The array of unmatched faces includes face metadata\. 

You can provide the source and target images as an image byte array \(Base64\-encoded image bytes\) or specify S3 objects\. In the AWS CLI exercise, you upload two JPEG images to your Amazon S3 bucket and specify the object key name\. In the Java exercise, you load two files from the local file system and input them as image byte arrays\.

The following examples show how you can use the operation with the AWS CLI, the AWS SDK for Java and the AWS SDK for Python \(Boto\)\. 

1. Upload two images \(source\.jpg and target\.jpg\) containing faces to your S3 bucket\. The exercise assume a \.jpg image\. If you use \.png, update the AWS CLI command accordingly\.

   For instructions, see [Uploading Objects into Amazon S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/UploadingObjectsintoAmazonS3.html) in the *Amazon Simple Storage Service Console User Guide*\.

1. Use the following example code to call the `CompareFaces` operation\.
   + Using AWS CLI

     ```
     aws rekognition compare-faces \
     --source-image '{"S3Object":{"Bucket":"bucket-name","Name":"source.jpg"}}' \
     --target-image '{"S3Object":{"Bucket":"bucket-name","Name":"target.jpg"}}' \
     --region us-east-1 \
     --profile adminuser
     ```
   + Using the AWS SDK for Java\. This example compares two images loaded from the local file system\. 

     ```
     package com.amazonaws.samples;
     
     import java.io.File;
     import java.io.FileInputStream;
     import java.io.InputStream;
     import java.nio.ByteBuffer;
     import java.util.List;
     
     import com.amazonaws.AmazonClientException;
     import com.amazonaws.auth.AWSCredentials;
     import com.amazonaws.auth.AWSStaticCredentialsProvider;
     import com.amazonaws.auth.profile.ProfileCredentialsProvider;
     import com.amazonaws.client.builder.AwsClientBuilder.EndpointConfiguration;
     import com.amazonaws.services.rekognition.AmazonRekognition;
     import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
     import com.amazonaws.services.rekognition.model.Image;
     import com.amazonaws.util.IOUtils;
     import com.amazonaws.services.rekognition.model.BoundingBox;
     import com.amazonaws.services.rekognition.model.CompareFacesMatch;
     import com.amazonaws.services.rekognition.model.CompareFacesRequest;
     import com.amazonaws.services.rekognition.model.CompareFacesResult;
     import com.amazonaws.services.rekognition.model.ComparedFace;
     
     
     public class CompareFacesExample {
     
        public static void main(String[] args) throws Exception{
            Float similarityThreshold = 70F;
            String sourceImage = "source.jpg";
            String targetImage = "target.jpg";
            ByteBuffer sourceImageBytes=null;
            ByteBuffer targetImageBytes=null;
     
     
            AWSCredentials credentials;
            try {
                credentials = new ProfileCredentialsProvider("AdminUser").getCredentials();
            } catch (Exception e) {
                throw new AmazonClientException("Cannot load the credentials from the credential profiles file. "
                        + "Please make sure that your credentials file is at the correct "
                        + "location (/Users/userid/.aws/credentials), and is in valid format.", e);
            }
     
            EndpointConfiguration endpoint=new EndpointConfiguration("endpoint",
                   "us-east-1");
     
             AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder
                    .standard()
                    .withEndpointConfiguration(endpoint)
                    .withCredentials(new AWSStaticCredentialsProvider(credentials))
                    .build();
     
     
            //Load source and target images and create input parameters
            try (InputStream inputStream = new FileInputStream(new File(sourceImage))) {
               sourceImageBytes = ByteBuffer.wrap(IOUtils.toByteArray(inputStream));
            }
            catch(Exception e)
            {
                System.out.println("Failed to load source image " + sourceImage);
                System.exit(1);
            }
            try (InputStream inputStream = new FileInputStream(new File(targetImage))) {
                targetImageBytes = ByteBuffer.wrap(IOUtils.toByteArray(inputStream));
            }
            catch(Exception e)
            {
                System.out.println("Failed to load target images: " + targetImage);
                System.exit(1);
            }
     
            Image source=new Image()
            		.withBytes(sourceImageBytes);
            Image target=new Image()
            		.withBytes(targetImageBytes);
     
            CompareFacesRequest request = new CompareFacesRequest()
                    .withSourceImage(source)
                    .withTargetImage(target)
                    .withSimilarityThreshold(similarityThreshold);
     
            // Call operation
            CompareFacesResult compareFacesResult=rekognitionClient.compareFaces(request);
     
     
            // Display results
            List <CompareFacesMatch> faceDetails = compareFacesResult.getFaceMatches();
            for (CompareFacesMatch match: faceDetails){
            	ComparedFace face= match.getFace();
            	BoundingBox position = face.getBoundingBox();
            	System.out.println("Face at " + position.getLeft().toString()
            			+ " " + position.getTop()
            			+ " matches with " + face.getConfidence().toString()
            			+ "% confidence.");
     
            }
            List<ComparedFace> uncompared = compareFacesResult.getUnmatchedFaces();
     
            System.out.println("There were " + uncompared.size()
            		+ " that did not match");
            System.out.println("Source image rotation: " + compareFacesResult.getSourceImageOrientationCorrection());
            System.out.println("target image rotation: " + compareFacesResult.getTargetImageOrientationCorrection());
        }
     }
     ```
   + Using AWS SDK for Python \(Boto\)\.

     ```
     import boto3
     
     if __name__ == "__main__":
     
         bucket='bucket-name'
         sourceFile='source.jpg'
         targetFile='target.jpg'
     
         client=boto3.client('rekognition','us-east-1')
     
         response=client.compare_faces(SimilarityThreshold=70,
                                       SourceImage={'S3Object':{'Bucket':bucket,'Name':sourceFile}},
                                       TargetImage={'S3Object':{'Bucket':bucket,'Name':targetFile}})
     
         for faceMatch in response['FaceMatches']:
             position = faceMatch['Face']['BoundingBox']
             confidence = str(faceMatch['Face']['Confidence'])
             print('The face at ' +
                    str(position['Left']) + ' ' +
                    str(position['Top']) +
                    ' matches with ' + confidence + '% confidence')
     ```