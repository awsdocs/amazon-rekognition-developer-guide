# Detecting text<a name="text-detection"></a>

Amazon Rekognition text detection can detect text in images and videos\. It can then convert the detected text into machine\-readable text\. You can use the machine\-readable text detection in images to implement solutions such as:
+ Visual search\. An example is retrieving and displaying images that contain the same text\.
+ Content insights\. An example is providing insights into themes that occur in text that's recognized in extracted video frames\. Your application can search recognized text for relevant content—such as news, sport scores, athlete numbers, and captions\.
+ Navigation\. An example is developing a speech\-enabled mobile app for visually impaired people that recognizes the names of restaurants, shops, or street signs\. 
+ Public safety and transportation support\. An example is detecting car license plate numbers from traffic camera images\. 
+ Filtering\. An example is filtering out personally identifiable information from images\. 

For text detection in videos, you can implement solutions such as: 
+ Searching videos for clips where specific text keywords, such as guest’s name on a graphic in a news show
+ Compliance and moderation \- detecting accidental text, profanity or spam
+ Finding all text overlays on the video timeline for further processing, such as replacing with text in another language for content internationalization
+ Finding text locations, so that other graphics can be aligned accordingly

[DetectText](API_DetectText.md) detects text in \.jpeg or \.png format images\. You can use the Amazon Rekognition Video API to detect text in video asynchronously with [StartTextDetection](API_StartTextDetection.md) and [GetTextDetection](API_GetTextDetection.md)\. Both image and video text detection APIs support most fonts, including highly stylized ones\. After detecting text, Amazon Rekognition creates a representation of detected words and lines of text, shows the relationship between them, and tells you where the text is on an image or frame of video\.

`DetectText` and `GetTextDetection` detects words and lines\.

A *word* is one or more ISO basic Latin script characters that aren't separated by spaces\. `DetectText` can detect up to 50 words in an image, and `GetTextDetection` can detect up to 50 words per frame of video\. Amazon Rekognition can also detect numbers and common symbols such as @, /, $, %\. \-, \_, \+, \*, and \#\.

A *line* is a string of equally spaced words\. A line isn't necessarily a complete sentence\. For example, a driver's license number is detected as a line\. A line ends when there is no aligned text after it\. Also, a line ends when there's a large gap between words, relative to the length of the words\. Depending on the gap between words, this means that Amazon Rekognition might detect multiple lines in text that are aligned in the same direction\. Periods don't represent the end of a line\. If a sentence spans multiple lines, the operation returns multiple lines\.

Consider the following image:

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/text.png)

The blue boxes represent information about the detected text and the location of the text that's returned by the `DetectText` operation \(on an image\) or the `GetTextDetection` operation \(on a single frame of a video\)\. In this example, Amazon Rekognition detects "IT's", "MONDAY", "but", "keep", and "Smiling" as words\. To be detected, text must be within \+/\- 90 degrees orientation of the horizontal axis\.

For an example, see [Detecting text in an image](text-detecting-text-procedure.md)\.