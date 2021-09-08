# Using Amazon Rekognition and Lambda to tag assets in an Amazon S3 bucket<a name="images-lambda-s3-tutorial"></a>

In this tutorial, you create an AWS Lambda function that automatically tags digital assets located in an Amazon S3 bucket\. The Lambda function reads all objects in a given Amazon S3 bucket\. For each object in the bucket, it passes the image to the Amazon Rekognition service to geneate a series of labels\. Each label is used to create a tag that is applied to the image\. After you execute the Lambda function, it automatically creates tags based on all images in a given Amazon S3 bucket and applies them to the images\.

For example, assume you run the Lambda function and you have this image in an Amazon S3 bucket\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/v2-image-tutorial-picture.png)

The application then automatically creates tags and applies them to the image\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/v2-image-tutorial-results.png)

**Note**  
The services you use in this tutorial are part of the AWS Free Tier\. When you are done with the tutorial, we recommend terminating any resources you created during the tutorial so that you are not charged\.

This tutorial uses the AWS SDK for Java version 2\. See the [AWS Documentation SDK examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/javav2/usecases) for additional Java V2 tutorials\.

**Topics**
+ [Prerequisites](#lambda-s3-tutorial-prerequisites)
+ [Configure the IAM Lambda role](#lambda-s3-tutorial-lambda-role)
+ [Create the project](#lambda-s3-tutorial-pom)
+ [Write the code](#lambda-s3-tutorial-code)
+ [Package the project](#lambda-s3-tutorial-package)
+ [Deploy the Lambda function](#lambda-s3-tutorial-deploy)
+ [Test the Lambda method](#lambda-s3-tutorial-test)

## Prerequisites<a name="lambda-s3-tutorial-prerequisites"></a>

Before you begin, you need to complete the steps in [Setting Up the AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup.html)\. Then make sure that you have the following:
+ Java 1\.8 JDK\.
+ Maven 3\.6 or higher\.
+ An [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket with 5\-7 nature images in it\. These images are read by the Lambda function\.

## Configure the IAM Lambda role<a name="lambda-s3-tutorial-lambda-role"></a>

This tutorial uses the Amazon Rekognition and Amazon S3 services\. Configure the **lambda\-support** role to have policies that enable it to invoke these services from a Lambda function\.

**To configure the role**

1. Sign in to the AWS Management Console and open the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

1. In the navigation pane, choose **Roles**, then choose **Create Role**\.

1. Choose **AWS service**, and then choose **Lambda**\.

1. Choose the **Permissions** tab\.

1. Search for **AWSLambdaBasicExecutionRole**\.

1. Choose **Next tags**\.

1. Choose **Review**\.

1. Name the role **lambda\-support**\.

1. Choose **Create role**\.

1. Choose **lambda\-support** to view the overview page\.

1. Choose **Attach policies**\.

1. Choose *AmazonRekognitionFullAccess* from the list of policies\.

1. Choose **Attach policy**\.

1. Search for **AmazonS3FullAccess**, and then choose **Attach policy**\.

## Create the project<a name="lambda-s3-tutorial-pom"></a>

Create a new Java project, then configure the Maven pom\.xml with the required settings and dependencies\. Make sure your pom\.xml file looks like the following:

```
<?xml version="1.0" encoding="UTF-8"?>
 <project xmlns="http://maven.apache.org/POM/4.0.0"
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>
<groupId>org.example</groupId>
<artifactId>WorkflowTagAssets</artifactId>
<version>1.0-SNAPSHOT</version>
<packaging>jar</packaging>
<name>java-basic-function</name>
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
</properties>
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>software.amazon.awssdk</groupId>
            <artifactId>bom</artifactId>
            <version>2.10.54</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
   <dependency>
        <groupId>com.amazonaws</groupId>
        <artifactId>aws-lambda-java-core</artifactId>
        <version>1.2.1</version>
    </dependency>
    <dependency>
        <groupId>com.google.code.gson</groupId>
        <artifactId>gson</artifactId>
        <version>2.8.6</version>
    </dependency>
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-api</artifactId>
        <version>2.10.0</version>
    </dependency>
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-core</artifactId>
        <version>2.13.0</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-slf4j18-impl</artifactId>
        <version>2.13.3</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-api</artifactId>
        <version>5.6.0</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <version>5.6.0</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>com.googlecode.json-simple</groupId>
        <artifactId>json-simple</artifactId>
        <version>1.1.1</version>
    </dependency>
    <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>s3</artifactId>
    </dependency>
    <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>rekognition</artifactId>
    </dependency>
</dependencies>
<build>
    <plugins>
        <plugin>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>2.22.2</version>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-shade-plugin</artifactId>
            <version>3.2.2</version>
            <configuration>
                <createDependencyReducedPom>false</createDependencyReducedPom>
            </configuration>
            <executions>
                <execution>
                    <phase>package</phase>
                    <goals>
                        <goal>shade</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.8.1</version>
            <configuration>
                <source>1.8</source>
                <target>1.8</target>
            </configuration>
        </plugin>
    </plugins>
  </build>
 </project>
```

## Write the code<a name="lambda-s3-tutorial-code"></a>

Use the AWS Lambda runtime Java API to create the Java class that defines the Lambda function\. In this example, there is one Java class for the Lambda function named **Handler** and additional classes required for this use case\. The following figure shows the Java classes in the project\. Notice that all Java classes are located in a package named **com\.example\.tags**\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/v2-image-tutorial-files.png)

Create the following Java classes for the code:
+ **Handler** uses the Lambda Java run\-time API and performs the use case described in this AWS tutorial\. The application logic that's executed is located in the handleRequest method\.
+ **S3Service** uses the Amazon S3 API to perform S3 operations\.
+ **AnalyzePhotos** uses the Amazon Rekognition API to analyze the images\.
+ **BucketItem** defines a model that stores Amazon S3 bucket information\.
+ **WorkItem** defines a model that stores Amazon Rekognition data\.

### Handler class<a name="w93aac47b9c25c11"></a>

This Java code represents the **Handler** class\. The class reads a flag that is passed to the Lambda function\. The **s3Service\.ListBucketObjects** method returns a **List** object where each element is a string value that represents the object key\. If the flag value is true, then tags are applied by iterating through the list and applying tags to each object by calling the **s3Service\.tagAssets** method\. If the flag value is false, then the **s3Service\.deleteTagFromObject** method is invoked that deletes the tags\. Also, notice that you can log messages to Amazon CloudWatch logs by using a **LambdaLogger** object\.

**Note**  
Make sure you assign your bucket name to the **bucketName** variable\.

```
package com.example.tags;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.LambdaLogger;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Handler implements RequestHandler<Map<String,String>, String> {

@Override
public String handleRequest(Map<String, String> event, Context context) {
    LambdaLogger logger = context.getLogger();
    String delFag = event.get("flag");
    logger.log("FLAG IS: " + delFag);
    S3Service s3Service = new S3Service();
    AnalyzePhotos photos = new AnalyzePhotos();

    String bucketName = "<Enter your bucket name>";
    List<String> myKeys = s3Service.listBucketObjects(bucketName);
    if (delFag.compareTo("true") == 0) {

        // Create a List to store the data.
        List<ArrayList<WorkItem>> myList = new ArrayList<>();

        // loop through each element in the List and tag the assets.
        for (String key : myKeys) {

            byte[] keyData = s3Service.getObjectBytes(bucketName, key);

            // Analyze the photo and return a list where each element is a WorkItem.
            ArrayList<WorkItem> item = photos.detectLabels(keyData, key);
            myList.add(item);
        }

        s3Service.tagAssets(myList, bucketName);
        logger.log("All Assets in the bucket are tagged!");

    } else {

        // Delete all object tags.
        for (String key : myKeys) {
            s3Service.deleteTagFromObject(bucketName, key);
            logger.log("All Assets in the bucket are deleted!");
        }
     }
    return delFag;
  }
 }
```

### S3Service class<a name="w93aac47b9c25c13"></a>

The following class uses the Amazon S3 API to perform S3 operations\. For example, the **getObjectBytes** method returns a byte array that represents the image\. Likewise, the **listBucketObjects** method returns a **List** object where each element is a string value that specifies the key name\.

```
 package com.example.tags;

 import software.amazon.awssdk.core.ResponseBytes;
 import software.amazon.awssdk.regions.Region;
 import software.amazon.awssdk.services.s3.S3Client;
 import software.amazon.awssdk.services.s3.model.GetObjectRequest;
 import software.amazon.awssdk.services.s3.model.PutObjectTaggingRequest;
 import software.amazon.awssdk.services.s3.model.GetObjectResponse;
 import software.amazon.awssdk.services.s3.model.S3Exception;
 import software.amazon.awssdk.services.s3.model.ListObjectsResponse;
 import software.amazon.awssdk.services.s3.model.S3Object;
 import software.amazon.awssdk.services.s3.model.GetObjectTaggingResponse;
 import software.amazon.awssdk.services.s3.model.ListObjectsRequest;
 import java.util.ArrayList;
 import java.util.List;
 import software.amazon.awssdk.services.s3.model.Tagging;
 import software.amazon.awssdk.services.s3.model.Tag;
 import software.amazon.awssdk.services.s3.model.GetObjectTaggingRequest;
 import software.amazon.awssdk.services.s3.model.DeleteObjectTaggingRequest;

 public class S3Service {

 private S3Client getClient() {

    Region region = Region.US_WEST_2;
    return S3Client.builder()
            .region(region)
            .build();
 }

 public byte[] getObjectBytes(String bucketName, String keyName) {

    S3Client s3 = getClient();

    try {

        GetObjectRequest objectRequest = GetObjectRequest
                .builder()
                .key(keyName)
                .bucket(bucketName)
                .build();

        // Return the byte[] from this object.
        ResponseBytes<GetObjectResponse> objectBytes = s3.getObjectAsBytes(objectRequest);
        return objectBytes.asByteArray();

    } catch (S3Exception e) {
        System.err.println(e.awsErrorDetails().errorMessage());
        System.exit(1);
    }
    return null;
 }

 // Returns the names of all images in the given bucket.
 public List<String> listBucketObjects(String bucketName) {

    S3Client s3 = getClient();
    String keyName;

    List<String> keys = new ArrayList<>();

    try {
        ListObjectsRequest listObjects = ListObjectsRequest
                .builder()
                .bucket(bucketName)
                .build();

        ListObjectsResponse res = s3.listObjects(listObjects);
        List<S3Object> objects = res.contents();

        for (S3Object myValue: objects) {
            keyName = myValue.key();
            keys.add(keyName);
        }
        return keys;

    } catch (S3Exception e) {
        System.err.println(e.awsErrorDetails().errorMessage());
        System.exit(1);
    }
    return null;
 }

 // Tag assets with labels in the given list.
 public void tagAssets(List myList, String bucketName) {

    try {

        S3Client s3 = getClient();
        int len = myList.size();

        String assetName = "";
        String labelName = "";
        String labelValue = "";

        // Tag all the assets in the list.
        for (Object o : myList) {

            // Need to get the WorkItem from each list.
            List innerList = (List) o;
            for (Object value : innerList) {

                WorkItem workItem = (WorkItem) value;
                assetName = workItem.getKey();
                labelName = workItem.getName();
                labelValue = workItem.getConfidence();
                tagExistingObject(s3, bucketName, assetName, labelName, labelValue);
            }
        }

    } catch (S3Exception e) {
        System.err.println(e.awsErrorDetails().errorMessage());
        System.exit(1);
    }
 }

 // This method tags an existing object.
 private void tagExistingObject(S3Client s3, String bucketName, String key, String label, String LabelValue) {

    try {

        // First need to get existing tag set; otherwise the existing tags are overwritten.
        GetObjectTaggingRequest getObjectTaggingRequest = GetObjectTaggingRequest.builder()
                .bucket(bucketName)
                .key(key)
                .build();

        GetObjectTaggingResponse response = s3.getObjectTagging(getObjectTaggingRequest);

        // Get the existing immutable list - cannot modify this list.
        List<Tag> existingList = response.tagSet();
        ArrayList<Tag> newTagList = new ArrayList(new ArrayList<>(existingList));

        // Create a new tag.
        Tag myTag = Tag.builder()
                .key(label)
                .value(LabelValue)
                .build();

        // push new tag to list.
        newTagList.add(myTag);
        Tagging tagging = Tagging.builder()
                .tagSet(newTagList)
                .build();

        PutObjectTaggingRequest taggingRequest = PutObjectTaggingRequest.builder()
                .key(key)
                .bucket(bucketName)
                .tagging(tagging)
                .build();

        s3.putObjectTagging(taggingRequest);
        System.out.println(key + " was tagged with " + label);

    } catch (S3Exception e) {
        System.err.println(e.awsErrorDetails().errorMessage());
        System.exit(1);
    }
  }

 // Delete tags from the given object.
 public void deleteTagFromObject(String bucketName, String key) {

    try {

        DeleteObjectTaggingRequest deleteObjectTaggingRequest = DeleteObjectTaggingRequest.builder()
                .key(key)
                .bucket(bucketName)
                .build();

        S3Client s3 = getClient();
        s3.deleteObjectTagging(deleteObjectTaggingRequest);

    } catch (S3Exception e) {
        System.err.println(e.awsErrorDetails().errorMessage());
        System.exit(1);
    }
  }
}
```

### AnalyzePhotos class<a name="w93aac47b9c25c15"></a>

The following Java code represents the **AnalyzePhotos** class\. This class uses the Amazon Rekognition API to analyze the images\.

```
package com.example.tags;

import software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider;
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.rekognition.RekognitionClient;
import software.amazon.awssdk.services.rekognition.model.Image;
import software.amazon.awssdk.services.rekognition.model.DetectLabelsRequest;
import software.amazon.awssdk.services.rekognition.model.DetectLabelsResponse;
import software.amazon.awssdk.services.rekognition.model.Label;
import software.amazon.awssdk.services.rekognition.model.RekognitionException;
import java.util.ArrayList;
import java.util.List;

public class AnalyzePhotos {

 // Returns a list of WorkItem objects that contains labels.
 public ArrayList<WorkItem> detectLabels(byte[] bytes, String key) {

    Region region = Region.US_EAST_2;
    RekognitionClient rekClient = RekognitionClient.builder()
            .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
            .region(region)
            .build();

    try {

        SdkBytes sourceBytes = SdkBytes.fromByteArray(bytes);

        // Create an Image object for the source image.
        Image souImage = Image.builder()
                .bytes(sourceBytes)
                .build();

        DetectLabelsRequest detectLabelsRequest = DetectLabelsRequest.builder()
                .image(souImage)
                .maxLabels(10)
                .build();

        DetectLabelsResponse labelsResponse = rekClient.detectLabels(detectLabelsRequest);

        // Write the results to a WorkItem instance.
        List<Label> labels = labelsResponse.labels();
        ArrayList<WorkItem> list = new ArrayList<>();
        WorkItem item ;
        for (Label label: labels) {
            item = new WorkItem();
            item.setKey(key); // identifies the photo.
            item.setConfidence(label.confidence().toString());
            item.setName(label.name());
            list.add(item);
        }
        return list;

    } catch (RekognitionException e) {
        System.out.println(e.getMessage());
        System.exit(1);
    }
    return null ;
  }
}
```

### BucketItem class<a name="w93aac47b9c25c17"></a>

The following Java code represents the **BucketItem** class that stores Amazon S3 object data\.

```
package com.example.tags;

public class BucketItem {

 private String key;
 private String owner;
 private String date ;
 private String size ;


 public void setSize(String size) {
    this.size = size ;
 }

 public String getSize() {
    return this.size ;
 }

 public void setDate(String date) {
    this.date = date ;
 }

 public String getDate() {
    return this.date ;
 }

 public void setOwner(String owner) {
    this.owner = owner ;
 }

 public String getOwner() {
    return this.owner ;
 }

 public void setKey(String key) {
    this.key = key ;
 }

 public String getKey() {
    return this.key ;
 }
}
```

### WorkItem class<a name="w93aac47b9c25c19"></a>

The following Java code represents the **WorkItem** class\.

```
 package com.example.tags;

 public class WorkItem {

 private String key;
 private String name;
 private String confidence ;

public void setKey (String key) {
    this.key = key;
}

public String getKey() {
    return this.key;
}

public void setName (String name) {
    this.name = name;
}

public String getName() {
    return this.name;
}

public void setConfidence (String confidence) {
    this.confidence = confidence;
}

public String getConfidence() {
    return this.confidence;
}

}
```

## Package the project<a name="lambda-s3-tutorial-package"></a>

Package up the project into a \.jar \(JAR\) file by using the following Maven command\.

```
mvn package
```

The JAR file is located in the **target** folder \(which is a child folder of the project folder\)\.

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/v2-image-tutorial-folder.png)

**Note**  
Notice the use of the **maven\-shade\-plugin** in the project’s POM file\. This plugin is responsible for creating a JAR that contains the required dependencies\. If you attempt to package up the project without this plugin, the required dependences are not included in the JAR file and you will encounter a **ClassNotFoundException**\.

## Deploy the Lambda function<a name="lambda-s3-tutorial-deploy"></a>

1. Open the [Lambda console](https://console.aws.amazon.com/lambda/home)\.

1. Choose **Create Function**\.

1. Choose **Author from scratch**\.

1. In the **Basic information** section, enter **cron** as the name\.

1. In the **Runtime**, choose **Java 8**\.

1. Choose **Use an existing role**, and then choose **lambda\-support** \(the IAM role that you created\)\.

1. Choose **Create function**\.

1. For **Code entry type**, choose **Upload a \.zip or \.jar file**\.

1. Choose **Upload**, and then browse to the JAR file that you created\.

1. For **Handler**, enter the fully qualified name of the function, for example, **com\.example\.tags\.Handler:handleRequest** \(**com\.example\.tags** specifies the package, **Handler** is the class followed by :: and method name\)\.

1. Choose **Save**\.

## Test the Lambda method<a name="lambda-s3-tutorial-test"></a>

At this point in the tutorial, you can test the Lambda function\.

1. In the Lambda console, click the **Test** tab and then enter the following JSON\.

   ```
                    {
   "flag": "true"
    }
   ```  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/v2-image-tutorial-test.png)
**Note**  
Passing **true** tags the digital assets and passing **false** deletes the tags\.

1. Choose the **Invoke** button\. After the Lambda function is invoked, you see a successful message\.  
![\[Image NOT FOUND\]](http://docs.aws.amazon.com/rekognition/latest/dg/images/v2-image-tutorial-success.png)

Congratulations, you have created an AWS Lambda function that automactially applies tags to difital assets located in an Amazon S3 bucket\. As stated at the beginning of this tutorial, be sure to terminate all of the resources you created while going through this tutorial to ensure that you’re not charged\.

For more AWS multiservice examples, see the [AWS Documentation SDK examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/javav2/usecases)\.