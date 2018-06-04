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

# CONNECT PORT SERIAL ARDUINO UNO 
status_port = False
try:
 try:   # crie um serial na porta ACM0
   arduino = serial.Serial("/dev/ttyACM0",9600)
   status_port = True
 except:  # CRIA SERIAL COM ACM1
   arduino = serial.Serial("/dev/ttyACM1",9600)
except :
  status_port = False
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
        if status_port == True:
         print "QUARTO 1 - ON"
         arduino.write("q")
         return 0
        else:
          print "BOARD NOT CONNECT! COMAND NOT SEND !" 

     if (str(msg.payload) == "OFF"):
        if status_port == True:
         print "QUARTO 1 - OFF"
         arduino.write("w")
         return 0   
        else:
         print "BOARD NOT CONNECT! COMAND NOT SEND !"   

    if msg.topic == "/home/SALA/01":
     if (str(msg.payload) == "ON"):
       if status_port == True:
        print "SALA 01 - ON"
        arduino.write("e")
        return 0
       else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"   

     if (str(msg.payload) == "OFF"):
       if status_port == True:
        arduino.write("r") 
        print "SALA 01 - OFF"
        return 0   
       else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"   
  
    if msg.topic == "/home/COZINHA/01":
     if (str(msg.payload) == "ON"):
      if status_port == True:
        arduino.write("t")
        print "COZINHA 01 - ON"
        return 0
      else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"   

     if (str(msg.payload) == "OFF"):
      if status_port == True:
        arduino.write("y")
        print "COZINHA 01 - OFF"
        return 0   
      else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"   

    if msg.topic == "/home/GARAGEM/01":
     if (str(msg.payload) == "ON"):
      if status_port == True:
        arduino.write("u")
        print "GARAGEM 01 - ON"
        return 0
      else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"   

     if (str(msg.payload) == "OFF"):
      if status_port == True:
        arduino.write("i")
        print "GARAGEM 01 - OFF"
        return 0   
      else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"   


    if msg.topic == "/home/QUARTO/02":
     if (str(msg.payload) == "ON"):
      if status_port == True:
        arduino.write("o")
        print "QUARTO 02 - ON"
        return 0
      else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"   

     if (str(msg.payload) == "OFF"):
      if status_port == True:
        arduino.write("p")
        print "QUARTO 02 - OFF"
        return 0
      else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"

### CORREDOR 

    if msg.topic == "/home/CORREDOR/01":
     if (str(msg.payload) == "ON"):
      if status_port == True:
        arduino.write("a")
        print "CORREDOR 01 - ON"
        return 0
      else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"

     if (str(msg.payload) == "OFF"):
      if status_port == True:
        arduino.write("s")
        print "CORREDOR 01 - OFF"
        return 0   
     else: 
        print "BOARD NOT CONNECT! COMAND NOT SEND !"

####  PORTA

    if msg.topic == "/home/PORTA/01":
     if (str(msg.payload) == "ON"):
      if status_port == True:
        arduino.write("d")
        print "PORTA 01 - ON"
        return 0
      else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"

     if (str(msg.payload) == "OFF"):
      if status_port == True:
        arduino.write("f")
        print "PORTA 01 - OFF"
        return 0   
      else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"


### PORTAO

    if msg.topic == "/home/PORTAO/01":
     if (str(msg.payload) == "ON"):
      if status_port == True:
        arduino.write("g")
        print "PORTAO 01 - ON"
        return 0
      else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"

     if (str(msg.payload) == "PARAR"):
      if status_port == True:   
        arduino.write("h")
        print "PORTAO 01 - PARAR"
        return 0   
      else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"
     if (str(msg.payload) == "OFF"):
      if status_port == True:
        arduino.write("j")
        print "PORTAO 01 - OFF"
        return 0 
      else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"

### VENTILADOR        

    if msg.topic == "/home/VENTILADOR/01":
     if (str(msg.payload) == "ON"):
       if status_port == True:
        arduino.write("z")
        print "VENTILADOR 01 - ON"
        return 0      
       else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"          
    
     if (str(msg.payload) == "OFF"):
      if status_port == True:
        arduino.write("x")
        print "VENTILADOR 01 - OFF"
        return 0      
      else:
        print "BOARD NOT CONNECT! COMAND NOT SEND !"        
    


    
#programa principal
client = mqtt.Client()
client.on_connect = on_connect   #configura callback (de quando eh estabelecida a conexao)
client.on_message = on_message   #configura callback (de quando eh recebida uma mensagem)

client.connect(networktools.local_ip(), 1883, 60)  #tenta se conectar ao broker na porta 1883 (o parametro '60' eh o tempo de keepalive). Nesse caso, se nenhuma mensagem for trafegada em ate 60 segundos, eh enviado um ping ao broker de tempos em tempos (para manter a conexao ativa)

#Loop infinito aguardando recepcao de mensagens. Esta funcao eh blocante.
client.loop_forever()
