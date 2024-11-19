import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def game_choice(difficulty_level):
    """ Function to select easy or hard for game mode"""
    number = random.randint(1, 101)
    guess_count = 0
    #print(f"My guessed number is {number}")
    if difficulty_level == "easy":
        while guess_count < 5:
            users_guess = int(input("Make a guess: "))
            if users_guess == number:
                print("That's the right number congrats you win")
                guess_count = 6
            elif users_guess < number:
                print("Your number is lower than mine, guess again: ")
                guess_count += 1
                if guess_count == 5:
                    print("Sorry you loose, too many guesses!")
            elif users_guess > number:
                print("Your number is higher than mine, guess again: ")
                guess_count += 1
                if guess_count == 5:
                    print("Sorry you loose, too many guesses!")
    if difficulty_level == "hard":
        while guess_count < 10:
            users_guess = int(input("Make a guess: "))
            if users_guess == number:
                print("That's the right number congrats you win")
                guess_count = 6
            elif users_guess < number:
                print("Your number is lower than mine, guess again: ")
                guess_count += 1
                if guess_count == 10:
                    print("Sorry you loose, too many guesses!")
            elif users_guess > number:
                print("Your number is higher than mine, guess again: ")
                guess_count += 1
                if guess_count == 10:
                    print("Sorry you loose, too many guesses!")



game_choice(difficulty)




