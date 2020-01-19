# Coded and Published by Matjf
# email: matteop2k5@gmail.com
# enjoy the script and wait for updates
#
# remember to ask question and report bugs


import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox, QMessageBox, QWidget, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
import pyautogui, time, subprocess
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QSize
import re
import webbrowser
import requests


#--------------------Sites Here-----------------------

sites=["https://direct-link.net/64899/youtube", "https://up-to-down.net/64899/matjfTampermonkey",
"https://direct-link.net/64899/matjfScript", "https://direct-link.net/64899/matjfDragon",
"https://direct-link.net/64899/matjfScript2", "https://direct-link.net/64899/matjfAimbot",
"https://link-to.net/64899/matjfScript3", "https://link-to.net/64899/culo", "https://direct-link.net/64899/1",
"https://direct-link.net/64899/2", "https://direct-link.net/64899/3", "https://up-to-down.net/64899/4",
"https://up-to-down.net/64899/5"]

#-----------------------loop, don't touch-------------------------

while i < 13:

    pyautogui.click(375, 53, duration=1, button='left')
    pyautogui.typewrite(sites[i], interval=0.01)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(985, 675, duration=0.3, interval=0.3, button='left')
    print("----------Solving NoRobot check--------")
    time.sleep(4)
    pyautogui.click(610, 955, duration=0.3, interval=0.3, button='left')
    time.sleep(7)
    print("----------Completing requests----------")
    pyautogui.click(985, 720, duration=0.3, interval=0.3, button='left')
    time.sleep(16)
    pyautogui.click(1410, 210, interval=1.0, duration=1.0, button='left')
    time.sleep(1)
    pyautogui.click(980, 820, interval=0.1, duration=0.1, button='left')
    time.sleep(85)
    pyautogui.click(1420, 210, interval=0.1, duration=0.1, button='left')
    time.sleep(5)
    print("----------Scrolling Down----------")
    pyautogui.scroll(-400)
    pyautogui.click(610, 500, interval=0.3, duration=0.3, button='left')
    print("---------finish----------")

    i = i + 1

