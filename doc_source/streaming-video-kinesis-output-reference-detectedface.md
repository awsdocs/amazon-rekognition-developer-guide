# DetectedFace<a name="streaming-video-kinesis-output-reference-detectedface"></a>

Information about a face that's detected in a streaming video frame\. Matching faces in the input collection are available in [MatchedFace](streaming-video-kinesis-output-reference-facematch.md) object field\.

**BoundingBox**

The bounding box coordinates for a face that's detected within an analyzed video frame\. The BoundingBox object has the same properties as the BoundingBox object that's used for image analysis\.

Type: [BoundingBox](API_BoundingBox.md) object 

**Confidence**

The confidence level \(1\-100\) that Rekognition Video has that the detected face is actually a face\. 1 is the lowest confidence, 100 is the highest\.

Type: Number

**Landmarks**

An array of facial landmarks\.

Type: [Landmark](API_Landmark.md) object array

**Pose**

Indicates the pose of the face as determined by its pitch, roll, and yaw\.

Type: [Pose](API_Pose.md) object

**Quality**

Identifies face image brightness and sharpness\. 

Type: [ImageQuality](API_ImageQuality.md) object