
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from datetime import datetime
from pytz import timezone
import logging
import time
import argparse
import json
from sense_hat import SenseHat
sense = SenseHat()
# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Published a new message: ")
    #print(message.payload)
   # print(message.topic)
    print("--------------\n\n")

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--endpoint", action="store", required=True, dest="host", help="Your AWS IoT custom endpoint")
parser.add_argument("-r", "--rootCA", action="store", required=True, dest="rootCAPath", help="Root CA file path")
parser.add_argument("-c", "--cert", action="store", dest="certificatePath", help="Certificate file path")
parser.add_argument("-k", "--key", action="store", dest="privateKeyPath", help="Private key file path")

args = parser.parse_args()
host = args.host
rootCAPath = args.rootCAPath
certificatePath = args.certificatePath
privateKeyPath = args.privateKeyPath


# Port defaults
port = 8883

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = None
myAWSIoTMQTTClient = AWSIoTMQTTClient("test")
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()
#if args.mode == 'both' or args.mode == 'subscribe':
#myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
#time.sleep(2)

loopCount = 0
while True:
#    if args.mode == 'both' or args.mode == 'publish':
        message = {}
        message['sequence'] = loopCount
        t = sense.get_temperature()
        p = sense.get_pressure()
        h = sense.get_humidity()
        tod = datetime.now(timezone('UTC')).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"Z"
        message['humidity'] = h
        message['pressure'] = p
        message['temperature'] = t
        message['date'] = tod
        messageJson = json.dumps(message)
#       if args.mode == 'publish':
#               print('Published topic %s: %s\n' % (topic, messageJson))
        loopCount += 1
        time.sleep(1)
