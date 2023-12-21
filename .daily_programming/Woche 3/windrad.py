# day 12
# windrad.py
from turtle import *
color('black')
pendown() # pen down --> Wenn die Turtle bewegt wird, wird eine Linie auf dem Bildschirm hinterlassen.
hideturtle() # turtle cursor wird nicht anzgezeigt
def rechteck(seite): # Prozedur rechteck wird definiert
    for i in [1,2]:
        forward(seite); left(90)
        forward(seite/4); left(90)

speed(0) # maximale Zeichengeschwindigkeit
width(2) # Zeichenstiftbreite
for i in range(1,9):
    rechteck(100)
    left(45)