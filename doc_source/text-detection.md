# Detecting text<a name="text-detection"></a>

Amazon Rekognition can detect text in images and videos\. It can then convert the detected text into machine\-readable text\. You can use machine\-readable text detection in images to implement solutions such as:
+ Visual search\. For example, retrieving and displaying images that contain the same text\.
+ Content insights\. For example, providing insights into themes that occur in text that's recognized in extracted video frames\. Your application can search recognized text for relevant content, such as news, sport scores, athlete numbers, and captions\.
+ Navigation\. For example, developing a speech\-enabled mobile app for visually impaired people that recognizes the names of restaurants, shops, or street signs\. 
+ Public safety and transportation support\. For example, detecting car license plate numbers from traffic camera images\. 
+ Filtering\. For example, filtering personally identifiable information \(PII\) from images\. 

For text detection in videos, you can implement solutions such as: 
+ Searching videos for clips with specific text keywords, such as a guest’s name on a graphic in a news show\.
+ Moderating content for compliance with organizational standards by detecting accidental text, profanity, or spam\.
+ Finding all text overlays on the video timeline for further processing, such as replacing text with text in another language for content internationalization\.
+ Finding text locations, so that other graphics can be aligned accordingly\.

To detect text in images in JPEG or PNG format, use the [DetectText](API_DetectText.md) operation\. To asynchronously detect text in video, use the [StartTextDetection](API_StartTextDetection.md) and [GetTextDetection](API_GetTextDetection.md) operations\. Both image and video text detection operations support most fonts, including highly stylized ones\. After detecting text, Amazon Rekognition creates a representation of detected words and lines of text, shows the relationship between them, and tells you where the text is on an image or video frame\.

The `DetectText` and `GetTextDetection` operations detect words and lines\. A *word* is one or more ISO\-standard Latin\-script characters from the standard English alphabet and ASCII symbols that aren't separated by spaces\. `DetectText` can detect up to 100 words in an image\. `GetTextDetection` can detect up to 50 words per frame of video\. The following table list the characters that Amazon Rekognition can detect\.


|  Category  |  Supported characters  | 
| --- | --- | 
| Uppercase letters |  ABCDEFGHIJKLMNOPQRSTUVWXYZ  | 
|  Lowercase letters  |  abcdefghijklmnopqrstuvwxyz  | 
|  Numbers  |  0123456789  | 
| Symbols | \! " \# $ % & \\ ' \( \) \* \+ , \- \. / : ; < = > ? @ \[ \\ \] ^ \_ ` \{ \| \} \~ | 

Amazon Rekognition is designed to detect words in English\. It might also detect words in other languages that use these characters, but it doesn't detect diacritics and other characters\. For example, it might detect "un" in French, but it might not detect "garçon" or might not detect it correctly\.

A *line* is a string of equally spaced words\. A line isn't necessarily a complete sentence \(periods don't indicate the end of a line\)\. For example, Amazon Rekognition detects a driver's license number as a line\. A line ends when there is no aligned text after it or when there's a large gap between words, relative to the length of the words\. Depending on the gap between words, Amazon Rekognition might detect multiple lines in text that are aligned in the same direction\. If a sentence spans multiple lines, the operation returns multiple lines\.

Consider the following image\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/text.png)

The blue boxes represent information about the detected text and the location of the text that's returned by the `DetectText` operation\. In this example, Amazon Rekognition detects "IT'S", "MONDAY", "but", "keep", and "Smiling" as words\. Amazon Rekognition detects "IT'S", "MONDAY", "but keep", and "Smiling" as lines\. To be detected, text must be within \+/\- 90 degrees orientation of the horizontal axis\.

For an example, see [Detecting text in an image](text-detecting-text-procedure.md)\.

**Topics**
+ [Detecting text in an image](text-detecting-text-procedure.md)
+ [Detecting text in a stored video](text-detecting-video-procedure.md)