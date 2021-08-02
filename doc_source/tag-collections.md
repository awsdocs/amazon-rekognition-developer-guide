# Tagging collections<a name="tag-collections"></a>

You can identify, organize, search for, and filter Amazon Rekognition collections by using tags\. Each tag is a label consisting of a user\-defined key and value\.

You can also use tags to control access for a collection by using Identity and Access Management \(IAM\)\. For more information, see [Controlling access to AWS resources using resource tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html)\.

**Topics**
+ [Add tags to a new collection](#add-tag-new-collection)
+ [Add tags to an existing collection](#add-tag-existing-collection)
+ [List tags in a collection](#list-tags-collection)
+ [Delete tags from a collection](#delete-tag-collection)

## Add tags to a new collection<a name="add-tag-new-collection"></a>

You can add tags to a collection as you create it using the `CreateCollection` operation\. Specify one or more tags in the `Tags` array input parameter\.

```
aws rekognition create-collection --collection-id "collection name"\
                --tags '{"key1":"value1","key2":"value2"}'
```

## Add tags to an existing collection<a name="add-tag-existing-collection"></a>

To add one or more tags to an existing collection, use the `TagResource` operation\. Specify the collection's Amazon Resource Name \(ARN\) \(`ResourceArn`\) and the tags \(`Tags`\) that you want to add\. The following example shows how to add two tags\.

```
aws rekognition tag-resource --resource-arn resource-arn \
                --tags '{"key1":"value1","key2":"value2"}'
```

**Note**  
If you do not know the collection's Amazon Resource Name, you can use the `DescribeCollection` operation\.

## List tags in a collection<a name="list-tags-collection"></a>

To list the tags attached to a collection, use the `ListTagsForResource` operation and specify the ARN of the collection \(`ResourceArn`\)\. The response is a map of tag keys and values that are attached to the specified collection\.

```
aws rekognition list-tags-for-resource --resource-arn resource-arn
```

The output displays a list of tags attached to the collection:

```
                {
    "Tags": {
        "Dept": "Engineering",
        "Name": "Ana Silva Carolina",
        "Role": "Developer"
    }
}
```

## Delete tags from a collection<a name="delete-tag-collection"></a>

To remove one or more tags from a collection, use the `UntagResource` operation\. Specify the ARN of the model \(`ResourceArn`\) and the tag keys \(`Tag-Keys`\) that you want to remove\.

```
aws rekognition untag-resource --resource-arn resource-arn \
                --tag-keys '["key1","key2"]'
```

Alternatively, you can specify tag\-keys in this format:

```
--tag-keys key1,key2
```