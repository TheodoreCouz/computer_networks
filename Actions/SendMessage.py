import pyshark
import pyautogui
from Manager import Manager

class SendMessage(Manager):
    def __init__(self):
        super().__init__()

    def start(self, interface):
        Manager.initialize(self, interface)
        print("Trying to send a message")
        Manager.openSkype(self)

    def listen(self):
        Manager.capture.sniff(timeout=Manager.timeout)
        Manager.capture()


ManagerInstance = SendMessage()
ManagerInstance.start("eth0")
