import random

print("Number Guessing Game")

number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Congratulations! You guessed correctly.")
else:
    print("Wrong guess. The correct number was:", number)