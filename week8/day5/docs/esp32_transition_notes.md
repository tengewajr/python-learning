# TRANSITION FROM SIMULATOR TO ESP32

## Current System

The prototype currently generates simulated sensor
readings using Python.

The readings are transmitted to the FastAPI backend
using HTTP POST requests with JSON payloads.

## Proposed Physical Implementation

The Python simulator will be replaced by an ESP32
microcontroller connected to suitable sensors.

Potential sensors include:

- Temperature sensor
- Vibration sensor
- Current sensor
- Sound sensor

RPM measurement will require a suitable speed sensor.

## Proposed Communication Flow

Physical Sensors
       |
       v
     ESP32
       |
       v
 Wi-Fi / HTTP / JSON
       |
       v
 FastAPI Backend
       |
       v
 Data Storage / ML / Dashboard

## Components That Can Remain

- FastAPI backend
- Data validation
- CSV or future database storage
- Random Forest model
- Streamlit dashboard

## Requirements Before Hardware Deployment

- Select and verify sensor models.
- Calibrate sensor measurements.
- Confirm electrical compatibility.
- Define suitable sampling intervals.
- Implement secure communication.
- Test the system using real motor measurements.