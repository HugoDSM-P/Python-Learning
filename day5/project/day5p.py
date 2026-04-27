from random import *

def choose_word():
    words = ["jacket", "moustache", "motorbike", "bananas"]
    return choice(words)
def initialize_display(word):
    return ["_"] * len(word)
def show_display(display):
    print("Word:", " ".join(display))
def update_display(word, display, guess):
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess
def play_game():
    secret_word = choose_word()
    display = initialize_display(secret_word)
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    show_display(display)

    while tries > 0:
        guess = input("\nChoose a letter: ").lower()
        if guess in guessed_letters:
            print("You already tried that letter.")
            continue
        guessed_letters.append(guess)
        if guess in secret_word:
            print("Correct!")
            update_display(secret_word, display, guess)
        else:
            tries -= 1
            print(f"Wrong! You have {tries} tries left.")
        show_display(display)
        if "_" not in display:
            print("You win!")
            return
    print(f"You lose! The word was: {secret_word}")

play_game()