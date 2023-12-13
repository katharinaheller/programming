# day 8
# Beispiele zur Verwendung vom Datentyp "String" in Python

# example 1 - String-Verkettung
str1 = "Hallo"
str2 = "Welt"
result = str1 + " " + str2 # mit Leerzeichen
print(result)
# Output: Hallo Welt

result1 = str1 + str2 # ohne Leerzeichen
print(result1)
# Output: HalloWelt

# example 2 - String Formatierung
name = "Katharina"
age = 18
text = "Mein Name ist {} und ich bin {} Jahre alt".format(name, age)
print(text)
# Output: Mein Name ist Katharina und ich bin 18 Jahre alt

# example 3 - String-Aufspaltung
sentence = "Wir lernen den Datentyp String kennen"
words = sentence.split()
print(words)
# Output: ['Wir', 'lernen', 'den', 'Datentyp', 'String', 'kennen'] --> der Satz, den wir der Variablen "sentence" übergeben haben, wird in eine Liste von Wörtern aufgespalten

# example 4 - String-Ersetzung
text = "Karotten sind gesund. Karotten sind lecker."
new_text = text.replace("Karotten", "Möhren")
print(new_text)
# Output: Möhren sind gesund. Möhren sind lecker. --> die Zeichenkette "Karotten" wird durch "Möhren" ersetzt

# example 5 - String-Überprüfung auf Unterstring
sentence1 = "String ist ein Datentyp in Python"
is_Datentyp = "Datentyp" in sentence1
print(is_Datentyp)
# Output: True --> Der daraus resultierende Boolean-Wert ist True (wahr), da der Substring "Datentyp" im String "sentence1" enthalten ist
is_Datentyp1 = "datentyp" in sentence1
print(is_Datentyp1)
# Output: False --> auch Groß- und Kleinschreibung spielt bei so einer Überprüfung eine Rolle, stimmt diese nicht überein, so ist der daraus resultierende Boolean-Wert False (falsch)