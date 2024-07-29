#include <Wire.h>
#include <DHT.h>
#include <Servo.h>





// CONST




// Sensor

#define SENSOR_TEMPERATURE 0x01
#define SENSOR_TEMP 0x01

#define SENSOR_HUMIDITY 0x02
#define SENSOR_HUM 0x02

#define SENSOR_LIGHT 0x03

#define SENSOR_COLOR 0x04


// Actuators

#define ACTR_SERVO 0x70

#define ACTR_PELTIER 0x71

#define ACTR_LED 0x72

#define ACTR_SIREN 0x73


// Ports

#define TEMP 0x10
#define HUM 0x25
#define LIGHT 0x45

#define SERVO 0x0C

#define DEBUG 0xFE
#define DISCOVERY 0xFF

#define OTHER 0x00
#define DIREKT 0x01
#define BLUETOOTH 0x02
#define I2C 0x03
#define SPI 0x04

typedef struct{
  uint8_t  port;
  int      dataLen;
  int     *data;
} recvCommand;

typedef struct{
  uint8_t conn_type;
  uint8_t spec;
  uint8_t port;
} Port;


DHT dht(7, DHT22);

Servo s2,s1;

int const address = 0x08;


Port ports[20];

int portsLen;

uint8_t port  = 0x00;
uint8_t len   = 0;

int buffLen = 2;
int dataLen = 0;

char     sendBuff[32];
float    buff[32];

int      servoPos;

int discoveryMode = 0;

recvCommand commands[10];

int i = 0;

/***
 * Setup
 * 
 * Just executed one
 ***/
void setup() 
{


  ports[0].conn_type  = DIREKT;  
  ports[0].spec       = SENSOR_TEMPERATURE;
  ports[0].port       = TEMP;

  ports[0].conn_type  = DIREKT;
  ports[1].spec       = SENSOR_HUMIDITY;
  ports[1].port       = HUM;

  ports[0].conn_type  = DIREKT;
  ports[2].spec       = SENSOR_LIGHT;
  ports[2].port       = LIGHT;

  ports[0].conn_type  = DIREKT;
  ports[3].spec       = ACTR_SERVO;
  ports[3].port       = SERVO;

  

  portsLen = arrayLength(ports);
  
  Serial.begin(9600);

  Wire.begin(address);
  

  
  s1.attach(9);
  s1.write(180);

  delay(100);

  Serial.println("System Ready");
  
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);

}


  int data[10]; // move back int to func later

/***
 * Main Loop
 * 
 * executed over and over and over and over + { while [ 1 ]; do echo "and over"; done }
 ***/
void loop() 
{
  readSensor();
   delay(2000);

   switch(port)
   {
      case SERVO:
       Serial.print(""); // Uncomment this line, if it stops working
        addCommand(port, dataLen - 1, data);
        port = 0;
      break;


    }
  

  switch(commands[i].port)
  {

    /***  
     *  Type : Actuator
     *  Spec : Servo
     ***/
    case SERVO:

      int pos, t;
      if ( commands[i].dataLen == 1 )
      {
        servoWrite(s1, servoPos);
      } else if (commands[i].dataLen == 2) 
      {
        t = commands[i].data[1];
        servoWrite(s1, servoPos, t);
      } else
          break;
    break;

    
    /***
     * Used for Debugging the connection
     ***/
    case DEBUG:
      while(Wire.available())
      {
        Serial.println(Wire.read());
      }
    break;
  }

  
  if (i<10 && commands[i].port != NULL)
  {
    commands[i].port = NULL;
    i += 1;
  } else
  {
    i = 0;  
  }
}





/***
 * receiveEvent
 * 
 * Executed on read and write request
 * 
 ***/

void receiveEvent(int byteCount)
{
  
   int i = 0;
  
   port = Wire.read();
      

   while (Wire.available())
   {   
       data[i] = Wire.read();
       i += 1;
   }
   dataLen = byteCount;

   if (port == SERVO)
      servoPos = data[0];

   if (port == DISCOVERY)
      if (discoveryMode == 0)
        discoveryMode = 1;
      else
        discoveryMode = 0;
    
}



  
/***
 * requestEvent
 * 
 * Executed on read requests
 * 
 * 
 ****/
void requestEvent()
{
  uint8_t buff2[32]; 
   if(discoveryMode == 1)
   {
      discoveryMode = 2;
      Wire.write(portsLen);
      return 0;
   } else if (discoveryMode == 2)
   {
      if (port == DISCOVERY)
      {
        discoveryMode = 0;
        port = 0;
        Wire.write( "", 32);
        return 0;
      }
      buff2[0] = ports[port].conn_type;
      buff2[1] = ports[port].spec;
      buff2[2] = ports[port].port;
      Wire.write(buff2,32);
      return 0;
   }

  switch(port)
  {
    case TEMP:
      setBuffer(buff[TEMP]*100, sizeof(int), 2);
      Wire.write(sendBuff, 32);
    break;


    case HUM:
      setBuffer(buff[HUM]*100, sizeof(int), 2);
      Wire.write(sendBuff, 32);
    break;


    case LIGHT:
      setBuffer(buff[LIGHT], sizeof(int), 0);
      Wire.write(sendBuff, 32);    
    break;

    case DISCOVERY:
      
    break;
  }
  

}




/***
 * readSenor
 * 
 * reads all the Sensor values and stores them inside of a variable
 * 
 ***/
void readSensor()
{
  buff[TEMP]  = dht.readTemperature();
  buff[HUM]   = dht.readHumidity();
  analogRead(0);
  buff[LIGHT] = analogRead(0);
}




/***
 * setBuffer
 * 
 * sets the send Buffer
 * 
 * Arguments
 *  - number    the number which has to be send
 *  - len       the length of the number in bytes
 *  - offset    the offset of the number, only for float values
 ***/
void setBuffer(int number, int len, int offset)
{

  sendBuff[0] = len;
  sendBuff[1] = offset; 
  
  for(int i = len-1, counter = 0 ; i >= 0 ; i--, counter++) 
  {
    sendBuff[counter+2] = number >> 8 * i;
  }
  
}



/***
 * addCommand
 * 
 * Adds a Command to the commads list
 * 
 * Arguments
 *  - port      behind which port is the function
 *  - dataLen   The amount of elements in the data array 
 *  - data      Important data which is needen to executed
 *              the function
 ***/
boolean addCommand(uint8_t port, int dataLen, int data[])
{
  for ( int i; i < 10 ; i++ )
  {
    if(commands[i].port == NULL)
    {
      commands[i].port     = port;
      commands[i].dataLen  = dataLen;
      for(int j = 0; j < 10; j++)
      {
        commands[i].data[j] = data[j];
      }  
      return true;
    }
  } 

  return false;
    
}





/***
 * servoWrite
 * 
 * Sets a servo to a certain degree
 * 
 * Arguments
 *  - &servo    The Servo that should be written to
 *  - pos       The degree the Servo should be set to
 ***/
void servoWrite(Servo &servo, int pos)
{
  int i;
  if( servo.read() > pos )
  { 
    for(i = servo.read(); i >= pos ; i--  )
    {
      servo.write(i);
      delay(50);
    }
  }else
  {
    for(i = servo.read(); i <= pos ; i++  )
    {
      servo.write(i);
      delay(50);
    }  
  }
}




/***
 * servoWrite
 * 
 * Sets a servo to a certain degree over a certain time frame
 * 
 * Arguments
 *  - &servo    The Servo that should be written to
 *  - pos       The degree the Servo should be set to
 *  - t         The time, in seconds, it takes to get to the 
 *              degree
 ***/
void servoWrite(Servo &s, int pos, int t)
{
  int spe;
  int i;
  if( s.read() > pos )
  { 
    spe = (t / (s.read() - pos)) * 1000;
    for(i = s.read(); i >= pos ; i--  )
    {
      s.write(i);
      delay(spe);
    }
  }else
  {
    spe =(t / (pos - s.read())) * 1000;
    for(i = s.read(); i <= pos ; i++  )
    {
      s.write(i);
      delay(spe);
    }  
  }  
}

/***
 * 
 * Returns the length of an Array
 * 
 ***/

uint8_t arrayLength(Port arr[])
{
  int i = 0;

  while(arr[i].port != 0)
  {
    i += 1;
  }

  return i;
}



