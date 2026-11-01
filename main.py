import os
import time
import argparse
import threading
# import config
from core import api
from pypresence import Presence
from pypresence.types import ActivityType
from cli import app as cli
from core import gui_loader
from gui_qt import gui

parser = argparse.ArgumentParser(
                    prog='Game Shell',
                    description='A Game launcher which is vey customizable.',
                    epilog='Litterally this is vey customizable.')

parser.add_argument('-ui', '--ui', help="Use a custom Interface. -ui <path>")
args = parser.parse_args()

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


if args.ui:
    gui_loader.run(api, args.ui)
else:
    cli.run(api)

# TESTS BEFORE APPLYING.
#gui_loader.run(api, "/home/isam/Projects/learn-python/test.py")
# # gui.run_gui(api)