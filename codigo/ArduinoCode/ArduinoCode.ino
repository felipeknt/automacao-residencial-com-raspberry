#include <Servo.h>

int lamp01 = 2;
int lamp02 = 3;
int lamp03 = 4;
int lamp04 = 5; 
int lamp05 = 6;
int lamp06 = 7;
int lamp07 = 8;

Servo porta;
Servo portao;

int ventilador = 9;

char letra;
int pos = 0;
void setup()
{
	Serial.begin(9600);
	  pinMode(lamp01,OUTPUT);
    pinMode(lamp02,OUTPUT);
    pinMode(lamp03,OUTPUT);
    pinMode(lamp04,OUTPUT);
    pinMode(lamp05,OUTPUT);
    pinMode(lamp06,OUTPUT);
    pinMode(lamp07,OUTPUT);
    porta.attach(11);
    portao.attach(10);
    pinMode(ventilador,OUTPUT);
}


void loop(){
  letra = Serial.read();
  switch(letra){
  case  'q': // LIGA LUZ LAMP01
  digitalWrite(lamp01,HIGH);
  Serial.println("LAMP01 - ON");
  break;
  case  'w': // DESLIGA LUZ LAMP01
  digitalWrite(lamp01,LOW);
  Serial.println("LAMP01 - OFF");
  break;

  case  'e': // LIGA LUZ LAMP02
  digitalWrite(lamp02,HIGH);
  Serial.println("LAMP02 - ON");
  break;
  case  'r': // DESLIGA LUZ LAMP02
  digitalWrite(lamp02,LOW);
  Serial.println("LAMP02 - OFF");
  break;

  case  't': // LIGA LUZ LAMP03
  digitalWrite(lamp03,HIGH);
  Serial.println("LAMP03 - ON");
  break;
  case  'y': // DESLIGA LUZ LAMP03
  digitalWrite(lamp03,LOW);
  Serial.println("LAMP03 - OFF");
  break;

  case  'u': // LIGA LUZ LAMP04
  digitalWrite(lamp04,HIGH);
  Serial.println("LAMP04 - ON");
  break;
  case  'i': // DESLIGA LUZ LAMP04
  digitalWrite(lamp04,LOW);
  Serial.println("LAMP04 - OFF");
  break;


  case  'o': // LIGA LUZ LAMP05
  digitalWrite(lamp05,HIGH);
  Serial.println("LAMP05 - ON");
  break;
  case  'p': // DESLIGA LUZ LAMP05
  digitalWrite(lamp05,LOW);
  Serial.println("LAMP05 - OFF");
  break;

  case  'a': // LIGA LUZ LAMP06
  digitalWrite(lamp06,HIGH);
  Serial.println("LAMP06 - ON");
  break;
  case  's': // DESLIGA LUZ LAMP06
  digitalWrite(lamp06,LOW);
  Serial.println("LAMP06 - OFF");
  break;


  case  'd': // LIGA LUZ LAMP07
  digitalWrite(lamp07,HIGH);
  Serial.println("LAMP07 - ON");
  break;
  case  'f': // DESLIGA LUZ LAMP07
  digitalWrite(lamp07,LOW);
  Serial.println("LAMP07 - OFF");
  break;

  case  'g': // MOVER SERVO 90 GRAUS
  porta.write(90);
  Serial.println("PORTA 90 GRAUS");
  break;
  case  'h': // MOVER SERVO 0 GRAUS
  porta.write(0);
  Serial.println("PORTA 0 GRAUS");
  break;


  case  'j': // MOVER SERVO 90 GRAUS
  Serial.println("PORTAO 90 GRAUS");
  portao.write(pos);              
  break;

  case  'k': // MOVER SERVO 0 GRAUS
  portao.write(0);              
    delay(15);                       
  
  Serial.println("PORTAO 0 GRAUS");
  break;
  
  case  'l': // MOVER SERVO 45 GRAUS
  portao.write(45);              
  Serial.println("PORTAO 45 GRAUS");
  break;

  case  'z': // LIGAR VENTILADOR
  digitalWrite(ventilador,HIGH);
  Serial.println("VENTILADOR ON");
  break;
  case 'x': // DESLIGAR VENTILADOR
  digitalWrite(ventilador,LOW);
  Serial.println("VENTILADOR OFF");
  break;

  }

}
