# What Is Amazon Rekognition?<a name="what-is"></a>

Amazon Rekognition makes it easy to add image and video analysis to your applications\. You just provide an image or video to the Rekognition API, and the service can identify objects, people, text, scenes, and activities\. It can detect any inappropriate content as well\. Amazon Rekognition also provides highly accurate facial analysis and facial recognition\. You can detect, analyze, and compare faces for a wide variety of use cases, including user verification, cataloging, people counting, and public safety\.

Amazon Rekognition is based on the same proven, highly scalable, deep learning technology developed by Amazon’s computer vision scientists to analyze billions of images and videos daily—and requires no machine learning expertise to use\. Amazon Rekognition includes a simple, easy\-to\-use API that can quickly analyze any image or video file that’s stored in Amazon S3\. Amazon Rekognition is always learning from new data, and we’re continually adding new labels and facial recognition features to the service\. 

Common use cases for using Amazon Rekognition include the following:

+ **Searchable image and video libraries** – Amazon Rekognition makes images and stored videos searchable so you can discover objects and scenes that appear within them\. 

   

+ **Face\-based user verification** – Amazon Rekognition enables your applications to confirm user identities by comparing their live image with a reference image\.

   

+ **Sentiment and demographic analysis** – Amazon Rekognition detects emotions such as happy, sad, or surprise, and demographic information such as gender from facial images\. Rekognition can analyze images, and send the emotion and demographic attributes to Amazon Redshift for periodic reporting on trends such as in store locations and similar scenarios\.

   

+ **Facial recognition** – With Amazon Rekognition, you can search images, stored videos, and streaming videos for faces that match those stored in a container known as a face collection\. A face collection is an index of faces that you own and manage\. Identifying people based on their faces requires two major steps in Amazon Rekognition: 

  1. Index the faces\.

  1. Search the faces\.

   

+ **Unsafe Content Detection** – Amazon Rekognition can detect explicit and suggestive adult content in images and in videos\. Developers can use the returned metadata to filter inappropriate content based on their business needs\. Beyond flagging an image based on the presence of adult content, the API also returns a hierarchical list of labels with confidence scores\. These labels indicate specific categories of adult content, thus allowing granular filtering and management of large volumes of user generated content \(UGC\)\. For example, social and dating sites, photo sharing platforms, blogs and forums, apps for children, e\-commerce sites, entertainment and online advertising services\. 

   

+ **Celebrity recognition** – Amazon Rekognition can recognize celebrities within supplied images and in videos\. Rekognition can recognize thousands of celebrities across a number of categories, such as politics, sports, business, entertainment, and media\. 

   

+ **Text detection** – Amazon Rekognition Text in Image allows you to recognize and extract textual content from images\. Text in Image supports most fonts including highly stylized ones\. It detects text and numbers in different orientations such as those commonly found in banners and posters\. In image sharing and social media applications, you can use it to enable visual search based on an index of images that contain the same keywords\. In media and entertainment applications, you can catalogue videos based on relevant text on screen, such as ads, news, sport scores, and captions\. Finally, in security and surveillance applications, you can identify vehicles based on license plate numbers from images taken by street cameras\. 

Some of the benefits of using Amazon Rekognition include:

+ **Integrate powerful image and video recognition into your apps** – Amazon Rekognition removes the complexity of building image recognition capabilities into your applications by making powerful and accurate analysis available with a simple API\. You don’t need computer vision or deep learning expertise to take advantage of Rekognition’s reliable image and video analysis\. With Rekognition’s API, you can easily and quickly build image and video analysis into any web, mobile or connected device application\.

   

+ **Deep learning\-based image and video analysis** – Rekognition uses deep learning technology to accurately analyze images, find and compare faces in images, and detect objects and scenes within your images and videos\. 

   

+ **Scalable image analysis** – Amazon Rekognition enables you to analyze millions of images so you can curate and organize massive amounts of visual data\.

   

+ **Integrate with other AWS services** – Amazon Rekognition is designed to work seamlessly with other AWS services like Amazon S3 and AWS Lambda\. Rekognition’s API can be called directly from Lambda in response to Amazon S3 events\. Since Amazon S3 and Lambda scale automatically in response to your application’s demand, you can build scalable, affordable, and reliable image analysis applications\. For example, each time a person arrives at your residence, your door camera can upload a photo of the visitor to Amazon S3, triggering a Lambda function that uses Rekognition API operations to identify your guest\. You can run analysis directly on images stored in Amazon S3 without having to load or move the data\. Support for AWS Identity and Access Management \(IAM\) makes it easy to securely control access to Rekognition API operations\. Using IAM, you can create and manage AWS users and groups to grant the appropriate access to your developers and end users\.

   

+ **Low cost** – With Amazon Rekognition, you pay for the images and videos you analyze and the face metadata that you store\. There are no minimum fees or upfront commitments\. Get started for free, and save more as you grow with Rekognition's tiered pricing model\. 

## Are You a First\-Time Amazon Rekognition User?<a name="first-time-user"></a>

If you are a first\-time user of Amazon Rekognition, we recommend that you read the following sections in order:

1. **[Amazon Rekognition: How It Works](how-it-works.md)** – This section introduces various Amazon Rekognition components that you work with to create an end\-to\-end experience\. 

1. **[Getting Started with Amazon Rekognition](getting-started.md)** – In this section you set your account and test the Amazon Rekognition API\.

1. **[Working with Images](images.md)** – This section provides information about using Amazon Rekognition with images stored in Amazon S3 buckets and images loaded from a local file system\.

1. **[Working with Stored Videos](video.md)** – This section provides information about using Amazon Rekognition with videos stored in an Amazon S3 bucket\.

1. **[Working with Streaming Videos](streaming-video.md)** – This section provides information about using Amazon Rekognition with streaming videos\.