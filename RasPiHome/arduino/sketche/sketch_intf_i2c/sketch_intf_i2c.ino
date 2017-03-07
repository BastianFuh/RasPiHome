#include <Wire.h>
#include <DHT.h>


// CONST

#define DEBUG 0


// READ / REQUEST

#define DHT_TEMPERATURE 1
#define DHT_HUMIDITY 2
#define DHT_HEAT_INDEX 3

// WRITE / RECEIVE

#define SERVO_WRITE 128

//


DHT dht(7, DHT22);




int const address = 0x08;



int functCode = 0;
int requestCode;
char buff[5];


int temp, hum;

void setup() 
{
  
  
  Serial.begin(9600);

  Wire.begin(address);
  
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);


}



void loop() 
{
  delay(100);
}

void receiveEvent(int byteCount)
{

    
    functCode = Wire.read();

    
    
    switch(functCode)
    {
      case DEBUG:
        Serial.println("-- Debug --");

        Serial.print("Received Bytes: ");
        Serial.println(byteCount);
        
        while(Wire.available())
        {
          Serial.println(Wire.read());
        }
      break;


      case DHT_TEMPERATURE:
        requestCode = DHT_TEMPERATURE;
        temp = (int) (dht.readTemperature()*100);
        Serial.print("Temperatur: ");
        Serial.println(temp);
      break;

      case DHT_HUMIDITY:
        requestCode = DHT_HUMIDITY;
        hum = (int) (dht.readHumidity()*100);
        Serial.print("Humidity: ");
        Serial.println(hum);
      break;
      
      case SERVO_WRITE:
        
 /*       if (Wire.available())
          sDeg  = Wire.read();

        if (Wire.available())
          eDeg = Wire.read();

        if (Wire.available())
          tim = Wire.read();*/
      break;

     
      default:
        Serial.println("Invalid Function Code");
    }
  
}


void requestEvent()
{
  char test[5];

//Serial.println("Request Event");
  //Serial.println(requestCode);
  
   delay(5000);
  switch(requestCode)
  {

    case DHT_TEMPERATURE:
      intToCharArr(temp, sizeof(int));

  
      
      Serial.println(buff[0]);
      Serial.println(buff[1]);
      Wire.write(buff, sizeof(int));
    break;


    case DHT_HUMIDITY:
      intToCharArr(hum , sizeof(int));
      Wire.write(buff, sizeof(int));
    break;


    case DHT_HEAT_INDEX:
      Wire.write((int)(dht.computeHeatIndex(dht.readTemperature(), dht.readHumidity(), false)*100));
    break;
    
    default:
      Serial.println("Invalid Function Code");
  }
  requestCode = 0;
}




void intToCharArr(int number, int len)
{
    for(int i = len-1, counter = 0 ; i >= 0 ; i--, counter++) 
    {
      buff[counter] = number >> 8 * i;
    }
}

 
