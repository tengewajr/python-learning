#Question 8 — Student Registration
"""
Start with
students = []

Ask the user to enter five student names.
Store them in the list.
"""

print("======Welcome to the Student Registration Program!======")
students = []
for i in range(5):
    name = input(f"Please enter the name of student {i + 1}: ")
    students.append(name)

print("Registered Students:")
for i, student in enumerate(students, start=1):
    print(f"{i}. {student}")
