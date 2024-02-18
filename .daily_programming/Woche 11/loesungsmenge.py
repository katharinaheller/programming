import tkinter as tk

def berechnen():
    eingabe = eingabefeld.get()
    if eingabe:
        ergebnis_label.config(text=f"{eingabe}, x ∈ R")

# GUI erstellen
root = tk.Tk()
root.title("Lösungsmenge mit 'x ∈ R' berechnen")

# Eingabefeld
eingabefeld = tk.Entry(root, width=40)
eingabefeld.pack(pady=10)

# Schaltfläche "Berechnen"
berechnen_button = tk.Button(root, text="Berechnen", command=berechnen)
berechnen_button.pack()

# Ergebnislabel
ergebnis_label = tk.Label(root, text="")
ergebnis_label.pack(pady=10)

root.mainloop()
