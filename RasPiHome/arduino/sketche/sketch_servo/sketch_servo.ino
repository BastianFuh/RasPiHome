#include <Servo.h>


Servo servo;

int pos;

void begin(int servoPin)
{
    servo.attach(servoPin);
}

boolean attached()
{
  servo.attached()
}

int read()
{
  return servo.read();
}

void write(int deg)
{
  servo.write(deg);
}

void move(int startDeg, int endDeg, int t )
{

  int s;
      
  if ( startDeg > endDeg )
  {
    s = t / (startDeg - endDeg);
    for( int i = startDeg; i > endDeg; i-- )
    {
      servo.write(i);
      delay(s);
    }
  }
  else
  {
    s = t / (endDeg - startDeg); 
        
    for( int i = startDeg; i < endDeg; i++ )
    {
      servo.write(i);
      delay(s);
    }
  }    
}



void end()
{
  servo.detach();  
}
  





