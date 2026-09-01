"""
TASK 1: Hangman Game
---------------------

Concepts used: random, while loop, if-else, strings, lists
"""

import random

# A small predefined list of words to choose from
WORD_LIST = ["python", "hangman", "keyboard", "developer", "django"]

MAX_INCORRECT_GUESSES = 6


def choose_word(word_list):
    """Randomly pick a word from the word list."""
    return random.choice(word_list)


def display_progress(word, guessed_letters):
    """
    Build a string showing guessed letters and blanks for
    letters that haven't been guessed yet.
    Example: word='python', guessed=['p','o'] -> 'p _ t _ o _'
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word(WORD_LIST)
    guessed_letters = []      # letters the player has already tried
    incorrect_guesses = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"Guess the word. You have {MAX_INCORRECT_GUESSES} wrong guesses allowed.")
    print("=" * 40)

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print("\nWord: " + display_progress(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_INCORRECT_GUESSES - incorrect_guesses}")
        print("Guessed letters: " + ", ".join(guessed_letters) if guessed_letters else "Guessed letters: none")

        guess = input("Guess a letter: ").lower().strip()

        # --- Basic input validation ---
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Check win condition: every letter in the word has been guessed
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 40)
            print(f"🎉 You won! The word was '{word}'.")
            print("=" * 40)
            return

    # Loop ended because incorrect_guesses reached the max
    print("\n" + "=" * 40)
    print(f"💀 Game over! You've used all {MAX_INCORRECT_GUESSES} incorrect guesses.")
    print(f"The word was: '{word}'")
    print("=" * 40)


def main():
    play_again = "yes"
    while play_again == "yes":
        play_hangman()
        play_again = input("\nPlay again? (yes/no): ").lower().strip()

    print("Thanks for playing Hangman!")


if __name__ == "__main__":
    main()