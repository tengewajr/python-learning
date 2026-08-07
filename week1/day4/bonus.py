print("======FYP Mindset Challenge======")
"""
Imagine your AI motor monitoring system measures temperatures every hour:
temperatures = [32, 35, 41, 37, 45, 30]
"""

temperatures = []

# Ask the user to input 6 temperatures and store them in the list.
for i in range(6):
    temp = float(input(f"Please enter temperature for hour {i + 1}: "))
    temperatures.append(temp)

#Print every temperature in the list using a loop.
for temp in temperatures:
    print(f"Temperature: {temp}°C")

# Find the highest temperature in the list and print it.
highest_temp = max(temperatures)
print(f"Highest Temperature: {highest_temp}°C")

#Find the lowest temperature in the list and print it.
lowest_temp = min(temperatures)
print(f"Lowest Temperature: {lowest_temp}°C")

#Calculate the average temperature and print it.
average_temp = sum(temperatures) / len(temperatures)
print(f"Average Temperature: {average_temp:.2f}°C")
