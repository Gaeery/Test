import random
import SwordAndMagicPictures
reload(SwordAndMagicPictures)  # make sure global variables are reloaded
import ControlLib
from SwordAndMagicPictures import *
from ControlLib import *
Settings.MoveMouseDelay = 0.1

lib = GaeeryLib()
lib.setROI( gameRegion )
#lib.setRoiRectangle(0,0,500,500)
#lib.setRoiRectangle(0,0,1920,1080)

def SayThanks():
    lib.clickImageInRegion("emotion menu", Region(315,917,142,118), "1504394917440.png")
    return lib.clickImageInRegion("Thanks.", Region(0,91,551,610), "1504395063209.png", 1.5)
def SayThanksIfRare():
    if lib.exists( "rare", "1504308263995.png", 3):
        if lib.clickImage( "local talk", Pattern("1504437289796.png").similar(0.80)):
            sleep(0.1)
        return SayThanks()
    return False
