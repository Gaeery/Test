import time
import math
import ControlLib
from ControlLib import *
import HeavenM_hotkeys
from HeavenM_hotkeys import *

Settings.MoveMouseDelay = 0.1


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
regionStatusFirst = Region(345,333,86,96)
regionStatus = Region()
imageHp90 = Pattern("imageHp90.png").similar(0.90)
imageHp65 = Pattern("imageHp65.png").similar(0.85)
imageHp40 = Pattern("imageHp40.png").similar(0.85)
imageMp90 = Pattern("imageMp90.png").similar(0.95)
imageMp50 = Pattern("imageMp50.png").similar(0.85)
imageMp10 = Pattern("imageMp10.png").similar(0.90)
imageParty = Pattern("imageParty.png").similar(0.95)
pRecoverHp = Location(921, 921)
pRecoverMp = Location(1037, 916)

pHpWater = Location(808, 921)
pGoToTown = Location(1160, 916)
pGameWnidow = Location(800, 14)

bFlyIfNoHp = True
pEscape = Location(493, 808)


lib = GaeeryLib()
lib.setRoi(regionParty)

def checkHp():
    global nBackHomeCount
    global lib
    global regionHp
    global regionStatus
    

    locParty = lib.find("party", imageParty)
    
    partyMembers = lib.findAll("party members", imageParty)
    if partyMembers != None:
        sortedPartyMembers = sorted(partyMembers, key=by_y)
        locParty = sortedPartyMembers[0]
    
 
    
    if locParty == None:
        leftRoi = GaeeryLib()
        leftRoi.setRoi(regionLeftScreen)
        characterPage = leftRoi.find("character data", "1513897038903.png")
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
            regionHp.highlight()
            regionStatus.highlight()
            sleep(1)
            regionHp.highlight()
            regionStatus.highlight()
    
    if regionHp.exists(imageHp90, 0.3):
        nBackHomeCount = 0
        if not regionHp.exists(imageMp90, 0.1):     
            Debug.user("Hp is OK")            
            recoverMp()
        else:
            #Debug.user("Hp & Mp are OK")
            usingFightingSkill(True)
                
            
    elif regionHp.exists(imageHp65, 0.3):
        Debug.user("Hp is 65~90")
        #click(pHpWater)  
        if regionHp.exists(imageMp10, 0.3):     
            Debug.user("has mp")
            recoverHp()
        else:
            Debug.user("no mp")
            usingFightingSkill(False)
            recoverMp()
        nBackHomeCount = 0
    elif regionHp.exists(imageHp40, 0.5):
        Debug.user("Hp is 40~65")
        bringGameToFront()
        drinkWater()
        if regionHp.exists(imageMp10, 0.3):     
            Debug.user("has mp")
            recoverHp()
        else:
            Debug.user("no mp")
            usingFightingSkill(False)
            recoverMp()
            #escape()
        escape()
        nBackHomeCount = 0
    else:       
        Debug.user("Hp is lower than 40")
        drinkWater()
        if regionHp.exists(imageMp10, 0.3):     
            Debug.user("has mp")
            recoverHp()
        
        if checkStatus():
            return

        escape()

        if not bFlyIfNoHp:
            return
            
        nBackHomeCount = nBackHomeCount + 1
        if nBackHomeCount < 2:
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

# return True if in special status
def checkStatus():
    if regionStatus.exists("1513870172508.png", 0.2):
        recoverPoison()
        return True
    if regionStatus.exists("1513870381521.png", 0.2):
        Debug.user("You have become a stone.....")
        return True
    if regionStatus.exists("1513955946438.png", 0.2):
        Debug.user("You are stunned.....")
        return True
    return False
    
def recoverMp():
    Debug.user("Use MP recover skill")
    type(keyMpRecover)
    sleep(1.7)
    
def recoverHp():
    Debug.user("Use HP recover skill")
    type(keyHpRecover)
    sleep(0.6)

def recoverPoison():
    Debug.user("Use rescue poison skill")
    type(keyPoisonRescue)
    sleep(0.6)

def drinkWater():
    Debug.user("Drink water!")
    type(keyHpWater)
    
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
        if not regionSkill.exists("1513525529844.png", 0.1):
            Debug.user("This skill doesn't support 'auto'")
            return
    else:
        if not regionSkill.exists("1513524888200.png", 0.1):
            Debug.user("no 'auto'")
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

def login():
    imageWaitForLogin = "imageWaitForLogin.png"
    imageLoginButton = "imageLoginButton.png"
    
    if Region(753,689,393,120).waitVanish(imageWaitForLogin):
        sleep(5)
        click(imageLoginButton)

bringGameToFront()
while True:
    #checkBufferStatus()
    previousTime = time.time()
    checkHp()
    if time.time()-previousTime > 4:
        Debug.user("pause a while, need to bring game to front")
        bringGameToFront()

    sleep(0.3)
