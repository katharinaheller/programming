import pandas as pd
import matplotlib.pyplot as plt

# Beispiel-Daten: Studenten und ihre Prüfungsergebnisse
studenten_daten = {
    'Student': ['Steven', 'Laurin', 'Albert', 'Calvin', 'Kay'],
    'Ergebnis': [45, 100, 70, 1, 27]
}

# Erstellen eines Pandas DataFrame
df = pd.DataFrame(studenten_daten)

# Visualisierung der Prüfungsergebnisse als Balkendiagramm
plt.figure(figsize=(8, 5))
plt.bar(df['Student'], df['Ergebnis'], color='skyblue')
plt.title('Prüfungsergebnisse der Studenten')
plt.xlabel('Studenten')
plt.ylabel('Ergebnis')
plt.ylim(0, 100)  # Festlegen der y-Achsenbegrenzung
plt.show()
