# Sensor Data Validation Notes

## 1. Introduction
This document describes the validation rules
applied to incoming motor sensor readings.

## 2. Expected Sensor Payload
- temperature
- vibration
- current
- sound
- rpm

## 3. Validation Rules
- All five fields are required.
- Sensor values must be numeric.
- Negative values are rejected.
- Values outside the defined prototype
  ranges are rejected.
- Unexpected fields are rejected.

## 4. Accepted Reading
Include one valid JSON payload.

## 5. Rejected Readings
Include examples of:
- Missing sensor field
- Negative temperature
- Invalid data type

## 6. HTTP Response
Valid readings: 200
Invalid readings: 422

## 7. Limitations
The validation ranges are prototype
assumptions and require confirmation
against actual sensor and motor specifications.