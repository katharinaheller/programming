import pandas as pd
import random

# Liste von Tierarten und Merkmalen
tierarten = ['Elefant', 'Giraffe', 'Ratte', 'Pinguin', 'Zebra', 'Känguru']
merkmale = ['Farbe', 'Größe', 'Gewicht', 'Lebensraum']

# Funktion zur Erstellung von Zufallsdaten für Tiere
def erstelle_zufallstier():
    tier = random.choice(tierarten)
    farbe = random.choice(['Grau', 'Braun', 'Schwarz', 'Weiß'])
    größe = random.randint(1, 10)
    gewicht = random.randint(5, 500)
    lebensraum = random.choice(['Dschungel', 'Savanne', 'Eis', 'Wüste'])
    return {'Tierart': tier, 'Farbe': farbe, 'Größe': größe, 'Gewicht': gewicht, 'Lebensraum': lebensraum}

# Erstelle eine Liste von Zufallstieren
zufallstiere = [erstelle_zufallstier() for _ in range(10)]

# Erstelle ein Pandas DataFrame aus der Liste
tier_dataframe = pd.DataFrame(zufallstiere)

# Anzeige des DataFrames
print("Zufallszoo:")
print(tier_dataframe)
