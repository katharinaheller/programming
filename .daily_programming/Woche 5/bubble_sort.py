# Bubble Sort: Ein einfacher Sortieralgorithmus, ideal für kleine Daten/Arrays

def sort_(arr, temporary=False, reverse=False):
    # Kopie des Arrays erstellen, falls temporary True ist
    ar = arr[:] if temporary else arr

    # Länge des Arrays
    length = len(ar)

    # Haupt-Loop: Nach jeder Iteration ist das rechteste Element sortiert
    while length > 0:
        # Durchlauf durch alle unsortierten Elemente
        for i in range(0, length - 1):
            if reverse:
                # Elemente in absteigender Reihenfolge tauschen
                if ar[i] < ar[i + 1]:
                    ar[i], ar[i + 1] = ar[i + 1], ar[i]
            else:
                # Elemente in aufsteigender Reihenfolge tauschen
                if ar[i] > ar[i + 1]:
                    ar[i], ar[i + 1] = ar[i + 1], ar[i]

        # Länge reduzieren, da das rechteste Element nun sortiert ist
        length -= 1

    # Wenn temporary True ist, die sortierte Kopie zurückgeben, sonst None
    return ar if temporary else None

# Testing
tests = [[7, 8, 9, 6, 4, 5, 3, 2, 1, 15], [1, 90, 1110, 1312, 1110, 98, 76, 54, 32, 10]] 

for test in tests:
    accend, decend = sort_(test, True), sort_(test, True, True)
    if accend == sorted(test) and decend == sorted(test, reverse=True):
        print("Original: {}".format(test))
        print("Sortiert: {}".format(accend))
        print("Sortiert (absteigend): {}\n".format(decend))
    else:
        print("Etwas ist schief gelaufen!\n")

# Bubble Sort funktioniert gut für kleine Daten/Arrays!