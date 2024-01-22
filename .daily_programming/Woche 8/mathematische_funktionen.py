# Importiere die benötigten mathematischen Funktionen aus dem Modul 'math'
from math import pi, radians, degrees, sin, cos, tan, asin #aisn --> Arkussinus

# Setze den Winkel in Grad
ad = 90

# Konvertiere den Winkel von Grad zu Bogenmaß (radians)
ar = radians(ad)

# Konvertiere den Winkel von Bogenmaß zurück zu Grad
ad = degrees(ar)

# Überprüfe, ob die Umwandlung von Grad zu Bogenmaß und zurück zu Grad korrekt ist (. --> es handelt sich um eine Fließkommazahl, drückt eindeutig eine Ganzzahl aus)
print(ad == 90.)

# Überprüfe, ob der Winkel in Bogenmaß richtig in Pi/2 umgewandelt wurde
print(ar == pi / 2.)

# Überprüfe die Trigonometrie-Identität sin(ar)/cos(ar) == tan(ar)
print(sin(ar) / cos(ar) == tan(ar))

# Überprüfe die Umkehrfunktion der Sinusfunktion: asin(sin(ar)) == ar
print(asin(sin(ar)) == ar)
