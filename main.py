import os
import time
import threading
# import config
from core import api
from pypresence import Presence
from pypresence.types import ActivityType
from cli import app as cli
from core import gui_loader
from gui_qt import gui

def rpc():
    RPC = Presence("1566360323605274654")
    RPC.connect()
    RPC.update(
        activity_type=ActivityType.PLAYING,
        state="Game Shell",
        state_url="https://github.com/isam-ahmed0",
        details="A Game launcher which is vey customizable.",
        details_url="https://github.com/isam-ahmed0/gameshell",
        # large_image="logo",
        # large_url="https://project-website.com",
        # buttons=[
        #     {"label": "View Project", "url": "https://github.com/username/project"},
        #     {"label": "Documentation", "url": "https://docs.project.com"}
        # ]
    )

rpc_thread = threading.Thread(target=rpc, daemon=True)
rpc_thread.start()

# gui.run_gui(api)
cli.run(api)
#gui_loader.run(api, "/home/isam/Projects/learn-python/test.py")