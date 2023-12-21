# day 9
def ist_primzahl(zahl):
    if zahl <= 1:
        return False
    for i in range(2, int(zahl**0.5) + 1):
        if zahl % i == 0:
            return False
    return True

# Eingabe einer Zahl durch den Benutzer
eingabe = int(input("Gib eine Zahl ein: "))

# Überprüfung, ob die eingegebene Zahl eine Primzahl ist
if ist_primzahl(eingabe):
    print(eingabe, "ist eine Primzahl.")
else:
    print(eingabe, "ist keine Primzahl.")



