import turtle
import math

# Funktion zur Zeichnung einer Spirale
def draw_spiral(radius, angle, steps):
    for _ in range(steps):
        turtle.forward(radius)
        turtle.left(angle)

# Turtle-Eigenschaften
turtle.speed(100)  # Zeichengeschwindigkeit
turtle.pensize(2)  # Stiftgröße
turtle.bgcolor("black")  # Hintergrund auf Schwarz
turtle.pencolor("red")  # Stiftfarbe auf Cyan

# bunte Spirale zeichnen
for i in range(100):  # Anzahl Wiederholungen
    draw_spiral(10 + i * 5, 90, 4)  # den Radius und den Winkel anpassen
    turtle.left(10)  # die Turtle um 10 Grad drehen

turtle.hideturtle()
turtle.done()
