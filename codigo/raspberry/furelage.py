import paho.mqtt.client as mqtt
import serial


#Callback  - chamada quando a conexao eh estabelecida
def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker. Retorno da conexao: "+str(rc))

    # Informa que o topico que este subscriber ira "escutar" eh o "MQTTEdison" 
    client.subscribe("MQTT_RASPBERRY")

# Callback - chamado quando alguma mensagem é recebida
def on_message(client, userdata, msg):
	print("Topico: "+msg.topic+" - Mensagem recebida: "+str(msg.payload)) 
	
	if (str(msg.payload) == "AcendeLED1"):
		led1.write(1)
	    	return 0
		
	if (str(msg.payload) == "AcendeLED2"):
		led2.write(1)
		return 0
		
	if (str(msg.payload) == "ApagaLED1"):
		led1.write(0)
		return 0
		
	if (str(msg.payload) == "ApagaLED2"):
		led2.write(0)
		return 0
	
	#writes on LCD Display the message received
	
	
#programa principal
client = mqtt.Client()
client.on_connect = on_connect   #configura callback (de quando eh estabelecida a conexao)
client.on_message = on_message   #configura callback (de quando eh recebida uma mensagem)

client.connect("test.mosquitto.org", 1883, 60)  #tenta se conectar ao broker na porta 1883 (o parametro '60' eh o tempo de keepalive). Nesse caso, se nenhuma mensagem for trafegada em ate 60 segundos, eh enviado um ping ao broker de tempos em tempos (para manter a conexao ativa)

#Loop infinito aguardando recepcao de mensagens. Esta funcao eh blocante.
client.loop_forever()