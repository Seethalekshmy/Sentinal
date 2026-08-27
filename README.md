# SENTINEL — ESP32 Wi-Fi Security Monitor

A hardware-based Wi-Fi monitoring project built using an **ESP32 and Python**.

SENTINEL scans nearby Wi-Fi networks, collects wireless network information,
converts the data into JSON, sends it to a Python backend through USB Serial,
and stores the collected data in a SQLite database.

> Project Status:  Early Development

---

## Overview

SENTINEL is being developed as a lightweight wireless monitoring system
that combines **embedded systems, networking, Python, databases, and
cybersecurity concepts**.

Currently, the ESP32 performs Wi-Fi scanning and sends structured network
information to a Python application.

The Python backend receives the data and stores each observation in a
SQLite database for future analysis.

---

## Current Architecture

```text
             Wi-Fi Environment
                    │
                    ▼
             ┌─────────────┐
             │    ESP32    │
             │ Wi-Fi Scan  │
             └──────┬──────┘
                    │
                    ▼
                  JSON
                    │
                    ▼
              USB Serial
                    │
                    ▼
             ┌─────────────┐
             │   Python    │
             │   Receiver  │
             └──────┬──────┘
                    │
                    ▼
             ┌─────────────┐
             │   SQLite    │
             │   Database  │
             └─────────────┘
