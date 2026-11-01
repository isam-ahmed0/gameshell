import os
import platform
import sys
import time
import asyncio
# import config
import json
import webbrowser
import subprocess


def identify_os():
    os_name = platform.system()
    return os_name

def launch(g):
    source = g["source"]
    os_name = identify_os()
    if source == "steam":
        webbrowser.open(f"steam://rungameid/{g["path"]}")
    elif source == "exe":
        if os_name == "Linux":
            proton = g["proton"]
            prefix = g["prefix"]

            env = os.environ.copy()
            env["STEAM_COMPAT_DATA_PATH"] = prefix
            env["STEAM_COMPAT_CLIENT_INSTALL_PATH"] = os.path.expanduser("~/.steam/steam")

            env["__NV_PRIME_RENDER_OFFLOAD"] = "1"
            env["__GLX_VENDOR_LIBRARY_NAME"] = "nvidia"
            env["__VK_LAYER_NV_optimus"] = "NVIDIA_only"

            subprocess.Popen(["python3", proton, "run", g["path"]], env=env)

        elif os_name == "Windows":
            subprocess.Popen(g["path"])
    elif source == "crossflatform":
        subprocess.Popen(g["path"])

        
    # subprocess.Popen(g["path"])

def load_games():
    with open("games.json", "r") as f:
        return json.load(f)

def save_games(games_list):
    with open("games.json", "w") as f:
        json.dump(games_list, f, indent=4)

def add_games(g, s, p, proton=None, prefix=None):
    games = load_games()
    games.append({"name": g, "source": s, "path": p, "proton": proton, "prefix": prefix})
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

# Tests before using api.

# print(identify_os())
# gamess = add_games(g="Don't Starve", s="steam", p="219740")
# print(gamess)
# add_games(g="Don't Starve", s="steam", p="219740")