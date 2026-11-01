# [isam-ahmed0/gameshell](https://github.com/isam-ahmed0/gameshell)

This project is for beginners.

I have made the core/api so any beginener can make there own GUI or CLI.

Im a beginner too.

### [Screenshots](https://github.com/isam-ahmed0/gameshell/tree/main/screenshots)

## Lore
I noticed that Windows shell/de is heavy and replace possible.
I am making this game shell so it will work as Shell/DE/WM for Linux and Windows.

I only know Python. Im still Learning.
So I cant make the Shell/DE/WM now cuz Im a Beginner.

I have made *API*, *Core* for future.

Also I wanted my own launcher like lutris and faugus.

So now This is very customizable. It supports Any Interface. 

Anyone can make **Launcher APP, Launcher CLI, Launcher Web, Desktop Enviroment, Windows Shell(Replaces ``explorer.exe``)**

Use your Creativity to make not just an app.

## Core
It is based on core features

### API

``api.launch(g)`` [g is game]

``api.laod_games()``

``add_games(g, s, p, proton=None, prefix=None)`` [s is source and p is path.] [proton and prefix are linux only]

``api.save_games(games_list)``

``api.remove_game(game_name)``

``api.edit_games(old_name, new_name=None, new_path=None)`` [Proton edit and prefix edit will be added soon.]

### Interface
You can make your own GUi or CLI.

gui_loader.py loads gui.

PySide6, TKinter, CustomTKinter, Web base(django, fastapi), kivy or any gui support

Also a CLI and a PySide6(Qt) GUI is in this repo.

Example
``def run(api):``

it supports --ui or -ui for loading custom ui.


## Conclusion
Also It has some Example GUI/CLI

no ai. I writed myself

