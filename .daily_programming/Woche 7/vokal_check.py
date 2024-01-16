def vokal_check(wort):
    vokale = set("aeiou")
    return any(buchstabe in vokale for buchstabe in wort.lower())

def main():
    eingabe = input("Gib Wörter durch Leerzeichen getrennt ein: ")
    wortliste = eingabe.split()

    worte_mit_vokalen = []
    worte_ohne_vokale = []

    for wort in wortliste:
        if vokal_check(wort):
            worte_mit_vokalen.append(wort)
        else:
            worte_ohne_vokale.append(wort)

    print("\nWörter mit Vokalen:", ", ".join(worte_mit_vokalen))
    print("Wörter ohne Vokale:", ", ".join(worte_ohne_vokale))

if __name__ == "__main__":
    main()
