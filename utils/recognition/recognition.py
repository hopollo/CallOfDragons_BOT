from utils.log import log
from utils.config import cfg
import os
import pyautogui as pg
import cv2 as cv
import numpy as np
from utils.action import MouseClick, MouseMove

imgs_folder_path = cfg["folders"]["img"]

images = []

found_any = False


def loadImages():
    try:
        log("Loading images...")

        items = os.listdir(imgs_folder_path)

        for item in items:
            item_path = os.path.join(imgs_folder_path, item)

            if os.path.isfile(item_path):
                images.append(item_path)

        log(f"{len(images)} images available")

        findInteraction()
    except:
        log(
            "img folder not found, please create it & insert at least one image to detect"
        )


def findInteraction():
    try:
        log("Searching for interactions...")

        desktop_screenshot = "screenshot.png"
        pg.screenshot(desktop_screenshot)

        img = cv.imread(desktop_screenshot, cv.IMREAD_GRAYSCALE)
        assert img is not None, "Target image could not be read"

        for imageToSearch in images:
            template = cv.imread(imageToSearch, cv.IMREAD_GRAYSCALE)
            assert template is not None, "Screenshot could not be read"
            w, h = template.shape[::-1]

            res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)

            treshold = 0.95

            loc = np.where(res >= treshold)
            for pt in zip(*loc[::-1]):
                cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                x, y = pt[0] + w // 2, pt[1] + h // 2
                pg.moveTo(x, y, duration=1)
                pg.click(x, y)

    except Exception as e:
        log(f"ERROR: {str(e)}")
