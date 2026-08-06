#Age Checker Program

print("=======Age Checker============")
age = int(input("Please enter your Age:"))
print("Age:", age)

if age < 0:
    print("Invalid Age. Please enter a valid age.")

elif age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

