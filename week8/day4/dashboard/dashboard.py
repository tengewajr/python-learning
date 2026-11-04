# WEEK 8 DAY 4 - INTEGRATED MOTOR MONITORING DASHBOARD

from pathlib import Path
from datetime import datetime, timezone

import joblib
import pandas as pd
import requests
import streamlit as st


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="SMART AI Motor Monitoring",
    page_icon="⚙️",
    layout="wide"
)


# ==========================================
# 2. CONFIGURATION AND MODEL LOADING
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

API_URL = "http://127.0.0.1:8000"

MODEL_PATH = BASE_DIR / "motor_health_model.pkl"

FRESHNESS_LIMIT_SECONDS = 10

FEATURES = [
    "temperature",
    "vibration",
    "current",
    "sound",
    "rpm"
]


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


try:
    model = load_model()

except Exception as error:
    st.error(f"Unable to load ML model: {error}")
    st.stop()


# ==========================================
# 3. DASHBOARD HEADER
# ==========================================

st.title("SMART AI Motor Monitoring System")

st.caption(
    "Real-Time Industrial Motor Health Monitoring "
    "and Predictive Maintenance Prototype"
)

st.divider()


# ==========================================
# 4. FETCH SENSOR HISTORY FROM API
# ==========================================

@st.fragment(run_every="2s")
def live_dashboard():

    try:

        response = requests.get(
            f"{API_URL}/history",
            timeout=5
        )

        response.raise_for_status()

        result = response.json()

    except requests.RequestException as error:

        st.error(
            f"Backend connection failed: {error}"
        )

        st.warning(
            "Check whether the FastAPI backend is running."
        )

        return

    records = result.get("history", [])

    if not records:

        st.info(
            "No motor readings available. "
            "Start the sensor simulator."
        )

        return

    df = pd.DataFrame(records)

    # Convert sensor columns to numeric values
    for column in FEATURES:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce",
        utc=True
    )

    df["received_at"] = pd.to_datetime(
        df["received_at"],
        errors="coerce",
        utc=True
    )

    df = df.dropna(
        subset=FEATURES + ["timestamp", "received_at"]
    )

    if df.empty:

        st.warning("No valid sensor readings found.")

        return

    df = df.sort_values("received_at").reset_index(drop=True)


    # ======================================
    # 5. MACHINE LEARNING PREDICTION
    # ======================================

    try:

        X = df[FEATURES]

        predictions = model.predict(X)

        probabilities = model.predict_proba(X)

        df["prediction"] = predictions

        df["prediction_probability"] = (
            probabilities.max(axis=1) * 100
        )

    except Exception as error:

        st.error(f"ML prediction failed: {error}")

        return


    # ======================================
    # 6. DATA FRESHNESS
    # ======================================

    latest = df.iloc[-1]

    current_time = datetime.now(timezone.utc)

    data_age = (
        current_time - latest["received_at"].to_pydatetime()
    ).total_seconds()

    freshness_status = (
        "LIVE"
        if 0 <= data_age <= FRESHNESS_LIMIT_SECONDS
        else "STALE"
    )


    # ======================================
    # 7. MOTOR HEALTH OVERVIEW
    # ======================================

    st.subheader("Motor Health Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Motor Health",
        str(latest["prediction"])
    )

    col2.metric(
        "Prediction Confidence",
        f"{latest['prediction_probability']:.2f}%"
    )

    col3.metric(
        "Total Readings",
        len(df)
    )

    col4.metric(
        "Temperature",
        f"{latest['temperature']:.2f} °C"
    )

    st.divider()


    # ======================================
    # 8. DATA FRESHNESS STATUS
    # ======================================

    st.subheader("System Data Status")

    col1, col2 = st.columns(2)

    col1.metric(
        "Data Freshness",
        freshness_status
    )

    col2.metric(
        "Data Age",
        f"{max(data_age, 0):.2f} seconds"
    )

    st.caption(
        f"Last received: {latest['received_at']}"
    )

    st.divider()


    # ======================================
    # 9. LIVE SENSOR MEASUREMENTS
    # ======================================

    st.subheader("Sensor Measurements")

    chart_data = (
        df.tail(50)
        .set_index("timestamp")
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write("Temperature (°C)")
        st.line_chart(chart_data[["temperature"]])

        st.write("Vibration")
        st.line_chart(chart_data[["vibration"]])

        st.write("Current (A)")
        st.line_chart(chart_data[["current"]])

    with col2:

        st.write("Sound")
        st.line_chart(chart_data[["sound"]])

        st.write("Motor Speed (RPM)")
        st.line_chart(chart_data[["rpm"]])

    st.divider()


    # ======================================
    # 10. MOTOR HEALTH PREDICTION HISTORY
    # ======================================

    st.subheader("Motor Health Prediction History")

    prediction_counts = (
        df["prediction"]
        .value_counts()
        .rename_axis("Health Status")
        .reset_index(name="Number of Readings")
        .set_index("Health Status")
    )

    st.bar_chart(prediction_counts)

    st.divider()


    # ======================================
    # 11. RECENT MOTOR READINGS
    # ======================================

    st.subheader("Recent Motor Readings")

    display_columns = [
        "reading_id",
        "timestamp",
        "temperature",
        "vibration",
        "current",
        "sound",
        "rpm",
        "prediction",
        "prediction_probability"
    ]

    st.dataframe(
        df[display_columns].tail(20).iloc[::-1],
        hide_index=True,
        use_container_width=True
    )

    st.caption(
        "Dashboard automatically refreshes every 2 seconds."
    )


# ==========================================
# 12. RUN DASHBOARD
# ==========================================

live_dashboard()