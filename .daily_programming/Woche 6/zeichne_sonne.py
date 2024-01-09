import turtle

def zeichne_sonne():
    # Sonne zeichnen
    turtle.color("yellow")  # Farbe auf Gelb setzen
    turtle.begin_fill()  # Fülle beginnen
    for _ in range(12):
        turtle.forward(100)  # Länge des Sonnenstrahls
        turtle.right(150)  # Winkel zwischen den Sonnenstrahlen
    turtle.end_fill()  # Füllen beenden

def main():
    # Ein neues Fenster öffnen
    turtle.title("Sonne")
    turtle.bgcolor("skyblue")  # Hintergrundfarbe setzen

    # Sonne zeichnen
    zeichne_sonne()

    # Das Turtle-Fenster anzeigen
    turtle.mainloop()

if __name__ == "__main__":
    main()
