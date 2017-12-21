# Detecting Labels in an Image<a name="labels-detect-labels-image"></a>

You can use the [DetectLabels](API_DetectLabels.md) operation to detect labels in an image\. For an example, see [Analysing Images Stored in an Amazon S3 Bucket](images-s3.md)\.

For each label, Rekognition Image returns a name and a confidence value in the analysis\. The following is an example response from `DetectLabels`\.

```
{
    "Labels": [
        {
            "Confidence": 98.4629,
            "Name": "beacon"
        },
        {
            "Confidence": 98.4629,
            "Name": "building"
        },
        {
            "Confidence": 98.4629,
            "Name": "lighthouse"
        },
        {
            "Confidence": 87.7924,
            "Name": "rock"
        },
        {
            "Confidence": 68.1049,
            "Name": "sea"
        }
    ]
}
```

The response shows that the operation detected five labels \(that is, beacon, building, lighthouse, rock, and sea\)\. Each label has an associated level of confidence\. For example, the detection algorithm is 98\.4629% confident that the image contains a building\. 

If the input image you provide contains a person, the `DetectLabels` operation detects labels such as person, clothing, suit, and selfie, as shown in the following example response:

```
{
    "Labels": [
        {
            "Confidence": 99.2786,
            "Name": "person"
        },
        {
            "Confidence": 90.6659,
            "Name": "clothing"
        },
        {
            "Confidence": 90.6659,
            "Name": "suit"
        },
        {
            "Confidence": 70.0364,
            "Name": "selfie"
        }
    ]
}
```

**Note**  
If you want facial features describing the faces in an image, use the `DetectFaces` operation instead\.