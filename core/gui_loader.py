# planninggg....

import os
import sys
import importlib.util
from pathlib import Path
import subprocess

def run_direct(api, path):
    subprocess.Popen(["python3", path])

def run(api, path):
    module_name = os.path.basename(path).replace(".py", "")
    spec = importlib.util.spec_from_file_location(module_name, path)
    gui = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gui)

    gui.run(api)