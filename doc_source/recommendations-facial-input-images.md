# Recommendations for facial comparison input images<a name="recommendations-facial-input-images"></a>

 The models used for face comparison operations are designed to work for a wide variety of poses, facial expressions, age ranges, rotations, lighting conditions, and sizes\. We recommend that you use the following guidelines when choosing reference photos for [CompareFaces](API_CompareFaces.md) or for adding faces to a collection using [IndexFaces](API_IndexFaces.md)\.
+ Use an image with a face that is within the recommended range of angles\. The pitch should be less than 30 degrees face down and less than 45 degrees face up\. The yaw should be less than 45 degrees in either direction\. There is no restriction on the roll\.
+ Use an image of a face with both eyes open and visible\.
+ When creating a collection using `IndexFaces`, use multiple face images of an individual with different pitches and yaws \(within the recommended range of angles\)\. We recommend that at least five images of the person are indexed—straight on, face turned left with a yaw of 45 degrees or less, face turned right with a yaw of 45 degrees or less, face tilted down with a pitch of 30 degrees or less, and face tilted up with a pitch of 45 degrees or less\. If you want to track that these face instances belong to the same individual, consider using the external image ID attribute if there is only one face in the image being indexed\. For example, five images of John Doe can be tracked in the collection with external image IDs as John\_Doe\_1\.jpg, … John\_Doe\_5\.jpg\.
+ Use an image of a face that is not obscured or tightly cropped\. The image should contain the full head and shoulders of the person\. It should not be cropped to the face bounding box\.
+ Avoid items that block the face, such as headbands and masks\.
+ Use an image of a face that occupies a large proportion of the image\. Images where the face occupies a larger portion of the image are matched with greater accuracy\. 
+ Ensure that images are sufficiently large in terms of resolution\. Amazon Rekognition can recognize faces as small as 50 x 50 pixels in image resolutions up to 1920 x 1080\. Higher\-resolution images require a larger minimum face size\. Faces larger than the minimum size provide a more accurate set of facial comparison results\.
+ Use color images\. 
+ Use images with flat lighting on the face, as opposed to varied lighting such as shadows\. 
+ Use images that have sufficient contrast with the background\. A high\-contrast monochrome background works well\.
+ Use images of faces with neutral facial expressions with mouth closed and little to no smile for applications that require high precision\.
+ Use images that are bright and sharp\. Avoid using images that may be blurry due to subject and camera motion as much as possible\. [DetectFaces](API_DetectFaces.md) can be used to determine the brightness and sharpness of a face\.
+ Ensure that recent face images are indexed\.