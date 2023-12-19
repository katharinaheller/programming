#day 11
import random

def choose_word():
    words = ["strings", "python", "pipe", "hangman", "programming", "happiness", "learning", "software", "hardware"]
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    print("Willkommen zum kreativen Hangman-Spiel!")
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6

    while True:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Rate einen Buchstaben: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("Du hast diesen Buchstaben bereits geraten. Versuche es erneut.")
            elif guess in word_to_guess:
                print("Richtig geraten!")
                guessed_letters.append(guess)
            else:
                print("Falsch geraten!")
                incorrect_attempts += 1
                print_hangman(incorrect_attempts)

            if set(guessed_letters) == set(word_to_guess):
                print("Herzlichen Glückwunsch! Du hast das Wort erraten: ", word_to_guess)
                break

            if incorrect_attempts == max_attempts:
                print("Leider hast du alle Versuche aufgebraucht. Das Wort war: ", word_to_guess)
                break
        else:
            print("Ungültige Eingabe. Bitte gib einen einzelnen Buchstaben ein.")

def print_hangman(incorrect_attempts):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]

    print(stages[incorrect_attempts])

if __name__ == "__main__":
    hangman()
