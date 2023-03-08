import pyautogui as pg
import time

positionsToDefine = [
    "OpenDiscussionWithY",
    "ChatBox",
    "SendMessage",
    "StartVideoCall",
    "StartAudioCall"
]
seconds = 3

FILE = "Positions"
open(FILE, 'w').close()
file = open(FILE, "w")
file.write("NAME X Y\n")

def openSkype():
    pg.press("win")
    pg.write("Skype", interval=0.1)
    pg.press("enter")

def alttab():
    pg.keyDown('alt')
    time.sleep(.2)
    pg.press('tab')
    time.sleep(.2)
    pg.keyUp('alt')

def ListenToClick():
    time.sleep(seconds)
    return pg.position()
    
for p in positionsToDefine:
    print(p)
    time.sleep(2)
    openSkype()
    time.sleep(seconds)
    position = ListenToClick()
    file.write(f"{p} {position[0]} {position[1]} \n")
    alttab()

file.close()
