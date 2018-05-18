# Exercise 1: Detect Objects and Scenes in an Image \(Console\)<a name="detect-labels-console"></a>

This section shows how, at a very high level, Amazon Rekognition's objects and scenes detection capability works\. When you specify an image as input, the service detects the objects and scenes in the image and returns them along with a percent confidence score for each object and scene\.

For example, Amazon Rekognition detects the following objects and scenes in the sample image: skateboard, sport, person, auto, car and vehicle\. To see all the confidence scores shown in this response, choose **Show more** in the **Labels \| Confidence** pane\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/detect-scenes.png)

Amazon Rekognition also returns a confidence score for each object detected in the sample image, as shown in the following sample response\. 

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/labels-confidence-score.png)

You can also look at the request to the API and the response from the API as a reference\.

Request

```
{
   "contentString":{
      "Attributes":[
         "ALL"
      ],
      "Image":{
         "S3Object":{
            "Bucket":"console-sample-images",
            "Name":"skateboard.jpg"
         }
      }
   }
}
```

Response

```
{
   "Labels":[
      {
         "Confidence":99.25359344482422,
         "Name":"Skateboard"
      },
      {
         "Confidence":99.25359344482422,
         "Name":"Sport"
      },
      {
         "Confidence":99.24723052978516,
         "Name":"People"
      },
      {
         "Confidence":99.24723052978516,
         "Name":"Person"
      },
      {
         "Confidence":99.23908233642578,
         "Name":"Human"
      },
      {
         "Confidence":97.42484283447266,
         "Name":"Parking"
      },
      {
         "Confidence":97.42484283447266,
         "Name":"Parking Lot"
      },
      {
         "Confidence":91.53300476074219,
         "Name":"Automobile"
      },
      {
         "Confidence":91.53300476074219,
         "Name":"Car"
      },
      {
         "Confidence":91.53300476074219,
         "Name":"Vehicle"
      },
      {
         "Confidence":76.85114288330078,
         "Name":"Intersection"
      },
      {
         "Confidence":76.85114288330078,
         "Name":"Road"
      },
      {
         "Confidence":76.21503448486328,
         "Name":"Boardwalk"
      },
      {
         "Confidence":76.21503448486328,
         "Name":"Path"
      },
      {
         "Confidence":76.21503448486328,
         "Name":"Pavement"
      },
      {
         "Confidence":76.21503448486328,
         "Name":"Sidewalk"
      },
      {
         "Confidence":76.21503448486328,
         "Name":"Walkway"
      },
      {
         "Confidence":66.71541595458984,
         "Name":"Building"
      },
      {
         "Confidence":62.04711151123047,
         "Name":"Coupe"
      },
      {
         "Confidence":62.04711151123047,
         "Name":"Sports Car"
      },
      {
         "Confidence":61.98909378051758,
         "Name":"City"
      },
      {
         "Confidence":61.98909378051758,
         "Name":"Downtown"
      },
      {
         "Confidence":61.98909378051758,
         "Name":"Urban"
      },
      {
         "Confidence":60.978023529052734,
         "Name":"Neighborhood"
      },
      {
         "Confidence":60.978023529052734,
         "Name":"Town"
      },
      {
         "Confidence":59.22066116333008,
         "Name":"Sedan"
      },
      {
         "Confidence":56.48063278198242,
         "Name":"Street"
      },
      {
         "Confidence":54.235477447509766,
         "Name":"Housing"
      },
      {
         "Confidence":53.85226058959961,
         "Name":"Metropolis"
      },
      {
         "Confidence":52.001792907714844,
         "Name":"Office Building"
      },
      {
         "Confidence":51.325313568115234,
         "Name":"Suv"
      },
      {
         "Confidence":51.26075744628906,
         "Name":"Apartment Building"
      },
      {
         "Confidence":51.26075744628906,
         "Name":"High Rise"
      },
      {
         "Confidence":50.68067932128906,
         "Name":"Pedestrian"
      },
      {
         "Confidence":50.59548568725586,
         "Name":"Freeway"
      },
      {
         "Confidence":50.568580627441406,
         "Name":"Bumper"
      }
   ]
}
```

For more information, see [Amazon Rekognition: How It Works](how-it-works.md)\.

## Detect Objects and Scenes in an Image You Provide<a name="detect-label-own-image"></a>

You can upload an image that you own or provide the URL to an image as input in the Amazon Rekognition console\. Amazon Rekognition returns the object and scenes, confidence scores for each object, and scene it detects in the image you provide\.

**Note**  
The image must be less than 5MB in size and must be of JPEG or PNG format\.

**To detect objects and scenes in an image you provide**

1. Open the Amazon Rekognition console\.

1. Choose **Object and scene detection**\.

1. Do one of the following: 
   + Upload an image – Choose **Upload**, go to the location where you stored your image, and then select the image\. 
   + Use a URL – Type the URL in the text box, and then choose **Go**\.

1. View the confidence score of each label detected in the **Labels \| Confidence** pane\.