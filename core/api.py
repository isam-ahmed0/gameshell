import os
import platform
import sys
import time
import asyncio
# import config
import json
from PIL import Image, ImageDraw, ImageFont
import webbrowser
import subprocess

from pathlib import Path


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

            # WAIT, THIS IS FOR NVIDIA WITH AN INTEGRETED GPU. YOU SHOULD REMOVE OR EDIT.
            env["__NV_PRIME_RENDER_OFFLOAD"] = "1"
            env["__GLX_VENDOR_LIBRARY_NAME"] = "nvidia"
            env["__VK_LAYER_NV_optimus"] = "NVIDIA_only"

            subprocess.Popen(["python3", proton, "run", g["path"]], env=env)

        elif os_name == "Windows":
            subprocess.Popen(g["path"])
    elif source == "crossplatform":
        subprocess.Popen(g["path"])
    else:
        pass

        
    # subprocess.Popen(g["path"])

def games_json():
    os_name = identify_os()
    if os_name == "Linux":
        config_dir = Path.home() / ".config" / "gameshell"
    elif os_name == "Windows":
        config_dir = Path(os.getenv("APPDATA")) / "gameshell"
    
    config_dir.mkdir(parents=True, exist_ok=True)

    games_file = config_dir / "games.json"

    return games_file 

def load_games():
    game_list = games_json()
    if not game_list.exists():
        Path("example.json").copy(game_list)
    try:
        with open(game_list, "r") as f:
            return json.load(f)
    except Exception as e:
        return(e)

def save_games(games_list):
    game_list = games_json()
    if not game_list.exists():
        game_list.touch()
    try:
        with open(game_list, "w") as f:
            json.dump(games_list, f, indent=4)
    except Exception as e:
        return(e)

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

def share(g):
    W, X = 800, 400
    img = Image.new("RGB", (W, X), color="white")
    game = g["name"]
    draw = ImageDraw.Draw(img)
    ont = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 60)
    draw.text((W/2, 150), game, fill="black", font=ont, stroke_width=1, anchor="mm")
    draw.text((W/2, 200), "Play with Game Shell", fill="black", anchor="mm")
    img.show()


# Tests before using api.

# print(identify_os())
# gamess = add_games(g="Don't Starve", s="steam", p="219740")
# print(gamess)
# add_games(g="Don't Starve", s="steam", p="219740")

# share()