from utils import get_difficulty_settings, prompt_play_again
import random

def play_game():
    print("🎯 Welcome to the Guess the Number Game!")

    difficulty = input("Choose difficulty (easy / medium / hard): ").lower()
    lower, upper, max_attempts = get_difficulty_settings(difficulty)

    number_to_guess = random.randint(lower, upper)
    attempts = 0

    print(f"I'm thinking of a number between {lower} and {upper}. You have {max_attempts} attempts!")

    while attempts < max_attempts:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("🔻 Too low.")
            elif guess > number_to_guess:
                print("🔺 Too high.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")
    else:
        print(f"💥 Out of attempts! The number was {number_to_guess}.")

    if prompt_play_again():
        play_game()
    else:
        print("👋 Thanks for playing!")

if __name__ == "__main__":
    play_game()
