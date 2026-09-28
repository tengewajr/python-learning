import random
import csv
from pathlib import Path


# ==================================================
# 1. MOTOR CONDITION RANGES
# ==================================================

HEALTHY = {
    "temperature": (58, 64),
    "vibration": (0.10, 0.20),
    "current": (7.8, 8.7),
    "sound": (28, 34),
    "rpm": (1470, 1490)
}


WARNING = {
    "temperature": (65, 74),
    "vibration": (0.20, 0.38),
    "current": (8.7, 9.8),
    "sound": (34, 41),
    "rpm": (1380, 1470)
}


FAULT = {
    "temperature": (75, 85),
    "vibration": (0.38, 0.60),
    "current": (9.8, 11.5),
    "sound": (41, 50),
    "rpm": (1250, 1380)
}


CONDITIONS = {
    "HEALTHY": HEALTHY,
    "WARNING": WARNING,
    "FAULT": FAULT
}


# ==================================================
# 2. GENERATE ONE SENSOR READING
# ==================================================

def generate_reading(condition):

    values = CONDITIONS[condition]

    return {
        "temperature": round(
            random.uniform(*values["temperature"]), 2
        ),

        "vibration": round(
            random.uniform(*values["vibration"]), 2
        ),

        "current": round(
            random.uniform(*values["current"]), 2
        ),

        "sound": round(
            random.uniform(*values["sound"]), 2
        ),

        "rpm": round(
            random.uniform(*values["rpm"])
        ),

        "health_status": condition
    }


# ==================================================
# 3. GENERATE DATASET
# ==================================================

output_file = (
    Path(__file__).resolve().parent
    / "motor_health_training_data.csv"
)


number_per_class = 500


with open(
    output_file,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "temperature",
        "vibration",
        "current",
        "sound",
        "rpm",
        "health_status"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    for condition in CONDITIONS:

        for _ in range(number_per_class):

            reading = generate_reading(condition)

            writer.writerow(reading)


print("==============================================")
print("      MOTOR HEALTH TRAINING DATA")
print("==============================================")

print("Dataset created successfully.")
print(f"File: {output_file}")
print(f"Records per class: {number_per_class}")
print(f"Total records: {number_per_class * 3}")