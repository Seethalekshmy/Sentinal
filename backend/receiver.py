import serial
import json

from database import create_database, save_network


# ESP32 serial port
PORT = "/dev/cu.usbserial-0001"
BAUD_RATE = 115200


# Create database and table
create_database()


# Connect to ESP32
ser = serial.Serial(PORT, BAUD_RATE, timeout=1)


print("================================")
print("       SENTINEL BACKEND")
print("================================")
print("Waiting for ESP32 data...\n")


while True:

    # Read one line from ESP32
    line = ser.readline().decode("utf-8", errors="ignore").strip()

    # Ignore empty lines
    if not line:
        continue

    try:

        # Convert JSON text into Python dictionary
        data = json.loads(line)

        # Save data into database
        save_network(data)

        # Display data
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