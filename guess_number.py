import random

def play_game(lives):
    while lives > 0:
        print(f"\nYou have {lives} guesses left...")
        guess = int(input("\nWhat is your guess? "))
        if guess == TARGET:
            return f"\nYou guessed {guess} and the target is {TARGET} - well done!"
        elif guess < TARGET:
            print("\nYou guessed too low...")
        elif guess > TARGET:
            print("\nYou guessed too high...")
        lives -= 1
    return f"\nThe target was: {TARGET} - nevermind!"

# main
play_again = True
while play_again:
    TARGET = random.randint(1, 100)
    print("\nI have chosen a random number from 1 to 100.")
    choice = input("\n(e)asy or (h)ard? ")
    if choice[0].lower() == "e":
        result = play_game(10)
    else:
        result = play_game(5)
    print(result)
    play_on = input("\nPlay again? (y)es or (n)o: ")
    if play_on[0].lower() == "n":
        play_again = False




