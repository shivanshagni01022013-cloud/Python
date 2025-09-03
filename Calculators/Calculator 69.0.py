#All credits to Chatgpt
import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())

        if op == "+":
            result = n1 + n2
        elif op == "-":
            result = n1 - n2
        elif op == "*":
            result = n1 * n2
        elif op == "/":
            if n2 == 0:
                raise ZeroDivisionError("Division by zero")
            result = n1 / n2
        elif op == "**":
            result = n1 ** n2
        elif op == "%":
            if n2 == 0:
                raise ZeroDivisionError("Modulus by zero")
            result = n1 % n2

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")
    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))

# GUI setup
window = tk.Tk()
window.title("Calculator with Buttons")

tk.Label(window, text="Enter 1st number:").grid(row=0, column=0)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

tk.Label(window, text="Enter 2nd number:").grid(row=1, column=0)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

# Operation buttons
button_frame = tk.Frame(window)
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="+", width=5, command=lambda: calculate("+")).grid(row=0, column=0)
tk.Button(button_frame, text="-", width=5, command=lambda: calculate("-")).grid(row=0, column=1)
tk.Button(button_frame, text="*", width=5, command=lambda: calculate("*")).grid(row=0, column=2)
tk.Button(button_frame, text="/", width=5, command=lambda: calculate("/")).grid(row=0, column=3)
tk.Button(button_frame, text="**", width=5, command=lambda: calculate("**")).grid(row=1, column=1)
tk.Button(button_frame, text="%", width=5, command=lambda: calculate("%")).grid(row=1, column=2)

# Result label
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=3, column=0, columnspan=2)

window.mainloop()
