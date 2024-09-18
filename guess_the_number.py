import random
from ascii import logo, party
import os

def guess_the_number():
    rng = random.randint(1, 100)

    difficulties = {"easy": 10, "norsmal": 5, "hard": 3}

    print(logo)

    print("Welcome to Guess the Number! Try to guess the number between 1 and 100.")

    # Getting user to select difficulty.
    for stage, lives in difficulties.items():
        print(f"             {stage} -- {lives} lives.             ")
    print()

    difficulty_chosen = input("Please type in a difficulty (easy/normal/hard):  ")
    if difficulty_chosen in difficulties:
        lives = difficulties[difficulty_chosen]
        print(f"Chosen difficulty: {difficulty_chosen}. You have {lives} lives!")
        print()
    else:
        raise Exception("No such difficulty exists.")

    game_is_on = True
    already_made_guesses = set()

    while game_is_on:
        # Prompting user for guess
        try:
            user_guess = int(input("Please enter a guess: "))
        except ValueError:
            print(f"Invalid input! Please try again...")
        else:
            if user_guess not in already_made_guesses:
                already_made_guesses.add(user_guess)
                if user_guess > rng:
                    lives -= 1
                    if lives == 0:
                        print()
                        print(f"Wrong! The correct number was: {rng}.")
                        print(f"Lives remaining: 0. YOU LOSE !!!")
                        game_is_on = False
                    else:
                        print("Too high! Try again...")
                        print(f"## Lives remaining: {lives}.")
                        print()
                elif user_guess < rng:
                    lives -= 1
                    if lives == 0:
                        print()
                        print(f"Wrong! The correct number was: {rng}.")
                        print(f"Lives remaining: 0. YOU LOSE !!!")
                        game_is_on = False
                    else:
                        print("Too low! Try again...")
                        print(f"## Lives remaining: {lives}.")
                        print()
                else:
                    print(party)
                    print("You guessed correctly! YOU WIN!!!")
                    game_is_on = False

                    restart = input("Would you like to play another round? (Y/n): ").lower()

                    if restart == 'y':
                        print(f"\n" * 100)
                        guess_the_number()
                    else:
                        print()
                        print("Thank you for playing. Goodbye!")
            else:
                print("You have already guess that. Enter another guess.")


guess_the_number()