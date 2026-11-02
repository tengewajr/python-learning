
from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, timezone

app = FastAPI(title="Week 8 Day 2 - Reliable Motor API")

# Temporary duplicate tracking for this test.
# Day 3 will introduce persistent storage.
processed_readings = set()


class SensorData(BaseModel):
    model_config = ConfigDict(extra="forbid")

    reading_id: str = Field(strict=True, min_length=1)
    timestamp: datetime

    temperature: float = Field(strict=True, ge=0, le=150, allow_inf_nan=False)
    vibration: float = Field(strict=True, ge=0, le=10, allow_inf_nan=False)
    current: float = Field(strict=True, ge=0, le=100, allow_inf_nan=False)
    sound: float = Field(strict=True, ge=0, le=120, allow_inf_nan=False)
    rpm: float = Field(strict=True, ge=0, le=10000, allow_inf_nan=False)


@app.get("/")
def home():
    return {"message": "Week 8 Day 2 API is running", "status": "ONLINE"}


@app.post("/sensor-data")
def receive_sensor_data(data: SensorData):

    if data.reading_id in processed_readings:
        return {
            "message": "Duplicate reading ignored",
            "reading_id": data.reading_id,
            "status": "DUPLICATE"
        }

    processed_readings.add(data.reading_id)

    received_at = datetime.now(timezone.utc).isoformat()

    print(f"\nReading ID: {data.reading_id}")
    print(f"Source timestamp: {data.timestamp}")
    print(f"Received at: {received_at}")
    print(f"Temperature: {data.temperature} °C")
    print(f"Vibration: {data.vibration}")
    print(f"Current: {data.current} A")
    print(f"Sound: {data.sound} dB")
    print(f"RPM: {data.rpm}")
    print("Status: ACCEPTED")

    return {
        "message": "Reading received successfully",
        "reading_id": data.reading_id,
        "status": "ACCEPTED",
        "received_at": received_at
    }
