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

nRecoverHpThreshold = 80
nRecoverMpThreshold = 80
nDrinkWaterThreshold = 50
nBackToTownThreshold = 30

nBackHomeCountdownTimes = 2

bUseFightingSkill = True
keyTripleArrow = Key.F7
nMinMpPercentTripleArrow = 80
nIntervalTripleArrow = 6


# stay in a region
nIntervalCheckStayInterval = -1    # -1: disabled
#nIntervalCheckStayInterval = 8    # practice 4th floor
stayRegions = ["1514584075718.png", "1514584135275.png","1514584152621.png", "1514674804123.png"]   # practice 4th floor
locMoveToStayRegion = Location(353, 486)

# check and receive mail  
nIntervalCheckMailInterval = 60   #-1: disabled