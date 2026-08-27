import serial
import json

PORT = "/dev/cu.usbserial-0001"
BAUD_RATE = 115200

ser = serial.Serial(PORT, BAUD_RATE, timeout=1)

print("================================")
print("       SENTINEL BACKEND")
print("================================")
print("Waiting for ESP32 data...\n")

while True:

    line = ser.readline().decode("utf-8", errors="ignore").strip()

    if not line:
        continue

    try:
        data = json.loads(line)

        print("Network detected")
        print("----------------------------")
        print(f"SSID     : {data['ssid']}")
        print(f"BSSID    : {data['bssid']}")
        print(f"RSSI     : {data['rssi']} dBm")
        print(f"Channel  : {data['channel']}")
        print(f"Security : {data['security']}")
        print()

    except json.JSONDecodeError:
        # Ignore anything that isn't valid JSON
        continue