# Addition
def addition(a, b):
    summe = a + b
    return summe

# Beispiel
ergebnis_addition = addition(5, 3)
print("Addition:", ergebnis_addition)

# Subtraktion
def subtraktion(a, b):
    differenz = a - b
    return differenz
# Beispiel
ergebnis_subtraktion = subtraktion(8, 3)
print("Subtraktion:", ergebnis_subtraktion)

# Multiplikation
def multiplikation(a, b):
    produkt = a * b
    return produkt

# Beispiel
ergebnis_multiplikation = multiplikation(4, 6)
print("Multiplikation:", ergebnis_multiplikation)

# Division
def division(a, b):
    if b != 0:
        quotient = a / b
        return quotient
    else:
        return "Division durch Null ist nicht erlaubt."

# Beispiel
ergebnis_division = division(9, 3)
print("Division:", ergebnis_division)

