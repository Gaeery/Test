import time
import math
import ControlLib
from ControlLib import *
import HeavenM_hotkeys
from HeavenM_hotkeys import *
from java.awt import Robot

Settings.MoveMouseDelay = 0.1

r = Robot()

bufferRegion =  Region(145,155,466,40)


# store image and its offset
class BufferStatus():
    image = 0
    name = ""
    useSkillSteps = []
    def __init__(self, name, image, useSkillSteps = []):
        self.image = image
        self.name = unicode(name, "utf8")
        self.useSkillSteps = useSkillSteps

BufferList = [ 
        BufferStatus("精靈餅乾", "1513000438389.png", [Pattern("1513012091917.png").similar(0.95), Pattern("1513012115279.png").similar(0.95), Pattern("1513012153809.png").similar(0.95), "1513012783396.png", "1513012843741.png"]),
        BufferStatus("食物", Pattern("1513000766333.png").similar(0.59), [Pattern("1513012091917.png").similar(0.95), Pattern("1513012115279.png").similar(0.95), "1513053707716.png", "1513053720833.png" , "1513012843741.png"]),
        BufferStatus("保護罩", Pattern("1513000826312.png").similar(0.67), ["1513012904938.png", "1513012930638.png", "1513012940942.png", "1513012843741.png"]),
        BufferStatus("鎧甲護持", Pattern("1513000907139.png").similar(0.69), ["1513012904938.png","1513013125930.png","1513013138966.png", "1513012843741.png"]),
        BufferStatus("負重強化", Pattern("1513000932286.png").similar(0.65), ["1513012904938.png","1513013030782.png","1513013041431.png", "1513012843741.png"]),
        BufferStatus("變身", Pattern("1513001027215.png").similar(0.68)),
        BufferStatus("強化戰鬥卷軸", Pattern("1513001000565.png").similar(0.59)),
        BufferStatus("自我加速藥水", Pattern("1513004774208.png").similar(0.72), [Pattern("1513012091917.png").similar(0.95), Pattern("1513012115279.png").similar(0.95), "1513033719938.png", "1513033735138.png", "1513012843741.png"]),
        ]

def checkBufferStatus():
    lib = GaeeryLib()
    lib.setROI(Region(1303,49,502,710))
 
    for buffer in BufferList:
        if not bufferRegion.exists(buffer.image, 0):
            Debug.user( "no buffer %s" % buffer.name )
            for step in buffer.useSkillSteps:
                lib.clickImage( "use skill step", step)
                sleep(0.5)

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

regionLeftScreen = Region(503,144,91,88)
regionParty = Region(302,343,28,363)
regionHpFirst = Region(140,370,161,40)
regionHp = Region()
regionMp = Region(140,77,294,25)
regionStatusFirst = Region(345,333,86,96)
regionStatus = Region()
imageHp90 = Pattern("imageHp90.png").similar(0.90)
imageHp65 = Pattern("imageHp65.png").similar(0.85)
imageHp40 = Pattern("imageHp40.png").similar(0.85)
imageMp90 = Pattern("imageMp90.png").similar(0.95)
imageMp50 = Pattern("imageMp50.png").similar(0.85)
imageMp10 = "imageMp10.png"
imageMp10_1 = "imageMp10_1.png"
imageParty = Pattern("imageParty.png").similar(0.95)

nHploc_y = 385
nMploc_y = 400
nPercent_x = [ 275, 240, 202, 190, 157 ]
nPercent = [90, 60, 40, 30, 10]

pRecoverHp = Location(921, 921)
pRecoverMp = Location(1037, 916)

pHpWater = Location(808, 921)
pGoToTown = Location(1160, 916)
pGameWnidow = Location(800, 14)

bFlyIfNoHp = True
pEscape = Location(493, 808)

previousTripleArrowTime = 0

lib = GaeeryLib()
lib.setRoi(regionParty)

def checkHp():
    global nBackHomeCount
    global lib
    global regionHp
    global regionStatus
    global nHploc_y
    global nMploc_y
    global previousTripleArrowTime
    global previousCheckStayTime

    locParty = lib.find("party", imageParty)
    
    partyMembers = lib.findAll("party members", imageParty)
    if partyMembers != None:
        sortedPartyMembers = sorted(partyMembers, key=by_y)
        locParty = sortedPartyMembers[0]
        #Debug.user("locParty.y=%d", locParty.y)
        nHploc_y = locParty.y + 14
        nMploc_y = nHploc_y + 15
    
    if locParty == None:
        leftRoi = GaeeryLib()
        leftRoi.setRoi(regionLeftScreen)
        characterPage = leftRoi.find("character data", "1513897038903.png")
        if characterPage != None:
            Debug.user("close characterPage")
            click(characterPage)
            return

        menuRoi = GaeeryLib()
        menuRoi.setRoi(Region(1726,47,93,85))
        menuPage = menuRoi.find("menu", "1513897038903.png")
        if menuPage != None:
            Debug.user("close menu")
            click(menuPage)
            return

        #talk
        if Region(1541,670,118,40).exists("1514506603250.png", 0):
            click(Location(1637, 874))
            sleep(1)
            return

        if Region(925,711,294,123).exists( "1514109969796.png", 0):  #mission page
            click( "1514109969796.png" )
            sleep(1)            
            return
            
        if characterPage != None:
            Debug.user("close characterPage")
            click(characterPage)
            return
        
        Debug.user("Change to party page")
        if Region(194,241,69,54).exists("1513943945882.png", 0.3):
            click( locPartyPage )
        if Region(72,353,53,47).exists("1513948889607.png", 0.3):
            click( locCreateParty )
        if Region(945,816,322,78).exists("1513949150393.png", 3):
            click( locCreatePartyConfirm )
        return
    else:
        regionHpCurrent = Region( regionHpFirst.x, locParty.y, regionHpFirst.w, regionHpFirst.h )
        if math.fabs(regionHpCurrent.y - regionHp.y)>5:
            regionHp = regionHpCurrent
            regionStatus = Region( regionStatusFirst.x, locParty.y-40, regionStatusFirst.w, regionStatusFirst.h ) 
            
            #regionHp.highlight()
            regionStatus.highlight()
            sleep(1)
            #regionHp.highlight()
            regionStatus.highlight()

    hpPercent = getHpStatus()
    mpPercent = getMpStatus()

    Debug.user("Hp: %d, Mp: %d" % (hpPercent, mpPercent) )

    if bUseFightingSkill and mpPercent >= nMinMpPercentTripleArrow:
        if time.time()-previousTripleArrowTime >= nIntervalTripleArrow:
            useTripleArrow()
            previousTripleArrowTime = time.time()



    if hpPercent >= 90:
        nBackHomeCount = 0
        if mpPercent < 90:     
            recoverMp()
        #else:
            #usingFightingSkill(True)
            
    elif hpPercent >= 60:
        #Debug.user("Hp is 60~90")
        #click(pHpWater)  
        if mpPercent >= 10:     
            recoverHp()
        else:
            #usingFightingSkill(False)
            recoverMp()
        nBackHomeCount = 0
    elif hpPercent >= 40:       
        #Debug.user("Hp is 40~60")
        bringGameToFront()
        drinkWater()
        if mpPercent >= 10:   
            recoverHp()
        else:
            #escape()
            recoverMp()
        #escape()
        nBackHomeCount = 0
    else:       
        Debug.user("Hp is lower than 40")
        if checkStatus():
            return
        drinkWater()
        if hasMp():  
            recoverHp()
        
        if checkStatus():
            return

        if not bFlyIfNoHp:
            return
            
        nBackHomeCount = nBackHomeCount + 1
        if nBackHomeCount < 2:
            escape()
            return
        
        Debug.user("return to town!!")
        screenCapture()
        click(pGoToTown)
        exit(1)


def escape():
    Debug.user("Run away")
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
    for i in range( len(nPercent_x) ):
        color = r.getPixelColor(nPercent_x[i], nHploc_y) 
        #printColor( format("Hp %d Color" % nPercent[i]), color)
        if color.getRed() >= 139 and color.getBlue() < 50:
            return nPercent[i]
    return -1

def getMpStatus():
    for i in range( len(nPercent_x) ):
        color = r.getPixelColor(nPercent_x[i], nMploc_y) 
        #printColor( format("Mp %d Color" % nPercent[i]), color)
        if color.getBlue() >= 125 and color.getRed() < 30:
            return nPercent[i]
    return -1

def isMpFull():
    locHighMp = Location(397, 89)
    highMpColor = r.getPixelColor(locHighMp.x, locHighMp.y) # get the color object
    #printColor( "highMpColor", highMpColor)
    if highMpColor.getBlue() >= 125 & highMpColor.getRed() < 30:
        return True
    return False



# return True if in special status
def checkStatus():
    regionSelfStatus = Region(138,197,88,42)
    if regionSelfStatus.exists("1513870172508.png", 0.2):
        recoverPoison()
        sleep(0.5)
        return True
    
    if regionStatus.exists("1513870172508.png", 0.2):
        recoverPoison()
        sleep(0.5)
        return True
    if regionStatus.exists("1513870381521.png", 0.2):
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
    sleep(0.6)

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

def getColor(loc):
    return r.getPixelColor(loc.x, loc.y)



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
    #close menu
    click(locMenu)
    sleep(1)
    
#while True:
#    Debug.user("Hp status: %d" % getHpStatus())
#    Debug.user("Mp status: %d" % getMpStatus())
#    sleep(0.3)
#    continue

bringGameToFront()
screenCapture()

def closeMission():
    if Region(1021,750,101,54).exists("1514556735445.png", 0):
        click(Location(1065, 775))
        sleep(1)

while True:
    #checkBufferStatus()
    previousTime = time.time()
    getGiftFromMail()
    closeMission()
    checkHp()
    stayInMapRegion()
    if time.time()-previousTime > 4:
        Debug.user("pause a while, need to bring game to front")
        bringGameToFront()

    sleep(0.3)
