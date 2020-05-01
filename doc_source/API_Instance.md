# Instance<a name="API_Instance"></a>

An instance of a label returned by Amazon Rekognition Image \([DetectLabels](API_DetectLabels.md)\) or by Amazon Rekognition Video \([GetLabelDetection](API_GetLabelDetection.md)\)\.

## Contents<a name="API_Instance_Contents"></a>

 **BoundingBox**   <a name="rekognition-Type-Instance-BoundingBox"></a>
The position of the label instance on the image\.  
Type: [BoundingBox](API_BoundingBox.md) object  
Required: No

 **Confidence**   <a name="rekognition-Type-Instance-Confidence"></a>
The confidence that Amazon Rekognition has in the accuracy of the bounding box\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

## See Also<a name="API_Instance_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/Instance) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/Instance) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/Instance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/Instance) 