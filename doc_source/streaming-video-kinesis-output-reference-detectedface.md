# DetectedFace<a name="streaming-video-kinesis-output-reference-detectedface"></a>

Information about a face that's matched in a streaming video frame\. Each `DetectedFace` includes information about the detected face and the faces in the input collection that match the detected face\.

**[BoundingBox](API_BoundingBox.md)**

The bounding box coordinates for a face that's detected within an analyzed video frame\. The BoundingBox object has the same properties as the BoundingBox object that's used for image analysis\.

**Confidence**

The confidence level that Rekognition Video has that the detected face is actually a face\.

**Landmarks**

An array of facial landmarks\. For more information, see [Landmark](API_Landmark.md)\.

**[Pose](API_Pose.md)**

Indicates the pose of the face as determined by its pitch, roll, and yaw\.

**Quality**

Identifies face image brightness and sharpness\. The quality values are the same as the [ImageQuality](API_ImageQuality.md) object\.

**MatchedFaces**

An array of face match information for faces in the input collection that match the face that's recognized in `FaceDetail`\. 

Type: [](streaming-video-kinesis-output-reference-facematch.md) object 