# Using Python<a name="images-bytes-python"></a>

The following [AWS SDK for Python](https://aws.amazon.com/sdk-for-python/) example shows how to load an image from the local file system and call the [detect\_labels](http://boto3.readthedocs.org/en/latest/reference/services/rekognition.html#Rekognition.Client.detect_labels) operation\. 

```
import boto3

if __name__ == "__main__":

    imageFile='input.jpg'
    client=boto3.client('rekognition','us-west-2')
   
    with open(imageFile, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        
    print('Detected labels in ' + imageFile)    
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))

    print('Done...')
```