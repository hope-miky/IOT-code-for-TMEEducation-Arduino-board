#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>
#include "DHTesp.h"

#ifdef ESP32
#pragma message(THIS EXAMPLE IS FOR ESP8266 ONLY!)
#error Select ESP8266 board.
#endif

#define WIFI_SSID "HUAWEI-E5373-81E4"
#define WIFI_PASSWORD "gabbja8g"
#define FIREBASE_HOST "iotfortme.firebaseio.com"
#define FIREBASE_AUTH "ZZHgyCDfFSBLWmoSa6wM6OGjKXXBBO9LrOCU5I7R"

DHTesp dht;

int LED1 = 15;
String val = "";
void setup()
{
Serial.begin(9600);

pinMode(LED1, OUTPUT);

  delay(2000);
  Serial.println('\n');
  
  wifiConnect();

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  delay(10);
  dht.setup(4, DHTesp::DHT11); // Connect DHT sensor to GPIO 4
  delay(10);
}

void loop()
{  
  delay(dht.getMinimumSamplingPeriod());
  
  float humidity = dht.getHumidity();
  float temperature = dht.getTemperature();
  
  val = Firebase.getString("Light");
  delay(100);
  
  Serial.print("LED State: " + val);
  Serial.print("\t\t");
  Serial.print("temperature: " + String(temperature));
  Serial.print("\t\t");
  Serial.println("Humidity: " + String(humidity));
  
  if (Firebase.failed()) {
      Serial.print("reading button state failed:");
      Serial.println(Firebase.error());  
      return;
    }
else{
digitalWrite(LED1, val.toInt());
delay(10);
}

Firebase.setFloat("Temp", temperature);
  // handle error
  if (Firebase.failed()) {
      Serial.print("updating temprature failed:");
      Serial.println(Firebase.error());  
      return;
  }
  delay(100);

  Firebase.setFloat("Humidity", humidity);
  // handle error
  if (Firebase.failed()) {
      Serial.print("updating humidity failed:");
      Serial.println(Firebase.error());  
      return;
  }
  delay(100);
  
  
if(WiFi.status() != WL_CONNECTED)
{
  wifiConnect();
}
delay(100);

}

void wifiConnect()
{
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);             // Connect to the network
  Serial.print("Connecting to ");
  Serial.print(WIFI_SSID); Serial.println(" ...");

  int teller = 0;
  while (WiFi.status() != WL_CONNECTED)
  {                                       // Wait for the Wi-Fi to connect
    delay(1000);
    Serial.print(++teller); Serial.print(' ');
  }

  Serial.println('\n');
  Serial.println("Connection established!");  
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());         // Send the IP address of the ESP8266 to the computer
}
