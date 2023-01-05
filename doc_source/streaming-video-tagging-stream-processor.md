# Tagging the Amazon Rekognition Video stream processor<a name="streaming-video-tagging-stream-processor"></a>

You can identify, organize, search for, and filter Amazon Rekognition stream processors by using tags\. Each tag is a label consisting of a user\-defined key and value\.

**Topics**
+ [Add tags to a new stream processor](#add-tag-new-stream-processor)
+ [Add tags to an existing stream processor](#add-tag-existing-stream-processor)
+ [List tags in a stream processor](#list-tags-stream-processor)
+ [Delete tags from a stream processor](#delete-tag-stream-processor)

## Add tags to a new stream processor<a name="add-tag-new-stream-processor"></a>

You can add tags to a stream processor as you create it using the `CreateStreamProcessor` operation\. Specify one or more tags in the `Tags` array input parameter\. The following is a JSON example for the `CreateStreamProcessor` request with tags\.

```
{
       "Name": "streamProcessorForCam",
       "Input": {
              "KinesisVideoStream": {
                     "Arn": "arn:aws:kinesisvideo:us-east-1:nnnnnnnnnnnn:stream/inputVideo"
              }
       },
       "Output": {
              "KinesisDataStream": {
                     "Arn": "arn:aws:kinesis:us-east-1:nnnnnnnnnnnn:stream/outputData"
              }
       },
       "RoleArn": "arn:aws:iam::nnnnnnnnnnn:role/roleWithKinesisPermission",
       "Settings": {
              "FaceSearch": {
                     "CollectionId": "collection-with-100-faces",
                     "FaceMatchThreshold": 85.5
              },
              "Tags": { 
      "Dept": "Engineering",
        "Name": "Ana Silva Carolina",
        "Role": "Developer"
       }
}
```

## Add tags to an existing stream processor<a name="add-tag-existing-stream-processor"></a>

To add one or more tags to an existing stream processor, use the `TagResource` operation\. Specify the stream processor's Amazon Resource Name \(ARN\) \(`ResourceArn`\) and the tags \(`Tags`\) that you want to add\. The following example shows how to add two tags\.

```
aws rekognition tag-resource --resource-arn resource-arn \
                --tags '{"key1":"value1","key2":"value2"}'
```

**Note**  
If you do not know the stream processor's Amazon Resource Name, you can use the `DescribeStreamProcessor` operation\.

## List tags in a stream processor<a name="list-tags-stream-processor"></a>

To list the tags attached to a stream processor, use the `ListTagsForResource` operation and specify the ARN of the stream processor \(`ResourceArn`\)\. The response is a map of tag keys and values that are attached to the specified stream processor\.

```
aws rekognition list-tags-for-resource --resource-arn resource-arn
```

The output displays a list of tags attached to the stream processor:

```
                {
    "Tags": {
        "Dept": "Engineering",
        "Name": "Ana Silva Carolina",
        "Role": "Developer"
    }
}
```

## Delete tags from a stream processor<a name="delete-tag-stream-processor"></a>

To remove one or more tags from a stream processor, use the `UntagResource` operation\. Specify the ARN of the model \(`ResourceArn`\) and the tag keys \(`Tag-Keys`\) that you want to remove\.

```
aws rekognition untag-resource --resource-arn resource-arn \
                --tag-keys '["key1","key2"]'
```

Alternatively, you can specify tag\-keys in this format:

```
--tag-keys key1,key2
```