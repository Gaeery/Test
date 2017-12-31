'''
    #usage
    lib = GaeeryLib()
    lib.setROI(Screen().getBounds())
    #lib.setRoiRectangle(0,0,500,500)
    lib.setRoiRectangle(0,0,1920,1080)
    lib.clickImage( "menu", "1504253535945.png")
'''


from sikuli import *

gameRegion = Region(0,30,557,988)

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

# click a image in game region,  support timeout,  return True if success
def c(target, timeout = 1):
    return clickInRegion(gameRegion, target, timeout)

# click a image in game region,  support timeout,  return True if success
def d(msg, target, timeout = 1):
    Debug.user(msg)
    return clickInRegion(gameRegion, target, timeout)

'''# second game
def d2(msg, target, retry = 1):
    Debug.user(msg)
    return clickInRegion(gameRegion2, target, retry)
'''

#click location with log
def l(msg, location):
    Debug.user(msg)
    click(location)

'''
def findLocation(reg, target, timeout = 1):
    try:
        if reg.exists(target, timeout):
            loc = reg.find(target)
            Debug.user("Found target")
            return loc
    except FindFailed:
        Debug.user("Can't find target")
    return None
'''

def clickLocIfExist(loc):
    if loc!=None:
        click(loc)



def clickRegionBottom ( region ):
    #click(region)
    click(region.offset(0, region.h/2))

def clickImageBottomInRegion( message, region, image, timeout = 0 ):
    Debug.user("[clickImageInRegion] %s" % message )
    sc = Screen()
    sc.setAutoWaitTimeout(timeout)
    sc.setROI(region)
    try:
        target = sc.find(image)
        clickRegionBottom( target )
        return True
    except FindFailed:
        Debug.user("[clickImageInRegion] can't find %s" % message )
        return False
    


class Automation:
    def getTargetInRegion( region ):
        raise ValueError('not impelmented')
    def __init__(self):
        return
    def __str__(self):
        return ("Automation class")

class ImageTarget(Automation):
    def getTargetInRegion( region ):
        raise ValueError('not impelmented')
    def __init__(self,image):
        suer.__init__()
        self.image = image

# store image and its offset
class ImageOffset(Automation):
    image = 0
    offsetX = 0
    offsetY = 0
    #def __init__(image):
    #    self.image = image
    def __init__(self,image, offsetX, offsetY):
        #super.__init__(self);
        self.image = image
        self.offsetX = offsetX
        self.offsetY = offsetY



from sikuli import *
import shutil

#compare function
def by_y(match):
    return match.y


class GaeeryLib:
    sc = Screen()
    roiRectangle = Screen().getBounds()
    regionImage = None
    
    def __init__(self):
        #constructor   
        self.region = Screen().getBounds()
        
    def setRoi(self, roiRectangle):
        #Debug.user( "setROI = %d, %d, %d, %d" % (roiRectangle.x , roiRectangle.y , roiRectangle.w , roiRectangle.h) )
        self.roiRectangle = roiRectangle

    def setRoiRectangle(self, x, y, w, h):
        self.setROI( Region(x,y,w,h) )
        
    def clickImage( self, message, image, timeout = 0 ):
        Debug.user(message)
        self.sc.setAutoWaitTimeout(timeout)
        self.sc.setROI(self.roiRectangle)
        try:
            target = self.sc.find(image)
            click(target.getCenter())
            return True
        except FindFailed:
            Debug.user("can't find %s" % message )
            return False

    def find( self, message, image, timeout = 0 ):
        #Debug.user(message)
        self.sc.setAutoWaitTimeout(timeout)
        self.sc.setROI(self.roiRectangle)
        try:
            target = self.sc.find(image)
            #Debug.user("Found %s" % message )
            return target
        except FindFailed:
            Debug.user("can't find %s" % message )
            return None

    def findAll( self, message, image, timeout = 0 ):
        #Debug.user(message)
        self.sc.setAutoWaitTimeout(timeout)
        self.sc.setROI(self.roiRectangle)
        try:
            target = self.sc.findAll(image)
            #Debug.user("Found %s" % message )
            return target
        except FindFailed:
            Debug.user("can't find %s" % message )
            return None

    def exists( self, message, image, timeout = 0 ):
        Debug.user(message)
        self.sc.setROI(self.roiRectangle)
        if self.sc.exists(image, timeout):
            Debug.user("Exists %s" % message )
            return True
        else:
            Debug.user("not exists %s" % message )
            return False

    def clickImageInRegion( self, message, region, image, timeout = 0 ):
        Debug.user("[clickImageInRegion] %s" % message )
        sc = Screen()
        sc.setAutoWaitTimeout(timeout)
        sc.setROI(region)
        try:
            target = sc.find(image)
            click(target.getCenter())
            return True
        except FindFailed:
            Debug.user("[clickImageInRegion] can't find %s" % message )
            return False
        
     #def excuteAutomation(automation):
     #    automation.execute()

     
from java.awt import Robot
ControlLib_robot = Robot()
def getColor(loc):
    return ControlLib_robot.getPixelColor(loc.x, loc.y)

import time   
# log text to file with timestamp
def logToFile( strMessage, strFileName = os.path.join( getBundlePath(), "log.txt") ):
    localtime = time.localtime(time.time())
    timestring = time.strftime ('%Y/%m/%d %H:%M:%S')
    inp = open(strFileName, "a")
    inp.write('%s' % timestring)
    inp.write('  %s' % strMessage)
    inp.write('\r\n')
    inp.close()


# capture a screen
def screenCapture(strFileName = None, strPath = os.path.join(getBundlePath(),"screenCapture")):
    screen = Screen()
    img = capture(screen.getBounds())
    if not os.path.exists(strPath): 
        os.mkdir(strPath)
    if strFileName == None:
        strFileName = time.strftime ('%Y-%m-%d %H_%M_%S') + ".png"
    shutil.move(img, os.path.join( strPath, strFileName))
    Debug.user("screen captured : "+strFileName)

'''
def getRegionColorRate(region, color, rTolerence=10, gTolerence=10, bTolerence=10):
    matchPixels = 0
    for x in range(region.w):
        for y in range(region.h):
            Debug.user("x=%d y=%d" % (x, y))
            c = getColor(Location(region.x+x, region.y+y))
            if abs( c.getRed()-color.getRed() ) > rTolerence:
                continue
            matchPixels = matchPixels + 1
                    # and abs( c.getGreen()-color.getGreen() ) < gTolerence and abs( c.getBlue()-color.getBlue() ) < bTolerence
    result = matchPixels / region.w*region.h
    Debug.user("result=%f" % result)
    return result


Debug.user( "type test = %s" % getColor(Location(1365, 748)).__class__ )
from java.awt import Color
getRegionColorRate(Region(1357,747,85,8), Color(200,0,0) )
'''