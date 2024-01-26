import tkinter as tk
from tkinter import simpledialog
import random

def generate_teams(num_teams, players_per_team):
    total_players = num_teams * players_per_team
    players = [f"Player {i+1}" for i in range(total_players)]
    random.shuffle(players)

    teams = {f"Team {i+1}": players[i*players_per_team:(i+1)*players_per_team] 
             for i in range(num_teams)}
    return teams

def display_teams(teams):
    text.delete('1.0', tk.END)
    for team, members in teams.items():
        text.insert(tk.END, f"{team}: {', '.join(members)}\n")

def on_submit():
    num_teams = int(team_entry.get())
    players_per_team = int(player_entry.get())
    teams = generate_teams(num_teams, players_per_team)
    display_teams(teams)

root = tk.Tk()
root.title("Game Mod - Team Generator")

tk.Label(root, text="Number of Teams:").pack()
team_entry = tk.Entry(root)
team_entry.pack()

tk.Label(root, text="Players per Team:").pack()
player_entry = tk.Entry(root)
player_entry.pack()

submit_button = tk.Button(root, text="Generate Teams", command=on_submit)
submit_button.pack()

text = tk.Text(root)
text.pack()

root.mainloop()