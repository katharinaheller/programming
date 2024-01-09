# 1 Nested Loop Pattern Generator:

def generate_pattern(rows):
    for i in range(1, rows + 1): 
        for j in range(i): # diese Schleife wird so oft durchlaufen, wie der aktuelle index ist
            print(i, end="")
        print()

# Get user input for the number of rows
num_rows = int(input("Enter the number of rows: "))
generate_pattern(num_rows)
