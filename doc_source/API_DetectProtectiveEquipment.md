# DetectProtectiveEquipment<a name="API_DetectProtectiveEquipment"></a>

Detects Personal Protective Equipment \(PPE\) worn by people detected in an image\. Amazon Rekognition can detect the following types of PPE\.
+ Face cover
+ Hand cover
+ Head cover

You pass the input image as base64\-encoded image bytes or as a reference to an image in an Amazon S3 bucket\. The image must be either a PNG or JPG formatted file\. 

 `DetectProtectiveEquipment` detects PPE worn by up to 15 persons detected in an image\.

For each person detected in the image the API returns an array of body parts \(face, head, left\-hand, right\-hand\)\. For each body part, an array of detected items of PPE is returned, including an indicator of whether or not the PPE covers the body part\. The API returns the confidence it has in each detection \(person, PPE, body part and body part coverage\)\. It also returns a bounding box \([BoundingBox](API_BoundingBox.md)\) for each detected person and each detected item of PPE\. 

You can optionally request a summary of detected PPE items with the `SummarizationAttributes` input parameter\. The summary provides the following information\. 
+ The persons detected as wearing all of the types of PPE that you specify\.
+ The persons detected as not wearing all of the types PPE that you specify\.
+ The persons detected where PPE adornment could not be determined\. 

This is a stateless API operation\. That is, the operation does not persist any data\.

This operation requires permissions to perform the `rekognition:DetectProtectiveEquipment` action\. 

## Request Syntax<a name="API_DetectProtectiveEquipment_RequestSyntax"></a>

```
{
   "Image": { 
      "Bytes": blob,
      "S3Object": { 
         "Bucket": "string",
         "Name": "string",
         "Version": "string"
      }
   },
   "SummarizationAttributes": { 
      "MinConfidence": number,
      "RequiredEquipmentTypes": [ "string" ]
   }
}
```

## Request Parameters<a name="API_DetectProtectiveEquipment_RequestParameters"></a>

The request accepts the following data in JSON format\.

 ** [Image](#API_DetectProtectiveEquipment_RequestSyntax) **   <a name="rekognition-DetectProtectiveEquipment-request-Image"></a>
The image in which you want to detect PPE on detected persons\. The image can be passed as image bytes or you can reference an image stored in an Amazon S3 bucket\.   
Type: [Image](API_Image.md) object  
Required: Yes

 ** [SummarizationAttributes](#API_DetectProtectiveEquipment_RequestSyntax) **   <a name="rekognition-DetectProtectiveEquipment-request-SummarizationAttributes"></a>
An array of PPE types that you want to summarize\.  
Type: [ProtectiveEquipmentSummarizationAttributes](API_ProtectiveEquipmentSummarizationAttributes.md) object  
Required: No

## Response Syntax<a name="API_DetectProtectiveEquipment_ResponseSyntax"></a>

```
{
   "Persons": [ 
      { 
         "BodyParts": [ 
            { 
               "Confidence": number,
               "EquipmentDetections": [ 
                  { 
                     "BoundingBox": { 
                        "Height": number,
                        "Left": number,
                        "Top": number,
                        "Width": number
                     },
                     "Confidence": number,
                     "CoversBodyPart": { 
                        "Confidence": number,
                        "Value": boolean
                     },
                     "Type": "string"
                  }
               ],
               "Name": "string"
            }
         ],
         "BoundingBox": { 
            "Height": number,
            "Left": number,
            "Top": number,
            "Width": number
         },
         "Confidence": number,
         "Id": number
      }
   ],
   "ProtectiveEquipmentModelVersion": "string",
   "Summary": { 
      "PersonsIndeterminate": [ number ],
      "PersonsWithoutRequiredEquipment": [ number ],
      "PersonsWithRequiredEquipment": [ number ]
   }
}
```

## Response Elements<a name="API_DetectProtectiveEquipment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response\.

The following data is returned in JSON format by the service\.

 ** [Persons](#API_DetectProtectiveEquipment_ResponseSyntax) **   <a name="rekognition-DetectProtectiveEquipment-response-Persons"></a>
An array of persons detected in the image \(including persons not wearing PPE\)\.  
Type: Array of [ProtectiveEquipmentPerson](API_ProtectiveEquipmentPerson.md) objects

 ** [ProtectiveEquipmentModelVersion](#API_DetectProtectiveEquipment_ResponseSyntax) **   <a name="rekognition-DetectProtectiveEquipment-response-ProtectiveEquipmentModelVersion"></a>
The version number of the PPE detection model used to detect PPE in the image\.  
Type: String

 ** [Summary](#API_DetectProtectiveEquipment_ResponseSyntax) **   <a name="rekognition-DetectProtectiveEquipment-response-Summary"></a>
Summary information for the types of PPE specified in the `SummarizationAttributes` input parameter\.  
Type: [ProtectiveEquipmentSummary](API_ProtectiveEquipmentSummary.md) object

## Errors<a name="API_DetectProtectiveEquipment_Errors"></a>

 **AccessDeniedException**   
You are not authorized to perform the action\.  
HTTP Status Code: 400

 **ImageTooLargeException**   
The input image size exceeds the allowed limit\. If you are calling [DetectProtectiveEquipment](#API_DetectProtectiveEquipment), the image size or resolution exceeds the allowed limit\. For more information, see [Limits in Amazon Rekognition](limits.md)\.   
HTTP Status Code: 400

 **InternalServerError**   
Amazon Rekognition experienced a service issue\. Try your call again\.  
HTTP Status Code: 500

 **InvalidImageFormatException**   
The provided image format is not supported\.   
HTTP Status Code: 400

 **InvalidParameterException**   
Input parameter violated a constraint\. Validate your parameter before calling the API operation again\.  
HTTP Status Code: 400

 **InvalidS3ObjectException**   
Amazon Rekognition is unable to access the S3 object specified in the request\.  
HTTP Status Code: 400

 **ProvisionedThroughputExceededException**   
The number of requests exceeded your throughput limit\. If you want to increase this limit, contact Amazon Rekognition\.  
HTTP Status Code: 400

 **ThrottlingException**   
Amazon Rekognition is temporarily unable to process the request\. Try your call again\.  
HTTP Status Code: 500

## See Also<a name="API_DetectProtectiveEquipment_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS Command Line Interface](https://docs.aws.amazon.com/goto/aws-cli/rekognition-2016-06-27/DetectProtectiveEquipment) 
+  [AWS SDK for \.NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/rekognition-2016-06-27/DetectProtectiveEquipment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DetectProtectiveEquipment) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/DetectProtectiveEquipment) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/DetectProtectiveEquipment) 
+  [AWS SDK for JavaScript](https://docs.aws.amazon.com/goto/AWSJavaScriptSDK/rekognition-2016-06-27/DetectProtectiveEquipment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DetectProtectiveEquipment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DetectProtectiveEquipment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DetectProtectiveEquipment) 