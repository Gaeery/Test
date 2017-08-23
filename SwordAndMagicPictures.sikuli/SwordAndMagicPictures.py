from sikuli import *
imageTaskBoard = "imageTaskBoard.png"
imageMissionTabs1 = [ Pattern("1503324924500.png").similar(0.60), Pattern("1503324978946.png").similar(0.55) ]
imageMissionTabs2 = [ "1503325095445.png", "1503325058113.png" ]

target1 = "target1.png"
target2 = "target2.png"

gameRegion = Region(0,0,587,1024)


imageEvpEvent = [  Pattern("1503324924500.png").similar(0.60), "1503325058113.png", "target1.png", "1503505788578.png" ]

imageMissions = []