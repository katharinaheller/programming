import tkinter as tk
from tkinter import messagebox
import numpy as np

class MatrixCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Matrix Calculator")

        self.matrix_entry = tk.Text(master, height=5, width=20)
        self.matrix_entry.pack()

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate(self):
        matrix_str = self.matrix_entry.get("1.0", tk.END)
        try:
            matrix = np.array(eval(matrix_str))
            if len(matrix.shape) != 2:
                raise ValueError("Input is not a matrix")
            
            result = self.gaussian_elimination(matrix)
            result_str = "\n".join([str(row) for row in result])
            self.result_label.config(text="Stufenform der Matrix:\n" + result_str)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def gaussian_elimination(self, A):
        m, n = A.shape
        for i in range(min(m, n)):
            pivot_row = i
            while pivot_row < m and A[pivot_row, i] == 0:
                pivot_row += 1
            if pivot_row == m:
                continue
            A[[i, pivot_row]] = A[[pivot_row, i]]  # Swap rows
            for j in range(i + 1, m):
                factor = A[j, i] / A[i, i]
                A[j, i:] -= factor * A[i, i:]
        return A

def main():
    root = tk.Tk()
    app = MatrixCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
