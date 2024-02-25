import random

def choose_word():
    words = ["python", "hangman", "developer", "coding", "programming", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
  
def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6  
    while True:
        current_display = display_word(secret_word, guessed_letters)
        print("\nCurrent Word: " + current_display)
        if current_display == secret_word:
            print("Congratulations! You guessed the word: " + secret_word)
            break
        if incorrect_guesses >= max_attempts:
            print("Sorry, you've run out of attempts. The word was: " + secret_word)
            break
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        guessed_letters.append(guess)
        if guess not in secret_word:
            incorrect_guesses += 1
            print(f"Incorrect! Attempts left: {max_attempts - incorrect_guesses}")
        else:
            print("Correct!")
hangman()
