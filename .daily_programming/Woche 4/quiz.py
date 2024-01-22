class Quiz:
    def __init__(self):
        self.frage_antworten = {
            'Was ist die Hauptstadt von Frankreich?': 'Paris',
            'Wie viele Planeten hat unser Sonnensystem?': '8',
            'Was ist das größte Land der Welt?': 'Russland'
        }
        self.richtige_antworten = 0

    def frage_stellen(self, frage, antwort):
        benutzer_antwort = input(f'{frage}: ')
        if benutzer_antwort.lower() == antwort.lower():
            print('Richtig!')
            self.richtige_antworten += 1
        else:
            print(f'Falsch! Die richtige Antwort ist: {antwort}')

    def quiz_starten(self):
        print('Willkommen zum Quiz!')

        for frage, antwort in self.frage_antworten.items():
            self.frage_stellen(frage, antwort)

        print(f'Du hast {self.richtige_antworten} von {len(self.frage_antworten)} Fragen richtig beantwortet.')
        prozentsatz_richtig = (self.richtige_antworten / len(self.frage_antworten)) * 100

        if prozentsatz_richtig == 100:
            print('Perfekt! Du hast alle Fragen richtig beantwortet.')
        elif prozentsatz_richtig >= 75:
            print('Gut gemacht! Du hast die Mehrheit der Fragen richtig beantwortet.')
        elif prozentsatz_richtig >= 50:
            print('Nicht schlecht! Du hast die Hälfte der Fragen oder mehr richtig beantwortet.')
        else:
            print('Leider hast du weniger als die Hälfte der Fragen richtig beantwortet. Versuche es!')

# Beispielverwendung
if __name__ == "__main__":
    quiz = Quiz()
    quiz.quiz_starten()
