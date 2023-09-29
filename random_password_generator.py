import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_random_password():
    length = length_entry.get()
    try:
        length = int(length)
        if length <= 0:
            password_label.config(text="Invalid length")
        else:
            password = generate_password(length)
            password_label.config(text=f"Generated Password: {password}")
    except ValueError:
        password_label.config(text="Invalid length")

# Create the main window
window = tk.Tk()
window.title("Hacking Password Generator")
window.geometry("400x300")
window.configure(bg="black")

# Create a label for instructions
instructions_label = tk.Label(window, text="Enter password length:", font=("Courier", 18), bg="black", fg="green")
instructions_label.pack(pady=20)

# Create an entry widget for length input
length_entry = tk.Entry(window, font=("Courier", 18), bg="black", fg="green")
length_entry.pack()

# Create a button to generate passwords
generate_button = tk.Button(window, text="Generate Password", font=("Courier", 16), command=generate_random_password, bg="black", fg="green")
generate_button.pack(pady=20)

# Create a label to display the generated password
password_label = tk.Label(window, text="", font=("Courier", 14), bg="black", fg="green")
password_label.pack()

# Start the tkinter main loop
window.mainloop()
