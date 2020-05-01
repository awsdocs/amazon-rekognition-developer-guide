# Detecting Text in a Stored Video<a name="text-detecting-video-procedure"></a>

Amazon Rekognition Video text detection in stored videos is an asynchronous operation\. To start detecting text, call [StartTextDetection](API_StartTextDetection.md)\. Amazon Rekognition Video publishes the completion status of the video analysis to an Amazon SNS topic\. If the video analysis is successful, call [GetTextDetection](API_GetTextDetection.md) to get the analysis results\. For more information about starting video analysis and getting the results, see [Calling Amazon Rekognition Video Operations](api-video.md)\.

This procedure expands on the code in [Analyzing a Video Stored in an Amazon S3 Bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md)\. It uses an Amazon SQS queue to get the completion status of a video analysis request\.

**To detect text in a video stored in an Amazon S3 bucket \(SDK\)**

1. Perform the steps in [Analyzing a Video Stored in an Amazon S3 Bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md)\.

1. Add the following code to the class `VideoDetect` in step 1\.

------
#### [ Java ]

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   
   private static void StartTextDetection(String bucket, String video) throws Exception{
              
       NotificationChannel channel= new NotificationChannel()
               .withSNSTopicArn(snsTopicArn)
               .withRoleArn(roleArn);
       
       StartTextDetectionRequest req = new StartTextDetectionRequest()
               .withVideo(new Video()
                       .withS3Object(new S3Object()
                           .withBucket(bucket)
                           .withName(video)))
               .withNotificationChannel(channel);
       
       
       StartTextDetectionResult startTextDetectionResult = rek.startTextDetection(req);
       startJobId=startTextDetectionResult.getJobId();
       
   } 
   
   private static void GetTextDetectionResults() throws Exception{
       
       int maxResults=10;
       String paginationToken=null;
       GetTextDetectionResult textDetectionResult=null;
       
       do{
           if (textDetectionResult !=null){
               paginationToken = textDetectionResult.getNextToken();
   
           }
           
       
           textDetectionResult = rek.getTextDetection(new GetTextDetectionRequest()
                .withJobId(startJobId)
                .withNextToken(paginationToken)
                .withMaxResults(maxResults));
       
           VideoMetadata videoMetaData=textDetectionResult.getVideoMetadata();
               
           System.out.println("Format: " + videoMetaData.getFormat());
           System.out.println("Codec: " + videoMetaData.getCodec());
           System.out.println("Duration: " + videoMetaData.getDurationMillis());
           System.out.println("FrameRate: " + videoMetaData.getFrameRate());
               
               
           //Show text, confidence values
           List<TextDetectionResult> textDetections = textDetectionResult.getTextDetections();
   
   
           for (TextDetectionResult text: textDetections) {
               long seconds=text.getTimestamp()/1000;
               System.out.println("Sec: " + Long.toString(seconds) + " ");
               TextDetection detectedText=text.getTextDetection();
               
               System.out.println("Text Detected: " + detectedText.getDetectedText());
                   System.out.println("Confidence: " + detectedText.getConfidence().toString());
                   System.out.println("Id : " + detectedText.getId());
                   System.out.println("Parent Id: " + detectedText.getParentId());
                   System.out.println("Bounding Box" + detectedText.getGeometry().getBoundingBox().toString());
                   System.out.println("Type: " + detectedText.getType());
                   System.out.println();
           }
       } while (textDetectionResult !=null && textDetectionResult.getNextToken() != null);
         
           
   }
   ```

   In the function `main`, replace the lines: 

   ```
           StartLabelDetection(bucket, video);
   
           if (GetSQSMessageSuccess()==true)
           	GetLabelDetectionResults();
   ```

   with:

   ```
           StartTextDetection(bucket, video);
   
           if (GetSQSMessageSuccess()==true)
           	GetTextDetectionResults();
   ```

------
#### [ Python ]

   ```
   #Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
       def StartTextDetection(self):
           response=self.rek.start_text_detection(Video={'S3Object': {'Bucket': self.bucket, 'Name': self.video}},
               NotificationChannel={'RoleArn': self.roleArn, 'SNSTopicArn': self.snsTopicArn})
   
           self.startJobId=response['JobId']
           print('Start Job Id: ' + self.startJobId)
     
       def GetTextDetectionResults(self):
           maxResults = 10
           paginationToken = ''
           finished = False
   
           while finished == False:
               response = self.rek.get_text_detection(JobId=self.startJobId,
                                               MaxResults=maxResults,
                                               NextToken=paginationToken)
   
               print('Codec: ' + response['VideoMetadata']['Codec'])
               
               print('Duration: ' + str(response['VideoMetadata']['DurationMillis']))
               print('Format: ' + response['VideoMetadata']['Format'])
               print('Frame rate: ' + str(response['VideoMetadata']['FrameRate']))
               print()
   
               for textDetection in response['TextDetections']:
                   text=textDetection['TextDetection']
   
                   print("Timestamp: " + str(textDetection['Timestamp']))
                   print("   Text Detected: " + text['DetectedText'])
                   print("   Confidence: " +  str(text['Confidence']))
                   print ("      Bounding box")
                   print ("        Top: " + str(text['Geometry']['BoundingBox']['Top']))
                   print ("        Left: " + str(text['Geometry']['BoundingBox']['Left']))
                   print ("        Width: " +  str(text['Geometry']['BoundingBox']['Width']))
                   print ("        Height: " +  str(text['Geometry']['BoundingBox']['Height']))
                   print ("   Type: " + str(text['Type']) )
                   print()
   
                   if 'NextToken' in response:
                       paginationToken = response['NextToken']
                   else:
                       finished = True
   ```

   In the function `main`, replace the lines:

   ```
       analyzer.StartLabelDetection()
       if analyzer.GetSQSMessageSuccess()==True:
           analyzer.GetLabelDetectionResults()
   ```

   with:

   ```
       analyzer.StartTextDetection()
       if analyzer.GetSQSMessageSuccess()==True:
           analyzer.GetTextDetectionResults()
   ```

------
**Note**  
If you've already run a video example other than [Analyzing a Video Stored in an Amazon S3 Bucket with Java or Python \(SDK\)](video-analyzing-with-sqs.md), the code to replace might be different\.

1. Run the code\. Text that was detected in the video is shown in a list\.

## Filters<a name="text-detection-filters"></a>

Filters are optional request parameters that can be used when you call `StartTextDetection`\. Filtering by text region, size and confidence score provides you with additional flexibility to control your text detection output\. By using regions of interest, you an easily limit text detection to the regions that are relevant, for example, a bottom third region for graphics or a top left corner for reading scoreboards in a soccer game\. Word bounding box size filter can be used to avoid small background text which may be noisy or irrelevant\. And lastly, word confidence filter enables you to remove results that may be unreliable due to being blurry or smudged\. You can use the following filters:
+ **MinConfidence** –Sets the confidence level of word detection\. Words with detection confidence below this level are excluded from the result\. Values should be between 0\.5 and 1\. The default MinConfidence is 0\.8
+ **MinBoundingBoxWidth** – Sets the minimum width of the word bounding box\. Words with bounding boxes that are smaller than this value are excluded from the result\. The value is relative to the video frame width\.
+ **MinBoundingBoxHeight** – Sets the minimum height of the word bounding box\. Words with bounding box heights less than this value are excluded from the result\. The value is relative to the video frame height\.
+ **RegionsOfInterest** – Limits detection to a specific region of the frame\. The values are relative to the frame dimensions\. For objects only partially within the regions, the response is undefined\.

## GetTextDetection Response<a name="text-detecting-video-response"></a>

`GetTextDetection` returns an array \(`TextDetectionResults`\) that contains information about the text detected in the video\. An array element, [TextDetection](API_TextDetection.md), exists for each time a word or line is detected in the video\. The array elements are sorted by time \(in milliseconds\) since the start of the video\.

The following is a partial JSON response from `GetTextDetection`\. In the response, note the following:
+ **Text information** – The `TextDetectionResult` array element contains information about the detected text \([TextDetection](API_TextDetection.md)\) and the time that the text was detected in the video \(`Timestamp`\)\.
+ **Paging information** – The example shows one page of text detection information\. You can specify how many text elements to return in the `MaxResults` input parameter for `GetTextDetection`\. If more results than `MaxResults` exist, or there are more results than the default maximum, `GetTextDetection` returns a token \(`NextToken`\) that's used to get the next page of results\. For more information, see [Getting Amazon Rekognition Video Analysis Results](api-video.md#api-video-get)\.
+ **Video information** – The response includes information about the video format \(`VideoMetadata`\) in each page of information that's returned by `GetTextDetection`\.

```
{
    "JobStatus": "SUCCEEDED",
    "VideoMetadata": {
        "Codec": "h264",
        "DurationMillis": 174441,
        "Format": "QuickTime / MOV",
        "FrameRate": 29.970029830932617,
        "FrameHeight": 480,
        "FrameWidth": 854
    },
    "TextDetections": [
        {
            "Timestamp": 967,
            "TextDetection": {
                "DetectedText": "Twinkle Twinkle Little Star",
                "Type": "LINE",
                "Id": 0,
                "Confidence": 99.91780090332031,
                "Geometry": {
                    "BoundingBox": {
                        "Width": 0.8337579369544983,
                        "Height": 0.08365312218666077,
                        "Left": 0.08313830941915512,
                        "Top": 0.4663468301296234
                    },
                    "Polygon": [
                        {
                            "X": 0.08313830941915512,
                            "Y": 0.4663468301296234
                        },
                        {
                            "X": 0.9168962240219116,
                            "Y": 0.4674469828605652
                        },
                        {
                            "X": 0.916861355304718,
                            "Y": 0.5511001348495483
                        },
                        {
                            "X": 0.08310343325138092,
                            "Y": 0.5499999523162842
                        }
                    ]
                }
            }
        },
        {
            "Timestamp": 967,
            "TextDetection": {
                "DetectedText": "Twinkle",
                "Type": "WORD",
                "Id": 1,
                "ParentId": 0,
                "Confidence": 99.98338317871094,
                "Geometry": {
                    "BoundingBox": {
                        "Width": 0.2423887550830841,
                        "Height": 0.0833333358168602,
                        "Left": 0.08313817530870438,
                        "Top": 0.46666666865348816
                    },
                    "Polygon": [
                        {
                            "X": 0.08313817530870438,
                            "Y": 0.46666666865348816
                        },
                        {
                            "X": 0.3255269229412079,
                            "Y": 0.46666666865348816
                        },
                        {
                            "X": 0.3255269229412079,
                            "Y": 0.550000011920929
                        },
                        {
                            "X": 0.08313817530870438,
                            "Y": 0.550000011920929
                        }
                    ]
                }
            }
        },
        {
            "Timestamp": 967,
            "TextDetection": {
                "DetectedText": "Twinkle",
                "Type": "WORD",
                "Id": 2,
                "ParentId": 0,
                "Confidence": 99.982666015625,
                "Geometry": {
                    "BoundingBox": {
                        "Width": 0.2423887550830841,
                        "Height": 0.08124999701976776,
                        "Left": 0.3454332649707794,
                        "Top": 0.46875
                    },
                    "Polygon": [
                        {
                            "X": 0.3454332649707794,
                            "Y": 0.46875
                        },
                        {
                            "X": 0.5878220200538635,
                            "Y": 0.46875
                        },
                        {
                            "X": 0.5878220200538635,
                            "Y": 0.550000011920929
                        },
                        {
                            "X": 0.3454332649707794,
                            "Y": 0.550000011920929
                        }
                    ]
                }
            }
        },
        {
            "Timestamp": 967,
            "TextDetection": {
                "DetectedText": "Little",
                "Type": "WORD",
                "Id": 3,
                "ParentId": 0,
                "Confidence": 99.8787612915039,
                "Geometry": {
                    "BoundingBox": {
                        "Width": 0.16627635061740875,
                        "Height": 0.08124999701976776,
                        "Left": 0.6053864359855652,
                        "Top": 0.46875
                    },
                    "Polygon": [
                        {
                            "X": 0.6053864359855652,
                            "Y": 0.46875
                        },
                        {
                            "X": 0.7716627717018127,
                            "Y": 0.46875
                        },
                        {
                            "X": 0.7716627717018127,
                            "Y": 0.550000011920929
                        },
                        {
                            "X": 0.6053864359855652,
                            "Y": 0.550000011920929
                        }
                    ]
                }
            }
        },
        {
            "Timestamp": 967,
            "TextDetection": {
                "DetectedText": "Star",
                "Type": "WORD",
                "Id": 4,
                "ParentId": 0,
                "Confidence": 99.82640075683594,
                "Geometry": {
                    "BoundingBox": {
                        "Width": 0.12997658550739288,
                        "Height": 0.08124999701976776,
                        "Left": 0.7868852615356445,
                        "Top": 0.46875
                    },
                    "Polygon": [
                        {
                            "X": 0.7868852615356445,
                            "Y": 0.46875
                        },
                        {
                            "X": 0.9168618321418762,
                            "Y": 0.46875
                        },
                        {
                            "X": 0.9168618321418762,
                            "Y": 0.550000011920929
                        },
                        {
                            "X": 0.7868852615356445,
                            "Y": 0.550000011920929
                        }
                    ]
                }
            }
        }
    ],
    "NextToken": "NiHpGbZFnkM/S8kLcukMni15wb05iKtquu/Mwc+Qg1LVlMjjKNOD0Z0GusSPg7TONLe+OZ3P",
    "TextModelVersion": "3.0"
}
```