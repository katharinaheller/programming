def print_christmas_tree(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(f"{spaces}{stars}")

    # Stamm des Baumes
    trunk_spaces = " " * (height - 1)
    print(f"{trunk_spaces}|||")

if __name__ == "__main__":
    tree_height = int(input("Gib die Höhe des Weihnachtsbaums ein: "))
    print_christmas_tree(tree_height)

