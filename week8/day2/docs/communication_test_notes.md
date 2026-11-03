# Communication Test Notes – Week 8 Day 2

## Objective
To test reliable communication between the motor simulator
and FastAPI backend.

## Test Cases

| Test | Expected Behaviour | Observed Result |
|---|---|---|
| Backend online | Reading accepted | Pending |
| Backend unavailable | Limited retries performed | Pending |
| Backend restarted | New readings delivered | Pending |
| Duplicate reading ID | Duplicate ignored | Pending |

## Communication Improvements
- Added a 5-second HTTP timeout.
- Implemented a maximum of three attempts.
- Added a 2-second retry delay.
- Added unique reading identifiers.
- Added UTC timestamps.
- Added duplicate-reading detection.

## Limitations
Duplicate tracking currently uses an in-memory set.
It is cleared whenever the backend restarts.
Persistent duplicate detection will be considered
during the storage implementation.