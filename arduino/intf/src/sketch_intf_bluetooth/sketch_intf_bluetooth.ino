#include <SoftwareSerial.h>


int const tx  = 11;
int const rx  = 10;

SoftwareSerial btSerial(rx, tx);
String btData;

void setup() 
{
  
    Serial.begin(9600);   
  
    btSerial.begin(9600);  
}

void loop() 
{
  delay(100);
  if(btSerial.available())
  {

    Serial.println(btSerial.readStringUntil('x'));
    
  }
  delay(100);
  btSerial.write("Pong");
  delay(1000);

}

