import random

def guess_the_number():
    # Zufallszahl zwischen 1 und 100 generieren
    secret_number = random.randint(1, 100)
    
    print("Willkommen beim Zahlenraten-Spiel!")
    print("Ich habe eine Zahl zwischen 1 und 100 gewählt. Versuche sie zu erraten.")

    attempts = 0
    guessed_number = False

    while not guessed_number:
        try:
            # Benutzereingabe abfragen
            guess = int(input("Dein Tipp: "))
            attempts += 1

            # Überprüfen, ob die Eingabe korrekt ist
            if guess == secret_number:
                guessed_number = True
            elif guess < secret_number:
                print("Zu niedrig. Versuche es erneut.")
            else:
                print("Zu hoch. Versuche es erneut.")
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")

    print(f"Glückwunsch! Du hast die Zahl {secret_number} in {attempts} Versuchen erraten.")

if __name__ == "__main__":
    guess_the_number()
