#Program 2 – Student Record
"""
Store the following information using a dictionary:
•	Name
•	University
•	Course
•	Age
Display the information neatly.
"""
print("===== STUDENT RECORD =====")

student = {
"name": input("Enter your name: "),
"university": input("Enter your university: "),
"course": input("Enter your course: "),
"age": int(input("Enter your age: "))
}

print("\n===== STUDENT INFORMATION =====")

for key, value in student.items():
    print(f"{key.capitalize()}: {value}")