from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, timezone
from pathlib import Path
import csv
import os

app = FastAPI(
    title="Week 8 Day 4 - Sensor History & Freshness API",
    description="Motor sensor data storage and freshness monitoring",
    version="1.0"
)

# Create the data directory and CSV file automatically
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CSV_FILE = DATA_DIR / "sensor_data.csv"

DATA_DIR.mkdir(parents=True, exist_ok=True)

FIELDS = [
    "reading_id", "timestamp", "received_at",
    "temperature", "vibration", "current", "sound", "rpm"
]

if not CSV_FILE.exists():
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()

# Experimental freshness threshold
FRESHNESS_LIMIT_SECONDS = 10

class SensorData(BaseModel):
    model_config = ConfigDict(extra="forbid")

    reading_id: str = Field(strict=True, min_length=1)
    timestamp: datetime

    temperature: float = Field(strict=True, ge=0, le=150, allow_inf_nan=False)
    vibration: float = Field(strict=True, ge=0, le=10, allow_inf_nan=False)
    current: float = Field(strict=True, ge=0, le=100, allow_inf_nan=False)
    sound: float = Field(strict=True, ge=0, le=120, allow_inf_nan=False)
    rpm: float = Field(strict=True, ge=0, le=10000, allow_inf_nan=False)

def read_all_records():
    with open(CSV_FILE, "r", newline="") as file:
        return list(csv.DictReader(file))

@app.get("/")
def home():
    return {
        "message": "Day 4 Sensor History API is running",
        "status": "ONLINE"
    }

@app.post("/sensor-data")
def receive_sensor_data(data: SensorData):

    records = read_all_records()

    # Prevent duplicate readings
    if any(row["reading_id"] == data.reading_id for row in records):
        return {
            "message": "Duplicate reading ignored",
            "reading_id": data.reading_id,
            "status": "DUPLICATE"
        }

    received_at = datetime.now(timezone.utc)

    record = {
        "reading_id": data.reading_id,
        "timestamp": data.timestamp.isoformat(),
        "received_at": received_at.isoformat(),
        "temperature": data.temperature,
        "vibration": data.vibration,
        "current": data.current,
        "sound": data.sound,
        "rpm": data.rpm
    }

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow(record)

    print(f"Stored reading: {data.reading_id}")

    return {
        "message": "Reading stored successfully",
        "reading_id": data.reading_id,
        "status": "ACCEPTED"
    }

@app.get("/history")
def get_history():
    records = read_all_records()

    return {
        "total_readings": len(records),
        "history": records
    }

@app.get("/latest")
def get_latest_reading():
    records = read_all_records()

    if not records:
        return {
            "message": "No sensor readings available",
            "status": "NO DATA"
        }

    latest = records[-1]

    received_time = datetime.fromisoformat(latest["received_at"])
    age = (datetime.now(timezone.utc) - received_time).total_seconds()

    status = (
        "LIVE"
        if 0 <= age <= FRESHNESS_LIMIT_SECONDS
        else "STALE"
    )

    return {
        "reading": latest,
        "data_age_seconds": round(age, 2),
        "freshness_limit_seconds": FRESHNESS_LIMIT_SECONDS,
        "status": status
    }