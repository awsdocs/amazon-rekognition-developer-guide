# BoundingBox<a name="API_BoundingBox"></a>

Identifies the bounding box around the object, face or text\. The `left` \(x\-coordinate\) and `top` \(y\-coordinate\) are coordinates representing the top and left sides of the bounding box\. Note that the upper\-left corner of the image is the origin \(0,0\)\. 

The `top` and `left` values returned are ratios of the overall image size\. For example, if the input image is 700x200 pixels, and the top\-left coordinate of the bounding box is 350x50 pixels, the API returns a `left` value of 0\.5 \(350/700\) and a `top` value of 0\.25 \(50/200\)\.

The `width` and `height` values represent the dimensions of the bounding box as a ratio of the overall image dimension\. For example, if the input image is 700x200 pixels, and the bounding box width is 70 pixels, the width returned is 0\.1\. 

**Note**  
 The bounding box coordinates can have negative values\. For example, if Amazon Rekognition is able to detect a face that is at the image edge and is only partially visible, the service can return coordinates that are outside the image bounds and, depending on the image edge, you might get negative values or values greater than 1 for the `left` or `top` values\. 

## Contents<a name="API_BoundingBox_Contents"></a>

 **Height**   <a name="rekognition-Type-BoundingBox-Height"></a>
Height of the bounding box as a ratio of the overall image height\.  
Type: Float  
Required: No

 **Left**   <a name="rekognition-Type-BoundingBox-Left"></a>
Left coordinate of the bounding box as a ratio of overall image width\.  
Type: Float  
Required: No

 **Top**   <a name="rekognition-Type-BoundingBox-Top"></a>
Top coordinate of the bounding box as a ratio of overall image height\.  
Type: Float  
Required: No

 **Width**   <a name="rekognition-Type-BoundingBox-Width"></a>
Width of the bounding box as a ratio of the overall image width\.  
Type: Float  
Required: No

## See Also<a name="API_BoundingBox_SeeAlso"></a>

For more information about using this API in one of the language\-specific AWS SDKs, see the following:

+  [AWS SDK for C\+\+](http://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/BoundingBox) 

+  [AWS SDK for Go](http://docs.aws.amazon.com/goto/SdkForGoV1/rekognition-2016-06-27/BoundingBox) 

+  [AWS SDK for Java](http://docs.aws.amazon.com/goto/SdkForJava/rekognition-2016-06-27/BoundingBox) 

+  [AWS SDK for Ruby V2](http://docs.aws.amazon.com/goto/SdkForRubyV2/rekognition-2016-06-27/BoundingBox) 