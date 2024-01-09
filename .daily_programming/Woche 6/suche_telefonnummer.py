import re

def suche_telefonnummer(text):
    telefon_muster = re.compile(r"\d{3}-\d{3}-\d{4}")
    treffer = telefon_muster.findall(text)

    if treffer:
        return f"Telefonnummern im Text gefunden: {', '.join(treffer)}"
    else:
        return "Keine Telefonnummern im Text gefunden."

def main():
    # Beispieltext
    text = "Hallo, dies ist ein Beispieltext. Die Telefonnummern sind 123-456-7890 und 987-654-3210."

    # Suche nach Telefonnummern im Text
    ergebnis = suche_telefonnummer(text)

    # Ausgabe des Ergebnisses
    print(ergebnis)

if __name__ == "__main__":
    main()
