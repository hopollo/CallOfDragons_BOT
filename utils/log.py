from utils.config import cfg
from os.path import join, exists
from os import makedirs
import datetime

def log(text):
  currentTime = datetime.datetime.now().strftime("%d/%m %H:%M:%S")
  line = f'[{currentTime}]: {text}'
  print(line)
  writeToLogs(line)

def writeToLogs(line):
  currentDate = datetime.datetime.now().strftime("%d_%m")

  logsFolder = cfg["folders"]["logs"]
  fileName = f"log-{currentDate}.txt"
  filePath = join(logsFolder, fileName)

  try:
    if not exists(logsFolder):
      makedirs(logsFolder)
  except:
    print('Impossible to create logs folder !')

  with open(filePath, 'a') as file:
    file.write(f"{line}\n")