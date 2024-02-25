import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    user_number = int(input("Think of a number and enter it: "))
    lower_limit = 1
    upper_limit = 100
    attempts = 0
    while True:
        computer_guess = random.randint(lower_limit, upper_limit)
        print(f"Computer's guess: {computer_guess}")
        attempts += 1
        if computer_guess == user_number:
            print(f"The computer guessed your number {user_number} in {attempts} attempts. Well done!")
            break
        elif computer_guess < user_number:
            print("Too low! The computer will try a higher number.")
            lower_limit = computer_guess + 1
        else:
            print("Too high! The computer will try a lower number.")
            upper_limit = computer_guess - 1
guess_the_number()
