from random import randint

name = input("What is your name: ")
guess = int(input("Try to guess the number between 1 and 100: "))
number = randint(1, 100)
tries = 1

while tries < 8:
    if guess < 0 or guess > 100:
        print(f"The number {guess} is not between 1 and 100")
    else:
        if number > guess:
            print("The random number is higher than the guess")
        elif number < guess:
            print("The random number is lower than the guess")
        else:
            print(f"Congratulations {name} you've guessed the number {number} in {tries} tries")
            break
    guess = int(input("Try another time: "))
    tries = tries + 1
