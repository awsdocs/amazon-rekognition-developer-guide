# Getting Information about a Celebrity<a name="get-celebrity-info-procedure"></a>

In these procedures, you get celebrity information by using the [GetCelebrityInfo](API_GetCelebrityInfo.md) API operation\. The celebrity is identified by using the celebrity ID returned from a previous call to `RecognizeCelebrities`\. 

## Prerequisites<a name="get-celebrity-info-prerequisites"></a>

To run these procedures, you need to have the AWS CLI and AWS SDK for Java installed\. For more information, see [Getting Started with Amazon Rekognition](getting-started.md)\. The AWS account you use must have access permissions to the Amazon Rekognition API\. For more information, see [Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference](api-permissions-reference.md)\.

These procedures also require the celebrity ID for a celebrity that Rekognition knows\. Use the celebrity ID you note in [Recognizing Celebrities in an Image](celebrities-procedure-image.md)\. 

## <a name="to-get-celebrity-information-cli"></a>

**To get celebrity information \(AWS CLI\)**

1. On the command line, type the following command\. Replace `ID` with one of the celebrity IDs displayed in [Recognizing Celebrities in an Image](celebrities-procedure-image.md)\.

   ```
   aws rekognition get-celebrity-info --id ID
   ```

1. To run the command, choose **Enter**\. The JSON output for the `GetCelebrityInfo` API operation is displayed\.

## <a name="to-get-celebrity-information-sdk"></a>

**To get celebrity information \(SDK\)**

1. Use the following AWS SDK for Java example code to get information about a celebrity that Amazon Rekognition recognized in an image\. Replace `ID` with one of the celebrity IDs displayed in [Recognizing Celebrities in an Image](celebrities-procedure-image.md)\.

   ```
   import com.amazonaws.AmazonClientException;
   import com.amazonaws.auth.AWSCredentials;
   import com.amazonaws.auth.AWSStaticCredentialsProvider;
   import com.amazonaws.auth.profile.ProfileCredentialsProvider;
   import com.amazonaws.regions.Regions;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.GetCelebrityInfoRequest;
   import com.amazonaws.services.rekognition.model.GetCelebrityInfoResult;
   
   public class CelebrityInfo {
   
      public static void main(String[] args) {
         String id = "ID";
   
         AWSCredentials credentials;
         try {
            credentials = new ProfileCredentialsProvider("AdminUser").getCredentials();
         } catch (Exception e) {
            throw new AmazonClientException("Cannot load the credentials from the credential profiles file. "
               + "Please make sure that your credentials file is at the correct "
               + "location (/Users/userid>.aws/credentials), and is in valid format.", e);
         }
   
         AmazonRekognition amazonRekognition = AmazonRekognitionClientBuilder
                 .standard()
                 .withRegion(Regions.US_WEST_2)
                 .withCredentials(new AWSStaticCredentialsProvider(credentials))
                 .build();
   
   
         GetCelebrityInfoRequest request = new GetCelebrityInfoRequest()
            .withId(id);
   
         System.out.println("Getting information for celebrity: " + id);
   
         GetCelebrityInfoResult result=amazonRekognition.getCelebrityInfo(request);
   
         //Display celebrity information
         System.out.println("celebrity name: " + result.getName());
         System.out.println("Further information (if available):");
         for (String url: result.getUrls()){
            System.out.println(url);
         }
      }
   }
   ```

1. Run the example code\. The celebrity name and information about the celebrity, if it is available, is displayed\.