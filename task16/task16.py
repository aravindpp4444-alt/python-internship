import random

# Random number generate (1 to 100)
secret_number = random.randint(1, 100)

guess = None

print("🎯 Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again ⬆️")
    elif guess > secret_number:
        print("Too high! Try again ⬇️")
    else:
        print("🎉 Congratulations! You guessed the correct number!")
