from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from pathlib import Path
import csv


app = FastAPI()


# ==================================================
# 1. SENSOR DATA MODEL
# ==================================================

class SensorData(BaseModel):
    temperature: float
    vibration: float
    current: float
    sound: float
    rpm: float


# ==================================================
# 2. HOME ENDPOINT
# ==================================================

@app.get("/")
def home():

    return {
        "message": "SMART AI Motor Monitoring Backend is running"
    }


# ==================================================
# 3. SENSOR DATA ENDPOINT
# ==================================================

@app.post("/sensor-data")
def receive_sensor_data(data: SensorData):

    # Generate server-side timestamp
    received_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # Display received data
    print("\n==============================================")
    print("        SENSOR DATA RECEIVED")
    print("==============================================")

    print(f"Time         : {received_at}")
    print(f"Temperature  : {data.temperature} °C")
    print(f"Vibration    : {data.vibration}")
    print(f"Current      : {data.current} A")
    print(f"Sound        : {data.sound} dB")
    print(f"RPM          : {data.rpm} rpm")

    # ==================================================
    # 4. SAVE DATA TO CSV
    # ==================================================

    csv_file = Path(__file__).resolve().parent / "sensor_data.csv"

    file_exists = csv_file.exists()

    with open(
        csv_file, 
        "a", 
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        # Write header only when the file is new
        if not file_exists:
            writer.writerow([
                "timestamp",
                "temperature",
                "vibration",
                "current",
                "sound",
                "rpm"
            ])

        # Write the received reading
        writer.writerow([
            received_at,
            data.temperature,
            data.vibration,
            data.current,
            data.sound,
            data.rpm
        ])

    # ==================================================
    # 5. RETURN API RESPONSE
    # ==================================================

    return {
        "message": "Sensor data received and stored successfully",
        "timestamp": received_at,
        "data": data.model_dump()
    }
