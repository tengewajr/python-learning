# New validation backend from original week7/day3/main.py  backend code. 
# This version uses FastAPI and Pydantic for data validation.

from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, timezone

app = FastAPI(
    title="Week 8 - Sensor Data Validation API",
    description="Testing data quality and validation for the SMART AI Motor Monitoring System",
    version="1.0"
)


# Define the expected sensor data structure
class SensorData(BaseModel):

    model_config = ConfigDict(extra="forbid")

 # ge=0, le=150, allow_inf_nan=False ensures that the temperature is a float between 0 and 150, 
 # and does not allow infinite or NaN values.  
    temperature: float = Field(
        strict=True, ge=0, le=150, allow_inf_nan=False
    )

    vibration: float = Field(
        strict=True, ge=0, le=10, allow_inf_nan=False
    )

    current: float = Field(
        strict=True, ge=0, le=100, allow_inf_nan=False
    )

    sound: float = Field(
        strict=True, ge=0, le=120, allow_inf_nan=False
    )

    rpm: float = Field(
        strict=True, ge=0, le=10000, allow_inf_nan=False
    )


# API home endpoint
@app.get("/")
def home():

    return {
        "message": "Week 8 Sensor Validation API is running",
        "status": "ONLINE"
    }


# Receive and validate sensor readings
@app.post("/sensor-data")
def receive_sensor_data(data: SensorData):

    received_at = datetime.now(timezone.utc).isoformat()

    print("\n========== SENSOR DATA RECEIVED ==========")

    print(f"Received At: {received_at}")
    print(f"Temperature: {data.temperature} °C")
    print(f"Vibration:   {data.vibration}")
    print(f"Current:     {data.current} A")
    print(f"Sound:       {data.sound} dB")
    print(f"Motor RPM:   {data.rpm}")

    print("Data validation: SUCCESS")
    print("==========================================\n")

    return {
        "message": "Sensor data received and validated successfully",
        "validation_status": "VALID",
        "received_at": received_at,
        "sensor_data": data.model_dump()
    }
