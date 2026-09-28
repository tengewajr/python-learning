from fastapi import FastAPI
from pydantic import BaseModel

from datetime import datetime

from pathlib import Path
import csv
import joblib
import pandas as pd

app = FastAPI()


# ==================================================
# 1. LOAD MACHINE LEARNING MODEL
# ==================================================

MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "day4"
    / "motor_health_model.pkl"
)   

model = joblib.load(MODEL_PATH)

# ==================================================
# 2. MODEL FEATURES
# ==================================================

FEATURES = [
    "temperature",
    "vibration",
    "current",
    "sound",
    "rpm"
]


# ==================================================
# 3. SENSOR DATA MODEL
# ==================================================

class SensorData(BaseModel):

    temperature: float
    vibration: float
    current: float
    sound: float
    rpm: float


# ==================================================
# 4. HOME ENDPOINT
# ==================================================

@app.get("/")
def home():

    return {
        "message": 
        "SMART AI Motor Monitoring Backend is running"
    }

# ==================================================
# 5. SENSOR DATA ENDPOINT
# ==================================================

@app.post("/sensor-data")
def receive_sensor_data(data: SensorData):

    # --------------------------------------------------
    # Server-side timestamp
    # --------------------------------------------------
    received_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # --------------------------------------------------
    # Prepare sensor data for ML Model
    # --------------------------------------------------

    model_input = pd.DatFrame(
        [[
            data.temperature,
            data.vibration,
            data.current,
            data.sound,
            data.rpm
    ]],
        columns = FEATURES
    )

     # ==================================================
    # 6. MACHINE LEARNING PREDICTION
    # ==================================================

    prediction = model.predict(
        model_input
    )[0]

    probabilities = model.predict_proba(
        model_input
    )[0]

    prediction_probability = (
        max(probabilities) * 100
    )


    # ==================================================
    # 7. MOTOR HEALTH RECOMMENDATION
    # ==================================================

    if prediction == "HEALTHY":

        recommendation = (
            "Motor operating normally. "
            "Continue monitoring."
        )

    elif prediction == "WARNING":

        recommendation = (
            "Abnormal motor condition detected. "
            "Inspect and continue monitoring."
        )

    else:

        recommendation = (
            "Critical motor condition detected. "
            "Inspection is recommended."
        )

    # ==================================================
    # 8. DISPLAY LIVE RESULT
    # ==================================================

    print("\n==============================================")
    print("         LIVE MOTOR ANALYSIS")
    print("==============================================")

    print(f"Time          : {received_at}")
    print(f"Temperature   : {data.temperature} °C")
    print(f"Vibration     : {data.vibration}")
    print(f"Current       : {data.current} A")
    print(f"Sound         : {data.sound} dB")
    print(f"RPM           : {data.rpm} rpm")

    print("----------------------------------------------")

    print(f"ML Prediction : {prediction}")
    print(f"Confidence    : {prediction_probability:.2f}%"    )

    print(f"Recommendation: {recommendation}")


    # ==================================================
    # 9. SAVE DAY 4 MOTOR HEALTH DATA TO CSV
    # ==================================================

    csv_file = (
        Path(__file__).resolve().parent 
        / "day4"
        / "motor_health_data.csv"
    )

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
                "rpm",
                "prediction",
                "prediction_probability"
            ])

        # Write current reading
        writer.writerow([
            received_at,
            data.temperature,
            data.vibration,
            data.current,
            data.sound,
            data.rpm,
            prediction,
            round(prediction_probability, 2)
        ])

    # ==================================================
    # 10. RETURN API RESPONSE
    # ==================================================

    return {
        "message":
            "Sensor data received and stored successfully",

        "timestamp": 
            received_at,

        "prediction":
            prediction,

        "prediction_probability":
            round(prediction_probability, 2),

        "recommendation":
            recommendation
    }
