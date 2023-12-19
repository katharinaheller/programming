def print_spaces(count):
    for _ in range(count):
        print(" ", end="")

def print_slash():
    print("/", end="")

def print_backslash():
    print("\\", end="")

def print_line(spaces_before, slashes_between):
    print_spaces(spaces_before)
    print_slash()
    print_spaces(slashes_between)
    print_backslash()
    print()

def print_pattern(rows):
    for i in range(rows):
        spaces_before = rows - i - 1
        slashes_between = 2 * i
        print_line(spaces_before, slashes_between)

# Anzahl der Reihen
rows = 8

# Aufruf der Funktion
print_pattern(rows)
