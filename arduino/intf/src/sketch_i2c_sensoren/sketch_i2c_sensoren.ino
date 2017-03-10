#include <Wire.h>
#include <Adafruit_TCS34725.h>

uint16_t clea, red, green, blue;

Adafruit_TCS34725 rgbLS;

void setup() 
{
  Wire.begin();

  rgbLS.begin();

  Serial.begin(9600);


}

void loop()
{

  rgbLS.setInterrupt(false);
  delay(100);
  rgbLS.getRawData(&red, &green, &blue,&clea);
  rgbLS.setInterrupt(true);

  uint32_t sum = clea;
  float r, g, b;

  r = red;   r /= sum;
  g = green; g /= sum;
  b = blue; b /= sum;

  r *= 256; g *= 256; b *= 256;

  Serial.print("Clear Value: "); Serial.println(clea);
  Serial.print("R Hex: "); Serial.println((int) r, HEX);
  Serial.print("G Hex: "); Serial.println((int) g, HEX);
  Serial.print("B Hex: "); Serial.println((int) b, HEX);




  delay(1000);
}
