# ComparedSourceImageFace<a name="API_ComparedSourceImageFace"></a>

Type that describes the face Amazon Rekognition chose to compare with the faces in the target\. This contains a bounding box for the selected face and confidence level that the bounding box contains a face\. Note that Amazon Rekognition selects the largest face in the source image for this comparison\. 

## Contents<a name="API_ComparedSourceImageFace_Contents"></a>

 **BoundingBox**   <a name="rekognition-Type-ComparedSourceImageFace-BoundingBox"></a>
Bounding box of the face\.  
Type: [BoundingBox](API_BoundingBox.md) object  
Required: No

 **Confidence**   <a name="rekognition-Type-ComparedSourceImageFace-Confidence"></a>
Confidence level that the selected bounding box contains a face\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

## See Also<a name="API_ComparedSourceImageFace_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ComparedSourceImageFace) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/ComparedSourceImageFace) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/ComparedSourceImageFace) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/ComparedSourceImageFace) 