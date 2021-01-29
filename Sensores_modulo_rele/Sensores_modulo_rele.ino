// Example testing sketch for various DHT humidity/temperature sensors
// Written by ladyada, public domain

#include "DHT.h"

#define DHTPIN 2     // what digital pin we're connected to

// Uncomment whatever type you're using!
#define DHTTYPE DHT11   // DHT 11
//define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

// Connect pin 1 (on the left) of the sensor to +5V
// NOTE: If using a board with 3.3V logic like an Arduino Due connect pin 1
// to 3.3V instead of 5V!
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

// Initialize DHT sensor.
// Note that older versions of this library took an optional third parameter to
// tweak the timings for faster processors.  This parameter is no longer needed
// as the current DHT reading algorithm adjusts itself to work on faster procs.
DHT dht(DHTPIN, DHTTYPE);
int analogPin = 0;
int ledVerde = 8;
int ledAmarelo = 9;
int ledVermelho=10;

int valAnalog;
int tensao;

#define pin1 12
#define pin2 13

void setup() {
  Serial.begin(9600);
  
  pinMode(ledVerde, OUTPUT);
  pinMode(ledAmarelo, OUTPUT);
  pinMode(ledVermelho, OUTPUT);
  digitalWrite(ledVerde, LOW);
  digitalWrite(ledAmarelo, LOW);
  digitalWrite(ledVermelho, LOW);

  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  
  dht.begin();
}

void loop() {
  
  delay(2000);

  valAnalog = analogRead(analogPin);
  tensao = map(valAnalog, 0, 1023, 0, 5);

  if (tensao < 2) {
    digitalWrite(ledVerde, HIGH); 
    digitalWrite(ledAmarelo, HIGH); 
    digitalWrite(ledVermelho, HIGH);
    digitalWrite(pin1, LOW);
  } else 
    if (tensao < 3) {
        digitalWrite(ledVerde, HIGH); 
        digitalWrite(ledAmarelo, HIGH); 
        digitalWrite(ledVermelho, LOW);
        digitalWrite(pin1, LOW);
      }
      else
      {
        digitalWrite(ledVerde, LOW); 
        digitalWrite(ledAmarelo, LOW); 
        digitalWrite(ledVermelho, LOW);
        digitalWrite(pin1, HIGH);
      }

   
  float h = dht.readHumidity();
  float t = dht.readTemperature();

 
  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

if (t > 25){
  digitalWrite(pin2, LOW);
}
if (t < 23){
  digitalWrite(pin2, HIGH);
}

  // Compute heat index in Fahrenheit (the default)

  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print(h);
  Serial.print(' ');
  Serial.print(t);
  Serial.print(' ');
  Serial.print(digitalRead(pin1));
  Serial.print(' ');
  Serial.println(digitalRead(pin2));


  
}
