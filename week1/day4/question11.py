#Question 11 — Guessing Game (Improved)
"""
Improve today's program.
Requirements:
✅ Count attempts.
✅ If the guess is too high
Too High

If too low
Too Low

When correct
Congratulations!
You guessed the number in X attempts.
"""

import random
print("======Welcome to the Guessing Game!======")

secret = random.randint(1, 20)

guess = 0
attempts = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1

    if guess <= 0 or guess > 20:
        print("Please enter a valid number between 1 and 20.")

    elif guess > secret:
        print("Too high!")

    elif guess < secret:
        print("Too low!")

    else: 
        print("Congratulations!")
        print(f"You guessed the number in {attempts} attempts.")