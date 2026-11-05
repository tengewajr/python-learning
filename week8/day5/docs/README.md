# SMART AI MOTOR MONITORING SYSTEM

## 1. Project Overview

A machine-learning-based prototype for monitoring
industrial motor operating conditions and identifying
potential health states using simulated sensor data.

## 2. Technologies Used

- Python 3.13
- FastAPI
- Uvicorn
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- Requests
- CSV data storage

## 3. Sensor Parameters

- Temperature
- Vibration
- Current
- Sound
- RPM

## 4. System Components

1. Motor sensor simulator
2. FastAPI backend
3. Data validation and duplicate detection
4. CSV sensor history storage
5. Random Forest classification model
6. Streamlit monitoring dashboard

## 5. Installation

Install the required packages:

pip install fastapi "uvicorn[standard]" requests pandas numpy scikit-learn joblib streamlit

## 6. Running the System

Terminal 1 - Backend:

cd week8/day5/backend

python -m uvicorn main:app --reload

Terminal 2 - Simulator:

cd week8/day5/simulator

python motor_sensor_simulator.py

Terminal 3 - Dashboard:

cd week8/day5/dashboard

python -m streamlit run dashboard.py

## 7. API Endpoints

GET /

POST /sensor-data

GET /history

GET /latest

API documentation:

http://127.0.0.1:8000/docs

## 8. Simulation Modes

- HEALTHY
- WARNING
- FAULT

## 9. Limitations

- Sensor measurements are simulated.
- The ML model was trained using synthetic data.
- The prototype has not been validated on physical
  industrial motor hardware.
- The freshness threshold is experimental.
- Predictions are not certified industrial safety decisions.

## 10. Future Improvements

- Integrate physical ESP32 hardware.
- Connect actual motor sensors.
- Collect real industrial motor datasets.
- Calibrate sensors and validate the ML model.
- Improve data storage and deployment security.