import tkinter as tk

def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear_entry():
    entry.delete(0, tk.END)

def append_text(text):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + text)

# Create the main window
window = tk.Tk()
window.title("Hacking Calculator")
window.geometry("400x500")
window.configure(bg="black")

# Create an entry widget for input and result
entry = tk.Entry(window, font=("Courier", 24), bd=10, justify="right", bg="black", fg="green")
entry.pack(fill="both", expand=True)

# Create a grid of buttons for digits and operations
button_frame = tk.Frame(window)
button_frame.pack(fill="both", expand=True)

button_texts = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row, col = 0, 0
for text in button_texts:
    if text == "C":
        tk.Button(button_frame, text=text, font=("Courier", 18), width=5, height=2, command=clear_entry, bg="red", fg="black").grid(row=row, column=col)
    elif text == "=":
        tk.Button(button_frame, text=text, font=("Courier", 18), width=5, height=2, command=evaluate_expression, bg="green", fg="black").grid(row=row, column=col)
    else:
        tk.Button(button_frame, text=text, font=("Courier", 18), width=5, height=2, command=lambda t=text: append_text(t), bg="black", fg="green").grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the tkinter main loop
window.mainloop()
