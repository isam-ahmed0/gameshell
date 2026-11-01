# planninggg....

import os
import sys
import importlib.util
from pathlib import Path
import subprocess

def run_direct(api, path):
    subprocess.Popen(["python3", path])

def run(api, path):
    if os.path.isdir(path):
        module_path = os.path.join(path, "main.py")
        module_name = os.path.basename(path)

        if path not in sys.path:
            sys.path.append(path)
    else:
        module_path = path
        module_name = os.path.basename(path).replace(".py", "")
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    gui = importlib.util.module_from_spec(spec)

    og_dir = os.getcwd()
    gui_dir = path if os.path.isdir(path) else os.path.dirname(path)
    os.chdir(gui_dir)

    spec.loader.exec_module(gui)

    gui.run(api)

    os.chdir(og_dir)