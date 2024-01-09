# Definition der AND-Gatterfunktion, die zwei Eingaben logisch verknüpft
def and_gate(input1, input2):
    return input1 and input2

# Definition der OR-Gatterfunktion, die zwei Eingaben logisch verknüpft (mit ODER)
def or_gate(input1, input2):
    return input1 or input2

# Definition der NOT-Gatterfunktion, die die logische Negation einer Eingabe durchführt
def not_gate(input1):
    return not input1

# Definition der NAND-Gatterfunktion, die die Negation des logischen UND von zwei Eingaben durchführt
def nand_gate(input1, input2):
    return not (input1 and input2)

# Definition der NOR-Gatterfunktion, die die Negation des logischen ODER von zwei Eingaben durchführt
def nor_gate(input1, input2):
    return not (input1 or input2)

# Definition der XOR-Gatterfunktion, die die exklusive ODER-Operation von zwei Eingaben durchführt
def xor_gate(input1, input2):
    return (input1 or input2) and not (input1 and input2)

# Definition der XNOR-Gatterfunktion, die die Negation der exklusiven ODER-Operation von zwei Eingaben durchführt
def xnor_gate(input1, input2):
    return not ((input1 or input2) and not (input1 and input2))

# Beispielverwendung der Gatterfunktionen
input_a = True
input_b = False

# Ausgabe der Ergebnisse der verschiedenen Gatteroperationen für die gegebenen Eingaben
print("AND Gate:", and_gate(input_a, input_b)) # True(=1) UND False(=0) --> 0 = False
print("OR Gate:", or_gate(input_a, input_b)) # True ODER False --> True
print("NOT Gate (Input A):", not_gate(input_a)) # nicht True --> False (gegenwärtiges Element von der Aussage von einem Bestandteil)
print("NAND Gate:", nand_gate(input_a, input_b)) # nicht (True und False) --> nicht (False) --> True --> (gegenwärtiges Element von der Gesamtaussage mit UND verknüpft)
print("NOR Gate:", nor_gate(input_a, input_b)) # nicht ( True oder False) --> nicht (True) --> False (--> gegenwärtiges Element von der Gesamtaussage mit ODER verknüpft)
print("XOR Gate:", xor_gate(input_a, input_b)) # (True or False) and nicht (True and False) --> (True) and nicht (False) --> (True) and (True) --> True 
print("XNOR Gate:", xnor_gate(input_a, input_b)) # nicht ((True or False) and nicht (True and False)) --> nicht ((True) and nicht (False)) --> nicht ((True) and (True)) --> nicht (True) --> False
