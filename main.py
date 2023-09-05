from utils.launcher.launcher import isGameRunning
from utils.log import log
from utils.recognition.recognition import loadImages 

def init():
  log('Starting bot...')
  isGameRunning()
  loadImages()

init()