# day 3 - Programm, um das Alter abzufragen

# Funktion, um das Alter abzufragen
def alter_abfragen():
    while True:
        try:
            # Benutzer nach dem Alter fragen
            alter = int(input("Bitte geben Sie Ihr Alter ein: "))

            # Alter überprüfen
            if alter < 0:
                print("Bitte geben Sie ein gültiges Alter ein.")
            else:
                return alter

        except ValueError:
            print("Bitte geben Sie eine numerische Zahl für das Alter ein.")

# Hauptprogramm
if __name__ == "__main__":
    print("Willkommen! Dies ist ein Programm zum Abfragen des Alters.")
    
    # Alter abfragen
    benutzer_alter = alter_abfragen()

    # Ausgabe des Alters
    print("Sie sind", benutzer_alter, "Jahre alt.")
