#Multiplication Table
"""
Program 1 – Multiplication Table
Ask the user for a number.

Display its multiplication table from 1 to 10. Example:
7 × 1 = 7
7 × 2 = 14
...
7 × 10 = 70
"""

print("=======Multiplication Table============")
number = int(input("Please enter a number to generate its multiplication table: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

