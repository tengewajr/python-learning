# Day 2
# Motor Sensor Simulator
# Simulates an ESP32-connected industrial motor

import time
import random
from datetime import datetime


# ==================================================
# 1. MOTOR CONDITIONS
# ==================================================

HEALTHY = {
    "temperature": 61.0,
    "vibration": 0.15,
    "current": 8.3,
    "sound": 31,
    "rpm": 1482
}


WARNING = {
    "temperature": 70.0,
    "vibration": 0.28,
    "current": 9.2,
    "sound": 38,
    "rpm": 1430
}

FAULT = {
    "temperature": 82.0,
    "vibration": 0.52,
    "current": 10.8,
    "sound": 45,
    "rpm": 1290
}


# ==================================================
# 2. GET TARGET CONDITIONS
# ==================================================

def get_target_condition(mode):

    if mode == "healthy":
        return HEALTHY

    elif mode == "warning":
        return WARNING

    elif mode == "fault":
        return FAULT

    else:
        raise ValueError(
        "Invalid mode. Choose healthy, warning or fault"
    )


# ==================================================
# 3. GRADUAL VALUE CALCULATION
# ==================================================

def gradual_value(start, end, progress):
    return start + (end - start) * progress


# ==================================================
# 4. GENERATE SENSOR READINGS
# ==================================================

def generate_sensor_reading(mode, progress):

    target = get_target_condition(mode)

    # Gradually move from healthy condition
    # towards the selected condition.
    temperature = gradual_value(
        HEALTHY["temperature"],
        target["temperature"],
        progress
    )

    vibration = gradual_value(
        HEALTHY["vibration"],
        target["vibration"],
        progress
    )

    current = gradual_value(
        HEALTHY["current"],
        target["current"],
        progress
    )

    sound = gradual_value(
        HEALTHY["sound"],
        target["sound"],
        progress
    )

    rpm = gradual_value(
        HEALTHY["rpm"],
        target["rpm"],
        progress
    )

    # Add small random variations so the 
    # readings do not look artificially perfect.

    temperature += random.uniform(-0.5, 0.5)
    vibration += random.uniform(-0.02, 0.02)
    current += random.uniform(-0.15, 0.15)
    sound += random.uniform(-1, 1)
    rpm += random.uniform(-5, 5)

    return {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "temperature": round(temperature, 2),
        "vibration": round(vibration, 2),
        "current": round(current, 2),
        "sound": round(sound, 2),
        "rpm": round(rpm)
    }

# ==================================================
# 5. GET USER INPUT
# ==================================================

print("==============================================")
print("        MOTOR SENSOR SIMULATOR")
print("==============================================")

mode = input(
    "\nEnter motor mode "
    "(healthy / warning / fault): "
).strip().lower()

try:
    number_of_readings = int (
    input("Enter number of sensor readings: ")
)
    if number_of_readings <= 0:
        raise ValueError("Number of readings must be greater than 0.")

except ValueError as e:
    print(f"Input error: {e}")
    exit()

# ==================================================
# 6. RUN SIMULATION
# ==================================================

print("\n==============================================")
print(f"        STARTING {mode.upper()} SIMULATION")
print("==============================================")

for i in range (number_of_readings):
    # Progress moves from 0.0 -> 1.0
    if number_of_readings == 1:
        progress = 1.0

    else:
        progress = i/(number_of_readings - 1)

    reading = generate_sensor_reading(mode, progress)

    print("\n----------------------------------------------")
    print(f"Reading {i + 1}/{number_of_readings}")
    print("----------------------------------------------")

    print(
        f"Time         : {reading['timestamp']}"
    )

    print(
        f"Progress     : {progress * 100.0:.2f}%"
    )

    print(
        f"Temperature  : {reading['temperature']} ℃"
    )

    print(
        f"Vibration    : {reading['vibration']}"
    )

    print(
        f"Current      : {reading['current']} A"
    )

    print(
        f"Sound        : {reading['sound']} dB"
    )

    print(
        f"RPM          : {reading['rpm']} rpm"
    )

    # Wait before taking the next sample.
    if i < number_of_readings - 1:
        time.sleep(2)

print("\n==============================================")
print("        SENSOR SIMULATION COMPLETE              ")
print("==============================================")
