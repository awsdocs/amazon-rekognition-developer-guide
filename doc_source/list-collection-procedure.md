# Listing Collections<a name="list-collection-procedure"></a>

You can use the [ListCollections](API_ListCollections.md) operation to list the collections in the region that you are using\.

For more information, see [Managing Collections](collections.md#managing-collections)\. 

**To list collections \(SDK\)**

1. If you haven't already:

   1. Create or update an IAM user with `AmazonRekognitionFullAccess` permissions\. For more information, see [Step 1: Set Up an AWS Account and Create an IAM User](setting-up.md#setting-up-iam)\.

   1. Install and configure the AWS CLI and the AWS SDKs\. For more information, see [Step 2: Set Up the AWS CLI and AWS SDKs](setup-awscli-sdk.md)\.

1. Use the following examples to call the `ListCollections` operation\.

------
#### [ Java ]

   The following example lists the collections in the current region\.

   ```
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
   import boto3
   
   if __name__ == "__main__":
   
       maxResults=2
       
       client=boto3.client('rekognition')
   
       #Display all the collections
       print('Displaying collections...')
       response=client.list_collections(MaxResults=maxResults)
   
       while True:
           collections=response['CollectionIds']
   
           for collection in collections:
               print (collection)
           if 'NextToken' in response:
               nextToken=response['NextToken']
               response=client.list_collections(NextToken=nextToken,MaxResults=maxResults)
               
           else:
               break
   
       print('done...')
   ```

------
#### [ \.NET ]

   The following example lists the collections in the current region\.

   ```
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

## ListCollections Operation Request<a name="listcollections-request"></a>

The input to `ListCollections` is the maximum number of collections to be returned\. 

```
{
    "MaxResults": 2
}
```

If the response has more faces than requested by `MaxResults`, a token is returned that you can use to get the next set of results, in a subsequent call to `ListCollections`\. For example:

```
{
    "NextToken": "MGYZLAHX1T5a....",
    "MaxResults": 2
}
```

## ListCollections Operation Response<a name="listcollections-operation-response"></a>

Amazon Rekognition returns an array of collections \(`CollectionIds`\)\. A separate array \(`FaceModelversions`\) provides the version of the face model used to analyze faces in each collection\. For example, in the following JSON response, the collection `MyCollection` analyzes faces by using version 2\.0 of the face model\. The collection `AnotherCollection` uses version 3\.0 of the face model\. For more information, see [Model Versioning](face-detection-model.md)\.

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