import pyautogui as pg

def MouseMove(x, y, duration=1):
  pg.moveTo(x=x, y=y, duration=duration)

def MouseClick(x, y, repeat=1):
  pg.click(x=x, y=y, clicks=repeat)