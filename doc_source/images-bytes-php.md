# Using PHP<a name="images-bytes-php"></a>

The following [AWS SDK for PHP](http://docs.aws.amazon.com/aws-sdk-php/v3/guide/index.html#getting-started) example shows how to load an image from the local file system and call the [DetectFaces](http://docs.aws.amazon.com/aws-sdk-php/v3/api/api-rekognition-2016-06-27.html#detectfaces) API operation\. 

```
<?php
    require 'path/vendor/autoload.php';

    use Aws\Rekognition\RekognitionClient;

    $options = [
        'region'            => 'us-west-2',
        'version'           => '2016-06-27',
    ];

    $rekognition = new RekognitionClient($options);

    #Get local image
    $fp_image = fopen('test.png', 'r');
    $image = fread($fp_image, filesize('test.png'));
    fclose($fp_image);


    # Call DetectFaces
    $result = $rekognition->DetectFaces(array(
       'Image' => array(
          'Bytes' => $image,
       ),
       'Attributes' => array('ALL')
       )
    );

    # Display info for each detected person
    print 'People: Image position and estimated age' . PHP_EOL;
    for ($n=0;$n<sizeof($result['FaceDetails']); $n++){

      print 'Position: ' . $result['FaceDetails'][$n]['BoundingBox']['Left'] . " "
      . $result['FaceDetails'][$n]['BoundingBox']['Top']
      . PHP_EOL
      . 'Age (low): '.$result['FaceDetails'][$n]['AgeRange']['Low']
      .  PHP_EOL
      . 'Age (high): ' . $result['FaceDetails'][$n]['AgeRange']['High']
      .  PHP_EOL . PHP_EOL;
    }
?>
```