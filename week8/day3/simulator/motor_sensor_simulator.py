
import time
import random
import requests
from datetime import datetime, timezone

API_URL = "http://127.0.0.1:8000/sensor-data"

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

def get_target_condition(mode):
    modes = {
        "healthy": HEALTHY,
        "warning": WARNING,
        "fault": FAULT
    }

    if mode not in modes:
        raise ValueError("Choose healthy, warning or fault")

    return modes[mode]


def gradual_value(start, end, progress):
    return start + (end - start) * progress


def generate_sensor_reading(mode, progress, sequence):
    target = get_target_condition(mode)

    reading = {
        "temperature": gradual_value(
            HEALTHY["temperature"], target["temperature"], progress
        ),
        "vibration": gradual_value(
            HEALTHY["vibration"], target["vibration"], progress
        ),
        "current": gradual_value(
            HEALTHY["current"], target["current"], progress
        ),
        "sound": gradual_value(
            HEALTHY["sound"], target["sound"], progress
        ),
        "rpm": gradual_value(
            HEALTHY["rpm"], target["rpm"], progress
        )
    }

    reading["temperature"] += random.uniform(-0.5, 0.5)
    reading["vibration"] += random.uniform(-0.02, 0.02)
    reading["current"] += random.uniform(-0.15, 0.15)
    reading["sound"] += random.uniform(-1, 1)
    reading["rpm"] += random.uniform(-5, 5)

    return {
        "reading_id": f"motor-01-{sequence:06d}",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature": round(reading["temperature"], 2),
        "vibration": round(max(0, reading["vibration"]), 2),
        "current": round(max(0, reading["current"]), 2),
        "sound": round(max(0, reading["sound"]), 2),
        "rpm": round(max(0, reading["rpm"]))
    }


def send_reading(payload):
    max_attempts = 3

    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.post(
                API_URL,
                json=payload,
                timeout=5
            )

            if response.status_code >= 500:
                print(f"Server error. Attempt {attempt}/{max_attempts}")
                if attempt < max_attempts:
                    time.sleep(2)
                    continue
                response.raise_for_status()

            response.raise_for_status()

            result = response.json()
            print(f"API response: {result['status']}")
            return True

        except (requests.Timeout, requests.ConnectionError) as error:
            print(f"Communication problem: {error}")

            if attempt < max_attempts:
                print("Retrying in 2 seconds...")
                time.sleep(2)
            else:
                print("Final failure: reading was not delivered.")

        except requests.HTTPError as error:
            print(f"API rejected the request: {error}")
            return False

    return False


def main():
    mode = input(
        "Choose motor condition (healthy/warning/fault): "
    ).lower().strip()

    target = get_target_condition(mode)

    number = int(input("Enter number of readings: "))

    if number < 1:
        print("Number of readings must be at least 1.")
        return

    for i in range(number):
        progress = i / (number - 1) if number > 1 else 1

        payload = generate_sensor_reading(
            mode, progress, i + 1
        )

        print(f"\nSending reading {i + 1}/{number}")
        print(payload)

        send_reading(payload)

        time.sleep(2)


if __name__ == "__main__":
    main()
