"""
Question 6 — Countdown

Ask the user to enter a starting number.
"""

print("======Welcome to the Countdown Program!======")
start_number = int(input("Please enter a starting number: "))

if start_number <= 0:
    print("Please enter a positive integer.")
else:
    print("Countdown:")
    for i in range(start_number, 0, -1):
        print(i)
    print("Blast off! 🚀")
    