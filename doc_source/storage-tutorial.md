# Storing Amazon Rekognition Data with Amazon RDS and DynamoDB<a name="storage-tutorial"></a>

When using Amazon Rekognition’s APIs, it’s important to remember that the API operations don’t save any of the generated labels\. You can save these labels by placing them in database, along with identifiers for the respective images\. 

This tutorial demonstrates detecting labels and saving those detected labels to a database\. The sample application developed in this tutorial will read images from an [Amazon S3 ](https://docs.aws.amazon.com/s3/index.html)bucket call the [ DetectLabels ](API_DetectLabels.md) operation on these images, and store the resulting labels in a database\. The application will store data in either an Amazon RDS database instance or a DynamoDB database, depending on which database type you'd like to use\.

You’ll use the [AWS SDK for Python](https://aws.amazon.com/sdk-for-python/) or this tutorial\. You can also see the AWS Documentation SDK examples [GitHub repo ](https://github.com/awsdocs/aws-doc-sdk-examples)for more Python tutorials\. 

**Topics**
+ [Prerequisites](#storage-tutorial-prerequisites)
+ [Getting Labels for Images in an Amazon S3 Bucket](#storage-tutorial-getting-labels)
+ [Creating an Amazyon DynamoDB Table](#storage-tutorial-creating-dynamodb)
+ [Uploading Data to DynamoDB](#storage-tutorial-uploading-dynamodb)
+ [Creating a MySQL Database in Amazon RDS](#storage-tutorial-creating-mysql)
+ [Uploading Data to a Amazon RDS MySQL Table](#storage-tutorial-uploading-mysql)

## Prerequisites<a name="storage-tutorial-prerequisites"></a>

Before you begin this tutorial, you’ll need install Python and complete the steps required to [set up the Python AWS SDK](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)\. Beyond this, ensure that you have:

[Created an AWS account and an IAM role](https://docs.aws.amazon.com/rekognition/latest/dg/setting-up.html)

[Installed the Python SDK \(Boto3\)](https://aws.amazon.com/sdk-for-python/)

[Properly configured your AWS access credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

[Created Amazon S3 bucket filled it with images](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)

[Created a RDS database instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html), if using RDS to store data



## Getting Labels for Images in an Amazon S3 Bucket<a name="storage-tutorial-getting-labels"></a>

Start by writing a function that will take the name of an image in your Amazon S3 bucket and retrieve that image\. This image will be displayed to confirm that the correct images are being passed into a call to [ DetectLabels ](API_DetectLabels.md) which is also in the function\. 

1. Find the Amazon S3 bucket you would like to use and write down its name\. You will make calls to this Amazon S3 bucket and read the images inside it\. Ensure your bucket contains some images to pass to the [ DetectLabels ](API_DetectLabels.md) operation\.

1. Write the code to connect to your Amazon S3 bucket\. You can connect to the Amazon S3 resource with Boto3 to retrieve an image from an Amazon S3 bucket\. Once connected to the Amazon S3 resource, you can access your bucket by providing the Bucket method with the name of your Amazon S3 bucket\. After connecting to the Amazon S3 bucket, you retrieve images from the bucket by using the Object method\. By making use of Matplotlib, you can use this connection to visualize your images as they process\. Boto3 is also used to connect to the Rekognition client\.

   In the following code, provide your region to the region\_name parameter\. You will pass the Amazon S3 bucket name and the image name to [ DetectLabels ](API_DetectLabels.md) , which returns the labels for the corresponding image\. After selecting just the labels from the response, both the name of the image and the labels are returned\.

   ```
   import boto3
   from io import BytesIO
   from matplotlib import pyplot as plt
   from matplotlib import image as mp_img
   
   boto3 = boto3.Session()
   
   def read_image_from_s3(bucket_name, image_name):
   
       # Connect to the S3 resource with Boto 3
       # get bucket and find object matching image name
       s3 = boto3.resource('s3')
       bucket = s3.Bucket(name=bucket_name)
       Object = bucket.Object(image_name)
   
       # Downloading the image for display purposes, not necessary for detection of labels
       # You can comment this code out if you don't want to visualize the images
       file_name = Object.key
       file_stream = BytesIO()
       Object.download_fileobj(file_stream)
       img = mp_img.imread(file_stream, format="jpeg")
       plt.imshow(img)
       plt.show()
   
       # get the labels for the image by calling DetectLabels from Rekognition
       client = boto3.client('rekognition', region_name="region-name")
       response = client.detect_labels(Image={'S3Object': {'Bucket': bucket_name, 'Name': image_name}},
                                       MaxLabels=10)
   
       print('Detected labels for ' + image_name)
   
       full_labels = response['Labels']
   
       return file_name, full_labels
   ```

1. Save this code in a file called get\_images\.py\.

## Creating an Amazyon DynamoDB Table<a name="storage-tutorial-creating-dynamodb"></a>

The following code uses Boto3 to connect to DynamoDB and uses the DynamoDB `CreateTable` method to create a table named Images\. The table has a composite primary key consisting of a partition key called Image and a sort key called Labels\. The Image key contains the name of the image, while the Labels key stores the labels assigned to that Image\. 

```
import boto3

def create_new_table(dynamodb=None):
    dynamodb = boto3.resource(
        'dynamodb',)
    # Table defination
    table = dynamodb.create_table(
        TableName='Images',
        KeySchema=[
            {
                'AttributeName': 'Image',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'Labels',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'Image',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Labels',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table

if __name__ == '__main__':
    device_table = create_new_table()
    print("Status:", device_table.table_status)
```

Save this code in an editor and run it once to create a DynamoDB table\.

## Uploading Data to DynamoDB<a name="storage-tutorial-uploading-dynamodb"></a>

Now that the DynamoDB database has been created and you have a function to get labels for images, you can store the labels in DynamoDB The following code retrieves all the images in an S3 bucket, get labels for them, and stores the data in DynamoDB\.

1. You’ll need to write the code for uploading the data to DynamoDB\. A function called `get_image_names` is used to connect to your Amazon S3 bucket and it returns the names of all images in the bucket as a list\. You’ll pass this list into the `read_image_from_S3` function, which is imported from the `get_images.py` file you created\. 

   ```
   import boto3
   import json
   from get_images import read_image_from_s3
   
   boto3 = boto3.Session()
   
   def get_image_names(name_of_bucket):
   
       s3_resource = boto3.resource('s3')
       my_bucket = s3_resource.Bucket(name_of_bucket)
       file_list = []
       for file in my_bucket.objects.all():
           file_list.append(file.key)
       return file_list
   ```

1. The `read_image_from_S3` function we created earlier will return the name of the image being processed and the dictionary of labels associated with that image\. A function called `find_values` is used to get just the labels from the response\. The name of the image and its labels are then ready to be uploaded to your DynamoDB table\.

   ```
   def find_values(id, json_repr):
       results = []
   
       def _decode_dict(a_dict):
           try:
               results.append(a_dict[id])
           except KeyError:
               pass
           return a_dict
   
       json.loads(json_repr, object_hook=_decode_dict) # Return value ignored.
       return results
   ```

1. You will use a third function, called `load_data`, to actually load the images and labels into the DynamoDB table you created\.

   ```
   def load_data(image_labels, dynamodb=None):
   
       if not dynamodb:
           dynamodb = boto3.resource('dynamodb')
   
       table = dynamodb.Table('Images')
   
       print("Adding image details:", image_labels)
       table.put_item(Item=image_labels)
       print("Success!!")
   ```

1. Here’s where the three functions we defined previously are called, and the operations are carried out\. Add the three functions defined above, along with the code below, to a Python file\. Run the code\. 

   ```
   bucket = "bucket_name"
   file_list = get_image_names(bucket)
   
   for file in file_list:
       file_name = file
       print("Getting labels for " + file_name)
       image_name, image_labels = read_image_from_s3(bucket, file_name)
       image_json_string = json.dumps(image_labels, indent=4)
       labels=set(find_values("Name", image_json_string))
       print("Labels found: " + str(labels))
       labels_dict = {}
       print("Saving label data to database")
       labels_dict["Image"] = str(image_name)
       labels_dict["Labels"] = str(labels)
       print(labels_dict)
       load_data(labels_dict)
       print("Success!")
   ```

You’ve just used [ DetectLabels ](API_DetectLabels.md) to generate labels for your images and stored those labels in an DynamoDB instance\. Be sure that you tear down all the resources you created while going through this tutorial\. That will prevent you from being charged for resources you aren’t using\. 

## Creating a MySQL Database in Amazon RDS<a name="storage-tutorial-creating-mysql"></a>

Before going further, make sure you have completed the [setup procedure](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SettingUp.html) for Amazon RDS and [created a MySQL DB instance ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html)using Amazon RDS\.

The following code makes use of the [PyMySQL](https://pypi.org/project/PyMySQL/) library and your Amazon RDS DB instance\. It creates a table to hold the names of your images and the labels associated with those images\. Amazon RDS receives commands to create tables and insert data into tables\. To use Amazon RDS, you must connect to the Amazon RDS host using your host name, username, and password\. You'll connect to Amazon RDS by providing these arguments to PyMySQL's `connect` function and creating an instance of a cursor\.

1. In the following code, replace the value of host with your Amazon RDS host endpoint and replace the value of user with the master username associated with your Amazon RDS instance\. You will also need to replace password with the master password for your main user\.

   ```
   import pymysql
   
   host = "host-endpoint"
   user = "username"
   password = "master-password"
   ```

1. Create a database and a table to insert your image and label data into\. Do this by running and committing a creation query\. The following code creates a database\. Run this code only once\.

   ```
   conn = pymysql.connect(host=host, user=user, passwd=password)
   print(conn)
   cursor = conn.cursor()
   print("Connection successful")
   
   # run once
   create_query = "create database rekogDB1"
   print("Creation successful!")
   cursor.execute(create_query)
   cursor.connection.commit()
   ```

1. Once the database has been created, you must create a table to insert your image names and labels into\. To create a table, you will first pass the use SQL command, along with the name of your database, to the `execute` function\. After the connection is made, a query to create a table is run\. The following code connects to the database and then creates a table with both a primary key, called `image_id`, and a text attribute storing the labels\. Use the imports and variables you defined earlier, and run this code to create a table in your database\. 

   ```
   # connect to existing DB
   cursor.execute("use rekogDB1")
   cursor.execute("CREATE TABLE IF NOT EXISTS test_table(image_id VARCHAR (255) PRIMARY KEY, image_labels TEXT)")
   conn.commit()
   print("Table creation - Successful creation!")
   ```

## Uploading Data to a Amazon RDS MySQL Table<a name="storage-tutorial-uploading-mysql"></a>

 After creating the Amazon RDS database and a table in the database, you can get labels for your images and store those labels in the Amazon RDS database\. 

1. Connect to your Amazon S3 bucket and retrieve the names of all the images in the bucket\. These image names will be passed into the `read_image_from_s3` function you created earlier to get the labels for all your images\. The following code connects to your Amazon S3 bucket and returns a list of all the images in your bucket\.

   ```
   import pymysql
   from get_images import read_image_from_s3
   import json
   import boto3
   
   host = "host-endpoint"
   user = "username"
   password = "master-password"
   
   conn = pymysql.connect(host=host, user=user, passwd=password)
   print(conn)
   cursor = conn.cursor()
   print("Connection successful")
   
   def get_image_names(name_of_bucket):
   
       s3_resource = boto3.resource('s3')
       my_bucket = s3_resource.Bucket(name_of_bucket)
       file_list = []
       for file in my_bucket.objects.all():
           file_list.append(file.key)
       return file_list
   ```

1. The response from the [ DetectLabels ](API_DetectLabels.md) API contains more than just the labels, so write a function to extract only the label values\. The following function returns a list full of just the labels\.

   ```
   def find_values(id, json_repr):
       results = []
   
       def _decode_dict(a_dict):
           try:
               results.append(a_dict[id])
           except KeyError:
               pass
           return a_dict
   
       json.loads(json_repr, object_hook=_decode_dict) # Return value ignored.
       return results
   ```

1. You will need a function to insert the image names and labels into your table\. The following function runs an insertion query and inserts any given pair of image name and labels\.

   ```
   def upload_data(image_id, image_labels):
   
       # insert into db
       cursor.execute("use rekogDB1")
       query = "INSERT IGNORE INTO test_table(image_id, image_labels) VALUES (%s, %s)"
       values = (image_id, image_labels)
       cursor.execute(query, values)
       conn.commit()
       print("Insert successful!")
   ```

1. Finally, you must run the functions you defined above\. In the following code, the names of all the images in your bucket are collected and provided to the function that calls [ DetectLabels ](API_DetectLabels.md)\. Afterward, the labels and the name of the image they apply to are uploaded to your Amazon RDS database\. Copy the three functions defined above, along with the code below, into a Python file\. Run the Python file\.

   ```
   bucket = "bucket-name"
   file_list = get_image_names(bucket)
   
   for file in file_list:
       file_name = file
       print("Getting labels for " + file_name)
       image_name, image_labels = read_image_from_s3(bucket, file_name)
       image_json = json.dumps(image_labels, indent=4)
       labels=set(find_values("Name", image_json))
       print("Labels found: " + str(labels))
       unique_labels=set(find_values("Name", image_json))
       print(unique_labels)
       image_name_string = str(image_name)
       labels_string = str(unique_labels)
       upload_data(image_name_string, labels_string)
       print("Success!")
   ```

You have successfully used DetectLabels to generate labels for your images and stored those labels in a MySQL database using Amazon RDS\. Be sure that you tear down all the resources you created while going through this tutorial\. This will prevent you from being charged for resources you aren’t using\. 

For more AWS multiservice examples, see the AWS Documentation SDK examples [GitHub repository\.](https://github.com/awsdocs/aws-doc-sdk-examples)