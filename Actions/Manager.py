import pyshark
import pyautogui as pg

class Manager():
    def __init__(self):
        self.capture = None
        self.timeout = 100
        self.speed = 0.1

    def initialize(self, interface):
        self.capture = pyshark.LiveCapture(interface=interface)
        print("Manager has been started")

    def openSkype(self):
        pg.press("win")
        pg.write("Skype", interval=self.speed)
        pg.press("enter")
    