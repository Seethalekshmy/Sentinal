#include <WiFi.h>

void setup() {
  Serial.begin(115200);

  WiFi.mode(WIFI_STA);
  WiFi.disconnect();

  delay(1000);

  Serial.println("================================");
  Serial.println("        SENTINEL v0.1");
  Serial.println("     Wi-Fi Recon Module");
  Serial.println("================================");
}

void loop() {

  Serial.println("\n[+] Starting Wi-Fi scan...");

  int networks = WiFi.scanNetworks();

  if (networks == 0) {
    Serial.println("[-] No networks detected.");
  } 
  else {

    Serial.print("[+] Networks detected: ");
    Serial.println(networks);

    for (int i = 0; i < networks; i++) {

      Serial.println("--------------------------------");

      Serial.print("SSID     : ");
      Serial.println(WiFi.SSID(i));

      Serial.print("BSSID    : ");
      Serial.println(WiFi.BSSIDstr(i));

      Serial.print("RSSI     : ");
      Serial.print(WiFi.RSSI(i));
      Serial.println(" dBm");

      Serial.print("Channel  : ");
      Serial.println(WiFi.channel(i));

      Serial.print("Security : ");

      switch (WiFi.encryptionType(i)) {

        case WIFI_AUTH_OPEN:
          Serial.println("OPEN");
          break;

        case WIFI_AUTH_WEP:
          Serial.println("WEP");
          break;

        case WIFI_AUTH_WPA_PSK:
          Serial.println("WPA");
          break;

        case WIFI_AUTH_WPA2_PSK:
          Serial.println("WPA2");
          break;

        case WIFI_AUTH_WPA_WPA2_PSK:
          Serial.println("WPA/WPA2");
          break;

        case WIFI_AUTH_WPA3_PSK:
          Serial.println("WPA3");
          break;

        case WIFI_AUTH_WPA2_WPA3_PSK:
          Serial.println("WPA2/WPA3");
          break;

        default:
          Serial.println("UNKNOWN");
      }
    }
  }

  WiFi.scanDelete();

  Serial.println("--------------------------------");
  Serial.println("[+] Scan complete.");
  Serial.println("[+] Next scan in 10 seconds...");

  delay(10000);
}
