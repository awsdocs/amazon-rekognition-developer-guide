# FaceRecord<a name="API_FaceRecord"></a>

Object containing both the face metadata \(stored in the backend database\), and facial attributes that are detected but aren't stored in the database\.

## Contents<a name="API_FaceRecord_Contents"></a>

 ** Face **   <a name="rekognition-Type-FaceRecord-Face"></a>
Describes the face properties such as the bounding box, face ID, image ID of the input image, and external image ID that you assigned\.   
Type: [ Face ](API_Face.md) object  
Required: No

 ** FaceDetail **   <a name="rekognition-Type-FaceRecord-FaceDetail"></a>
Structure containing attributes of the face that the algorithm detected\.  
Type: [ FaceDetail ](API_FaceDetail.md) object  
Required: No

## See Also<a name="API_FaceRecord_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:
+  [ AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/FaceRecord) 
+  [ AWS SDK for Go](https://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/FaceRecord) 
+  [ AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/FaceRecord) 
+  [ AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/FaceRecord) 