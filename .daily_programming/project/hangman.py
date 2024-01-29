import random
import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        self.word_to_guess = self.choose_word()
        self.guessed_letters = []
        self.incorrect_attempts = 0

        self.create_widgets()

    def choose_word(self):
        words = ["python", "hangman", "programming", "computer", "developer", "learning"]
        return random.choice(words)

    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    def guess_letter(self):
        guess = self.entry.get().lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in self.guessed_letters:
                messagebox.showinfo("Hangman", "You already guessed that letter. Try again.")
            elif guess in self.word_to_guess:
                self.guessed_letters.append(guess)
                self.update_display()
                if set(self.guessed_letters) == set(self.word_to_guess):
                    self.end_game("Congratulations! You guessed the word: {}".format(self.word_to_guess))
                else:
                    messagebox.showinfo("Hangman", "Good guess!")
            else:
                self.incorrect_attempts += 1
                self.update_display()
                if self.incorrect_attempts == 6:
                    self.end_game("Sorry, you ran out of attempts. The correct word was: {}".format(self.word_to_guess))
                else:
                    messagebox.showinfo("Hangman", "Incorrect guess. Attempts remaining: {}".format(6 - self.incorrect_attempts))
        else:
            messagebox.showinfo("Hangman", "Invalid input. Please enter a single letter.")

    def create_widgets(self):
        self.label_word = tk.Label(self.master, text=self.display_word(), font=("Arial", 18))
        self.label_word.pack(pady=10)

        self.entry = tk.Entry(self.master, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.btn_guess = tk.Button(self.master, text="Guess", command=self.guess_letter, font=("Arial", 14))
        self.btn_guess.pack()

    def update_display(self):
        self.label_word.config(text=self.display_word())

    def end_game(self, message):
        messagebox.showinfo("Hangman", message)
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()