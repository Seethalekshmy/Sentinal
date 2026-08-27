import sqlite3

DATABASE = "sentinel.db"


def create_database():

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS networks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ssid TEXT,
            bssid TEXT,
            rssi INTEGER,
            channel INTEGER,
            security TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def analyze_networks():

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT bssid, ssid, rssi, channel, security, timestamp
        FROM networks
        ORDER BY timestamp DESC
    """)

    networks = cursor.fetchall()

    connection.close()

    if not networks:
        print("No network data available.")
        return

    print("\n================================")
    print("       SENTINEL ANALYZER")
    print("================================")

    seen = set()

    for network in networks:

        bssid, ssid, rssi, channel, security, timestamp = network

        if bssid not in seen:

            seen.add(bssid)

            print("\nNetwork")
            print("----------------------------")
            print(f"SSID     : {ssid}")
            print(f"BSSID    : {bssid}")
            print(f"RSSI     : {rssi} dBm")
            print(f"Channel  : {channel}")
            print(f"Security : {security}")
            print(f"Last Seen: {timestamp}")

    print("\n================================")
    print(f"Unique Access Points: {len(seen)}")
    print("================================")


if __name__ == "__main__":

    create_database()
    analyze_networks()