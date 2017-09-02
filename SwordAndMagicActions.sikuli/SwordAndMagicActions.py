import random
import SwordAndMagicPictures
reload(SwordAndMagicPictures)  # make sure global variables are reloaded
import ControlLib
from SwordAndMagicPictures import *
from ControlLib import *


lib = GaeeryLib()
lib.setROI( Region(336,84,219,60))
#lib.setRoiRectangle(0,0,500,500)
#lib.setRoiRectangle(0,0,1920,1080)
while True:
    lib.find( "rare", "1504308263995.png")