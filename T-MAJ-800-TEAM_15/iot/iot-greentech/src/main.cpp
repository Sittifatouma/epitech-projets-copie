#include <Arduino.h>
#include <WiFiNINA.h>
#include <MQTT.h>
#include <DHT.h>

#define WIFI_SSID "FBX_5257"
#define WIFI_PSWD "6c696c6c653139313231393636"

#define MQTT_HOST "192.168.1.46"
#define MQTT_PORT 1883

#define AIR_TEMP_TOPIC "sensors/greentech/v1/nanorp2040/airTemperature"
#define AIR_HUM_TOPIC "sensors/greentech/v1/nanorp2040/airHumidity"
#define SOIL_MOIST_TOPIC "sensors/greentech/v1/nanorp2040/soilMoisture"
#define BRIGHT_TOPIC "sensors/greentech/v1/nanorp2040/brightness"

#define SOIL_MOISTURE_PIN A2
#define DRY 1020
#define UNDER_WATER 988

#define DHT11_PIN A1
#define DHTTYPE 11

#define BRIGHTNESS_PIN A0

MQTTClient client;
WiFiClient net;

DHT dht(DHT11_PIN, DHTTYPE);

void connect() {
  Serial.print("Checking wifi...");

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }

  Serial.println("\nWifi connected!");

  Serial.print("Checking mqqt...");
  while (!client.connect("nanorp2040", "greentech", "greentech")) {
    Serial.print(".");
    delay(1000);
  }

  Serial.println("\nConnected to mqtt server!\n");

  Serial.println();
}

void setup()
{
  Serial.begin(9600);

  dht.begin();

  WiFi.begin(WIFI_SSID, WIFI_PSWD);
  client.begin(MQTT_HOST, MQTT_PORT, net);

  connect();
}

void publishTopicValue(String topic, String payload)
{
  static int retries = 0;

  if (client.connected()) {
    client.publish(topic, payload);
    retries = 0;
  } else {
    connect();

    if (retries < 10) {
      retries++;
      publishTopicValue(topic, payload);
    } else {
      Serial.println("Couldnt connect to skipping publish\n");
    }
  }
}

void loop()
{
  int moisture_value = analogRead(SOIL_MOISTURE_PIN);
  int moisture_percentage = map(moisture_value, DRY, UNDER_WATER, 0, 100);

  Serial.print("Soil Moisture %: ");
  Serial.println(moisture_percentage);

  publishTopicValue(SOIL_MOIST_TOPIC, String(moisture_percentage));

  float air_temp = dht.readTemperature();
  float air_hum = dht.readHumidity();

  Serial.print("Air Temperature: ");
  Serial.println(air_temp);
  Serial.print("Air Humidity: ");
  Serial.println(air_hum); 

  publishTopicValue(AIR_TEMP_TOPIC, String(air_temp));
  publishTopicValue(AIR_HUM_TOPIC, String(air_hum));

  int brightness = analogRead(BRIGHTNESS_PIN);

  Serial.print("Brightness: ");
  Serial.println(brightness);

  publishTopicValue(BRIGHT_TOPIC, String(brightness));

  Serial.println("Wait 30s\n");
  delay(30000);
}