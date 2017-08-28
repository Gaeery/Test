
from sikuli import *

gameRegion = Region(0,0,587,1024)
imageTaskBoard = "imageTaskBoard.png"

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
            [gameRegion, "1503677033007.png", enumPageId_missionClosed, "Page: imageMissionClosed"]
        ]
        #enumPageId_mission = 0
        #enumPageId_again = 2
        #enumPageId_board = 3
        #enumPageId_close = 4
        #enumPageId_selectingTask = 5
        #enumPageId_openGift = 6 


imageMissionTab22 =  "1503325058113.png"
imageMissionTabs1 = [ Pattern("1503324924500.png").similar(0.60), Pattern("1503324978946.png").similar(0.55) ]
imageMissionTabs2 = [ "1503325095445.png", imageMissionTab22 ]

target1 = "target1.png"
target2 = "target2.png"


imageEvpEvent = [  Pattern("1503324924500.png").similar(0.60), "1503325058113.png", "target1.png", "1503505788578.png" ]
imageArmorMission = [ 
        imageMissionTabs1[1],
        imageMissionTabs2[0], 
        "1503507033623.png", "1503507047702.png" ]
imageMissions = []



enumPageIdMissionEnd = "enumPageMissionClose.png"