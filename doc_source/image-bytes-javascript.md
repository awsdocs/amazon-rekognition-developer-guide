# Using JavaScript<a name="image-bytes-javascript"></a>

The following JavaScript webpage example allows a user to choose an image and view the estimated ages of faces that are detected in the image\. The estimated ages are returned by a call to [ DetectFaces ](API_DetectFaces.md)\. 

The chosen image is loaded by using the JavaScript `FileReader.readAsDataURL` function, which base64\-encodes the image\. This is useful for displaying the image on an HTML canvas\. But, it means the image bytes have to be unencoded before they're passed to an Amazon Rekognition Image operation\. This example shows how to unencode the loaded image bytes\. If the encoded image bytes aren't useful to you, use `FileReader.readAsArrayBuffer` instead because the loaded image isn't encoded\. This means that Amazon Rekognition Image operations can be called without first unencoding the image bytes\. For an example, see [Using readAsArrayBuffer](#image-bytes-javascript-unencoded)\.

**To run the JavaScript example**

1. Load the example source code into an editor\.

1. Get the Amazon Cognito identity pool identifier\. For more information, see [Getting the Amazon Cognito identity pool identifier](#image-bytes-javascript-auth)\.

1. In the `AnonLog` function of the example code, change `IdentityPoolIdToUse` and `RegionToUse` to the values that you noted in step 9 of [Getting the Amazon Cognito identity pool identifier](#image-bytes-javascript-auth)\. 

1. In the `DetectFaces` function, change `RegionToUse` to the value you used in the previous step\.

1. Save the example source code as an `.html` file\.

1. Load the file into your browser\.

1. Choose the **Browse\.\.\.** button, and choose an image that contains one or more faces\. A table is shown that contains the estimated ages for each face detected in the image\. 

**Note**  
The following code example uses two scripts that are no longer part of Amazon Cognito\. To get these files, follow the links for [ aws\-cognito\-sdk\.min\.js](https://raw.githubusercontent.com/aws/amazon-cognito-identity-js/master/dist/aws-cognito-sdk.js) and [ amazon\-cognito\-identity\.min\.js](https://raw.githubusercontent.com/aws/amazon-cognito-identity-js/master/dist/amazon-cognito-identity.min.js), then save the text from each as seperate `.js` files\. 

## JavaScript example code<a name="image-bytes-javascript-code"></a>

The following code example uses JavaScript V2\. For an example in JavaScript V3, see [the example in the AWS Documentation SDK examples GitHub repository\.](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/javascriptv3/example_code/rekognition/estimate-age-example/src)

```
<!--
Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
-->
<!DOCTYPE html>
<html>
<head>
  <script src="aws-cognito-sdk.min.js"></script>
  <script src="amazon-cognito-identity.min.js"></script>
  <script src="https://sdk.amazonaws.com/js/aws-sdk-2.16.0.min.js"></script>
  <meta charset="UTF-8">
  <title>Rekognition</title>
</head>

<body>
  <H1>Age Estimator</H1>
  <input type="file" name="fileToUpload" id="fileToUpload" accept="image/*">
  <p id="opResult"></p>
</body>
<script>

  document.getElementById("fileToUpload").addEventListener("change", function (event) {
    ProcessImage();
  }, false);
  
  //Calls DetectFaces API and shows estimated ages of detected faces
  function DetectFaces(imageData) {
    AWS.region = "RegionToUse";
    var rekognition = new AWS.Rekognition();
    var params = {
      Image: {
        Bytes: imageData
      },
      Attributes: [
        'ALL',
      ]
    };
    rekognition.detectFaces(params, function (err, data) {
      if (err) console.log(err, err.stack); // an error occurred
      else {
       var table = "<table><tr><th>Low</th><th>High</th></tr>";
        // show each face and build out estimated age table
        for (var i = 0; i < data.FaceDetails.length; i++) {
          table += '<tr><td>' + data.FaceDetails[i].AgeRange.Low +
            '</td><td>' + data.FaceDetails[i].AgeRange.High + '</td></tr>';
        }
        table += "</table>";
        document.getElementById("opResult").innerHTML = table;
      }
    });
  }
  //Loads selected image and unencodes image bytes for Rekognition DetectFaces API
  function ProcessImage() {
    AnonLog();
    var control = document.getElementById("fileToUpload");
    var file = control.files[0];

    // Load base64 encoded image 
    var reader = new FileReader();
    reader.onload = (function (theFile) {
      return function (e) {
        var img = document.createElement('img');
        var image = null;
        img.src = e.target.result;
        var jpg = true;
        try {
          image = atob(e.target.result.split("data:image/jpeg;base64,")[1]);

        } catch (e) {
          jpg = false;
        }
        if (jpg == false) {
          try {
            image = atob(e.target.result.split("data:image/png;base64,")[1]);
          } catch (e) {
            alert("Not an image file Rekognition can process");
            return;
          }
        }
        //unencode image bytes for Rekognition DetectFaces API 
        var length = image.length;
        imageBytes = new ArrayBuffer(length);
        var ua = new Uint8Array(imageBytes);
        for (var i = 0; i < length; i++) {
          ua[i] = image.charCodeAt(i);
        }
        //Call Rekognition  
        DetectFaces(imageBytes);
      };
    })(file);
    reader.readAsDataURL(file);
  }
  //Provides anonymous log on to AWS services
  function AnonLog() {
    
    // Configure the credentials provider to use your identity pool
    AWS.config.region = 'RegionToUse'; // Region
    AWS.config.credentials = new AWS.CognitoIdentityCredentials({
      IdentityPoolId: 'IdentityPoolIdToUse',
    });
    // Make the call to obtain credentials
    AWS.config.credentials.get(function () {
      // Credentials will be available when this function is called.
      var accessKeyId = AWS.config.credentials.accessKeyId;
      var secretAccessKey = AWS.config.credentials.secretAccessKey;
      var sessionToken = AWS.config.credentials.sessionToken;
    });
  }
</script>
</html>
```

### Using readAsArrayBuffer<a name="image-bytes-javascript-unencoded"></a>

The following code snippet is an alternative implementation of the `ProcessImage` function in the sample code, using JavaScript V2\. It uses `readAsArrayBuffer` to load an image and call `DetectFaces`\. Because `readAsArrayBuffer` doesn't base64\-encode the loaded file, it's not necessary to unencode the image bytes before calling an Amazon Rekognition Image operation\.

```
//Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
//PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

function ProcessImage() {
    AnonLog();
    var control = document.getElementById("fileToUpload");
    var file = control.files[0];

    // Load base64 encoded image for display 
    var reader = new FileReader();
    reader.onload = (function (theFile) {
      return function (e) {
        //Call Rekognition  
        AWS.region = "RegionToUse";  
        var rekognition = new AWS.Rekognition();
        var params = {
          Image: {
          Bytes: e.target.result
        },
        Attributes: [
        'ALL',
      ]
    };
    rekognition.detectFaces(params, function (err, data) {
      if (err) console.log(err, err.stack); // an error occurred
      else {
       var table = "<table><tr><th>Low</th><th>High</th></tr>";
        // show each face and build out estimated age table
        for (var i = 0; i < data.FaceDetails.length; i++) {
          table += '<tr><td>' + data.FaceDetails[i].AgeRange.Low +
            '</td><td>' + data.FaceDetails[i].AgeRange.High + '</td></tr>';
        }
        table += "</table>";
        document.getElementById("opResult").innerHTML = table;
      }
    });

      };
    })(file);
    reader.readAsArrayBuffer(file);
  }
```

## Getting the Amazon Cognito identity pool identifier<a name="image-bytes-javascript-auth"></a>

For simplicity, the example uses an anonymous Amazon Cognito identity pool to provide unauthenticated access to the Amazon Rekognition Image API\. This might be suitable for your needs\. For example, you can use unauthenticated access to provide free, or trial, access to your website before users sign up\. To provide authenticated access, use an Amazon Cognito user pool\. For more information, see [Amazon Cognito User Pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html)\. 

The following procedure shows how to create an identity pool that enables access to unauthenticated identities, and how to get the identity pool identifier that's needed in the example code\.

**To get the identity pool identifier**

1. Open the Amazon Cognito [console](https://console.aws.amazon.com/cognito/federated)\.

1. Choose **Create new identity pool**\.

1. For **Identity pool name\***, type a name for your identity pool\.

1. In **Unauthenticated identities**, choose **Enable access to unauthenticated identities**\.

1. Choose **Create Pool**\.

1. Choose **View Details**, and note the role name for unauthenticated identities\.

1. Choose **Allow**\.

1. In **Platform**, choose **JavaScript**\.

1. In **Get AWS Credentials**, note the values of `AWS.config.region` and `IdentityPooldId` that are shown in the code snippet\.

1. Open the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

1. In the navigation pane, choose **Roles**\.

1. Choose the role name that you noted in step 6\.

1. In the **Permissions** tab, choose **Attach Policies**\.

1. Choose **AmazonRekognitionReadOnlyAccess**\.

1. Choose **Attach Policy**\.