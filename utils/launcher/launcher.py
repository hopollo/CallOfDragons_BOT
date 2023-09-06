import psutil
import subprocess
import pygetwindow as gw
from os.path import join
from utils.config import cfg
from utils.log import log
from pywinauto import Application
from utils.action import MouseMove, MouseClick
import time

isGameOpen = False

"""
We are just targeting the launcher
because you cannot open the game itself
"""


def isGameRunning():
    for process in psutil.process_iter(["name"]):
        if process.info["name"] == "CALLOFDRAGONS.exe":
            global isGameOpen
            isGameOpen = True
            return True
        elif process.info["name"] == "lancher.exe":
            return True
    return False


if isGameRunning():
    log("Game is already running, next step")
    gw.getWindowsWithTitle("Call of Dragons")[0].activate()
else:
    log("Opening the game...")
    try:
        gamePath = join(cfg["paths"]["gamePath"], "launcher")

        app = Application(backend="uia").start(f"{gamePath}.exe")

        launcherWindow = app.top_window()

        coords = launcherWindow.rectangle()
        left, top, right, bottom = coords.left, coords.top, coords.right, coords.bottom
        launcher_width = right - left
        launcher_heigth = bottom - top

        MouseMove(right - 130, bottom - 150)
        time.sleep(5)
        MouseClick(right - 130, bottom - 150)
        log("Game started with launcher action")

    except Exception as e:
        log(f"ERROR: {str(e)}")

while not isGameOpen:
    isGameRunning()
    time.sleep(5)
