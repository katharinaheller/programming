class Liste:
    def __init__(self):
        self.einträge = []

    def eintrag_hinzufügen(self, eintrag):
        self.einträge.append(eintrag)
        print(f'{eintrag} wurde zur Liste hinzugefügt.')

    def liste_anzeigen(self):
        if not self.einträge:
            print('Die Liste ist leer.')
        else:
            print('Liste:')
            for index, eintrag in enumerate(self.einträge, start=1):
                print(f'{index}. {eintrag}')

    def eintrag_entfernen(self, index):
        if 1 <= index <= len(self.einträge):
            entfernter_eintrag = self.einträge.pop(index - 1)
            print(f'{entfernter_eintrag} wurde von der Liste entfernt.')
        else:
            print('Ungültiger Index. Bitte wählen Sie eine gültige Position.')

# Beispielverwendung
if __name__ == "__main__":
    einkaufsliste = Liste()

    while True:
        print('\n1. Eintrag hinzufügen')
        print('2. Liste anzeigen')
        print('3. Eintrag entfernen')
        print('4. Programm beenden')

        auswahl = input('Bitte wählen Sie eine Option (1/2/3/4): ')

        if auswahl == '1':
            eintrag = input('Geben Sie den Eintrag ein: ')
            einkaufsliste.eintrag_hinzufügen(eintrag)
        elif auswahl == '2':
            einkaufsliste.liste_anzeigen()
        elif auswahl == '3':
            index = int(input('Geben Sie den Index des Eintrags zum Entfernen ein: '))
            einkaufsliste.eintrag_entfernen(index)
        elif auswahl == '4':
            break
        else:
            print('Ungültige Auswahl. Bitte geben Sie 1, 2, 3 oder 4 ein.')
