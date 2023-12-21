# day 7
# Beispiele zur Verwendung vom Datentyp set in PYthon

# example 1 - Vereinigung von Sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

union_result = set_a.union(set_b)
print(union_result)
# Output: {1, 2, 3, 4, 5, 6, 7, 8} --> union() fügt somit beide sets in ein einzelnes Set mit allen Elementen die darin enthalten sind, sind diesselben Elemnte in beiden Sets vorhanden, so wird dieses im gemeinsamen Set nur einmalig ausgegeben

# example 2 - Differenz von Sets
set_c = {10, 20, 30, 40, 50}
set_d = {30, 40, 50}
difference_result = set_c.difference(set_d)
print(difference_result)
# Output: {10, 20} --> Nur die Elemnte aus set_c werden ausgegeben, die nicht in set_d enthalten sind

# example 3 - Symmetrische Differenz von Sets
set_e = {1, 2, 3, 4, 5}
set_f = {4, 5, 6, 7, 8}
symmetric_difference_result = set_e.symmetric_difference(set_f)
print(symmetric_difference_result) 
# Output: {1, 2, 3, 6, 7, 8} --> nur die Elemente der beiden Sets werden ausgegeben, die in einem der Sets, aber nicht in beiden enthalten sind

# examaple 4 - Überprüfen auf Teilmengen
set_g = {1, 2, 3, 4, 5}
set_h = {2, 4}
is_subset = set_g.issubset(set_h)
print(is_subset)
# Output: False --> es wird üerprüft, ob das set "set_g" eine Teilmenge von dem Set "set_h" ist, da set_h mehr Elemente als set_h enthält ist dies nicht der Fall
is_subset1 = set_h.issubset(set_g)
print(is_subset1)
# Output: True --> da set_g eine Teilmenge von set_g ist, ist der Boolean-Wert True also wahr

# example 5 - Hinzufügen von Elementen
set_i = {1, 2, 3}
set_i.add(4)
print(set_i)
# Output: {1, 2, 3, 4} --> das Element "4" wird zum set_i hinzugefügt

set_i.add(5)
print(set_i)
# Output: {1, 2, 3, 4, 5} 
 
set_i.add(5)
print(set_i)
# Output: {1, 2, 3, 4, 5} --> versucht man, ein gleiches Element nochmal zu einem Set hinzuzufügen, wird dieses nicht erneut zum Set hinzugefügt, da die Elemente in einem Set einmalig sind
