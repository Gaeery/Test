import random
import ControlLib
from ControlLib import *
reload(ControlLib)  # make sure global variables are reloaded

while True:
    if Region(442,38,426,101).exists("1519655731194.png", 0):
        click(Location(947, 671))
        sleep(0.2)
        click(Location(938, 543))
        sleep(0.2)
        click(Location(1058, 450))
        sleep(1)