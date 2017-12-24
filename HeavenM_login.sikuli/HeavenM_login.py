import time
import ControlLib
from ControlLib import *
import HeavenM_hotkeys
from HeavenM_hotkeys import *

imageLoginButton = "imageLoginButton.png"

def login():
    imageWaitForLogin = "imageWaitForLogin.png"
    
    if Region(753,689,393,120).waitVanish(imageWaitForLogin, FOREVER):
        sleep(5)
        wait(imageLoginButton, FOREVER)
        click(imageLoginButton)

login()