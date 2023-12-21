import random

class Würfelspiel:
    def __init__(self):
        self.punkte = 0

    def würfeln(self):
        wurf = random.randint(1, 6)
        print(f'Du hast eine {wurf} gewürfelt.')

        if wurf == 1:
            print('Du hast leider eine 1 gewürfelt und keine Punkte erhalten.')
            self.punkte = 0
        else:
            self.punkte += wurf
            print(f'Deine aktuellen Punkte: {self.punkte}')

    def spiel_starten(self):
        print('Willkommen beim Würfelspiel!')
        input('Drücke Enter, um das Spiel zu starten.')

        while True:
            self.würfeln()
            fortsetzen = input('Möchtest du weiter würfeln? (ja/nein): ').lower()

            if fortsetzen != 'ja':
                print(f'Du hast das Spiel beendet. Deine Endpunktzahl: {self.punkte}')
                break

# Beispielverwendung
if __name__ == "__main__":
    spiel = Würfelspiel()
    spiel.spiel_starten()
