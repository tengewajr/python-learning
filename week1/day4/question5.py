#Question 5 — Sum of Numbers
"""
Ask the user for a number.
Suppose the user enters 10

Output
1+2+3+4+5+6+7+8+9+10
Sum = 55
"""

print("======Welcome to the Sum of Numbers Calculator!======")
number = int(input("Please enter a number: "))

if number <= 0:
    print("Please enter a positive integer.")

else:
    print("Output:")
    
    for i in range(1, number + 1):
        if i < number:
            print(i, end="+")
        else:
            print(i)

    sum_of_numbers = sum(range(1, number + 1))
    print(f"Sum = {sum_of_numbers}")

