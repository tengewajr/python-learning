#Simple Calculator Program

print("=======Simple Calculator============")

num1 = float(input("Please enter first number:"))
num2 = float(input("Please enter second number:"))

operation = input ("Choose operation (+,-*, / or Addition, Subtraction, Multiplication, Division)\n").lower()

if operation in ("addition","+"):
    result = num1 + num2
    print("Result: ", result)

elif operation in ("subtraction","-"):
    result = num1 - num2
    print("Result: ", result)

elif operation in ("multiplication","*"):
    result = num1 * num2
    print("Result: ", result)

elif operation in ("division","/"):
    if num2 != 0:
        result = num1 / num2
        print("Result: ", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation! Please choose a valid operation.")