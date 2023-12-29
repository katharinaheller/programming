import datetime

def neujahrsgruss():
    aktuelles_datum = datetime.datetime.now()
    neujahrsdatum = datetime.datetime(aktuelles_datum.year + 1, 1, 1, 0, 0, 0)

    # Berechne die verbleibende Zeit bis zum nächsten Neujahr
    verbleibende_zeit = neujahrsdatum - aktuelles_datum
    verbleibende_tage = verbleibende_zeit.days
    verbleibende_stunden, restsekunden = divmod(verbleibende_zeit.seconds, 3600)
    verbleibende_minuten, verbleibende_sekunden = divmod(restsekunden, 60)

    # Ausgabe der Neujahrsnachricht mit Sekundenanzahl
    print(f"Heute ist {aktuelles_datum.strftime('%d.%m.%Y %H:%M:%S')}.")
    print(f"Es sind noch {verbleibende_tage} Tage, {verbleibende_stunden} Stunden, {verbleibende_minuten} Minuten und {verbleibende_sekunden} Sekunden bis zum nächsten Neujahr!")

if __name__ == "__main__":
    neujahrsgruss()
