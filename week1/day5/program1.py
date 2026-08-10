#Program 1 – BMI Calculator
"""Create a function that calculates Body Mass Index. Input:
•	Weight (kg)
•	Height (m)
Output:

BMI = 23.8
Healthy Weight
"""

print("===== BMI CALCULATOR =====")

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi  

Weight = float(input("Enter your weight in kg: "))
Height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(Weight, Height)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")

elif 18.5 <= bmi < 24.9:
    print("You have a healthy weight.")
else:
    print("You are overweight.")