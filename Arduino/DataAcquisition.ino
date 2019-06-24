#include<DS1302.h>
#include <SD.h>
#include <SPI.h>
#include <OneWire.h>
#include <DallasTemperature.h>
OneWire ourWire1(9);
DallasTemperature sensors1(&ourWire1);
File myFile;
DS1302 rtc(8,7,6);
Time t;
int pinCS =10;
int contador=0;
void setup() {
  delay(1000);
  Serial.begin(9600);
  sensors1.begin();
  pinMode(pinCS,OUTPUT);
  if(SD.begin()){
    Serial.println("contador,fecha,hora,temperature");
  }
  else{
    Serial.begin("SD card no pudo iniciar correctamente");
    return;
  }
}

void loop() {
  contador=contador+1;
  sensors1.requestTemperatures();
  float temp1 = sensors1.getTempCByIndex(0);
  Serial.println(temp1);
  t=rtc.getTime();
  myFile=SD.open("datos_v1.txt", FILE_WRITE);
  if(myFile){
      myFile.print(contador);
      myFile.print(",");
      myFile.print(t.date);
      myFile.print("-");
      myFile.print(t.mon,DEC);
      myFile.print("-");
      myFile.print(t.year);
      myFile.print(",");
      myFile.print(t.hour);
      myFile.print(":");
      myFile.print(t.min);
      myFile.print(":");
      myFile.print(t.sec);
      myFile.print(",");
      myFile.println(temp1);
      myFile.close();
  }
  else{
    Serial.println("Error opening file");
  }
  Serial.print(contador);
  Serial.print(",");
  Serial.print(t.date);
  Serial.print("-");
  Serial.print(t.mon,DEC);
  Serial.print("-");
  Serial.print(t.year);
  Serial.print(",");
  Serial.print(t.hour);
  Serial.print(":");
  Serial.print(t.min);
  Serial.print(":");
  Serial.print(t.sec);
  Serial.print(",");
  Serial.println(temp1);
  delay(1000);
}
