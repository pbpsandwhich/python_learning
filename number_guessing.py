import random
from ng_art import art
print(art)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def game_choice(difficulty_level):
    """ Function to select easy or hard for game mode"""
    number = random.randint(1, 101)
    guess_count = 0
    #print(f"My guessed number is {number}")
    if difficulty_level == "easy":
        while guess_count < 10:
            users_guess = int(input("Make a guess: "))
            if users_guess == number:
                print("That's the right number congrats you win")
                guess_count = 11
            elif users_guess < number:
                guess_count += 1
                print(f"Your number is lower than mine, you have {10 - guess_count} guesses left, guess again: ")
                if guess_count == 10:
                    print("Sorry you loose, too many guesses!")
            elif users_guess > number:
                guess_count += 1
                print(f"Your number is higher than mine, you have {10 - guess_count} guesses left, guess again: ")
            
                if guess_count == 10:
                    print("Sorry you loose, too many guesses!")
    if difficulty_level == "hard":
        while guess_count < 5:
            users_guess = int(input("Make a guess: "))
            if users_guess == number:
                print("That's the right number congrats you win")
                guess_count = 6
            elif users_guess < number:
                guess_count += 1
                print(f"Your number is lower than mine, you have {5 - guess_count} guesses left, guess again: ")
                
                if guess_count == 5:
                    print("Sorry you loose, too many guesses!")
            elif users_guess > number:
                guess_count += 1
                print(f"Your number is higher than mine, you have {5 - guess_count} guesses left, guess again: ")
                
                if guess_count == 5:
                    print("Sorry you loose, too many guesses!")



game_choice(difficulty)




