import random
import SwordAndMagicPictures
reload(SwordAndMagicPictures)  # make sure global variables are reloaded
import ControlLib
from SwordAndMagicPictures import *
from ControlLib import *
import SwordAndMagicActions
from SwordAndMagicActions import *
reload(SwordAndMagicActions) 

pHpWater = Location(802, 922)
#bufferImages = "bufferRegion.png"
bufferRegion =  Region(145,155,466,40)


imageNoHp = Pattern("imageHasHp.png").similar(0.74)
imageHp50p = Pattern("imageHp50p.png").similar(0.61)
imageHp50Region = Region(149,56,287,26)

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
        #BufferStatus("精靈餅乾", "1513000438389.png", [Pattern("1513012091917.png").similar(0.95), Pattern("1513012115279.png").similar(0.95), Pattern("1513012153809.png").similar(0.95), "1513012783396.png", "1513012843741.png"]),
        #BufferStatus("食物", Pattern("1513000766333.png").similar(0.59), [Pattern("1513012091917.png").similar(0.95), Pattern("1513012115279.png").similar(0.95), "1513053707716.png", "1513053720833.png" , "1513012843741.png"]),
        #BufferStatus("保護罩", Pattern("1513000826312.png").similar(0.67), ["1513012904938.png", "1513012930638.png", "1513012940942.png", "1513012843741.png"]),
        #BufferStatus("鎧甲護持", Pattern("1513000907139.png").similar(0.69), ["1513012904938.png","1513013125930.png","1513013138966.png", "1513012843741.png"]),
        #BufferStatus("負重強化", Pattern("1513000932286.png").similar(0.65), ["1513012904938.png","1513013030782.png","1513013041431.png", "1513012843741.png"]),
        #BufferStatus("變身", Pattern("1513001027215.png").similar(0.68)),
        #BufferStatus("強化戰鬥卷軸", Pattern("1513001000565.png").similar(0.59)),
        #BufferStatus("自我加速藥水", Pattern("1513004774208.png").similar(0.72), [Pattern("1513012091917.png").similar(0.95), Pattern("1513012115279.png").similar(0.95), "1513033719938.png", "1513033735138.png", "1513012843741.png"]),
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
                
def checkHp():
    global nBackHomeCount
    if imageHp50Region.exists(imageNoHp, 0):
        Debug.user("Hp is lower than 70")
        click(pHpWater)
        nBackHomeCount = 0
    elif imageHp50Region.exists(imageHp50p, 0):
        Debug.user("Hp is lower than 50")
        click(pHpWater)
        nBackHomeCount = nBackHomeCount + 1
        if nBackHomeCount > 5:
            click(Location(1736, 915))
            exit
    else:
        Debug.user("Hp is OK")

regionHp = Region(715,352,457,155)
imageHp80 = Pattern("imageHp70.png").similar(0.80)
imageHp70 = "imageHp50.png"
imageHp60 = Pattern("imageHp30.png").similar(0.60)
def checkHp2():
    global nBackHomeCount
    if regionHp.exists(imageHp80, 1):
        Debug.user("Hp is OK")
        nBackHomeCount = 0
    elif regionHp.exists(imageHp70, 1):
        Debug.user("Hp is 50~70")
        useSelfRecover()
        nBackHomeCount = 0
    elif regionHp.exists(imageHp60, 1):
        Debug.user("Hp is 30~50")
        click(pHpWater)        
        useSelfRecover()
        nBackHomeCount = 0
    else:
        Debug.user("Hp is lower than 50")
        nBackHomeCount = nBackHomeCount + 1
        if nBackHomeCount < 3:
            return
        
        Debug.user("return to town!!")
        screenCapture("before return.png")
        click(Location(1736, 915))
        exit(1)

def useSelfRecover():
    lib = GaeeryLib()
    lib.setROI(Region(751,869,1038,104))
    imageSelfRecover = Pattern("imageSelfRecover.png").exact()
    imageRecover = "imageRecover.png"
    skill = lib.find( "find self recover skill", imageSelfRecover )
    if skill == None:
        click(Location(1533, 597))
        sleep(0.5)
    lib.clickImage( "use skill to rescue self", imageSelfRecover)


while True:
    #checkBufferStatus()
    checkHp2()
    sleep(0.3)
