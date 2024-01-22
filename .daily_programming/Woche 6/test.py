def solve_eight_queens():
    board_size = 8
    queens_positions = [-1] * board_size
    current_row = 0

    while current_row >= 0:
        if not is_queen_present(current_row, queens_positions):
            place_queen(current_row, queens_positions)
        else:
            if not move_queen(current_row, queens_positions):
                remove_queen(current_row, queens_positions)
                current_row -= 1
                continue

        all_clear = True

        while has_conflict(current_row, queens_positions):
            if not move_queen(current_row, queens_positions):
                remove_queen(current_row, queens_positions)
                current_row -= 1
                all_clear = False
                break

        if all_clear:
            current_row += 1

def is_queen_present(row, queens_positions):
    return queens_positions[row] != -1

def place_queen(row, queens_positions):
    queens_positions[row] = find_available_column(row, queens_positions)

def move_queen(row, queens_positions):
    queens_positions[row] = -1
    queens_positions[row] = find_available_column(row, queens_positions)
    return queens_positions[row] != -1

def remove_queen(row, queens_positions):
    queens_positions[row] = -1

def has_conflict(row, queens_positions):
    for i in range(row):
        if (
            queens_positions[i] == queens_positions[row] or
            abs(queens_positions[i] - queens_positions[row]) == abs(i - row)
        ):
            return True
    return False

def find_available_column(row, queens_positions):
    board_size = len(queens_positions)
    for col in range(board_size):
        if not any(row == queens_positions[i] or abs(row - queens_positions[i]) == abs(col - i) for i in range(row)):
            return col
    return -1