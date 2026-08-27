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


def save_network(data):

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO networks
        (ssid, bssid, rssi, channel, security)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data["ssid"],
        data["bssid"],
        data["rssi"],
        data["channel"],
        data["security"]
    ))

    connection.commit()
    connection.close()