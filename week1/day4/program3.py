#Number Guessing Game
"""
Program 3 – Number Guessing Game
Generate a random number between 1 and 20.

Keep asking the user to guess until they get the correct answer. 
Display messages like:
Too High
Too Low
Correct!
"""

print("Welcome to the Number Guessing Game!")
import random

secret = random.randint(1, 20)

guess = 0

while guess != secret:

 guess=int(input("Guess a number between 1 and 20: "))

 if guess > secret:
     print("Too high!")
 elif guess < secret:
     print("Too low!")
 else:
     print("🎉Correct!")
