# WEEK 8 DAY 4 - SYSTEM INTEGRATION TESTING

## 1. Objective

To test the integration of the motor sensor simulator,
FastAPI backend, CSV storage, Machine Learning model
and Streamlit dashboard.

## 2. Test Cases

| Test | Expected Result | Outcome |
|---|---|---|
| Backend availability | API ONLINE | PASS |
| Healthy simulation | Readings accepted | PASS |
| Warning simulation | Readings accepted | PASS |
| Fault simulation | Readings accepted | PASS |
| CSV storage | Readings saved | PASS |
| Duplicate reading | Duplicate ignored | PASS |
| Invalid temperature | HTTP 422 | PASS |
| Freshness monitoring | LIVE/STALE detected | PASS |
| Dashboard integration | Dashboard displays data | PASS |
| ML integration | Predictions displayed | PASS |

## 3. Observations

The system successfully received and stored motor sensor
readings under healthy, warning and fault simulation
conditions. Duplicate readings were ignored, while
invalid sensor values were rejected.

The backend successfully identified fresh and outdated
sensor data. The Streamlit dashboard displayed sensor
measurements, historical charts and machine learning
predictions.

## 4. Conclusion

The integration tests demonstrated that the prototype
components can communicate and operate together.
The system is ready for final documentation and
demonstration preparation.

Note: Testing was conducted using simulated sensor data.
The prototype has not yet been validated on physical
industrial motor hardware.