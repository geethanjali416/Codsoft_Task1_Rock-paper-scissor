import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors Game")
        self.master.configure(bg='#F0F0F0')  # Set background color for the window

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0
        self.tries_left = 5

        self.create_widgets()

    def create_widgets(self):
        self.label_header = tk.Label(self.master, text="Rock Paper Scissors Game", font=("Arial", 18), bg='#F0F0F0')
        self.label_header.pack(pady=10)

        self.label_choices = tk.Label(self.master, text="Choose your move:", bg='#F0F0F0')
        self.label_choices.pack()

        self.button_rock = tk.Button(self.master, text="Rock", width=10, command=lambda: self.play_game(1), bg='#FFA500', fg='white')
        self.button_rock.pack(pady=5)

        self.button_paper = tk.Button(self.master, text="Paper", width=10, command=lambda: self.play_game(2), bg='#1E90FF', fg='white')
        self.button_paper.pack(pady=5)

        self.button_scissors = tk.Button(self.master, text="Scissors", width=10, command=lambda: self.play_game(3), bg='#DC143C', fg='white')
        self.button_scissors.pack(pady=5)

        self.label_score = tk.Label(self.master, text=f"Score: You {self.user_score} - {self.computer_score} Computer", bg='#F0F0F0')
        self.label_score.pack(pady=10)

        self.label_tries = tk.Label(self.master, text=f"Tries left: {self.tries_left}", bg='#F0F0F0')
        self.label_tries.pack(pady=5)

    def play_game(self, user_choice):
        computer_choice = random.randint(1, 3)
        result = self.determine_winner(user_choice, computer_choice)
        self.update_scoreboard(result)
        self.tries_left -= 1
        self.label_tries.config(text=f"Tries left: {self.tries_left}")

        if self.tries_left == 0:
            self.end_game()

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return 'tie'
        elif (player_choice == 1 and computer_choice == 3) or \
             (player_choice == 2 and computer_choice == 1) or \
             (player_choice == 3 and computer_choice == 2):
            return 'win'
        else:
            return 'lose'

    def update_scoreboard(self, result):
        if result == 'win':
            self.user_score += 1
        elif result == 'lose':
            self.computer_score += 1

        self.label_score.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")

    def end_game(self):
        if self.user_score > self.computer_score:
            messagebox.showinfo("Game Over", "Congratulations! You won the game.")
        elif self.user_score < self.computer_score:
            messagebox.showinfo("Game Over", "Sorry! Computer won the game.")
        else:
            messagebox.showinfo("Game Over", "It's a tie game.")

        self.master.quit()

def main():
    root = tk.Tk()
    root.configure(bg='#F0F0F0')  # Set background color for the window
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
