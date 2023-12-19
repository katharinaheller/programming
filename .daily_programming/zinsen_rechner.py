import re

def ist_gueltiger_name(name):
    return bool(re.match("^[a-zA-Z]+$", name))

def ist_gueltiges_kapital(kapital):
    return kapital.replace('.', '', 1).isdigit()

def ist_gueltiger_zinssatz(zinssatz):
    return zinssatz.replace('.', '', 1).isdigit()

# Variable
name = input("Moin! Wie heißt du? ")

while not ist_gueltiger_name(name):
    print("Ungültiger Name! Bitte gib nur Buchstaben ein.")
    name = input("Moin! Wie heißt du? ")

kapital = input("Kapital? ")

while not ist_gueltiges_kapital(kapital):
    print("Ungültiges Kapital! Bitte gib nur Zahlen ein.")
    kapital = input("Kapital? ")

zinssatz = input("Zinssatz in Prozent? ")

while not ist_gueltiger_zinssatz(zinssatz):
    print("Ungültiger Zinssatz! Bitte gib nur Zahlen ein.")
    zinssatz = input("Zinssatz in Prozent? ")

# Verarbeitung
kapital = float(kapital)
zinssatz = float(zinssatz)
zinsen = kapital * zinssatz / 100

# Ausgabe
print(f"{name}, deine Zinsen sind {zinsen:.2f}")
