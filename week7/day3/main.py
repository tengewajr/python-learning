
# Week 7 Day 4
# FastAPI + Real-Time Motor Health Prediction

from fastapi import FastAPI
from pydantic import BaseModel

from datetime import datetime
from pathlib import Path

import pandas as pd
import csv
import joblib


app = FastAPI()


# ==================================================
# 1. DEFINE FILE PATHS AND LOAD MODEL
# ==================================================

WEEK7_DIR = Path(__file__).resolve().parent.parent

DAY4_DIR = WEEK7_DIR / "day4"

MODEL_PATH = DAY4_DIR / "motor_health_model.pkl"

CSV_PATH = DAY4_DIR / "motor_health_data.csv"


if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Trained model not found: {MODEL_PATH}"
    )

model = joblib.load(MODEL_PATH)


# ==================================================
# 2. DEFINE MODEL FEATURES
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
        "message": "SMART AI Motor Monitoring System is running",
        "model": "Random Forest",
        "status": "Online"
    }


# ==================================================
# 5. RECEIVE SENSOR DATA
# ==================================================

@app.post("/sensor-data")
def receive_sensor_data(data: SensorData):

    received_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    # ==================================================
    # 6. PREPARE INPUT FOR MACHINE LEARNING
    # ==================================================

    model_input = pd.DataFrame(
        [{
            "temperature": data.temperature,
            "vibration": data.vibration,
            "current": data.current,
            "sound": data.sound,
            "rpm": data.rpm
        }],
        columns=FEATURES
    )


    # ==================================================
    # 7. GENERATE ML PREDICTION
    # ==================================================

    prediction = model.predict(
        model_input
    )[0]

    probabilities = model.predict_proba(
        model_input
    )[0]


    class_probabilities = {
        str(label): round(float(probability) * 100, 2)
        for label, probability in zip(
            model.classes_,
            probabilities
        )
    }

    prediction_probability = class_probabilities[
        str(prediction)
    ]


    # ==================================================
    # 8. GENERATE RECOMMENDATION
    # ==================================================

    if prediction == "HEALTHY":

        recommendation = (
            "Motor operating normally. "
            "Continue monitoring."
        )

    elif prediction == "WARNING":

        recommendation = (
            "Abnormal motor condition detected. "
            "Inspection and continued monitoring recommended."
        )

    else:

        recommendation = (
            "Critical motor condition detected. "
            "Inspect the motor."
        )


    # ==================================================
    # 9. DISPLAY LIVE MOTOR ANALYSIS
    # ==================================================

    print("\n==============================================")
    print("             LIVE MOTOR ANALYSIS")
    print("==============================================")

    print(f"Time         : {received_at}")
    print(f"Temperature  : {data.temperature} °C")
    print(f"Vibration    : {data.vibration}")
    print(f"Current      : {data.current} A")
    print(f"Sound        : {data.sound}")
    print(f"RPM          : {data.rpm} rpm")

    print("----------------------------------------------")

    print(f"Prediction   : {prediction}")
    print(f"Probability  : {prediction_probability:.2f}%")

    print("\nClass probabilities:")

    for label, probability in class_probabilities.items():
        print(f"{label:<10}: {probability:.2f}%")

    print(f"\nRecommendation: {recommendation}")


    # ==================================================
    # 10. SAVE MOTOR HEALTH DATA
    # ==================================================

    CSV_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    file_exists = (
        CSV_PATH.exists()
        and CSV_PATH.stat().st_size > 0
    )

    with open(
        CSV_PATH,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

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

        writer.writerow([
            received_at,
            data.temperature,
            data.vibration,
            data.current,
            data.sound,
            data.rpm,
            prediction,
            prediction_probability
        ])


    # ==================================================
    # 11. RETURN API RESPONSE
    # ==================================================

    return {
        "message": "Motor data processed successfully",
        "timestamp": received_at,
        "prediction": prediction,
        "prediction_probability": prediction_probability,
        "class_probabilities": class_probabilities,
        "recommendation": recommendation
    }
