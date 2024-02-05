from sympy import Matrix, I

# komplexe Matrix M definieren
M = Matrix([[1 + 5*I, 10 - 4*I], [9 - I, 4 + 3*I]])

# Determinante der Matrix M berechnen
determinant_M = M.det()

# Ergebnis ausgeben
print("Determinante der Matrix M:", determinant_M)
