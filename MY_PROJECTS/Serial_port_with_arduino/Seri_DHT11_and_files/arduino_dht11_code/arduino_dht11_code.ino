#include <DHT.h>
#include <DHT_U.h>



#define dht_type DHT11
#define dht_pin 2

DHT dht(dht_pin, dht_type);


void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float sicaklik = dht.readTemperature();
  float nem = dht.readHumidity();

  Serial.println(String(sicaklik) + "," + String(nem));
  delay(500);

}
