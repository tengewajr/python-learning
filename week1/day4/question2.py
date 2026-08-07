#Question 2 — Largest Number
"""
Ask the user to enter three numbers.
Display the largest.

Example:
First Number: 15
Second Number: 20
Third Number: 12

Largest Number is 20
"""

print("======Welcome to the Largest Number Finder!======")
print("Please enter three numbers to find the largest among them.")
num1 = float(input("First Number: "))
num2 = float(input("Second Number: "))
num3 = float(input("Third Number: "))

largest = max(num1, num2, num3)
print(f"Largest Number is {largest}")

smallest = min(num1, num2, num3)
print(f"Smallest Number is {smallest}")