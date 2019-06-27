#include<DS1302.h>
#include <SD.h>
#include <SPI.h>
#include <OneWire.h>
#include <DallasTemperature.h>
OneWire ourWire1(9); //Se establece el pin 9 como bus OneWire
DallasTemperature sensors1(&ourWire1); //Se declara una variable u objeto para nuestro sensor1
DS1302 rtc(8, 7, 6); //(RST, DAT, CLK)
File myFile;
Time t;


int pinCS = 10; // Pin 10 on Arduino Uno
int contador = 0;

float tempDigital;


void setup()
{
  delay(1000);
  Serial.begin(9600);

  sensors1.begin(); //Se inicia el sensor 1

  pinMode(pinCS, OUTPUT);
  // Configuracion inicial de la SDCard
  if (SD.begin())
  {
    Serial.println("SD card lista para usarse");
  }
  else
  {
    Serial.println("SD card no pudo iniciar correctamente");
    return;
  }
}


void loop() {
  contador = contador + 1;

  sensors1.requestTemperatures(); //Se envía el comando para leer la temperatura
  tempDigital= sensors1.getTempCByIndex(0); //Se obtiene la temperatura en ºC del sensor 1

  myFile = SD.open("datos_v1.txt", FILE_WRITE);

  if (contador == 1) myFile.println("ID,dia,fecha,tiempo,temperatura");
  if (contador == 1) Serial.println("ID,dia,fecha,tiempo,temperatura");


  t = rtc.getTime();
  myFile.print(contador); //Segundos.
  myFile.print(",");
  if (t.dow == 1) myFile.print("Monday");
  if (t.dow == 2) myFile.print("Tuesday");
  if (t.dow == 3) myFile.print("Wednesday");
  if (t.dow == 4) myFile.print("Thursday");
  if (t.dow == 5) myFile.print("Friday");
  if (t.dow == 6) myFile.print("Saturday");
  if (t.dow == 7) myFile.print("Sunday");
  myFile.print(",");
  myFile.print(t.date); // Dia del mes.
  myFile.print("-");
  myFile.print(t.mon, DEC); // Mes.
  myFile.print("-");
  myFile.print(t.year); //Año.
  myFile.print(",");
  myFile.print(t.hour); //Hora en formato 0-24 horas.
  myFile.print(":");
  myFile.print(t.min); //Minutos.
  myFile.print(":");
  myFile.print(t.sec); //Segundos.
  myFile.print(",");
  myFile.println(tempDigital);

  delay(1000); // Demora para no sobrecargar las comunicaciones con el modulo.

  myFile.close(); // close the file
}
