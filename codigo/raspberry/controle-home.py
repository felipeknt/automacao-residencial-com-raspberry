import serial

LOCAL = '' # PARTE DA CASA
ID = ''    # IDENTICACAO DO ATUADOR
STATUS = '' # LETRA A SER ENVIADA PARA O ARDUINO 

TOPICO = "/HOME/%s/%s/%s" % (LOCAL,ID,STATUS) 

ser = ''
try:
 arduino = serial.Serial("/dev/ttyACM0",9600)
 ser = True
except:
 try:
   arduino = serial.Serial("/dev/ttyACM1",9600)
   ser = True
 except:
   try:
      arduino = serial.Serial("/dev/ttyUSB0",9600)
      ser = True
   except:
      print "FAIL MODA FOKA SERIAL USB"
      ser = False
pass

def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker. Retorno da conexao: "+str(rc))

    # Informa que o topico que este subscriber ira "escutar" eh o "MQTTEdison" 
    client.subscribe("MQTT_RASPBERRY")

# Callback - chamado quando alguma mensagem é recebida
def on_message(client, userdata, msg):
	print("Topico: "+msg.topic+" - Mensagem recebida: "+str(msg.payload)) 
	if (str(msg.payload) == "Hello Word"):
       print "Hello Word"
       return 0


#programa principal
client = mqtt.Client()
client.on_connect = on_connect   #configura callback (de quando eh estabelecida a conexao)
client.on_message = on_message   #configura callback (de quando eh recebida uma mensagem)

client.connect("127.0.0.1", 1883, 60)  #tenta se conectar ao broker na porta 1883 (o parametro '60' eh o tempo de keepalive). Nesse caso, se nenhuma mensagem for trafegada em ate 60 segundos, eh enviado um ping ao broker de tempos em tempos (para manter a conexao ativa)

#Loop infinito aguardando recepcao de mensagens. Esta funcao eh blocante.
client.loop_forever()
