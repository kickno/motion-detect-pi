#!/bin/bash
cd /home/pi/aws-iot-device-sdk-python/samples
python hatsensor.py --endpoint a1fekhflh4ppjg-ats.iot.ap-northeast-1.amazonaws.com --rootCA ./cert/root.ca.pem --cert ./cert/57d3036c13-certificate.pem.crt --key ./cert/57d3036c13-private.pem.key

