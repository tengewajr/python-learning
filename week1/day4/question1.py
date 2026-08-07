#Question 1 — Even or Odd
"""
Write a program that asks the user to enter an integer.
Display:
Even Number
or
Odd Number
"""

print("======Welcome to the Even or Odd Checker!======")
number = int(input("Please enter an integer: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")