#include <servo.h>

int lamp01 = 2;
int lamp02 = 3;
int lamp03 = 4;
int lamp04 = 5; 
int lamp05 = 6;
int lamp06 = 7;

Servo porta;
Servo portao;

int ventilador = 8;

char letra;

void setup
{
	Serial.begin(9600);
	pinMode(lamp01,OUTPUT);]
    pinMode(lamp02,OUTPUT);
    pinMode(lamp03,OUTPUT);
    pinMode(lamp04,OUTPUT);
    pinMode(lamp05,OUTPUT);
    pinMode(lamp06,OUTPUT);
    porta.attach(9);
    portao.attach(10);
    pinMode(ventilador,OUTPUT);
}


void loop{
  letra = Serial.read();
  switch(letra){
  case  'q': // LIGA LUZ LAMP01
  digitalWrite(lamp01,HIGH);
  break;
  case  'w': // DESLIGA LUZ LAMP01
  digitalWrite(lamp01,LOW);
  break;

  case  'e': // LIGA LUZ LAMP01
  digitalWrite(lamp02,HIGH);
  break;
  case  'r': // DESLIGA LUZ LAMP01
  digitalWrite(lamp02,LOW);
  break;

  case  't': // LIGA LUZ LAMP01
  digitalWrite(lamp03,HIGH);
  break;
  case  'y': // DESLIGA LUZ LAMP01
  digitalWrite(lamp03,LOW);
  break;

  case  'u': // LIGA LUZ LAMP01
  digitalWrite(lamp04,HIGH);
  break;
  case  'i': // DESLIGA LUZ LAMP01
  digitalWrite(lamp04,LOW);
  break;


  case  'o': // LIGA LUZ LAMP01
  digitalWrite(lamp05,HIGH);
  break;
  case  'p': // DESLIGA LUZ LAMP01
  digitalWrite(lamp05,LOW);
  break;

  case  'a': // LIGA LUZ LAMP01
  digitalWrite(lamp06,HIGH);
  break;
  case  's': // DESLIGA LUZ LAMP01
  digitalWrite(lamp06,LOW);
  break;


  case  'd': // LIGA LUZ LAMP01
  digitalWrite(lamp07,HIGH);
  break;
  case  'f': // DESLIGA LUZ LAMP01
  digitalWrite(lamp07,LOW);
  break;

  case  'g': // LIGA LUZ LAMP01
  porta.write(90);
  break;
  case  'h': // DESLIGA LUZ LAMP01
  porta.write(0);
  break;


  case  'j': // LIGA LUZ LAMP01
  portao.write(90)
  break;
  case  'k': // DESLIGA LUZ LAMP01
  porta0.write(0);
  break;

  case  'l': // DESLIGA LUZ LAMP01
  digitalWrite(ventilador,HIGH);
  break;
  case 'z':
  digitalWrite(ventilador,LOW);
  break;
    
  }

}