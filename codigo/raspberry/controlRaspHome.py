#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import serial
import networktools
"""
>>> networktools.local_ip
<function local_ip at 0x7f776296d6e0>
>>> networktools.local_ip()
'192.168.0.9'
>>> networktools.local_ip()
'192.168.0.9'
"""
TOPIC = "/home/#"

test = networktools.test_cloud()

#Callback  - chamada quando a conexao eh estabelecida
def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker. Retorno da conexao: "+str(rc))

    # Informa que o topico que este subscriber ira "escutar" eh o "MQTTEdison" 
    client.subscribe([(TOPIC,0)])

# Callback - chamado quando alguma mensagem é recebida
def on_message(client, userdata, msg):
    print("Topico: "+msg.topic+" - Mensagem recebida: "+str(msg.payload)) 
#### LAMPADAS APP 
    if msg.topic == "/home/QUARTO/01":
     if (str(msg.payload) == "ON"):
        print "QUARTO 1 - ON"
        return 0
     if (str(msg.payload) == "OFF"):
        print "QUARTO 1 - OFF"
        return 0   
    if msg.topic == "/home/SALA/01":
     if (str(msg.payload) == "ON"):
        print "SALA 01 - ON"
        return 0
     if (str(msg.payload) == "OFF"):
        print "SALA 01 - OFF"
        return 0   

    if msg.topic == "/home/COZINHA/01":
     if (str(msg.payload) == "ON"):
        print "COZINHA 01 - ON"
        return 0
     if (str(msg.payload) == "OFF"):
        print "COZINHA 01 - OFF"
        return 0   

    if msg.topic == "/home/GARAGEM/01":
     if (str(msg.payload) == "ON"):
        print "GARAGEM 01 - ON"
        return 0
     if (str(msg.payload) == "OFF"):
        print "GARAGEM 01 - OFF"
        return 0   

    if msg.topic == "/home/QUARTO/02":
     if (str(msg.payload) == "ON"):
        print "QUARTO 02 - ON"
        return 0
     if (str(msg.payload) == "OFF"):
        print "QUARTO 02 - OFF"
        return 0   

    if msg.topic == "/home/CORREDOR/01":
     if (str(msg.payload) == "ON"):
        print "CORREDOR 01 - ON"
        return 0
     if (str(msg.payload) == "OFF"):
        print "CORREDOR 01 - OFF"
        return 0   
####  PORTÃO GARAGEM
    if msg.topic == "/home/PORTA/01":
     if (str(msg.payload) == "ON"):
        print "PORTA 01 - ON"
        return 0
     if (str(msg.payload) == "OFF"):
        print "PORTA 01 - OFF"
        return 0   

    if msg.topic == "/home/PORTAO/01":
     if (str(msg.payload) == "ON"):
        print "PORTAO 01 - ON"
        return 0
     if (str(msg.payload) == "PARAR"):
        print "PORTAO 01 - PARAR"
        return 0   
     if (str(msg.payload) == "OFF"):
        print "PORTAO 01 - OFF"
        return 0   
    if msg.topic == "/home/VENTILADOR/01":
     if (str(msg.payload) == "ON"):
        print "VENTILADOR 01 - ON"
        return 0      
    
     if (str(msg.payload) == "OFF"):
        print "VENTILADOR 01 - OFF"
        return 0      
    
    
    
#programa principal
client = mqtt.Client()
client.on_connect = on_connect   #configura callback (de quando eh estabelecida a conexao)
client.on_message = on_message   #configura callback (de quando eh recebida uma mensagem)

client.connect(networktools.local_ip(), 1883, 60)  #tenta se conectar ao broker na porta 1883 (o parametro '60' eh o tempo de keepalive). Nesse caso, se nenhuma mensagem for trafegada em ate 60 segundos, eh enviado um ping ao broker de tempos em tempos (para manter a conexao ativa)

#Loop infinito aguardando recepcao de mensagens. Esta funcao eh blocante.
client.loop_forever()
