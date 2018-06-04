#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as paho
import base64

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
    data = base64.b64decode(str(msg.payload))
    print data
    
client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("broker.mqttdashboard.com", 1883)
client.subscribe("/home/QUARTO/01", qos=1)
 
client.loop_forever()