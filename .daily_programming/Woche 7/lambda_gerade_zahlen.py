# Liste von Zahlen
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Verwendung von Lambda-Funktion, um gerade Zahlen zu filtern
gerade_zahlen = list(filter(lambda x: x % 2 == 0, zahlen))

# Ausgabe der Ergebnisse
print("Ursprüngliche Zahlen:", zahlen)
print("Gerade Zahlen:", gerade_zahlen)
