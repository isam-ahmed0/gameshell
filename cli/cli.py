import os
import time
from cli import logo

def run(api):
    def show_games():
        print("Choose game")
        games = api.load_games()
        for i, game in enumerate(games, start=1):
            print(f"[{i}]. {game["name"]}")
        return games
    def list():
        pass

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(logo.logo())
        print("Game Shell")
        print("1. Launch")
        print("2. Remove game")
        print("3. Add Game")
        print("4. Edit Game")
        print("Q. Exit")
        choose = input("Choose: ")

        if choose == "1":
            # show_games()
            games = show_games()
            choice = int(input("Enter game no.: "))
            try:
                api.launch(games[choice - 1])
            except Exception as e:
                print(e)
            choice = input("Enter to continue")

        elif choose == "2":
            games = show_games()
            choice = int(input("Enter game no.: "))
            g_name = games[choice - 1]
            api.remove_game(g_name["name"])

        elif choose == "3":
            games = api.load_games()
            game_name = input("Enter Game name: ")
            game_source = input("Enter Game source (e.g.: steam): ")
            game_path = input("Enter Game Path/ID: ")

            api.add_games(g=game_name, s=game_source, p=game_path)
        
        elif choose == "4":
            games = show_games()
            choice = int(input("Enter game no.: "))
            g_name = games[choice - 1]
            old_name = g_name["name"]
            new_name = input("Enter Game name: ")
            new_path = input("Enter new path/id: ")

            try:
                api.edit_games(old_name, new_name, new_path)
            except Exception as e:
                print(e)
            

        elif choose.upper() == "Q":
            break
        else:
            print(f"{choose} is invalid")
            choice = input("Enter to continue")