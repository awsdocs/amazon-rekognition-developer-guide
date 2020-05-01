# CustomLabel<a name="API_CustomLabel"></a>

A custom label detected in an image by a call to [DetectCustomLabels](API_DetectCustomLabels.md)\.

## Contents<a name="API_CustomLabel_Contents"></a>

 **Confidence**   <a name="rekognition-Type-CustomLabel-Confidence"></a>
The confidence that the model has in the detection of the custom label\. The range is 0\-100\. A higher value indicates a higher confidence\.  
Type: Float  
Valid Range: Minimum value of 0\. Maximum value of 100\.  
Required: No

 **Geometry**   <a name="rekognition-Type-CustomLabel-Geometry"></a>
The location of the detected object on the image that corresponds to the custom label\. Includes an axis aligned coarse bounding box surrounding the object and a finer grain polygon for more accurate spatial information\.  
Type: [Geometry](API_Geometry.md) object  
Required: No

 **Name**   <a name="rekognition-Type-CustomLabel-Name"></a>
The name of the custom label\.  
Type: String  
Required: No

## See Also<a name="API_CustomLabel_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CustomLabel) 
+  [AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/CustomLabel) 
+  [AWS SDK for Java](https://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/CustomLabel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CustomLabel) 