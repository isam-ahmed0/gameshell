import json

games = [
    {"name": "Among Us", "path": "lutris"}
]

def load_games():
    with open("games.json", "r") as f:
        return json.load(f)

def save_games(games_list):
    with open("games.json", "w") as f:
        json.dump(games_list, f, indent=4)

games = load_games()

print(games)