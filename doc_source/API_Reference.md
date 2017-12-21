# API Reference<a name="API_Reference"></a>

 This section provides documentation for the Amazon Rekognition API operations\. 

## HTTP Headers<a name="http-headers"></a>

Beyond the usual HTTP headers, Amazon Rekognition HTTP operations have the following required headers:


| Header | Value | Description | 
| --- | --- | --- | 
|  Content\-Type:  |  application/x\-amz\-json\-1\.1  |  Specifies that the request content is JSON\. Also specifies the JSON version\.  | 
|  X\-Amz\-Date:  |  <Date>  |  The date used to create the signature in the Authorization header\. The format must be ISO 8601 basic in the YYYYMMDD'T'HHMMSS'Z' format\. For example, the following date/time 20141123T120000Z is a valid x\-amz\-date for use with Amazon Rekognition\.   | 
|  X\-Amz\-Target:  |  RekognitionService\.<operation>  |  The target Amazon Rekognition operation\. For example, use `RekognitionService.ListCollections` to call the `ListCollections` operation\.  | 

**Topics**

+ [Actions](API_Operations.md)

+ [Data Types](API_Types.md)