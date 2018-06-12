# Detecting Text<a name="text-detection"></a>

Amazon Rekognition Text in Image can detect text in images and convert it into machine\-readable text\. You can use the machine\-readable text to implement solutions such as:
+ Visual search\. An example is retrieving and displaying images that contain the same text\.
+ Content insights\. An example is providing insights into themes that occur in text recognized in extracted video frames\. Your application can search recognized text for relevant content—such as news, sport scores, athlete numbers, and captions\.
+ Navigation\. An example is developing a speech\-enabled mobile app for visually impaired people that recognizes the names of restaurants, shops, or street signs\. 
+ Public safety and transportation support\. An example is detecting car license plate numbers from traffic camera images\. 
+ Filtering\. An example is filtering out personally identifiable information from images\. 

[DetectText](API_DetectText.md) detects text in \.jpeg or \.png format images and supports most fonts, including highly stylized ones\. After detecting text, `DetectText` creates a representation of detected words and lines of text, and shows the relationship between them\. The `DetectText` API also tells you where the text is on an image\.

Consider the following image: 

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/text.png)

The blue boxes represent information about the detected text and location of the text that the `DetectText` operation returns\. To be detected, text must be within \+/\- 30\-degrees orientation of the horizontal axis\. `DetectText` categorizes recognized text as either a word or a line of text\.

A *word* is one or more ISO basic Latin script characters that aren't separated by spaces\. `DetectText` can detect up to 50 words in an image\.

A *line* is a string of equally spaced words\. A line isn't necessarily a complete sentence\. For example, a driver's license number is detected as a line\. A line ends when there is no aligned text after it\. Also, a line ends when there's a large gap between words, relative to the length of the words\. This means, depending on the gap between words, Amazon Rekognition might detect multiple lines in text that are aligned in the same direction\. Periods don't represent the end of a line\. If a sentence spans multiple lines, the `DetectText` operation returns multiple lines\.

Amazon Rekognition can also detect numbers and common symbols, such as @, /, $,%, \-, \_, \+, \*, and \#\.

****

For an example, see [Detecting Text in an Image](text-detecting-text-procedure.md)\.