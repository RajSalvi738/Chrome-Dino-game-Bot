from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Coordinates():
    replayBtn = (480, 464)
    dinosaur = (186, 489)#491 #22 #469
    # 240=xcordinate to check for tree
    # y-cordinate = 420


def restartGame():
    pyautogui.click(Coordinates.replayBtn)
    pyautogui.keyDown('down')


def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.18)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')


def imageGrab():
    box = (Coordinates.dinosaur[0]+60, Coordinates.dinosaur[1],
           Coordinates.dinosaur[0]+160, Coordinates.dinosaur[1]+5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()


def main():
    restartGame()
    while True:
        if(imageGrab() != 747):
            pressSpace()
            time.sleep(0.1)


main()
