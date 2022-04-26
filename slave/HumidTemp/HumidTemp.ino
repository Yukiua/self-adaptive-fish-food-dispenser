#include "DHT.h";
#define Type DHT11;
int sensePin = 9;
DHT HT(sensePin,DHT11);
float humidity;
float tempC;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  HT.begin();
  delay(500);
}

void loop() {
  // put your main code here, to run repeatedly:
  humidity = HT.readHumidity();
  tempC = HT.readTemperature();
  Serial.print(humidity);
  Serial.print(",");
  Serial.print(tempC);
  delay(1000);
}
