def dezimal_zu_binaer(dezimalzahl):
    if dezimalzahl < 0:
        return "Negative Dezimalzahlen werden nicht unterstützt."
    elif dezimalzahl == 0:
        return "0b0"
    else:
        binärzahl = bin(dezimalzahl)
        return binärzahl

# Benutzereingabe für die Dezimalzahl
dezimalzahl = int(input("Geben Sie eine Dezimalzahl ein: "))

# Aufruf der Funktion und Ausgabe des Ergebnisses
ergebnis = dezimal_zu_binaer(dezimalzahl)

print(f"Die Binärzahl von {dezimalzahl} ist: {ergebnis}")
