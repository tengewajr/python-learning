# Week 7 Day 1 — Hardware Research

## FYP
SMART AI Power Monitor and Predictive Maintenance System for Industrial Motors

## 1. Project Hardware Architecture

Industrial Motor
→ Temperature, Vibration, Current and Sound Sensors
→ ESP32
→ Wi-Fi
→ Backend/API
→ Machine Learning + Database
→ Dashboard
→ Motor Health Status

### Meaning of the arrows

- Motor → Sensors: Sensors measure physical/electrical conditions associated with motor operation.
- Sensors → ESP32: The ESP32 receives sensor signals through appropriate interfaces.
- ESP32 → Wi-Fi: The ESP32 sends collected readings through a wireless network.
- Wi-Fi → Backend/API: Sensor data is transmitted to the server for processing.
- Backend/API → Machine Learning: Validated readings are prepared and passed to the trained model.
- Backend/API → Database: Readings and predictions can be stored for monitoring and later analysis.
- Machine Learning → Dashboard: The model prediction is made available to the dashboard.
- Dashboard → Motor Health Status: The dashboard presents readings, trends, prediction and motor status.

---

# 2. Temperature Sensor

## Preferred candidate: DS18B20

**What it measures:**  
Temperature in degrees Celsius.

**Type of output:**  
Digital output.

**How ESP32 would read it:**  
Through the 1-Wire digital communication bus using a GPIO/data pin.

**Possible use in motor monitoring:**  
Monitor motor temperature and identify abnormal thermal changes or overheating trends.

**Limitations / considerations:**  
The sensor measures the temperature at its sensing location, so mounting position and thermal contact matter. It also has a finite temperature range and accuracy.

**Relevant specifications:**
- -55°C to +125°C measurement range
- ±0.5°C accuracy from -10°C to +85°C
- 9-bit to 12-bit resolution
- 1-Wire interface
- A unique 64-bit device code allows multiple sensors on one bus

---

# 3. Vibration Sensor

## Preferred candidate: ADXL345

**What it measures:**  
Acceleration on three axes, including dynamic acceleration caused by motion or vibration.

**Type of output:**  
Digital output.

**How ESP32 would read it:**  
Through I2C or SPI.

**Possible use in motor monitoring:**  
Monitor mechanical vibration and detect changes in vibration behaviour that may indicate abnormal motor operation.

**Limitations / considerations:**  
The sensor measures acceleration rather than directly reporting a single industrial vibration severity value. Signal processing and feature extraction will therefore be needed for advanced analysis.

**Relevant specifications:**
- 3-axis digital accelerometer
- Selectable ranges: ±2g, ±4g, ±8g, ±16g
- I2C and SPI interfaces
- Selectable bandwidth
- FIFO memory is available for buffered data

---

# 4. Current Sensor

## Candidate: ACS712

**What it measures:**  
Electrical current, including AC or DC current.

**Type of output:**  
Analog voltage proportional to measured current.

**How ESP32 would read it:**  
The ESP32 can read the analog output using an ADC input, with appropriate electrical interfacing and scaling.

**Possible use in motor monitoring:**  
Observe electrical loading and changes in motor current during different operating conditions.

**Limitations / considerations:**  
The ACS712 device is specified for 5 V single-supply operation, so the sensor/module output must be checked before connecting it to an ESP32 ADC. The ESP32 ADC input must not be exposed to an unsafe voltage. Current-sensor calibration is also important.

**Relevant specifications from the manufacturer:**
- Galvanic isolation
- Output proportional to AC or DC current
- 5 V single-supply operation
- Different variants have different sensitivities
- Isolation is specified by the manufacturer for the IC

---

# 5. Sound Sensor

## Preferred candidate: INMP441 MEMS Microphone

**What it measures:**  
Acoustic/sound pressure converted into a digital audio signal.

**Type of output:**  
Digital I2S output.

**How ESP32 would read it:**  
Through the I2S digital audio interface.

**Possible use in motor monitoring:**  
Capture acoustic behaviour of the motor and investigate abnormal changes in sound.

**Limitations / considerations:**  
Environmental noise, microphone placement, mechanical mounting and signal-processing methods can strongly affect the measurements.

**Relevant specifications:**
- Digital-output omnidirectional MEMS microphone
- 24-bit I2S interface
- Wide frequency response
- High signal-to-noise ratio

---

# 6. Alternative Sensors Listed in the Week 7 Guide

### Temperature
- DS18B20
- DHT22

### Vibration
- MPU6050
- ADXL345

### Current
- ACS712
- SCT-013

### Sound
- Microphone module
- MEMS microphone

---

# 7. Analog vs Digital Sensors

## Analog sensor

Produces a continuously varying electrical signal.

Example:  
ACS712 current sensor → analog voltage → ESP32 ADC → digital value.

Concept:

Physical quantity
→ Sensor
→ Analog electrical signal
→ ESP32 ADC
→ Digital reading

## Digital sensor

Communicates data in a digital format.

Examples:
- DS18B20 → 1-Wire
- ADXL345 → I2C/SPI
- INMP441 → I2S

Concept:

Physical quantity
→ Sensor
→ Digital communication
→ ESP32
→ Digital reading

---

# 8. Role of ESP32

The ESP32 acts as the field-side controller.

Main responsibilities:

1. Read sensor measurements.
2. Collect measurements at a defined sampling interval.
3. Format the readings, for example as JSON.
4. Connect to Wi-Fi.
5. Transmit the readings to the backend/API.

The ESP32 does not need to perform the whole dashboard/backend workload.

---

# 9. Main FYP Data Flow

Real Motor
→ Sensors
→ ESP32
→ Wi-Fi
→ FastAPI Backend
→ Data Processing
→ ML Model
→ Database / Results
→ Streamlit Dashboard
→ Motor Health Status

---

# 10. Why Multiple Sensors?

A single threshold such as:

Temperature > X

is a simple rule.

A multi-sensor ML approach combines several measurements:

Temperature
+ Vibration
+ Current
+ RPM
+ Sound
→ ML Model
→ Prediction

The purpose is to investigate whether combined operating-condition information can provide more useful motor-health prediction than relying on one simple threshold.

---

# 11. Important FYP Design Note

The Week 6 ML model was trained using:

- Air temperature
- Process temperature
- RPM
- Torque
- Tool wear

The physical Week 7 prototype is being designed around measurements such as:

- Temperature
- Vibration
- Current
- Sound
- RPM
- Voltage / Power where appropriate

Therefore, these feature sets must not be treated as automatically interchangeable.

Before final hardware-to-ML integration, the ML pipeline must use features whose meanings and measurements match the data actually produced by the prototype.

---

# 12. Real Data Integration Later

The complete system can support three data sources:

## Mode 1 — Simulation
Python Sensor Simulator
→ FastAPI
→ ML
→ Dashboard

## Mode 2 — Real-data replay
Real Motor CSV
→ Data Replayer
→ FastAPI
→ ML
→ Dashboard

## Mode 3 — Physical IoT
Real Motor
→ Sensors
→ ESP32
→ Wi-Fi
→ FastAPI
→ ML
→ Dashboard

The backend, ML and dashboard can therefore be designed as reusable components while the data source changes.

---

# 13. Day 1 Panel Questions

### Q1. What is an ESP32?
A microcontroller used to interface with sensors, process or format readings, and communicate data over networks such as Wi-Fi.

### Q2. What is GPIO?
General Purpose Input/Output pins used by the microcontroller to communicate with external devices.

### Q3. What is ADC?
Analog-to-Digital Conversion. It converts an analog electrical signal into a digital value that the microcontroller can process.

### Q4. Why is ADC important?
Because some sensors produce analog outputs that must be converted into digital values before software can use them.

### Q5. Why use a vibration sensor?
To measure mechanical motion/acceleration and observe changes in motor vibration behaviour.

### Q6. Why measure current?
To observe electrical loading and operating-condition changes.

### Q7. Why use a microphone?
To capture acoustic behaviour and investigate abnormal sound patterns.

### Q8. Why use Wi-Fi?
To transfer sensor data from the ESP32 to the backend/server wirelessly.

### Q9. Why do we need an API?
To provide a defined communication interface through which sensor data can be sent to and processed by the backend.

### Q10. Why use ML instead of only temperature thresholds?
Because the project investigates the use of multiple motor-condition measurements together to support motor-health prediction.

### Q11. What happens to sensor data after the ESP32?
The readings are transmitted to the backend, validated/processed, passed to the ML model, stored where required, and displayed on the dashboard.

### Q12. What would change when replacing the simulator with a real ESP32?
The simulator/data source would be replaced by ESP32 + real sensors. The backend, ML model and dashboard can remain as the same downstream architecture.

---

# 14. Day 1 Practical Deliverable

Create:

hardware_research.md

The file should contain the four sensor studies above, followed by the FYP architecture and the explanation of each data-flow arrow.

## Day 1 Success Test

Before moving to Day 2, you should be able to draw this from memory:

Motor
↓
Sensors
↓
ESP32
↓
Wi-Fi
↓
Backend/API
↓
ML + Database
↓
Dashboard
↓
Motor Health Status
