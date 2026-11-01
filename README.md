# [isam-ahmed0/gameshell](https://github.com/isam-ahmed0/gameshell)

This project is for beginners.

I have made the core/api so any beginener can make there own GUI or CLI.

Im a beginner too.

### Core
It uses core/api

``api.launch(g)`` [g is game]

``api.laod_games()``

``add_games(g, s, p, proton=None, prefix=None)`` [s is source and p is path.] [proton and prefix are linux only]

``api.save_games(games_list)``

``api.remove_game(game_name)``

``api.edit_games(old_name, new_name=None, new_path=None)`` [Proton edit and prefix edit will be added soon.]

### Interface
You can make your own GUi or CLI.

PySide6, TKinter, CustomTKinter, Web base(django, fastapi), kivy or any gui support

Example
``def run(api):``


### Conclusion
Also It has and Example GUI/CLI

no ai. I writed myself

