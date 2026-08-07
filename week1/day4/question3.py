#Question 3 — Positive, Negative or Zero
"""
Input one number.
Display whether it is:
Positive
Negative
Zero
"""

print("======Welcome to the Positive, Negative or Zero Checker!======")
number = float(input("Please enter a number: "))

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")