from sikuli import *

keyHpWater = Key.F1
keyHpRecover = Key.F2
keyMpRecover = Key.F3
keyGoToTown = Key.F4
keyPoisonRescue = Key.F5

keyTransport = Key.F8  #run away
keyPracticeTask = Key.F9

keyPickup = "g"

locPartyPage = Location(228, 270)
locCreateParty = Location(96, 377)
locCreatePartyConfirm = Location(1071, 850)



bUseFightingSkill = True
keyTripleArrow = Key.F7
nMinMpPercentTripleArrow = 60
nIntervalTripleArrow = 4


# stay in a region
nIntervalCheckStayInterval = -1    # -1: disabled
stayRegions = ["1514584075718.png", "1514584135275.png","1514584152621.png"]
locMoveToStayRegion = Location(353, 486)

# check and receive mail  
nIntervalCheckMailInterval = 60   #-1: disabled