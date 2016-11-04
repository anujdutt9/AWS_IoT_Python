# Publishes the Data to AWS IoT

import os
import socket
import ssl
import paho.mqtt.client as mqtt                         # Import the Paho-MQTT Client
from time import sleep                                  # Import sleep from time for delays
import RPi.GPIO as GPIO                                 # Import GPIO Library for Raspberry Pi


# Initialize the Connection Flag as False
connection_flag = False

# Set Mode of RPi Pins i.e Broadcom or Chipset
GPIO.setmode(GPIO.BCM)

# Define LED
# Put LED Numbers
led = 21

# Set Pin as Output
GPIO.setup(led1,GPIO.OUT)       # Pin 21

# Initialize LED's
GPIO.output(led1,GPIO.LOW)


# Check if the Connection to AWS Cloud has been Made.
def on_connect(client, userdata, flags, rc):
    global connection_flag
    connection_flag = True
    print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

# Initiate Paho-MQTT Client
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

# Define the AWS Host Key  ; Thing Name defined in AWS IoT; Root Certificate Path; Certificate Path; Private Key Certificate Path  
awshost = "axxxxxxxxxxxxx.iot.us-west-2.amazonaws.com"
# AWS Port(Default: 8883)
awsport = 8883
# Client ID
clientId = "Thing_Name"
# Thing Name defined in AWS IoT
thingName = "Thing_Name"
# Root Certificate Path
caPath = "Path_of_rootCA.crt"
# Certificate Path
certPath = "Path_of_public_certificate"
# Private Key Certificate Path
keyPath = "Path_of_Private_Key"

# Configure network encryption and authentication options
# Enable SSL/TLS support
mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

# Connect to AWS Host
mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_start()


while True:
	if connection_flag = True:
		GPIO.output(led1,GPIO.HIGH)
		
		# Update LED Data on AWS IoT in Real Time
		# State tells the current and previous state of LED
		# Reported gives the timestamp
        	jsonMessage = "{ \"state\": { \"reported\": { \"Led\": " + str(state) + "} } }"
        	mqttc.publish("$aws/things/Thing_Name/shadow/update", jsonMessage, qos=1)

		# Publish the Data to AWS IOT and get it on Subscription
        	mqttc.publish("LED1: ", state1, qos=1)
        	print("LED1: " + "%d" % state1 )
		sleep(1.0)
		
		# Update LED Data on AWS IoT in Real Time
		GPIO.output(led1,GPIO.HIGH)
        	jsonMessage = "{ \"state\": { \"reported\": { \"Led\": " + str(state) + "} } }"
        	mqttc.publish("$aws/things/Thing_Name/shadow/update", jsonMessage, qos=1)
        	sleep(1.0)
		# Publish the Data to AWS IOT and get it on Subscription
        	mqttc.publish("LED1: ", state1, qos=1)
        	print("LED1: " + "%d" % state1 )		
    else:
		print("Waiting for Connection...")

ser.close()
GPIO.cleanup()
      
