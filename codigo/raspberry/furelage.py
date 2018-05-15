#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import serial

TOPIC = "home/#"

#Callback  - chamada quando a conexao eh estabelecida
def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker. Retorno da conexao: "+str(rc))

    # Informa que o topico que este subscriber ira "escutar" eh o "MQTTEdison" 
    client.subscribe([(TOPIC,0)])

# Callback - chamado quando alguma mensagem é recebida
def on_message(client, userdata, msg):
    print("Topico: "+msg.topic+" - Mensagem recebida: "+str(msg.payload)) 
    if msg.topic == "home/quarto/01":
     if (str(msg.payload) == "ON"):
        print "QUARTO 1 - ON"
        return 0
     if (str(msg.payload) == "OFF"):
        print "QUARTO 1 - OFF"
        return 0   
    if msg.topic == "home/quarto/02":
     if (str(msg.payload) == "ON"):
        print "QUARTO 2 - ON"
        return 0
     if (str(msg.payload) == "OFF"):
        print "QUARTO 2 - OFF"
        return 0   

    if msg.topic == "home/quarto/03":
     if (str(msg.payload) == "ON"):
        print "QUARTO 3 - ON"
        return 0
     if (str(msg.payload) == "OFF"):
        print "QUARTO 3 - OFF"
        return 0   

    if msg.topic == "home/sala/01":
     if (str(msg.payload) == "ON"):
        print "SALA 1 - ON"
        return 0
     if (str(msg.payload) == "OFF"):
        print "SALA 1 - OFF"
        return 0   



    
    
#programa principal
client = mqtt.Client()
client.on_connect = on_connect   #configura callback (de quando eh estabelecida a conexao)
client.on_message = on_message   #configura callback (de quando eh recebida uma mensagem)

client.connect("127.0.0.1", 1883, 60)  #tenta se conectar ao broker na porta 1883 (o parametro '60' eh o tempo de keepalive). Nesse caso, se nenhuma mensagem for trafegada em ate 60 segundos, eh enviado um ping ao broker de tempos em tempos (para manter a conexao ativa)

#Loop infinito aguardando recepcao de mensagens. Esta funcao eh blocante.
client.loop_forever()