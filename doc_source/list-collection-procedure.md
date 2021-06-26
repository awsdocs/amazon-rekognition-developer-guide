# Listing collections<a name="list-collection-procedure"></a>

You can use the [ListCollections](API_ListCollections.md) operation to list the collections in the region that you are using\.

For more information, see [Managing collections](collections.md#managing-collections)\. 



**To list collections \(SDK\)**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` permissions\. For more information, see [Step 1: Set up an AWS account and create an IAM user](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Use the following examples to call the `ListCollections` operation\.

------
#### [ Java ]

   The following example lists the collections in the current region\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   package aws.example.rekognition.image;
   
   import java.util.List;
   import com.amazonaws.services.rekognition.AmazonRekognition;
   import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
   import com.amazonaws.services.rekognition.model.ListCollectionsRequest;
   import com.amazonaws.services.rekognition.model.ListCollectionsResult;
   
   public class ListCollections {
   
      public static void main(String[] args) throws Exception {
   
   
         AmazonRekognition amazonRekognition = AmazonRekognitionClientBuilder.defaultClient();
    
   
         System.out.println("Listing collections");
         int limit = 10;
         ListCollectionsResult listCollectionsResult = null;
         String paginationToken = null;
         do {
            if (listCollectionsResult != null) {
               paginationToken = listCollectionsResult.getNextToken();
            }
            ListCollectionsRequest listCollectionsRequest = new ListCollectionsRequest()
                    .withMaxResults(limit)
                    .withNextToken(paginationToken);
            listCollectionsResult=amazonRekognition.listCollections(listCollectionsRequest);
            
            List < String > collectionIds = listCollectionsResult.getCollectionIds();
            for (String resultId: collectionIds) {
               System.out.println(resultId);
            }
         } while (listCollectionsResult != null && listCollectionsResult.getNextToken() !=
            null);
        
      } 
   }
   ```

------
#### [ AWS CLI ]

   This AWS CLI command displays the JSON output for the `list-collections` CLI operation\. 

   ```
   aws rekognition list-collections 
   ```

------
#### [ Python ]

   The following example lists the collections in the current region\.

   ```
   #Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   #PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   import boto3
   
   def list_collections():
   
       max_results=2
       
       client=boto3.client('rekognition')
   
       #Display all the collections
       print('Displaying collections...')
       response=client.list_collections(MaxResults=max_results)
       collection_count=0
       done=False
       
       while done==False:
           collections=response['CollectionIds']
   
           for collection in collections:
               print (collection)
               collection_count+=1
           if 'NextToken' in response:
               nextToken=response['NextToken']
               response=client.list_collections(NextToken=nextToken,MaxResults=max_results)
               
           else:
               done=True
   
       return collection_count   
   
   def main():
   
       collection_count=list_collections()
       print("collections: " + str(collection_count))
   if __name__ == "__main__":
       main()
   ```

------
#### [ \.NET ]

   The following example lists the collections in the current region\.

   ```
   //Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
   //PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)
   
   using System;
   using Amazon.Rekognition;
   using Amazon.Rekognition.Model;
   
   public class ListCollections
   {
       public static void Example()
       {
           AmazonRekognitionClient rekognitionClient = new AmazonRekognitionClient();
   
           Console.WriteLine("Listing collections");
           int limit = 10;
   
           ListCollectionsResponse listCollectionsResponse = null;
           String paginationToken = null;
           do
           {
               if (listCollectionsResponse != null)
                   paginationToken = listCollectionsResponse.NextToken;
   
               ListCollectionsRequest listCollectionsRequest = new ListCollectionsRequest()
               {
                   MaxResults = limit,
                   NextToken = paginationToken
               };
   
               listCollectionsResponse = rekognitionClient.ListCollections(listCollectionsRequest);
   
               foreach (String resultId in listCollectionsResponse.CollectionIds)
                   Console.WriteLine(resultId);
           } while (listCollectionsResponse != null && listCollectionsResponse.NextToken != null);
       }
   }
   ```

------

## ListCollections operation request<a name="listcollections-request"></a>

The input to `ListCollections` is the maximum number of collections to be returned\. 

```
{
    "MaxResults": 2
}
```

If the response has more collections than are requested by `MaxResults`, a token is returned that you can use to get the next set of results, in a subsequent call to `ListCollections`\. For example:

```
{
    "NextToken": "MGYZLAHX1T5a....",
    "MaxResults": 2
}
```

## ListCollections operation response<a name="listcollections-operation-response"></a>

Amazon Rekognition returns an array of collections \(`CollectionIds`\)\. A separate array \(`FaceModelversions`\) provides the version of the face model used to analyze faces in each collection\. For example, in the following JSON response, the collection `MyCollection` analyzes faces by using version 2\.0 of the face model\. The collection `AnotherCollection` uses version 3\.0 of the face model\. For more information, see [Model versioning](face-detection-model.md)\.

`NextToken` is the token that's used to get the next set of results, in a subsequent call to `ListCollections`\. 

```
{
    "CollectionIds": [
        "MyCollection",
        "AnotherCollection"
    ],
    "FaceModelVersions": [
        "2.0",
        "3.0"
    ],
    "NextToken": "MGYZLAHX1T5a...."
}
```