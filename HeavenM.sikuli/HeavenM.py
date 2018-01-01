import time
import math
import ControlLib
from ControlLib import *
import HeavenM_hotkeys
from HeavenM_hotkeys import *


Settings.MoveMouseDelay = 0.1





# store image and its offset
class BufferStatus():
    image = 0
    name = ""
    useSkillSteps = []
    def __init__(self, name, image, useSkillSteps = []):
        self.image = image
        self.name = unicode(name, "utf8")
        self.useSkillSteps = useSkillSteps


def doImageSteps( steps ):
    lib = GaeeryLib()
    i = 0
    for step in steps:
        lib.clickImage( "use image step " + str(i), step)
        i = i + 1
        sleep(0.5) 

def doPositionSteps( steps ):
    i = 0
    for step in steps:
        Debug.user( "click position step " + str(i) )
        click(step)
        i = i + 1
        sleep(0.5) 

nBackHomeCount = 0


regionStatus = Region(142,194,87,41)


pGameWnidow = Location(800, 14)



previousTripleArrowTime = 0

lib = GaeeryLib()
#lib.setRoi(regionParty)


class Status():
    Normal = 0
    Poison = -2

    currentStatus = Normal
    def setStatus(self, status):
        if status != self.Normal:
            Debug.user("change status to %d" % status)
        self.currentStatus = status
    def getCurrentStatus(self):
        return self.currentStatus
    
status = Status()
def checkHp():
    global nBackHomeCount
    global lib
    global previousTripleArrowTime

    #locParty = lib.find("party", imageParty)

    hpPercent = getHpStatus()
    mpPercent = getMpStatus()

    Debug.user("Hp: %d, Mp: %d" % (hpPercent, mpPercent) )

    if hpPercent >= 0 and hpPercent <= nBackToTownThreshold:
        Debug.user("warning: no hp!!")
        nBackHomeCount = nBackHomeCount + 1
        screenCapture()
        if nBackHomeCount >= nBackHomeCountdownTimes:
            Debug.user("return to town!!")
            click(pGoToTown)
            exit(1)
        sleep(1)
    else:
        nBackHomeCount = 0
        
    if status.getCurrentStatus() == Status.Poison:
        recoverPoison()

    if hpPercent < 0:
        Debug.user("warning: can't detect HP")
        checkOtherPagesIfNoHp()
        return

    if nIntervalTripleArrow > 0 and mpPercent >= nMinMpPercentTripleArrow:
        if time.time()-previousTripleArrowTime >= nIntervalTripleArrow:
            useTripleArrow()
            previousTripleArrowTime = time.time()

    if hpPercent >= 0 and hpPercent <= nDrinkWaterThreshold:
        bringGameToFront()
        drinkWater()

    if hpPercent >= 0:
        if mpPercent < nReservedMp:
            if hpPercent <= nReservedMp_FullRecover:
                drinkWater()
                recoverHp() 
            else:
                drinkWater()                
        elif hpPercent <= nRecoverHpThreshold:
            recoverHp() 
        
    if mpPercent <= 10 or (mpPercent < nRecoverMpThreshold and hpPercent >= nRecoverHpThreshold):     
        recoverMp()


def checkOtherPagesEveryTime():
    if lib.clickImageInRegion("talking", Region(1541,670,118,40), "1514506603250.png", 0):
        sleep(1)
        return

def checkOtherPagesIfNoHp():
    
    if lib.clickImageInRegion("menu", Region(1726,47,93,85), "1513897038903.png", 0):
        sleep(1)
        return


    if lib.clickImageInRegion("accept the mission", Region(925,711,294,123), "1514109969796.png", 0):
        sleep(2)
        enableAutoFighting(True)
        return
    if lib.clickImageInRegion("award", Region(909,348,68,44), "1514792827025.png", 0):
        sleep(1)
        return
    

def escape():
    Debug.user("Run away")
    pEscape = Location(493, 808)
    click( pEscape )   
    screenCapture()
    sleep(1)
    type(keyTransport)
    sleep(1)
    drinkWater()
    sleep(0.5)
    recoverHp()
    #click(Location(1400, 752))

def hasMp():
    locLowMp = Location(164, 88)
    lowMpColor = r.getPixelColor(locLowMp.x, locLowMp.y) # get the color object
    printColor( "lowMpColor", lowMpColor)
    if lowMpColor.getBlue() >= 139 & lowMpColor.getRed() < 50:
        return True
    return False

def isMpFull():
    locHighMp = Location(397, 89)
    highMpColor = r.getPixelColor(locHighMp.x, locHighMp.y) # get the color object
    printColor( "highMpColor", highMpColor)
    if highMpColor.getBlue() >= 139 & highMpColor.getRed() < 50:
        return True
    return False


def getHpStatus():
    x100 = 425
    x0 = 162
    nAverageAmount = 3
    for i in range( 10 ):  #hp 10~90%
        nHploc_y = 76
        r = 0
        g = 0
        b = 0
        for j in range(nAverageAmount):  #hp color average
            color = getColor( Location( x100 - (x100-x0) * i / 10 , nHploc_y-j)  )
            #printColor( format("Hp %d Color" % (10-i)), color)
            r = r + color.getRed()
            g = g + color.getGreen()
            b = b + color.getBlue()
        r = r/nAverageAmount
        g = g/nAverageAmount
        b = b/nAverageAmount
        
        if r > g+100 and r > b+100:
            status.setStatus(Status.Normal)
            Debug.user( "Hp %d average Color = %d,%d,%d" % (10-i,r,g,b) )
            return 100-i*10
        elif g >= r+30 and g >= b+30:
            Debug.user("poison")
            status.setStatus(Status.Poison)
            Debug.user( "Hp %d average Color = %d,%d,%d" % (10-i,r,g,b) )
            return 100-i*10
    status.setStatus(Status.Normal)
    return -1


def getMpStatus():
    x100 = 425
    x0 = 162

    nAverageAmount = 3
    for i in range( 10 ):  #hp 10~90%  
        nHploc_y = 92
        r = 0
        g = 0
        b = 0
        for j in range(nAverageAmount):  #hp color average
            color = getColor( Location( x100 - (x100-x0) * i / 10 , nHploc_y-j)  )
            #printColor( format("(x=%d) Mp %d Color" % ( ( x100 - (x100-x0) * i / 10), (10-i) )), color)
            r = r + color.getRed()
            g = g + color.getGreen()
            b = b + color.getBlue()
        r = r/nAverageAmount
        g = g/nAverageAmount
        b = b/nAverageAmount
        

        if b > r+100 and b > g+10:
            Debug.user( "Mp %d average Color = %d,%d,%d" % (10-i,r,g,b) )
            return 100-i*10
    return -1



# return True if in special status
def checkStatus():
    regionSelfStatus = Region(138,197,88,42)
    '''
    if regionSelfStatus.exists("1513870172508.png", 0.2):
        recoverPoison()
        sleep(0.5)
        return True
    
    if regionStatus.exists("1513870172508.png", 0.2):
        recoverPoison()
        sleep(0.5)
        return True
    '''
    if regionStatus.exists("1513870381521.png", 0.5):
        Debug.user("You have become a stone.....")
        return True
    if regionStatus.exists("1513955946438.png", 0.2):
        Debug.user("You are stunned.....")
        return True

    if regionStatus.exists("1514110143993.png", 0.2):
        Debug.user("You are stunned (case 2).....")
        return True
    return False
    
def recoverMp():
    #Debug.user("Use MP recover skill")
    type(keyMpRecover)
    sleep(1.8)
    
def recoverHp():
    #Debug.user("Use HP recover skill")
    type(keyHpRecover)
    sleep(0.6)

def recoverPoison():
    Debug.user("Use rescue poison skill")
    type(keyPoisonRescue)
    sleep(1)

def drinkWater():
    Debug.user("Drink water!")
    type(keyHpWater)

def useTripleArrow():
    Debug.user("useTripleArrow")
    if Region(786,106,86,96).exists("1514469461757.png", 0):
        Debug.user("targeting a player...")
        return
    type(keyTripleArrow)
    sleep(0.6)
    
def useSelfRecoverOldWay():
    lib = GaeeryLib()
    lib.setROI(Region(751,869,1038,104))
    imageSelfRecover = Pattern("imageSelfRecover.png").similar(0.95)
    imageRecover = "imageRecover.png"    
    skill = lib.find( "find self recover skill", imageSelfRecover )
    if skill == None:
        click(pRecoverHp)
        sleep(0.5)
    lib.clickImage( "use skill to rescue self", imageSelfRecover)

bUsingFightingSkill = False
def usingFightingSkill( bOn ):
    global bUsingFightingSkill 
    if not bUseFightingSkill:
        return
    regionSkill = Region(1574,863,100,130)
    if bOn: 
        if regionSkill.exists("1513524888200.png", 0):
            #Debug.user("already on")
            return
        
        if not regionSkill.exists("1513525529844.png", 0.1):
            Debug.user("This skill doesn't support 'auto'")
            return
    else:
        if regionSkill.exists("1513525529844.png", 0):
            #Debug.user("already off")
            return            

        if not regionSkill.exists("1513524888200.png", 0.1):
            #Debug.user("no 'auto'")
            return
    
    switchAutoBuff(Location(1624, 924), bOn)
    bUsingFightingSkill = bOn



def switchAutoBuff( loc, bOn ):
    mouseMove(loc)
    mouseDown(Button.LEFT)
    if not bOn:
        Debug.user("Turn off skill %s" % loc)
        mouseMove( loc.offset(0, -30) )
    else:       
        Debug.user("Turn on skill %s" % loc)
        mouseMove( loc.offset(0, 30) )
    mouseUp(Button.LEFT)

def bringGameToFront():
    rightClick(pGameWnidow)

def printColor(strName, rgb):
    Debug.user("%s = %d,%d,%d" % (strName, rgb.getRed(), rgb.getGreen(), rgb.getBlue() ) )





previousCheckStayTime = 0 
# check if map contains stayRegions.  if not, click moveToStayRegion
def stayInMapRegion():
    global previousCheckStayTime
    if nIntervalCheckStayInterval < 0 or time.time()-previousCheckStayTime <= nIntervalCheckStayInterval:
        return
    
    previousCheckStayTime = time.time()
    regionMap = Region(1548,206,249,222)
    for stay in stayRegions:
        if regionMap.exists(stay, 0):
            Debug.user("found stay region")
            return
    Debug.user("move to stay region")
    click( locMoveToStayRegion )
    type(keyPickup)

previousCheckMailTime = 0 
def getGiftFromMail():
    global previousCheckMailTime
    if nIntervalCheckMailInterval < 0 or time.time()-previousCheckMailTime <= nIntervalCheckMailInterval:
        return
    previousCheckMailTime = time.time()

    Debug.user("check mail")
    
    locMenu = Location(1796, 73)
    menuColor = getColor(locMenu)
    #printColor("menuColor", menuColor)
    if menuColor.getRed() < 200 or menuColor.getBlue() > 50:
        return
    # menu is red
    if not Region(1431,465,53,67).exists(Pattern("1514418272184.png").similar(0.60), 0):
        
        click(locMenu)
        sleep(1)
        
    #menu opened
    locMail = Location(1483, 466)
    mailColor = getColor(locMail)
    #printColor("mailColor", mailColor)

    if mailColor.getRed() < 200 or mailColor.getBlue() > 50:
        #no mail, close menu
        click(locMenu)
        sleep(1)
        return
    
    #mail is red
    click(locMail)
    sleep(1)
    while True:
        imageReceiveGift = "1514418813566.png"
        if Region(1395,169,422,497).exists(imageReceiveGift, 0):
            click(imageReceiveGift)
            sleep(1)
        else:
            break
    #close mail
    click(locMenu)
    sleep(2)
    #close menu
    click(locMenu)
    sleep(1)
    
#while True:
#    Debug.user("Hp status: %d" % getHpStatus())
#    Debug.user("Mp status: %d" % getMpStatus())
#    sleep(0.3)
#    continue



def closeMission():
    if Region(1021,750,101,54).exists("1514556735445.png", 0):
        click(Location(1065, 775))
        sleep(1)

def enableAutoFighting(bEnable = True):
    if isAutoFighting() != bEnable:
        type(keyAutoFighting)

def isAutoFighting():
    r = 0
    g = 0
    b = 0
    for i in range(10):
        color = getColor(Location(1365, 752))
        if color.getRed() > r:
            r = color.getRed()
            if r >= 255:
                break
        g = g+color.getGreen()
        b = b+color.getBlue()
        sleep(0.1) 
    Debug.user("color = %d,%d,%d" % (r,g,b))
    return r > 230





bringGameToFront()
screenCapture("start.png")

enableAutoFighting(True)
            
while True:
    #checkBufferStatus()
    previousTime = time.time()
    getGiftFromMail()
    closeMission()
    checkHp()
    stayInMapRegion()
    checkOtherPagesEveryTime()
    if time.time()-previousTime > 4:
        Debug.user("pause a while, need to bring game to front")
        bringGameToFront()

    sleep(0.3)
