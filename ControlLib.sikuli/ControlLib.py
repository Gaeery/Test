from sikuli import *
import SwordAndMagicPictures
from SwordAndMagicPictures import *

gameRegion = SwordAndMagicPictures.gameRegion

Settings.MoveMouseDelay = 0.1

def clickInRegion(reg, target, timeout = 1):
    try:
        if not reg.exists(target, timeout): 
            Debug.user("Can't find target")
            return False
        loc = reg.find(target)
        Debug.user("Found target")
        reg.click(loc)
        return True
    except FindFailed:
        Debug.user("Can't find target")
    return False

# click a image in game region,  support retry,  return True if success
def c(target, timeout = 1):
    return clickInRegion(gameRegion, target, timeout)

# click a image in game region,  support retry,  return True if success
def d(msg, target, timeout = 1):
    Debug.user(msg)
    return clickInRegion(gameRegion, target, timeout)

# second game
def d2(msg, target, retry = 1):
    Debug.user(msg)
    return clickInRegion(gameRegion2, target, retry)

#click location with log
def l(msg, location):
    Debug.user(msg)
    click(location)


def findLocation(reg, target, timeout = 1):
    try:
        if reg.exists(target, timeout):
            loc = reg.find(target)
            Debug.user("Found target")
            return loc
    except FindFailed:
        Debug.user("Can't find target")
    return None

def clickLocIfExist(loc):
    if loc!=None:
        click(loc)



def clickRegionBottom ( region ):
    #click(region)
    click(region.offset(0, region.h/2))

