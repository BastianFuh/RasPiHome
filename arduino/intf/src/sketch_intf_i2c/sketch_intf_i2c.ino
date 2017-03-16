#include <MemoryFree.h>
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

#define TEMP 0x01
#define HUM 0x02
#define LIGHT 0x03

#define SERVO 0x0C

#define DEBUG 0xFE
#define DISCOVERY 0xFF


typedef struct{
  uint8_t  port;
  int      dataLen;
  int     *data;
} recvCommand;

typedef struct{
  uint8_t type;
  uint8_t port;
} Port;


DHT dht(7, DHT22);

Servo s2,s1;

int const address = 0x08;


Port ports[20];

uint8_t port  = 0x00;
uint8_t len   = 0;

int buffLen = 2;

char     sendBuff[32];
float    buff[32];

int      servoPos;

recvCommand commands[10];

int i = 0;

/***
 * Setup
 * 
 * Just executed one
 ***/
void setup() 
{
 
  ports[0].type = SENSOR_TEMPERATURE;
  ports[0].port = TEMP;

  ports[1].type = SENSOR_HUMIDITY;
  ports[1].port = HUM;

  ports[2].type = SENSOR_LIGHT;
  ports[2].port = LIGHT;
  
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
  delay(1000);

  readSensor();


  switch(commands[i].port)
  {
    /***  
     *  Type : Sensor
     *  Spec : Temp
     ***/
    case 0x00:           
    break;


    /***  
     *  Type : Sensor
     *  Spec : Humidity
     ***/
    case 0x0A:
    break;


    /***  
     *  Type : Sensor
     *  Spec : Light
     ***/
    case 0x0B:
    break;


    /***  
     *  Type : Actuator
     *  Spec : Servo
     ***/
    case SERVO:
    int pos, t;
      Serial.print("\n\n\nDataLen: ");
      Serial.println(commands[i].dataLen);
      if ( commands[i].dataLen == 1 )
      {
        Serial.print("\n\n\nPOSITION: ");
        Serial.println(commands[i].data[0]);
        Serial.println(commands[i].data[1]);
        Serial.println(commands[i].data[2]);
        Serial.println(commands[i].data[3]);
        Serial.println(commands[i].data[4]);
        Serial.println(commands[i].data[5]);
        Serial.println(commands[i].data[6]);
        Serial.println(commands[i].data[7]);
        Serial.println(commands[i].data[8]);
        Serial.println(commands[i].data[9]);
        pos = commands[i].data[0];
        servoWrite(s1, servoPos);

        Serial.print("\n\n\nTest: ");
        Serial.println(pos);
       
      } else if (commands[i].dataLen == 2) 
      {
        t = commands[i].data[1];
        servoWrite(s1, pos, t);
      } else
          break;
    break;


    /***  
     *  Type :      
     *  Spec :
     ***/
    case 0x0D:
    break;


    /***  
     *  Type :
     *  Spec : 
     ***/
    case 0x0E:
    break;


    /***  
     *  Type :
     *  Spec : 
     ***/
    case 0x0F:
    break;


    /***
     * Used for the Discovery Process, 
     ***/
     case DISCOVERY:
        
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


    default:
      Serial.println("Invalid Port");
  }

  
  if (i<10 && commands[i].port != NULL)
  {
    commands[i].port = NULL;
    i += 1;
  } else
  {
    i = 0;  
  }

   Serial.print("Ram Free: ");
   Serial.println(freeMemory());
}

int iPorts;
int discoveryFlag = 0;




/***
 * receiveEvent
 * 
 * Executed on read and write request
 * 
 ***/

void receiveEvent(int byteCount)
{
  
   int i = 0;
  
 //  if (discoveryFlag == 0)
      port = Wire.read();
 //  else
 //    iPorts = Wire.read();
      

   while (Wire.available())
   {   
       data[i] = Wire.read();
       i += 1;
   }
   i = 0;


 //  Serial.print("\n\nRECEIVE EVENT ON PORT: \n\n");
 //  Serial.println(port);
   
   switch(port)
   {
      case SERVO:
        addCommand(port, byteCount-1, data);
        servoPos = data[0];
      break;
   }
}

uint8_t portsLen = 0;


  
/***
 * requestEvent
 * 
 * Executed on read requests
 * 
 * 
 ****/
void requestEvent()
{
/*  
  Serial.print("Port ");
  Serial.println(port);

  Serial.print("DF: ");
  Serial.println(discoveryFlag);
  */
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
      if (iPorts == DISCOVERY)
      {
        discoveryFlag = 0;
        iPorts = 0;
        break;
      }
      
      if(discoveryFlag == 0)
      {
        portsLen = arrayLength(ports);
        Wire.write(portsLen);
        discoveryFlag = 1;
      } else if (discoveryFlag == 1)
      {
        sendBuff[0] = ports[iPorts].type;
        sendBuff[1] = ports[iPorts].port;
        
        Wire.write(sendBuff ,32);
      }
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
  buff[LIGHT] = analogRead(0);
  /*
  Serial.println("Read Sensors");
  Serial.print("Temperatur: ");
  Serial.println(buff[TEMP]);
  Serial.print("Humidity: ");
  Serial.println(buff[HUM]);
  Serial.print("Light: ");
  Serial.println(buff[LIGHT]);
*/
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
  Serial.println("Test - Servo 1");
  Serial.print("Postion: ");
  Serial.println(pos);
  int i;
  if( servo.read() > pos )
  { 
    for(i = servo.read(); i >= pos ; i--  )
    {
        //Serial.println("Test - Servo 1 - s.read >");
      servo.write(i);
      delay(50);
    }
  }else
  {
    for(i = servo.read(); i <= pos ; i++  )
    {
      //Serial.println("Test - Servo 1 - s.read <");
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
  Serial.println("Test - Servo 2");
  int spe;
  int i;
  if( s.read() > pos )
  { 
      Serial.println("Test - Servo 2");
    spe = (t / (s.read() - pos)) * 1000;
    for(i = s.read(); i >= pos ; i--  )
    {
      s.write(i);
      delay(spe);
    }
  }else
  {
      Serial.println("Test - Servo 2");
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



