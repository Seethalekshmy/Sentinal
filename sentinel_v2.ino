//sentinal_v2 gives the output in JSON format

#include <WiFi.h>

String getSecurityType(wifi_auth_mode_t type) {

  switch (type) {

    case WIFI_AUTH_OPEN:
      return "OPEN";

    case WIFI_AUTH_WEP:
      return "WEP";

    case WIFI_AUTH_WPA_PSK:
      return "WPA";

    case WIFI_AUTH_WPA2_PSK:
      return "WPA2";

    case WIFI_AUTH_WPA_WPA2_PSK:
      return "WPA/WPA2";

    case WIFI_AUTH_WPA3_PSK:
      return "WPA3";

    case WIFI_AUTH_WPA2_WPA3_PSK:
      return "WPA2/WPA3";

    default:
      return "UNKNOWN";
  }
}

void setup() {

  Serial.begin(115200);

  WiFi.mode(WIFI_STA);
  WiFi.disconnect();

  delay(1000);
}

void loop() {

  int networks = WiFi.scanNetworks();

  for (int i = 0; i < networks; i++) {

    String ssid = WiFi.SSID(i);
    String bssid = WiFi.BSSIDstr(i);

    int rssi = WiFi.RSSI(i);
    int channel = WiFi.channel(i);

    String security =
      getSecurityType(WiFi.encryptionType(i));

    // Send JSON
    Serial.print("{");

    Serial.print("\"ssid\":\"");
    Serial.print(ssid);
    Serial.print("\",");

    Serial.print("\"bssid\":\"");
    Serial.print(bssid);
    Serial.print("\",");

    Serial.print("\"rssi\":");
    Serial.print(rssi);
    Serial.print(",");

    Serial.print("\"channel\":");
    Serial.print(channel);
    Serial.print(",");

    Serial.print("\"security\":\"");
    Serial.print(security);
    Serial.print("\"");

    Serial.println("}");
  }

  WiFi.scanDelete();

  delay(10000);
}
