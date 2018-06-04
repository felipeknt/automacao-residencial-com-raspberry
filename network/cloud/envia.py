#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as paho
import time
import base64
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

client = paho.Client()
client.on_publish = on_publish
client.connect("broker.mqttdashboard.com", 1883)
client.loop_start()
encoded = base64.b64encode("ON")

while True:
    (rc, mid) = client.publish("/home/QUARTO/01", "%s" % encoded, qos=1)
    time.sleep(3)
