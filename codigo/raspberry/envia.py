# -*- coding: cp1252 -*-
import paho.mqtt.client as mqtt

from time import sleep

topico = "home/"


client = mqtt.Client()
# conecta no broker
client.connect("127.0.0.1", 1883)

while True:
    # envia a publicação
    client.publish("home/quarto/01","OFF")
    print "TOPICO: home/quarto/01 LETRA: OFF"    
    sleep(1)
    client.publish("home/quarto/01","ON")
    print "TOPICO: home/quarto/01 LETRA: ON"    
    sleep(1)

    client.publish("home/quarto/02","OFF")
    print "TOPICO: home/quarto/02 LETRA: OFF"    
    sleep(1)
    client.publish("home/quarto/02","ON")
    print "TOPICO: home/quarto/02 LETRA: ON"    
    sleep(1)
    