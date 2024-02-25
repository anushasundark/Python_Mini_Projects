import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    lower_limit = 1
    upper_limit = 100
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0
    while True:
        try:
            guess = int(input(f"Guess the number between {lower_limit} and {upper_limit}: "))
            attempts += 1
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
guess_the_number()
