from sikuli import *
import SwordAndMagicPictures
from SwordAndMagicPictures import *

gameRegion = SwordAndMagicPictures.gameRegion

Settings.MoveMouseDelay = 0.1

def clickInRegion(reg, target, timeout = 1):
    while timeout >= 0:    
        try:
            if not reg.exists(target, timeout): 
                retry = retry -1
                if retry >= 0:
                    Debug.user("not found, timeout %d", timeout)
                    sleep(1)
                continue
            loc = reg.find(target)
            Debug.user("Found target")
            reg.click(loc)
            return True
        except FindFailed:
            Debug.user("Can't find target")
        timeout = timeout -1
    return False

# click a image in game region,  support retry,  return True if success
def c(target, retry = 1):
    return clickInRegion(gameRegion, target, retry)

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


def findLocation(reg, target, retry = 1):
    while retry >= 0:    
        try:
            loc = reg.find(target)
            Debug.user("Found target")
            return loc
        except FindFailed:
            Debug.user("Can't find target")
        retry = retry -1
    return None

def clickLocIfExist(loc):
    if loc!=None:
        click(loc)



def clickRegionBottom ( region ):
    #click(region)
    click(region.offset(0, region.h/2))