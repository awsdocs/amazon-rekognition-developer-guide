# Guidelines on face attributes<a name="guidance-face-attributes"></a>

Amazon Rekognition returns a bounding box, landmarks, quality, and the pose for each face it detects\. Amazon Rekognition also returns predictions for emotion, gender, age, and other attributes for each face if the parameter for attributes is set to `ALL` in the API request\. Each attribute or emotion has a value and a confidence score\. For example, a certain face might be predicted as having the gender ‘Female’ with a confidence score of 85% and the emotion ‘Happy’ with a confidence score of 90%\.

A gender binary \(male/female\) prediction is based on the physical appearance of a face in a particular image\. It doesn't indicate a person’s gender identity, and you shouldn't use Amazon Rekognition to make such a determination\. We don't recommend using gender binary predictions to make decisions that impact  an individual's rights, privacy, or access to services\. 

Similarly, a prediction of an emotional expression is based on the physical appearance of a person's face in an image\. It doesn't indicate a person’s actual internal emotional state, and you shouldn't use Amazon Rekognition to make such a determination\. For example, a person pretending to have a happy face in a picture might look happy, but might not be experiencing happiness\. 

We recommend using a threshold of 99% or more for use cases where the accuracy of classification could have any negative impact on the subjects of the images\. The only exception is Age Range, where Amazon Rekognition estimates the lower and upper age for the person\. In this case, the wider the age range, the lower the confidence for that prediction\. As an approximation, you should use the mid\-point of the age range to estimate a single value for the age of the detected face\. \(The actual age does not necessarily correspond to this number\.\) 



One of the best uses of these attributes is generating aggregate statistics\. For example, attributes, such as Smile, Pose, and Sharpness, may be used to select the ‘best profile picture’ automatically in a social media application\. Another common use case is estimating demographics anonymously of a broad sample using the predicted gender and age attributes \(for example, at events or retail stores\)\. 

For more information about attributes, see [FaceDetail](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_FaceDetail.html)\.