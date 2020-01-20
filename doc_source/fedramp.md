# Using Amazon Rekognition as a FedRAMP Authorized Service<a name="fedramp"></a>

The AWS FedRAMP compliance program includes Amazon Rekognition as a FedRAMP\-authorized service\. If you're a federal or commercial customer, you can use the service to process and store sensitive workloads in the AWS US East and US West Regions, with data up to the moderate\-impact level\. You can use the service for sensitive workloads in the AWS GovCloud \(US\) Region's authorization boundary, with data up to the high\-impact level\. For more information about FedRAMP compliance, see [AWS FedRAMP Compliance](https://aws.amazon.com/compliance/fedramp/)\.

To be FedRAMP compliant, you can use a Federal Information Processing Standard \(FIPS\) endpoint\. This gives you access to FIPS 140\-2 validated cryptographic modules when you're working with sensitive information\. For more information about FIPS endpoints, see [FIPS 140\-2 Overview](https://aws.amazon.com/compliance/fips/)\.

You can use the AWS Command Line Interface \(AWS CLI\) or one of the AWS SDKs to specify the endpoint that is used by Amazon Rekognition\.

For endpoints that can be used with Amazon Rekognition, see [Amazon Rekognition Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#rekognition_region)\.

The following are examples from the [Listing Collections ](list-collection-procedure.md) topic in the *Amazon Rekognition Developer Guide*\. They are modified to specify the Region and FIPS endpoint through which Amazon Rekognition is accessed\.

------
#### [ Java ]

For Java, use the `withEndpointConfiguration` method when you construct the Amazon Rekognition client\. This example shows the collections you have that use the FIPS endpoint in the US East \(N\.Virginia\) Region:

```
//Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
//PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

package aws.example.rekognition.image;

import java.util.List;

import com.amazonaws.services.rekognition.AmazonRekognition;
import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
import com.amazonaws.services.rekognition.model.ListCollectionsRequest;
import com.amazonaws.services.rekognition.model.ListCollectionsResult;

public class ListCollections {

   public static void main(String[] args) throws Exception {


      AmazonRekognition amazonRekognition = AmazonRekognitionClientBuilder.standard()
         .withEndpointConfiguration(new AwsClientBuilder.EndpointConfiguration("https://rekognition-fips.us-east-1.amazonaws.com","us-east-1"))
         .build();
 

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

For the AWS CLI, use the `--endpoint-url` argument to specify the endpoint through which Amazon Rekognition is accessed\. This example shows the collections you have that use the FIPS endpoint in the US East \(Ohio\) Region:

```
aws rekognition list-collections --endpoint-url https://rekognition-fips.us-east-2.amazonaws.com --region us-east-2
```

------
#### [ Python ]

For Python, use the `endpoint_url` argument in the boto3\.client function\. Set it to the endpoint that you want to specify\. This example shows the collections you have that use the FIPS endpoint in the US West \(Oregon\) Region:

```
#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def list_collections():

    max_results=2
    
    client=boto3.client('rekognition', endpoint_url='https://rekognition-fips.us-west-2.amazonaws.com', region_name='us-west-2')

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