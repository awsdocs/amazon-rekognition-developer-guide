# Amazon Rekognition API Permissions: Actions, Permissions, and Resources Reference<a name="api-permissions-reference"></a>

When you are setting up [Access Control](authentication-and-access-control.md#access-control) and writing a permissions policy that you can attach to an IAM identity \(identity\-based policies\), you can use the following table as a reference\. The table lists each Amazon Rekognition API operation, the corresponding actions for which you can grant permissions to perform the action, and the AWS resource for which you can grant the permissions\. You specify the actions in the policy's `Action` field, and you specify the resource value in the policy's `Resource` field\. 

You can use AWS\-wide condition keys in your Amazon Rekognition policies to express conditions\. For a complete list of AWS\-wide keys, see [Available Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys) in the *IAM User Guide*\. 

**Note**  
To specify an action, use the `rekognition` prefix followed by the API operation name \(for example, `rekognition:DeleteCollection`\)\.

If you see an expand arrow \(**↗**\) in the upper\-right corner of the table, you can open the table in a new window\. To close the window, choose the close button \(**X**\) in the lower\-right corner\.


**Amazon Rekognition API and Required Permissions for Actions**  

| Amazon Rekognition API Operations | Required Permissions \(API Actions\) | Resources | 
| --- | --- | --- | 
|  [CreateCollection](API_CreateCollection.md)  |  `rekognition:CreateCollection`  |  arn:aws:rekognition:region:account\-id:collection/collection\-id  | 
|  [DeleteCollection](API_DeleteCollection.md)  |  `rekognition:DeleteCollection`  |  `arn:aws:rekognition:region:account-id:collection/collection-id`  | 
|  [DeleteFaces](API_DeleteFaces.md)  |  `rekognition:DeleteFaces`  |  `arn:aws:rekognition:region:account-id:collection/collection-id`  | 
|  [DescribeCollection](API_DescribeCollection.md)  |  `rekognition:DescribeCollection`  |  `arn:aws:rekognition:region:account-id:collection/collection-id`  | 
|  [IndexFaces](API_IndexFaces.md)  |  rekognition:IndexFaces  |  `arn:aws:rekognition:region:account-id:collection/collection-id`  | 
|  [ListCollections](API_ListCollections.md)  | `rekognition:ListCollections` | `arn:aws:rekognition:region:account-id:*` | 
|  [ListFaces](API_ListFaces.md)  |  rekognition:ListFaces  |  `arn:aws:rekognition:region:account-id:collection/collection-id`  | 
|  [SearchFaces](API_SearchFaces.md)  | `rekognition:SearchFaces` | `arn:aws:rekognition:region:account-id:collection/collection-id` | 
|  [SearchFacesByImage](API_SearchFacesByImage.md)  |  rekognition:SearchFacesByImage  |  `arn:aws:rekognition:region:account-id:collection/collection-id`  | 
|  [CreateStreamProcessor](API_CreateStreamProcessor.md)  |  rekognition:CreateStreamProcessor  |  `arn:aws:rekognition:region:account-id:collection/collection-id` `arn:aws:rekognition:region:account-id:streamprocessor/stream-processor-name`  | 
|  [DeleteStreamProcessor](API_DeleteStreamProcessor.md)  |  rekognition:DeleteStreamProcessor  |  `arn:aws:rekognition:region:account-id:streamprocessor/stream-processor-name`  | 
|  [ListStreamProcessors](API_ListStreamProcessors.md)  |  rekognition:ListStreamProcessors  |  `arn:aws:rekognition:region:account-id:streamprocessor/stream-processor-name`  | 
|  [StartStreamProcessor](API_StartStreamProcessor.md)  |  rekognition:StartStreamProcessor  |  `arn:aws:rekognition:region:account-id:streamprocessor/stream-processor-name`  | 
|  [StopStreamProcessor](API_StopStreamProcessor.md)  |  rekognition:StopStreamProcessor  |  `arn:aws:rekognition:region:account-id:streamprocessor/stream-processor-name`  | 
|  [CompareFaces](API_CompareFaces.md)  |  rekognition:CompareFaces  |  None used\.  | 
|  [DetectFaces](API_DetectFaces.md)  |  rekognition:DetectFaces  |  None used\.  | 
|  [DetectLabels](API_DetectLabels.md)  |  rekognition:DetectLabels  |  None used\.  | 
|  [DetectModerationLabels](API_DetectModerationLabels.md)  |  rekognition:DetectModerationLabels  |  None used\.  | 
|  [DetectText](API_DetectText.md)  |  rekognition:DetectText  |  None used\.  | 
|  [GetCelebrityInfo](API_GetCelebrityInfo.md)  |  rekognition:GetCelebrityInfo  |  None used\.  | 
|  [RecognizeCelebrities](API_RecognizeCelebrities.md)  |  rekognition:RecognizeCelebrities  |  None used\.  | 
|  [GetCelebrityRecognition](API_GetCelebrityRecognition.md)  |  rekognition:GetCelebrityRecognition  |  None used\.  | 
|  [GetContentModeration](API_GetContentModeration.md)  |  rekognition:GetContentModeration  |  None used\.  | 
|  [GetFaceDetection](API_GetFaceDetection.md)  |  rekognition:GetFaceDetection  |  None used\.  | 
|  [GetLabelDetection](API_GetLabelDetection.md)  |  rekognition:GetLabelDetection  |  None used\.  | 
|  [GetPersonTracking](API_GetPersonTracking.md)  |  rekognition:GetPersonTracking  |  None used\.  | 
|  [StartCelebrityRecognition](API_StartCelebrityRecognition.md)  |  rekognition:StartCelebrityRecognition  |  None used\.  | 
|  [StartContentModeration](API_StartContentModeration.md)  |  rekognition:StartContentModeration  |  None used\.  | 
|  [StartFaceDetection](API_StartFaceDetection.md)  |  rekognition:StartFaceDetection  |  None used\.  | 
|  [StartFaceSearch](API_StartFaceSearch.md)  |  rekognition:StartFaceSearch  |  None used\.  | 
|  [StartLabelDetection](API_StartLabelDetection.md)  |  rekognition:StartLabelDetection  |  None used\.  | 
|  [StartPersonTracking](API_StartPersonTracking.md)  |  rekognition:StartPersonTracking  |  None used\.  | 
