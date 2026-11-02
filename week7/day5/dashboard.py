# WEEK 7 DAY 5
# STREAMLIT MOTOR MONITORING DASHBOARD

from pathlib import Path

import pandas as pd
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
# 2. DEFINE DATA FILE PATH
# ==========================================

WEEK7_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = WEEK7_DIR / "day4" / "motor_health_data.csv"


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
# 4. LIVE DASHBOARD FUNCTION
# ==========================================

@st.fragment(run_every="2s")
def live_dashboard():

    # Check whether the data file exists
    if not DATA_FILE.exists():

        st.warning(
            "No motor data found. Start the FastAPI backend "
            "and run the motor sensor simulator."
        )

        return

    # Read sensor data
    try:

        df = pd.read_csv(DATA_FILE)

    except (pd.errors.EmptyDataError, pd.errors.ParserError) as error:

        st.error(f"Unable to read sensor data: {error}")

        return

    if df.empty:

        st.info("Waiting for sensor readings...")

        return

    # Check required columns
    required_columns = [
        "timestamp",
        "temperature",
        "vibration",
        "current",
        "sound",
        "rpm",
        "prediction",
        "prediction_probability"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:

        st.error(
            f"Missing columns in CSV file: {missing_columns}"
        )

        return

    # Convert data into appropriate types
    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        errors="coerce"
    )

    sensor_columns = [
        "temperature",
        "vibration",
        "current",
        "sound",
        "rpm",
        "prediction_probability"
    ]

    for column in sensor_columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    df = df.dropna(
        subset=["timestamp", "prediction"]
    )

    df = df.sort_values("timestamp")

    if df.empty:

        st.warning("No valid motor readings are available.")

        return

    # Get latest motor reading
    latest = df.iloc[-1]

    motor_status = str(latest["prediction"])

    prediction_probability = float(
        latest["prediction_probability"]
    )


    # ======================================
    # 5. MOTOR HEALTH OVERVIEW
    # ======================================

    st.subheader("Motor Health Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Motor Status",
        motor_status
    )

    col2.metric(
        "Prediction Confidence",
        f"{prediction_probability:.2f}%"
    )

    col3.metric(
        "Total Readings",
        len(df)
    )

    col4.metric(
        "Temperature",
        f"{latest['temperature']:.2f} °C"
    )

    st.caption(
        f"Last received reading: {latest['timestamp']}"
    )

    st.divider()


    # ======================================
    # 6. SENSOR MEASUREMENTS
    # ======================================

    st.subheader("Live Sensor Measurements")

    chart_data = (
        df.tail(50)
        .set_index("timestamp")
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write("Temperature (°C)")

        st.line_chart(
            chart_data[["temperature"]]
        )

        st.write("Vibration")

        st.line_chart(
            chart_data[["vibration"]]
        )

        st.write("Current (A)")

        st.line_chart(
            chart_data[["current"]]
        )

    with col2:

        st.write("Sound (dB)")

        st.line_chart(
            chart_data[["sound"]]
        )

        st.write("Motor Speed (RPM)")

        st.line_chart(
            chart_data[["rpm"]]
        )

    st.divider()


    # ======================================
    # 7. MOTOR HEALTH PREDICTION HISTORY
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
    # 8. RECENT MOTOR DATA
    # ======================================

    st.subheader("Recent Motor Readings")

    display_columns = [
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
        hide_index=True
    )

    st.caption(
        "Dashboard refreshes automatically every 2 seconds."
    )


# ==========================================
# 9. RUN DASHBOARD
# ==========================================

live_dashboard()