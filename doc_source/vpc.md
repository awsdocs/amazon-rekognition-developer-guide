# Using Amazon Rekognition with Amazon VPC Endpoints<a name="vpc"></a>

If you use Amazon Virtual Private Cloud \(Amazon VPC\) to host your AWS resources, you can establish a private connection between your VPC and Amazon Rekognition\. You can use this connection to enable Amazon Rekognition to communicate with your resources on your VPC without going through the public internet\.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network that you define\. With a VPC, you have control over your network settings, such the IP address range, subnets, route tables, and network gateways\. With VPC endpoints, the AWS network handles the routing between the VPC and AWS services\.

To connect your VPC to Amazon Rekognition, you define an interface VPC endpoint for Amazon Rekognition\. An interface endpoint is an elastic network interface with a private IP address that serves as an entry point for traffic destined to a supported AWS service\. The endpoint provides reliable, scalable connectivity to Amazon Rekognition—and it doesn't require an internet gateway, a network address translation \(NAT\) instance, or a VPN connection\. For more information, see [What Is Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/) in the *Amazon VPC User Guide*\.

Interface VPC endpoints are enabled by AWS PrivateLink\. This AWS technology enables private communication between AWS services by using an elastic network interface with private IP addresses\. For more information, see [AWS PrivateLink](https://aws.amazon.com/privatelink/)\.

## Creating Amazon VPC Endpoints for Amazon Rekognition<a name="vpc-create-endpoint"></a>

You can create two types of Amazon VPC endpoints to use with Amazon Rekognition\. 
+ A VPC endpoint to use with Amazon Rekognition operations\. For most users, this is the most suitable type of VPC endpoint\.
+ A VPC endpoint for Amazon Rekognition operations with endpoints that comply with the Federal Information Processing Standard \(FIPS\) Publication 140\-2 US government standard\. For more information, see [Endpoints for the AWS GovCloud \(US\) Regions](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/using-govcloud-endpoints.html)\.

To start using Amazon Rekognition with your VPC, use the Amazon VPC console to create an interface VPC endpoint for Amazon Rekognition\. For instructions, see the procedure "To create an interface endpoint to an AWS service using the console" in [Creating an Interface Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint)\. Note the following procedure steps:
+ Step 3 –For **Service category**, choose *AWS services*\.
+ Step 4 – For **Service Name**, choose one of the following options:
  + *com\.amazonaws\.region\.rekognition* – Creates a VPC endpoint for Amazon Rekognition operations\. 
  + *com\.amazonaws\.region\.rekognition\-fips* – Creates a VPC endpoint for Amazon Rekognition operations with endpoints that comply with the Federal Information Processing Standard \(FIPS\) Publication 140\-2 US government standard\.

For more information, see [Getting Started](https://docs.aws.amazon.com/vpc/latest/userguide/GetStarted.html) in the *Amazon VPC User Guide*\.