def get_difficulty_settings(level):
    level = level.lower()
    if level == "easy":
        return 1, 50, 10
    elif level == "medium":
        return 1, 100, 7
    elif level == "hard":
        return 1, 200, 5
    else:
        print("⚠️ Unknown difficulty. Defaulting to Medium.")
        return 1, 100, 7

def prompt_play_again():
    choice = input("Do you want to play again? (y/n): ").lower()
    return choice == 'y'
