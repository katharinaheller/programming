import re

# Beispiel: Suche nach allen Großbuchstaben
# Durch Hinzufügen von ^ und $ muss der gesamte String dem Muster entsprechen
uppercase_pattern = re.compile("^[A-Z]+$")
print(uppercase_pattern.search("Hello World"))
print(uppercase_pattern.search("HELLO WORLD"))
print(uppercase_pattern.search("HELLOWORLD"))

# Beispiel: Suche nach allen Kleinbuchstaben
lowercase_pattern = re.compile("^[a-z]+$")
print(lowercase_pattern.search("helloworld"))

# Die Match-Funktion sucht nach allen Übereinstimmungen
# Hinweis: ^ und $ wurden entfernt, was bedeutet, dass nicht der gesamte String übereinstimmen muss
match_pattern = re.compile("[a-z]+")
print(match_pattern.match("helloworld"))
print(match_pattern.match("hello world"))

# Erlaubt Klein- oder Großbuchstaben und erlaubt Leerzeichen
mixed_case_pattern = re.compile("^[a-zA-Z\s]+$")
print(mixed_case_pattern.match("Hello World"))
print(mixed_case_pattern.match("helloworld"))
print(mixed_case_pattern.match("hello world"))
print(mixed_case_pattern.match("hello wo8rld"))
