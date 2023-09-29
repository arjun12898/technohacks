import tkinter as tk
from tkinter import ttk
import random
import time

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        result_label.config(text="You win!", foreground="green")
        user_score += 1
        celebrate_effect()
    else:
        result_label.config(text="Computer wins!", foreground="red")
        computer_score += 1
        disappoint_effect()
    
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    
    play_again_button.pack()

def reset_game():
    result_label.config(text="")
    computer_choice_label.config(text="")
    play_again_button.pack_forget()

def celebrate_effect():
    for _ in range(3):
        result_label.update()
        time.sleep(0.2)
        result_label.config(foreground="green")
        result_label.update()
        time.sleep(0.2)
        result_label.config(foreground="black")

def disappoint_effect():
    for _ in range(3):
        result_label.update()
        time.sleep(0.2)
        result_label.config(foreground="red")
        result_label.update()
        time.sleep(0.2)
        result_label.config(foreground="black")

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Create a label for instructions
instruction_label = tk.Label(window, text="Choose your move:")
instruction_label.pack()

# Create buttons for rock, paper, and scissors with style
style = ttk.Style()
style.configure('TButton', font=("Helvetica", 16))
rock_button = ttk.Button(window, text="Rock", command=lambda: play_game("rock"))
paper_button = ttk.Button(window, text="Paper", command=lambda: play_game("paper"))
scissors_button = ttk.Button(window, text="Scissors", command=lambda: play_game("scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

# Create labels to display the result and computer's choice
result_label = tk.Label(window, text="", font=("Helvetica", 16))
computer_choice_label = tk.Label(window, text="", font=("Helvetica", 12))

result_label.pack()
computer_choice_label.pack()

# Create a "Play Again" button
play_again_button = ttk.Button(window, text="Play Again", command=reset_game)

# Create labels to display user and computer scores
user_score, computer_score = 0, 0
user_score_label = tk.Label(window, text=f"Your Score: {user_score}", font=("Helvetica", 12))
computer_score_label = tk.Label(window, text=f"Computer Score: {computer_score}", font=("Helvetica", 12))

user_score_label.pack()
computer_score_label.pack()

# Start the tkinter main loop
window.mainloop()
