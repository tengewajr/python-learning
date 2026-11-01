
# Week 7 Day 4
# Generate Synthetic Motor Health Training Data

import numpy as np
import pandas as pd

from pathlib import Path


# ==================================================
# 1. CONFIGURATION
# ==================================================

rng = np.random.default_rng(42)

number_per_class = 600

output_file = (
    Path(__file__).resolve().parent
    / "motor_health_training_data.csv"
)


# ==================================================
# 2. GENERATE SENSOR READINGS
# ==================================================

def generate_class(label, number, severity_range):

    severity = rng.uniform(
        severity_range[0],
        severity_range[1],
        number
    )

    temperature = (
        60 + 22 * severity
        + rng.normal(0, 3.5, number)
    )

    vibration = (
        0.12 + 0.40 * severity
        + rng.normal(0, 0.065, number)
    )

    current = (
        8.1 + 2.8 * severity
        + rng.normal(0, 0.60, number)
    )

    sound = (
        30 + 16 * severity
        + rng.normal(0, 3.5, number)
    )

    rpm = (
        1490 - 180 * severity
        + rng.normal(0, 40, number)
    )

    return pd.DataFrame({

        "temperature": np.clip(
            temperature, 35, 110
        ),

        "vibration": np.clip(
            vibration, 0.01, 1.2
        ),

        "current": np.clip(
            current, 0.2, 20
        ),

        "sound": np.clip(
            sound, 5, 100
        ),

        "rpm": np.clip(
            rpm, 500, 2500
        ),

        "health_status": label
    })


# ==================================================
# 3. GENERATE THREE CLASSES
# ==================================================

healthy_data = generate_class(
    "HEALTHY",
    number_per_class,
    (0.0, 0.50)
)

warning_data = generate_class(
    "WARNING",
    number_per_class,
    (0.25, 0.75)
)

fault_data = generate_class(
    "FAULT",
    number_per_class,
    (0.55, 1.0)
)


# ==================================================
# 4. COMBINE DATA
# ==================================================

df = pd.concat(
    [
        healthy_data,
        warning_data,
        fault_data
    ],
    ignore_index=True
)


df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)


# ==================================================
# 5. SAVE DATASET
# ==================================================

df.to_csv(
    output_file,
    index=False
)


# ==================================================
# 6. DISPLAY RESULTS
# ==================================================

print("==============================================")
print("       MOTOR HEALTH TRAINING DATA")
print("==============================================")

print(f"Total records: {len(df)}")

print("\nClass distribution:")

print(
    df["health_status"].value_counts()
)

print("\nDataset preview:")

print(df.head())

print("\nDataset saved successfully.")
print(output_file)
