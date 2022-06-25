#program input spam private chat
from typing import TextIO

import pyautogui,time
time.sleep(2)

while(True):
    a = open("TXT.txt", 'r')

    #OUTPUT

    for word in a:
        pyautogui.typewrite(word)
        pyautogui.press("ENTER")

