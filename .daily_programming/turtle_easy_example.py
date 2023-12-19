import turtle

# Turtle-Objekt erstellen
t = turtle.Turtle()

# Quadrat zeichnen
for _ in range(4):
    t.forward(100)  # Vorwärtsbewegung um 100 Einheiten
    t.left(90)      # Links drehen um 90 Grad

# Bildschirm aktualisieren
turtle.done()
