# DetectedFace<a name="streaming-video-kinesis-output-reference-detectedface"></a>

Information about a face that's detected in a streaming video frame\. Matching faces in the input collection are available in [MatchedFace](streaming-video-kinesis-output-reference-facematch.md) object field\.

**BoundingBox**

The bounding box coordinates for a face that's detected within an analyzed video frame\. The BoundingBox object has the same properties as the BoundingBox object that's used for image analysis\.

Type: [BoundingBox](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_BoundingBox.html) object 

**Confidence**

The confidence level \(1\-100\) that Amazon Rekognition Video has that the detected face is actually a face\. 1 is the lowest confidence, 100 is the highest\.

Type: Number

**Landmarks**

An array of facial landmarks\.

Type: [Landmark](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Landmark.html) object array

**Pose**

Indicates the pose of the face as determined by its pitch, roll, and yaw\.

Type: [Pose](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Pose.html) object

**Quality**

Identifies face image brightness and sharpness\. 

Type: [ImageQuality](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ImageQuality.html) object