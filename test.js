
var AWS = require('aws-sdk');
AWS.config.update(
  {
    accessKeyId: "xxxxxxxxxxx",
    secretAccessKey: "xxxxxxxxxxxxxxxxxx",
  }
);
var s3 = new AWS.S3();
s3.getObject(
  { Bucket: "motion-detect-photo", Key: "test.jpg" },
  function (error, data) {
    if (error != null) {
      //alert("Failed to retrieve an object: " + error);
    } else {
      //alert("Loaded " + data.ContentLength + " bytes");
      // do something with data.Body
    }
  }
);
