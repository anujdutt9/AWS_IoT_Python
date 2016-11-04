# Subscribes to Data Published to AWS Cloud

import paho.mqtt.client as mqtt
import os
import socket
import ssl

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc) )
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#" , 1 )

def on_message(client, userdata, msg):
    print("topic: "+msg.topic)
    print("Payload Data: "+str(msg.payload))


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

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_forever()
