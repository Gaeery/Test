
from sikuli import *
import ControlLib
from ControlLib import *

gameRegion = Region(0,0,587,1024)
#imageTaskBoard = "imageTaskBoard.png"  #normal
imageTaskBoard = Pattern("1515601825642.png").similar(0.96)
locationIronMonster = Location(112, 555)
locationFirstOriginalStone = Location(174, 431)
locationSecondOriginalStone = Location(508, 240)
locationDarkBoss = Location(384, 419)
locationLightBoss = Location(172, 434)
locationFireBoss = Location(495, 438)
locationWindBoss = Location(50, 387)
locationDustBoss = Location(208, 400)
locationWaterBoss = Location(103, 399)
locationSpecialPoints = Location(191, 426)
locationTank = Location(390, 289)
locationAngel = Location(476, 551)
locationAssassin = Location(166, 472)
locationGiant = Location(539, 341)
locationLif = Location(337, 631)



gameRegion2 = Region(587,0,566,1029)
escapeRegion = Region(400,932,166,93)
monsterRegion_Normal = Region(0,369,554,351)
monsterRegion_Small = Region(167,336,239,249)
monsterRegion_Left = Region(4,382,344,345)
monsterRegion_Up = Region(4,220,550,361)
monsterRegion_Full = Region(3,206,554,611)


imageMissionClosed = "te-1.png"
class PageId():
    def getPageImage( i ):
        return imagePages[i][1]
    
    enumPageId_unknown = -1
    enumPageId_mission = 0
    enumPageId_fighting = 1
    enumPageId_again = 2
    enumPageId_board = 3 #board
    enumPageId_close = 4
    enumPageId_selectingTask = 5
    enumPageId_openGift = 6
    enumPageId_missionClosed = 7
    enumPageId_skip = 8

    escapeRegion = Region(400,932,166,93)
    missionTimerRegion = Region(438,23,110,78)
    imagePages = [
            [escapeRegion, "1497776017507-2.png", enumPageId_fighting, "Page: Fighting" ],
            [escapeRegion, "1498270581243.png", enumPageId_fighting, "Page: Fighting (can't escape)" ],
            [gameRegion, "imageClose.png", enumPageId_close, "Page: close something"],
            [missionTimerRegion, Pattern("1499210289316.png").similar(0.80), enumPageId_mission, "Page: In a mission"],
            [gameRegion, "imageAgain.png", enumPageId_again, "Page: again"],
            [gameRegion, imageTaskBoard, enumPageId_board, "Page: task board"],
 
            [gameRegion, "imagePageSelectingTask.png", enumPageId_selectingTask, "Page: Selecting a task"],
            [gameRegion, "imagePageOpenGift.png", enumPageId_openGift, "Page: open gift"],
            [gameRegion, "1503677033007.png", enumPageId_missionClosed, "Page: imageMissionClosed"],
            [gameRegion, "1507194420421.png", enumPageId_skip, "Page: skip"]
        ]
        #enumPageId_mission = 0
        #enumPageId_again = 2
        #enumPageId_board = 3
        #enumPageId_close = 4
        #enumPageId_selectingTask = 5
        #enumPageId_openGift = 6 


imageMissionTab22 =  "1503325058113.png"
imageMissionTabs1 = [ Pattern("1503324924500.png").similar(0.60), Pattern("1503324978946.png").similar(0.51) ]
imageMissionTabs2 = [ "1503325095445.png", imageMissionTab22 ]

target1 = "target1.png"
target2 = "target2.png"


imageEvpEvent = [ imageMissionTabs1[1], imageMissionTabs2[1], "1505315719283.png", "1505315749946.png" ]
imageEvpEventWind = [ imageMissionTabs1[0], imageMissionTabs2[1], "1508342146553.png", "1508342154667.png"]
imageEvpEventDust = [ imageMissionTabs1[0], imageMissionTabs2[1], "1505924940340.png", "1505924953174.png" ]
imageEvpEventFire = [ imageMissionTabs1[0], imageMissionTabs2[1], "1507117532032.png", "1507124347810.png" ]

imageEvpTask = [ imageMissionTabs1[0], imageMissionTabs2[1],  "1512579269469.png", "1512579277996.png" ]
imageEvpPumpkin =  [ imageMissionTabs1[0], imageMissionTabs2[1], "1510836807935.png", "1510836861266.png" ]
imageEvpMonster = [ imageMissionTabs1[1], imageMissionTabs2[1], "1515368892874.png", "1515368916449.png"  ]
imageEvpCrab = [ imageMissionTabs1[1], imageMissionTabs2[1], "1515628116808.png", "1515628171242.png"  ]

imageSpecialMission = [ 
        imageMissionTabs1[0],
        imageMissionTabs2[1], 
        "1515431543087.png", 
        "1515431556157.png"
         ]

imageArmorMission = [ 
        imageMissionTabs1[1],
        imageMissionTabs2[0], 
        "1503507033623.png", 
         ]


imageMissions = []


imagesOffset_angleArmor =  [
                ImageOffset("1503967548244.png", 0, 10),
                ImageOffset("1503964578839.png", 0, 30),
                ImageOffset("1503964608384.png", 0, 20),
                ImageOffset("1503967522152.png", 0, 20),
                ImageOffset("1503964713241.png", 0, 20),
                ImageOffset(Pattern("1503966310928.png").similar(0.80), 75, 150),
                ImageOffset(Pattern("1504059658229.png").similar(0.80), 75, 150),
                ImageOffset(Pattern("1503964134166.png").similar(0.80), -150, 180),
                ImageOffset(Pattern("1503962423217.png").similar(0.80), 30, 50),
                ImageOffset("1504047503481.png", 10, 100),
                 ImageOffset(Pattern("1503963003921.png").similar(0.80), -400, 260),
                ImageOffset(Pattern("1503963735748.png").similar(0.80), -450, 320),      
                ] 
imagesOffset_AssassinArmor = [
                ImageOffset("1503967548244.png", 0, 10),  
                ImageOffset("1505232436315.png", 0, 10),  
                ] 


imagesOffset = []


enumPageIdMissionEnd = "enumPageMissionClose.png"