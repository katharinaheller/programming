def print_solution(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col):
    # Überprüfen, ob es eine Dame in der gleichen Zeile gibt
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # Überprüfen, ob es eine Dame in der linken oberen Diagonale gibt
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Überprüfen, ob es eine Dame in der linken unteren Diagonale gibt
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    return True

def solve_n_queens(board, col):
    if col == len(board):
        print_solution(board)
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = "Q"
            solve_n_queens(board, col + 1)
            board[i][col] = "."  # Backtracking

def eight_queens():
    n = 8
    # Initialisieren des Schachbretts
    board = [["." for _ in range(n)] for _ in range(n)]

    solve_n_queens(board, 0)

if __name__ == "__main__":
    eight_queens()
