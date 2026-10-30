import os
import sys
import time
import asyncio
# import config
import json
import webbrowser
import subprocess

def launch(g):
    source = g["source"]
    if source == "steam":
        webbrowser.open(f"steam://rungameid/{g["path"]}")

        
    # subprocess.Popen(g["path"])

def load_games():
    with open("games.json", "r") as f:
        return json.load(f)

def save_games(games_list):
    with open("games.json", "w") as f:
        json.dump(games_list, f, indent=4)

def add_games(g, s, p):
    games = load_games()
    games.append({"name": g, "source": s, "path": p})
    save_games(games)

def remove_game(game_name):
    games = load_games()
    games[:] = [g for g in games if g["name"] != game_name]
    save_games(games)

def edit_games(old_name, new_name=None, new_path=None):
    games = load_games()
    for game in games:
        if game["name"] == old_name:
            if new_name:
                game["name"] = new_name
            if new_path:
                game["path"] = new_path
            # if new_name and new_path:
                # game["name"] = new_name
                # game["path"] = new_path
        
        save_games(games)



# gamess = add_games(g="Don't Starve", s="steam", p="219740")
# print(gamess)
# add_games(g="Don't Starve", s="steam", p="219740")