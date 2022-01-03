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

------
#### [ AWS CLI ]

```
aws rekognition create-collection --collection-id "collection name"\
                --tags '{"key1":"value1","key2":"value2"}'
```

------
#### [ Python ]

```
import boto3

def create_collection(collection_id):
    client = boto3.client('rekognition')

    # Create a collection
    print('Creating collection:' + collection_id)
    response = client.create_collection(CollectionId=collection_id)
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')

def main():
    collection_id = 'NewCollectionName'
    create_collection(collection_id)

if __name__ == "__main__":
    main()
```

------

## Add tags to an existing collection<a name="add-tag-existing-collection"></a>

To add one or more tags to an existing collection, use the `TagResource` operation\. Specify the collection's Amazon Resource Name \(ARN\) \(`ResourceArn`\) and the tags \(`Tags`\) that you want to add\. The following example shows how to add two tags\.

------
#### [ AWS CLI ]

```
aws rekognition tag-resource --resource-arn resource-arn \
                --tags '{"key1":"value1","key2":"value2"}'
```

------
#### [ Python ]

```
import boto3

def create_tag():
    client = boto3.client('rekognition')
    response = client.tag_resource(ResourceArn="arn:aws:rekognition:region-name:5498347593847598:collection/NewCollectionName",
                                   Tags={
                                       "KeyName": "ValueName"
                                   })
    print(response)
    if "'HTTPStatusCode': 200" in str(response):
        print("Success!!")

def main():
    create_tag()

if __name__ == "__main__":
    main()
```

------

**Note**  
If you do not know the collection's Amazon Resource Name, you can use the `DescribeCollection` operation\.

## List tags in a collection<a name="list-tags-collection"></a>

To list the tags attached to a collection, use the `ListTagsForResource` operation and specify the ARN of the collection \(`ResourceArn`\)\. The response is a map of tag keys and values that are attached to the specified collection\.

------
#### [ AWS CLI ]

```
aws rekognition list-tags-for-resource --resource-arn resource-arn
```

------
#### [ Python ]

```
import boto3

def list_tags():
    client = boto3.client('rekognition')
    response = client.list_tags_for_resource(ResourceArn="arn:aws:rekognition:region-name:5498347593847598:collection/NewCollectionName")
    print(response)

def main():
    list_tags()

if __name__ == "__main__":
    main()
```

------

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

------
#### [ AWS CLI ]

```
aws rekognition untag-resource --resource-arn resource-arn \
                --tag-keys '["key1","key2"]'
```

Alternatively, you can specify tag\-keys in this format:

```
--tag-keys key1,key2
```

------
#### [ Python ]

```
import boto3

def list_tags():
    client = boto3.client('rekognition')
    response = client.untag_resource(ResourceArn="arn:aws:rekognition:region-name:5498347593847598:collection/NewCollectionName", TagKeys=['KeyName'])
    print(response)

def main():
    list_tags()

if __name__ == "__main__":
    main()
```

------