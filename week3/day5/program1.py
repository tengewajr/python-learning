# Creating a small CSV dataset yourself. 
"""
Columns:
StudyHours
Attendance
Assignments
Result
"""

import csv
import random

print("===== STUDENT DATA GENERATOR =====")

# Lock down the seed for reproducible results
random.seed(42)

num_rows = 30

# Counters for Pass and Fail
pass_count = 0
fail_count = 0

# Open a new file in write mode ('w')
with open(
    "week3/day5/student_data.csv",
    "w",
    newline="" # newline="" prevents blank rows between data in Windows
    ) as file:

    writer = csv.writer(file)

    # Write the csv header row
    writer.writerow([
        "StudyHours", 
        "Attendance", 
        "Assignments", 
        "Result"
        ])

    # Generate 30 students records
    for _ in range(num_rows):

        # Generate random student information
        study_hours = random.randint(1, 10)
        attendance = random.randint(50, 100)
        assignments = random.randint(40, 100)

        # Determine student result
        conditions_met = sum ([
            study_hours >= 5,
            attendance >= 70,
            assignments >= 65
        ])

        if conditions_met >= 2:
            result = "Pass"
            pass_count += 1

        else:
            result = "Fail"
            fail_count += 1

        # Write the generated row directly to the file
        writer.writerow([
            study_hours,
            attendance, 
            assignments, 
            result
        ])

print("New CSV file created successfully")
print(f"Number of records generated: {num_rows}")

print(f"Pass: {pass_count}")
print(f"Fail: {fail_count}")