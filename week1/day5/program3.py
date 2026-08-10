#Program 3 – Student Management System
"""Create a simple menu.
1.	Add Student
2.	View Students
3.	Exit

Store student names inside a list.
"""
print("===== STUDENT MANAGEMENT SYSTEM =====")

students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print(f"Student '{name}' has been added successfully.")

def view_students():
    if len(students) == 0:
        print("No students registered yet.")
    else:
        print("\n===== REGISTERED STUDENT LIST =====")

        for index, student in enumerate(students, start=1):
            print(f"{index}. {student}")

while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == '1':
        add_student()
        
    elif choice == '2':
        view_students()

    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")