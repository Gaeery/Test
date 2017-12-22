import time
import ControlLib
from ControlLib import *
import HeavenM_hotkeys
from HeavenM_hotkeys import *



images = [  "1513956456661.png"  ]

lib = GaeeryLib()

def clickTarget():
    for image in images:
       target = lib.find(image, 0) 
#

while True:
    type(Key.F9)

    sleep(0.6)
