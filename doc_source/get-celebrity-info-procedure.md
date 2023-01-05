# Getting information about a celebrity<a name="get-celebrity-info-procedure"></a>

In these procedures, you get celebrity information by using the [getCelebrityInfo](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetCelebrityInfo.html) API operation\. The celebrity is identified by using the celebrity ID that's returned from a previous call to [RecognizeCelebrities](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RecognizeCelebrities.html)\. 

## Calling GetCelebrityInfo<a name="get-celebrity-info-examples"></a>



These procedures require the celebrity ID for a celebrity that Amazon Rekognition knows\. Use the celebrity ID that you note in [Recognizing celebrities in an image](celebrities-procedure-image.md)\. 

**To get celebrity information \(SDK\)**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` and `AmazonS3ReadOnlyAccess` permissions\. For more information, see [Step 1: Set up an AWS account and create an IAM user](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and AWS SDKs\. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Use the following examples to call the `GetCelebrityInfo` operation\.

------
#### [ Java ]

   This example displays the name and information about a celebrity\.

   Replace `id` with one of the celebrity IDs displayed in [Recognizing celebrities in an image](celebrities-procedure-image.md)\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   package aws.example.rekognition.image;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.GetCelebrityInfoRequest;
   import com.amazonaws.services.rekognition.model.GetCelebrityInfoResult;
   
   
   public class CelebrityInfo {
   
      public static void main(String[] args) {
         String id = "nnnnnnnn";
   
         AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
   
         GetCelebrityInfoRequest request = new GetCelebrityInfoRequest()
            .withId(id);
   
         System.out.println("Getting information for celebrity: " + id);
   
         GetCelebrityInfoResult result=rekognitionClient.getCelebrityInfo(request);
   
         //Display celebrity information
         System.out.println("celebrity name: " + result.getName());
         System.out.println("Further information (if available):");
         for (String url: result.getUrls()){
            System.out.println(url);
         }
      }
   }
   ```

------
#### [ Java V2 ]

   This code is taken from the AWS Documentation SDK examples GitHub repository\. See the full example [here](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/javav2/example_code/rekognition/src/main/java/com/example/rekognition/CelebrityInfo.java)\.

   ```
       public static void getCelebrityInfo(RekognitionClient rekClient, String id) {
   
           try {
               GetCelebrityInfoRequest info = GetCelebrityInfoRequest.builder()
                   .id(id)
                   .build();
   
               GetCelebrityInfoResponse response = rekClient.getCelebrityInfo(info);
               System.out.println("celebrity name: " + response.name());
               System.out.println("Further information (if available):");
               for (String url: response.urls()){
                   System.out.println(url);
               }
   
           } catch (RekognitionException e) {
               System.out.println(e.getMessage());
               System.exit(1);
           }
       }
   ```

------
#### [ AWS CLI ]

   This AWS CLI command displays the JSON output for the `get-celebrity-info` CLI operation\. Replace `ID` with one of the celebrity IDs displayed in [Recognizing celebrities in an image](celebrities-procedure-image.md)\.

   ```
   aws rekognition get-celebrity-info --id ID
   ```

------
#### [ Python ]

   This example displays the name and information about a celebrity\.

   Replace `id` with one of the celebrity IDs displayed in [Recognizing celebrities in an image](celebrities-procedure-image.md)\.

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   
   def get_celebrity_info(id):
   
    
       client=boto3.client('rekognition')
   
       #Display celebrity info
       print('Getting celebrity info for celebrity: ' + id)
       
       response=client.get_celebrity_info(Id=id)
   
       print (response['Name'])  
       print ('Further information (if available):')
       for url in response['Urls']:
           print (url) 
   
   def main():
       id="nnnnnnnn"
       celebrity_info=get_celebrity_info(id)
   
   
   
   if __name__ == "__main__":
       main()
   ```

------
#### [ \.NET ]

   This example displays the name and information about a celebrity\.

   Replace `id` with one of the celebrity IDs displayed in [Recognizing celebrities in an image](celebrities-procedure-image.md)\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   using System;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   
   public class CelebrityInfo
   {
       public static void Example()
       {
           String id = "nnnnnnnn";
   
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           GetCelebrityInfoRequest celebrityInfoRequest = new GetCelebrityInfoRequest()
           {
               Id = id
           };
   
           Console.WriteLine("Getting information for celebrity: " + id);
   
           GetCelebrityInfoResponse celebrityInfoResponse = rekognitionClient.GetCelebrityInfo(celebrityInfoRequest);
   
           //Display celebrity information
           Console.WriteLine("celebrity name: " + celebrityInfoResponse.Name);
           Console.WriteLine("Further information (if available):");
           foreach (String url in celebrityInfoResponse.Urls)
               Console.WriteLine(url);
       }
   }
   ```

------

## GetCelebrityInfo operation request<a name="getcelebrityinfo-operation-request"></a>

The following is example JSON input and output for `GetCelebrityInfo`\. 

The input to `GetCelebrityInfo` is the ID for the required celebrity\.

```
{
    "Id": "nnnnnnn"
}
```

## GetCelebrityInfo operation response<a name="getcelebrityinfo-operation-response"></a>

`GetCelebrityInfo` returns an array \(`Urls`\) of links to information about the requested celebrity\.

```
{
    "Name": "Celebrity Name",
    "Urls": [
        "www.imdb.com/name/nmnnnnnnn"
    ]
}
```