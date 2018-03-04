import random
import SwordAndMagicPictures
reload(SwordAndMagicPictures)  # make sure global variables are reloaded
import ControlLib
from SwordAndMagicPictures import *
from ControlLib import *
Settings.MoveMouseDelay = 0.1

lib = GaeeryLib()
lib.setRoi( gameRegion )
#lib.setRoiRectangle(0,0,500,500)
#lib.setRoiRectangle(0,0,1920,1080)

def SayThanks():
    lib.clickImageInRegion("emotion menu", Region(315,917,142,118), "1504394917440.png")

    if lib.clickImageInRegion("Thanks.", Region(0,91,551,610), "1504395063209.png", 1.5):
        return True 
    lib.clickImage( "recent emotion", "1504566828246.png", 0.5)
    return lib.clickImageInRegion("Thanks.", Region(0,91,551,610), "1504395063209.png", 1)
def SayThanksIfRare():
    
    if lib.exists( "rare", Pattern("1519098369074.png").similar(0.60), 3): # Pattern("1504308263995.png").similar(0.60)
        if lib.clickImage( "local talk", Pattern("1504437289796.png").similar(0.80)):
            sleep(0.1)
        return SayThanks()
    return False

'''
#finder = Finder( Screen(0).capture() )
screen = Screen()
region =Region(8,387,539,502)
finder = Finder( screen.capture(region) )

finder.find(Pattern("1518231798070.png").targetOffset(-17,9))
while finder.hasNext():
    found = finder.next()
    print "found 2: ", found.__class__, "  ", found 
    #found.x = found.x + region.x
    #found.y = found.y + region.y
    center = found.getTarget()
    center.x = center.x + region.x
    center.y = center.y + region.y
    print center
    region.click(center)
    
finder.destroy()
'''