from utils.log import log
from utils.config import cfg
import os
import cv2
import numpy as np
from utils.action import MouseClick

imgs_folder_path = cfg['folders']['img']

images = []

found_any = False

def loadImages():
    try:
        log('Loading images...')

        items = os.listdir(imgs_folder_path)

        for item in items:
            item_path = os.path.join(imgs_folder_path, item)
            if os.path.isfile(item_path):
                images.append(item_path)

        log(f"{len(images)} images available")

        findInteraction()
    except:
        log('img folder not found, please create it & insert at least one image to detect')

def findInteraction():
    try:
      for target_image_path in images:
          target_image = cv2.imread(target_image_path)

          for reference_image_path in images:
            if target_image_path == reference_image_path:
              continue

            reference_image = cv2.imread(reference_image_path)

            res = cv2.matchTemplate(target_image, reference_image, cv2.TM_CCORR_NORMED)

            threshold = 0.8

            locations = np.where(res >= threshold)

            if len(locations[0]) > 0:
              for i in range(len(locations[0])):
                x, y = locations[1][i] + reference_image.shape[1] // 2, locations[0][i] + reference_image.shape[0] // 2
                MouseClick(x, y)
                found_any = True

      if found_any:
        log("Clicked on at least one image")
      else:
        log("No images found")
    except Exception as e:
      log(f'ERROR: {str(e)}')