#Program 1 – Student File
"""Create a program that saves student names into a text file. 
Read the file and display all students.
"""

print("===== STUDENT FILE PROGRAM =====")

students = []

number_of_students = int(input("How many students do you want to register? "))

for i in range(number_of_students):
    name = input(f"Enter the name of student {i + 1}: ")
    students.append(name)

#Write student names to a text file
with open("students.txt", "w") as file:
    for name in students:
        file.write(name + "\n")

print("\n Student names have been saved to 'students.txt'.")

#Read and display student names from the text file
print("===== DISPLAYING STUDENT NAMES =====")
with open("students.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line.strip()}")