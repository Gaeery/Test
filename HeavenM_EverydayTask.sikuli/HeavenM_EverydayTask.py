import time
import ControlLib
from ControlLib import *
import HeavenM_hotkeys
from HeavenM_hotkeys import *



images = [  "1514022180377.png" ]
#images = [ "1514022375233.png", Pattern("1513956456661.png").similar(0.90) , "1514022180377.png" ]
images = []

lib = GaeeryLib()

def clickTarget():
    ret = False
    i = 0
    for image in images:
       target = lib.find("target " + str(i),image, 0) 
       i = i + 1
       if target != None:
            click(target)
            click(target)
            ret = True
            sleep(5)
    return ret   
#

#Screen().getPixelColor( Location(161, 397) )
#exit(0)
while True:
    clickTarget()
    #Debug.user("found")
    type(keyPracticeTask)

    sleep(0.6)
