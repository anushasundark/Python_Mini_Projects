import random

def play_rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()
        if user_choice == 'q':
            print("Thanks for playing. Goodbye!")
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}\n")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            print("You win!")
        else:
            print("Computer wins!")
play_rock_paper_scissors()
