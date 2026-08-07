#Question 12 — Multiplication Table Generator
"""
Instead of printing only one table,

Ask
Up to which table? 5

Output
Table of 1
Table of 2
Table of 3
Table of 4
Table of 5

Each table should go from ×1 to ×10.
"""

print("======Welcome to the Multiplication Table Generator!======")
up_to = int(input("Up to which table would you like to generate? "))

if up_to <= 0:
    print("Please enter a positive integer.")
else:
    for i in range(1, up_to + 1):
        print(f"Table of {i}:")
        for j in range(1, 11):
            print(f"{i} × {j} = {i * j}")
        print()