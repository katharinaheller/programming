import tkinter as tk
from math import gcd

def find_lcm(x, y):
    return abs(x * y) // gcd(x, y)

def find_factors(x, y):
    lcm = find_lcm(x, y)
    factors = []
    if x != 0 and y != 0:
        factor_x = lcm // x
        factor_y = lcm // y
        factors.append((factor_x, factor_y))
    return factors

def find_smallest_common_divisor():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        lcm = find_lcm(num1, num2)
        factors = find_factors(num1, num2)
        factors_str = ", ".join([f"{factor[0]} * {num1} und {factor[1]} * {num2}" for factor in factors])
        result_label.config(text=f"Der kleinste gemeinsame Teiler ist: {lcm}. Er kann erreicht werden durch Multiplikation von: {factors_str}")
    except ValueError:
        result_label.config(text="Bitte geben Sie gültige Ganzzahlen ein.")

# GUI Setup
root = tk.Tk()
root.title("Kleinsten gemeinsamen Teiler finden")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label1 = tk.Label(frame, text="Erste Zahl:")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(frame, text="Zweite Zahl:")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(frame, text="Berechnen", command=find_smallest_common_divisor)
calculate_button.grid(row=2, columnspan=2, padx=5, pady=5)

result_label = tk.Label(frame, text="")
result_label.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()
