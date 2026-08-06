#Grade Calculator Program

print("=======Grade Calculator============")
marks = float(input("Please enter your Marks:"))

print("")
print("Marks:", marks)

if marks > 100 or marks < 0:
    print("Invalid Marks. Please enter marks between 0 and 100.")

elif marks >= 70:
    print("Your grade is A.")

elif marks >= 60:
    print("Your grade is B+")

elif marks >= 50:
    print("Your grade is B.")

elif marks >= 40:
    print("Your grade is C.")

else:
    print("Your grade is F.")