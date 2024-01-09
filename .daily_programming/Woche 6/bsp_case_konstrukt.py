# Beispiel für ein "case"-ähnliches Konstrukt mit einem Dictionary

def handle_positive():
    print("Die Zahl ist positiv.")

def handle_negative():
    print("Die Zahl ist negativ.")

def handle_zero():
    print("Die Zahl ist null.")

# Benutzer gibt eine Zahl ein
zahl = int(input("Gib eine Zahl ein: "))

# Dictionary, das Funktionen den entsprechenden Bedingungen zuordnet
case_dict = {
    zahl > 0: handle_positive,
    zahl < 0: handle_negative,
    zahl == 0: handle_zero
}

# Durchlaufe das Dictionary und führe die entsprechende Funktion aus
for condition, action in case_dict.items():
    if condition:
        action()
        break
