#Question 9 — Search Student
"""
Create a list
students = ["Rahim", "Aisha", "John", "David"]

Ask the user for a name.
If the name exists
Student Found

Otherwise
Student Not Found
"""

print("======Welcome to the Student Search Program!======")
students = ["Rahim", "Aisha", "John", "David"]

name_to_search = input("Please enter a name to search: ").lower()

if name_to_search in (student.lower() for student in students):
    print("Student Found")
    print(f"student name is {name_to_search.capitalize()}")
else:
    print("Student Not Found")  