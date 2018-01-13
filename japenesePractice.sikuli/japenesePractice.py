import random
import ControlLib
from ControlLib import *
reload(ControlLib)  # make sure global variables are reloaded
import SwordAndMagicPictures
reload(SwordAndMagicPictures)  # make sure global variables are reloaded
from SwordAndMagicPictures import *
import SwordAndMagicActions
from SwordAndMagicActions import *
reload(SwordAndMagicActions) 

enumPractice = 1
enumStoneMission = 2
enumFixLocation = 3
enumFixLocationTwice = 20
enumFixLocationDropExp = 15
enumFixLocationOtherServer = 4
enumFixLocationSkip= 11
enumMoveThanFind = 5  #special first
enumMoveThanFindLeft = 18
enumIronMonster = 6
enumAudoFindMonster = 7
enumMoveALittle = 8 
enumMoveALittleAndFindFighting = 13  #兔子
enumEVP = 9
enumEVP_branch = 14
enumAutoSkill = 10
enumArmorAngle = 16
enumArmorAssassin = 18
enumArmorMele = 19
enumArmorWeekend = 17
enumImageOffset = 21
#-------------
enumType = enumMoveALittleAndFindFighting
#enumType = enumMoveThanFind
#enumType = enumImageOffset
enumTypeNext = enumImageOffset

locationFixedMoveInMission =  Location(358, 462)
locationFixedMoveInMission2 = Location(513, 443)
        
# 技能使用
#autoKills = [5,0,1,2,3,4,2,3,4,2,3,4]  #一般
#autoKills = [2,3,1,5,0,4]  #土亡命
#autoKills = [1,2,5,0,3,4]  #光單
#autoKills = [3,1,2,5,0,3,4]  #光單

autoKills = [1,4,3,2,5,0,2]  #火範圍

#靈刀 
#autoKills = [0,1,2,3,4,5,3,4,-1,3,4,2,3,4,3,4,1,2,3,4,5,3,4,2,3,4,3,4,3,4,1,2,3,4,5,3,4,2,3,4,3,4,1,2,3,4,5,3,4,3,4,2,3,4,5,3,4,1,2,3,4,3,4]  


autoKills = [0,1,2,3, -5, 4]  #風補
#autoKills = [0,1,2,0,1,3,4,0,1,0,1,2,0,1,4,0,1,3,0,1,2,0,1,4,0,1,3]  #暗殺(雙獄鬼)
#autoKills = [0,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4]  #土單 (霸劍
#autoKills = [0,1,5,4,-1,3,4,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]  #土單EVP
#autoKills = [0,1,2,4,3,5,1,2,4,3,5]  #土單 (霸劍+血少
#autoKills = [1,0,2,3,5,1,3,-1,4,0,2,1,3,-1,4]  #土單 (無霸劍
#autoKills = [0,1,2,3,5,4, 0,4,1,3,5,2,4,0,3,1,5,4,2,3,0,4]  #光evp
#autoKills = [0,2,3,1,0,3,1]
#autoKills = [0, 3, 1, 2, -3, 4]  #光坦
#autoKills = [3, 1, 2, 0, 4, -7, 5, -7]  #水坦
#autoKills = [4,3, 1, 0, 2, -3, 4, -8, 5, -8]  #坦2
autoKills = [2,0,1,3,2,2,1]
#autoKills = [3,5,0,2,1]  
#autoKills = [0, -5, 1, -5, 2]  # 1~3 poison

# move if bMoveOnceInMission
bMoveOnceInMission = False

nMoveDelay = 5
# move if bMoveTwiceInMission
#locationFixedMoveInMission2 = locationWindBoss
nMoveDelay2 = 1
bMoveToFighting = True
# GPS buffer [ imageDoubleExp, imageDropIncrease, imageSpecialMonsterIncrease ] 
bUseGPS = True

bNeedToEnterEvpRoom = False



fireMonster = "imageMonster-2.png"
windMonster = "windMonster-1.png"
soilMonster = "soilMonster.png"
waterMonster = "waterMonster.png"
ironMonster = "1498839906365.png"
darkMonster = "darkMonster.png"
#goldenMonster = 
imageOtherFighting_ = "imageOtherFighting.png"
imageFightings = [ Pattern("1507897726703.png").similar(0.90), Pattern("imageOtherFighting.png").similar(0.85), Pattern("imageOtherFighting2.png").similar(0.90), Pattern("imageOtherFighting3.png").similar(0.75), Pattern("1503100614536.png").similar(0.75), Pattern("1503101128026.png").similar(0.75), Pattern("1503101630080.png").similar(0.75), "1503121487310.png", Pattern("1508031407013.png").similar(0.66), "1515246341319.png" ]


imageDoubleExp = "imageDoubleExp.png"
imageDropIncrease = "imageDropIncrease.png"
imageSpecialMonsterIncrease = "imageSpecialMonsterIncrease.png"

#after fight
imageAgain = "imageAgain.png"
#after getted gift
imageAgain2 = "imageAgain.png"

imageNextPage = Pattern("1499126342274.png").similar(0.98)

imageNextPage1 = Pattern("imageNextPage1.png").similar(0.97)
imageNextPage2 = imageNextPage1
imageNextPage22 = Pattern("1499986887004.png").similar(0.97)

imageNextPage3 = "imageNextPage3.png"
imageOpenGift = "imageOpenGift.png"
imageAgree = Pattern("imageAgree.png").similar(0.98)
imageGo = "imageGo.png"

imageFriendMenu = "imageFriendMenu.png"
imagePageSelectingTask = "imagePageSelectingTask.png"
imagePageOpenGift = "imagePageOpenGift.png"
imageConsole = "imageConsole.png"


monsterRegion = monsterRegion_Full


locationMonster = Location(84, 557)



locationDown = Location(280, 535)
locationUp = Location(280, 515)
nDelayBeforeUsingSkill = 0

Settings.MoveMouseDelay = 0.1
# ======== default值, 不要改這邊 =========
# 自己找怪撞
bFindMonsterBySelf = False
# 找任務目標的紅色箭頭
bFindTargetInMission = False
# 找有人嘁王 (disposed)
bBossMonsterFirst = False
# 先找Boss的圖
bMoveToBoss = False
imageBoss = [ "1502752920469.png" ]
# 怪的圖
imageMonsters = [ "1500760227483.png", "1500760266200.png" ]

#need to move a step in mission
#locationFixedMoveInMission = locationAssassin
#need to move second step in mission
bMoveTwiceInMission = False
#locationFixedMoveInMission2 = Location(335, 489)
# 是否要移到別人的戰鬥中


# 開禮物, True適用與各情況, False比較快
bNeedOpenGift = True

imageBonus1 = imageSpecialMonsterIncrease
imageBonus2 = imageDropIncrease

# 需要選人少的分流?
bNeedUseOtherBranchServer = False
# 戰鬥後, 位移一點
bMoveALittleAfterFight = False

# let second character fly to join
bSecondCharacterFlyToJoin = False
bCanEscap = True
nCheckFightingTimes = 1
bNeedTransfer = False
imageMissions = []
bNeedSayThanks = False


# ======== 需換的部分 ===============================================================

#imageMonster = locationWindBoss


#優先高的放後面, 或第一個
#autoKills = [3,5,4,0,2,1]
#autoKills = [2,5,0,1,3,4]
#autoKills = [0,1,2,3,4]
monsterPositions = [Location(439, 328), 
        Location(364, 651),   #泳裝1F
        Location(366, 682),  #舊寶石任
        Location(369, 612), 
        Location(460, 603),  #光試煉小怪
        #Location(379, 504), #light boss
        #Location(337, 514), #wind boss
        #Location(442, 530), #mud practice
        Location(463, 558), #地瓜頂
        Location(369, 502), #protector
        Location(385, 456),  #新寶石任, 生命氣息
        Location(399, 557), #泳裝
        Location(438, 450), #EVP, 洗腦
        Location(443, 539), #火小怪
        #Location(457, 603),
        Location(279, 671),
        Location(289, 514),
        Location(302, 372),
        Location(379, 522)
        ] 
# click skip before mission
bNeedSkip = False
# click skip after mission
bSkipBeforeAgain = False

bNeedAgree = True

# maximun time to stay in a mission.  (0: disable)
nMaximunMissionStayTime = 0
#if reach maximun time, change imagesOffset to imagesOffset_endMission
imagesOffset_endMission = []


nEnterMissionTime = time.time()





def refreshSetting():
    Debug.user('refresh setting, enumType= %d' % enumType)
    global imageMissions
    global  bMoveOnceInMission
    global  bFindTargetInMission 
    # 試煉/積分 True, 原石 False
    global  bNeedAgree 
    global  imageMonster 
    # 寶石任務 False
    global  bNeedOpenGift
    global  bUseGPS
    global imageBonus1 
    global imageBonus2
    global autoKills 

    
    # 先找Boss的圖
    global bMoveToBoss
    global imageBoss 
    
    global bFindMonsterBySelf
    global imageMonsters 
    global bMoveToFighting
    global monsterRegion
    global bNeedUseOtherBranchServer 
    global bMoveALittleAfterFight
    global autoKills 
    global bMoveOnceInMission 
    global locationFixedMoveInMission 
    global bMoveTwiceInMission 
    global locationFixedMoveInMission2 
    global bUseGPS 
    global nDelayBeforeUsingSkill 
    global bNeedTransfer 
    global bNeedToEnterEvpRoom
    global imagesOffset
    global imagesOffset_endMission
    global nMaximunMissionStayTime
    global enumType
    global bNeedSayThanks
    global monsterPositions
    global bNeedSkip
    global nMoveDelay
    bNeedSayThanks = False
    
    if enumType==enumPractice:
        #autoKills = [0,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4]  #土單 (霸劍
        # True   False
        #only move once
        bMoveOnceInMission = False
        locationFixedMoveInMission = Location(278, 400)
        bFindTargetInMission = False
        # 試煉/積分 True, 原石 False
        bNeedAgree = True
        imageMonster = darkMonster
        # 寶石任務 False
        bNeedOpenGift = True
        bUseGPS = True
        imageBonus1 = imageDropIncrease 
        imageBonus2 = imageSpecialMonsterIncrease
        #autoKills = [1,2,3,4,5]  #12345
        bNeedSayThanks = True
    elif enumType==enumStoneMission:
        bFindMonsterBySelf = True
        imagesOffset = [
                ImageOffset( "1512648310904.png", 0, 190),            
                ImageOffset( "1512648362171.png", 0, -230),  
                ImageOffset( "1515212634098.png", 40, 220),  
                ImageOffset( "1515329896146.png", 200, 15),  
        ] 
        bMoveToFighting = False
        monsterRegion = Region(0,89,560,860)
        #monsterRegion = monsterRegion_Up
        bNeedUseOtherBranchServer = False
        bNeedSkip = False
        bSkipBeforeAgain = False
        #autoKills = [0,1,2,3,4,5,-1]
        #autoKills = [5,5,1,3,0,2,0,2,4,]
        #autoKills = [3, 1, 0, 2, -3, 4, -9, 5, -9]  #坦
        #autoKills = [1,0,2,3,5,1,3,-1,4,0,2,1,3,-1,4]  #土單 (無霸劍
        #autoKills = [0,1,2,3,5,4, 0,4,1,3,5,2,4,0,3,1,5,4,2,3,0,4]  #光evp
        #autoKills = [0,1,2,3,4,5, 1,2,3,4, 1,2,3,4,5, 1,2,3,4, 1,2,3,4,5, 1,2,3,4, 1,2,3,4,5, 1,2,3,4]  #土單 
        #autoKills = [0,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4]  #土單 (霸劍
        #autoKills = [1,2,0,0]   #範圍PK
        #autoKills = [1,0,2,3,4,2,3,4] #單體PK
        #autoKills = [0,2,5,1,4,2,3,4,1,4,2,3,4,1,4]
        #autoKills = [0,1,2,3,4,5,3,4,-1,3,4,1,2,3,4,5,3,4,1,2,3,4,5,3,4]  #靈刀 
        bMoveOnceInMission = False
        #locationFixedMoveInMission = Location(357, 464)
        #locationFixedMoveInMission = Location(205, 520)
        locationFixedMoveInMission = Location(414, 449)   # godness
        bMoveTwiceInMission = False
        #locationFixedMoveInMission2 = Location(355, 742)
        nDelayBeforeUsingSkill = 0
        #monsterRegion = monsterRegion_Small
        bNeedTransfer = False
        bMoveALittleAfterFight = True
        bUseGPS = False
        imageBonus1 = imageDropIncrease
        imageBonus2 = imageDoubleExp
        bNeedSayThanks = False
    elif enumType==enumFixLocation:
        bNeedUseOtherBranchServer = False
        # True   False
        #only move once
        bMoveOnceInMission = True 
        bFindTargetInMission = False  
        # 試煉/積分 True, 原石 False  
        bNeedAgree = True
        # 寶石任務 False 
        bNeedOpenGift = True  
        # click skip before mission 
        bNeedSkip = True 
        # click skip after mission    
        bSkipBeforeAgain = True
    elif enumType==enumFixLocationTwice:  
        bNeedUseOtherBranchServer = True  
        # True   False
        #only move once
        bMoveOnceInMission = True
        bMoveTwiceInMission = True
        bFindTargetInMission = False  
        # 試煉/積分 True, 原石 False 
        #bNeedAgree = True 
        # 寶石任務 False 
        bNeedOpenGift = True 
        # click skip before mission  
        bNeedSkip = False   
        # click skip after mission 
        bSkipBeforeAgain = True    
        bMoveToFighting = True
    elif enumType==enumFixLocationDropExp:    
        # True   False 
        bUseGPS = True 
        imageBonus1 = imageDropIncrease   
        imageBonus2 = imageDoubleExp
        #only move once
        bMoveOnceInMission = True
        bFindTargetInMission = False
        bMoveToFighting = True 
        # 試煉/積分 True, 原石 False
        bNeedAgree = True   
        # 寶石任務 False 
        bNeedOpenGift = True 
        # click skip before mission
        bNeedSkip = False
        # click skip after mission
        bSkipBeforeAgain = False
    elif enumType==enumFixLocationSkip:    
        monsterRegion = monsterRegion_Left
        bMoveOnceInMission = True
        bNeedAgree = True
        # 寶石任務 False
        #bNeedOpenGift = True 
        #bNeedSkip = True
        bSkipBeforeAgain = False
    elif enumType==enumFixLocationOtherServer:
        #only move once
        bMoveOnceInMission = True
        bFindTargetInMission = False
        # 試煉/積分 True, 原石 False
        bNeedAgree = True
        # 寶石任務 False 
        bNeedOpenGift = True
        # click skip before mission
        bNeedSkip = False
        # click skip after mission
        bSkipBeforeAgain = False
        bNeedUseOtherBranchServer = True
        # let second character fly to join
        bSecondCharacterFlyToJoin = False
    elif enumType==enumMoveThanFind:
        # True   False
        #only move once
        bMoveOnceInMission = True
        #locationFixedMoveInMission = Location(295, 374) #光
        #locationFixedMoveInMission = Location(5, 526)
        bFindTargetInMission = False
        # 試煉/積分 True, 原石 False
        bNeedAgree = False
        imageBonus1 = imageSpecialMonsterIncrease
        imageBonus2 = imageDropIncrease

        
    elif enumType==enumMoveThanFindLeft:
        # True   False
        #only move once
        bMoveOnceInMission = True
        locationFixedMoveInMission = Location(267, 628)
        bFindTargetInMission = False
        # 試煉/積分 True, 原石 False
        bNeedAgree = True
        imageBonus1 = imageSpecialMonsterIncrease
        imageBonus2 = imageDropIncrease
        #monsterRegion = monsterRegion_Left 
    elif enumType==enumIronMonster:
        # True   False
        #only move once
        bMoveOnceInMission = True
        locationFixedMoveInMission = locationIronMonster
        bFindTargetInMission = False
        # 試煉/積分 True, 原石 False
        bNeedAgree = True
        # 寶石任務 False
        bNeedOpenGift = True
        imageMonster = ironMonster
        bUseGPS = False
        imageBonus1 = imageDoubleExp
        imageBonus2 = imageDropIncrease  
    elif enumType==enumMoveALittle:
        # 自己找怪撞
        bFindMonsterBySelf = False
        bMoveToFighting = False
        imageMonsters = [ "1500760227483.png", "1500760266200.png" ]
        bNeedUseOtherBranchServer = False
        bMoveToFighting = False
        bMoveALittleAfterFight = True
        nDelayBeforeUsingSkill = 0
        #monsterRegion = Region(166,391,229,191)
        # let second character fly to join
        #bSecondCharacterFlyToJoin = True
        #bSkipBeforeAgain = True
    elif enumType == enumMoveALittleAndFindFighting:
        bMoveOnceInMission = False
        locationFixedMoveInMission = Location(321, 264)
        # 自己找怪撞
        bFindMonsterBySelf = False
        bMoveToFighting = True
        bNeedUseOtherBranchServer = False
        bMoveALittleAfterFight = True
        monsterRegion = monsterRegion_Small
        imageBonus1 = imageDoubleExp
        imageBonus2 = imageDropIncrease  
        #autoKills = [5,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
    elif enumType==enumAudoFindMonster: 
        bMoveOnceInMission = True
        locationFixedMoveInMission = Location(12, 193)
        bMoveTwiceInMission = False
        locationFixedMoveInMission2 = Location(551, 477)
        bMoveALittleAfterFight = False
        
        # 自己找怪撞
        bFindMonsterBySelf = True
        bMoveToFighting = False
        imageMonsters = [ "1512041728979.png","1512041737652.png"                                              ]
        bNeedUseOtherBranchServer = True

        monsterRegion = monsterRegion_Full
        # let second character fly to join
        #bSecondCharacterFlyToJoin = True
        bNeedSkip = True
        autoKills = [1,2,0]
        bNeedUseOtherBranchServer = False
        bMoveALittleAfterFight = True
    elif enumType==enumEVP:
        imageMissions = imageEvpCrab
        bNeedToEnterEvpRoom = False
        
        bFindMonsterBySelf = False
        imageMonsters = [  ]
        imagesOffset = [
                ImageOffset("1515431713946.png", -3, -10),  
                ImageOffset("1515431741504.png", 0, 0),  
                ] 
        # maximun time to stay in a mission
        nMaximunMissionStayTime = 60
        #if reach maximun time, change imagesOffset to imagesOffset_endMission
        imagesOffset_endMission = [
                ImageOffset("1515456372044.png", 0, 0), 
                ImageOffset("1515456342067.png", 0, 0), 
                ImageOffset("1515456410781.png", 0, 0), 
                ImageOffset("1515456424941.png", 0, 0), 
                ImageOffset("1515456446359.png", 0, 0), 
                ImageOffset("1515455039689.png", 263, -32),  
                ImageOffset("1515455198724.png", 71, -7), 

                ]
        
        
        bMoveToFighting = True
        #monsterRegion = Region(69,407,385,248)
        #monsterRegion = monsterRegion_Up
        bNeedUseOtherBranchServer = False
        bNeedSkip = False
        bSkipBeforeAgain = False
        #autoKills = [0,1,2,3,4,5]
        #autoKills = [5,5,1,3,0,2,0,2,4,]
        autoKills = [4, 0, 1, 2, 3, 5, -5,  4, 0, 1, 2, 3, -5]  #坦
        #autoKills = [1,0,2,3,5,1,3,-1,4,0,2,1,3,-1,4]  #土單 (無霸劍
        #autoKills = [0,1,2,3,5,4, 0,4,1,3,5,2,4,0,3,1,5,4,2,3,0,4]  #光evp
        #autoKills = [0,1,2,3,4,5, 1,2,3,4, 1,2,3,4,5, 1,2,3,4, 1,2,3,4,5, 1,2,3,4, 1,2,3,4,5, 1,2,3,4]  #土單 
        #靈刀 
        #autoKills = [0,1,2,3,4,5,3,4,-1,3,4,1,2,3,4,3,4,1,2,3,4,5,3,4,1,2,3,4,3,4,3,4,1,2,3,4,5,3,4,1,2,3,4,3,4,1,2,3,4,5,3,4,3,4,1,2,3,4,5,3,4,1,2,3,4,3,4]  

        bMoveOnceInMission = True
        locationFixedMoveInMission = Location(243, 449)
        #locationFixedMoveInMission = Location(205, 520)
        bMoveTwiceInMission = False
        locationFixedMoveInMission2 = Location(355, 742)
        nDelayBeforeUsingSkill = 0
        #monsterRegion = monsterRegion_Small
        bNeedTransfer = False
        bMoveALittleAfterFight = False
        bUseGPS =False
        imageBonus1 = imageDropIncrease
        imageBonus2 = imageDoubleExp
        bNeedSayThanks = False
        nMoveDelay = 1
    elif enumType==enumEVP_branch:
        imageMissions = imageEvpEventWind
        bNeedToEnterEvpRoom = True
        
        bFindMonsterBySelf = False
        imageMonsters = [ "1506530623339.png" ]
        bMoveToFighting = False
        #monsterRegion = monsterRegion_Normal
        monsterRegion = monsterRegion_Small
        bNeedUseOtherBranchServer = True
        bMoveALittleAfterFight = False
        # let second character fly to join
        bSecondCharacterFlyToJoin = False
        bNeedSkip = False
        bSkipBeforeAgain = False
        #autoKills = [0,1,2,3,4,5]
        #autoKills = [2,3,1,5,0,2,4,2,2,3,3,1,2,3,1,4,4,5,1]  #坦
        #autoKills = [3,1,2,5,0,3,4]  #光單
        #autoKills = [0,1,2,5,4,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4]  #土單 血多一點
        #autoKills = [0,1,5,4,-1,3,4,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]  #土單 血少的怪
        #autoKills = [0,1,2,3,5,4, 0,4,1,3,5,2,4,0,3,1,5,4,2,3,0,4]  #光evp
        autoKills = [4,3,2,5,0,2,1]  #火範圍
        #靈刀 
        #autoKills = [0,1,5,3,4,5,3,4,-1,3,4,1,2,3,4,3,4,1,2,3,4,5,3,4,1,2,3,4,3,4,3,4,1,2,3,4,5,3,4,1,2,3,4,3,4,1,2,3,4,5,3,4,3,4,1,2,3,4,5,3,4,1,2,3,4,3,4]  

        bMoveOnceInMission = False
        locationFixedMoveInMission = Location(450, 391)
        bMoveTwiceInMission = False
        locationFixedMoveInMission2 = Location(369, 586)
        bUseGPS =False
        nDelayBeforeUsingSkill = 0
        bNeedTransfer = False

    elif enumType==enumAutoSkill:
        #autoKills = [0,1,2,3,4,5]
        #autoKills = [0,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4]  #土單 (霸劍
        bCanEscap = False
        nCheckFightingTimes = 4
    elif enumType==enumArmorAngle:
        imageMissions = imageArmorMission
    
        # 先找Boss的圖
        bMoveToBoss = True
        imageBoss = [ "1503320329329.png", "1503964977321.png", "1503965001575.png", "1503965024324.png" ]
        #imageBoss = [ "1503320329329.png", "1502752920469.png" ]
        
        bFindMonsterBySelf = True
        imageMonsters = [ ]

        imagesOffset = imagesOffset_angleArmor
        imageMonsters = []
        bMoveToFighting = False
        monsterRegion = monsterRegion_Full
        bNeedUseOtherBranchServer = True
        bMoveALittleAfterFight = False
        #autoKills = [0,1,2,3,4,5]  #12345
        autoKills = [0,1,5,4,-1,3,4,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]  #土單 血少的怪
        bMoveOnceInMission = False
        locationFixedMoveInMission = Location(29, 543)
        bMoveTwiceInMission = False
        locationFixedMoveInMission2 = Location(131, 645)
        bUseGPS =False
        nDelayBeforeUsingSkill = 0
        bNeedTransfer = True
    elif enumType==enumArmorWeekend:
        imageMissions =  [
            imageMissionTabs1[1],
            imageMissionTabs2[1], 
            "1506126880383.png", "1506127026448.png" ]

    
        # 先找Boss的圖
        bMoveToBoss = True
        #imageBoss = [ "1503320329329.png", "1503964977321.png", "1503965001575.png", "1503965024324.png" ]
        imageBoss = ["1503320329329.png", "1506127773060.png"]
        
        bFindMonsterBySelf = True
        #imageMonsters = [ "1504283821899.png", "1504283837684.png", "1504283849770.png" ]
        imageMonsters = ["1506127255039.png", "1506127311313.png","1506127326969.png", "1506127339509.png"]

        #imagesOffset = imagesOffset_angleArmor
        imagesOffset = []
        bMoveToFighting = False
        monsterRegion = monsterRegion_Full
        bNeedUseOtherBranchServer = True
        bMoveALittleAfterFight = True
        #autoKills = [1,5,2,3,4,2,3,4,2,3,4]  #12345
        autoKills = [0,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4]  #土單 (霸劍
        bMoveOnceInMission = True
        locationFixedMoveInMission = Location(448, 531)
        bMoveTwiceInMission = False
        locationFixedMoveInMission2 = Location(131, 645)
        nDelayBeforeUsingSkill = 0
        bNeedTransfer = False
        bUseGPS =True
        imageBonus1 = imageSpecialMonsterIncrease 
        imageBonus2 = imageDropIncrease
    elif enumType==enumArmorMele:
        imageMissions = imageArmorMission
    
        # 先找Boss的圖
        bMoveToBoss = True
        imageBoss = ["1503320329329.png", "1506127773060.png"]
        
        bFindMonsterBySelf = True
        imageMonsters = ["1506127255039.png", "1506127311313.png","1506127326969.png", "1506127339509.png"]

        imagesOffset = []
        bMoveToFighting = False
        monsterRegion = monsterRegion_Full
        bNeedUseOtherBranchServer = True
        bMoveALittleAfterFight = True
        #autoKills = [1,5,2,3,4,2,3,4,2,3,4]  #12345
        autoKills = [0,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4]  #土單 (霸劍
        bMoveOnceInMission = True
        locationFixedMoveInMission = Location(448, 531)
        bMoveTwiceInMission = False
        locationFixedMoveInMission2 = Location(131, 645)
        nDelayBeforeUsingSkill = 0
        bNeedTransfer = True
        bUseGPS =False
        imageBonus1 = imageSpecialMonsterIncrease 
        imageBonus2 = imageDropIncrease
    elif enumType==enumArmorAssassin:
        imageMissions = imageArmorMission
        
        bMoveToBoss = True
        imageBoss = [ "1503320329329.png" ]

        # 先找Boss的圖
        bMoveToBoss = True       
        bFindMonsterBySelf = True

        imagesOffset = imagesOffset_AssassinArmor
        imageMonsters = []
        bMoveToFighting = False
        monsterRegion = monsterRegion_Full
        bNeedUseOtherBranchServer = True
        bMoveALittleAfterFight = True
        autoKills = [1,2,3,4,5]  #12345
        autoKills = [0,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4]  #土單 (霸劍
        bMoveOnceInMission = True
        locationFixedMoveInMission = Location(181, 472)
        bUseGPS =False
        nDelayBeforeUsingSkill = 0
        bNeedTransfer = False
    elif enumType==enumImageOffset:
        imageMissions = imageEvpTask
        bFindMonsterBySelf = True
        bNeedToEnterEvpRoom = True
        imagesOffset = [
                #ImageOffset(  "1512605992877.png", 0, 0), 
                #ImageOffset( "1512606028160.png" , 0, 0), 
                #ImageOffset( Pattern("1512579138496.png").similar(0.50), 125, 110),  
                ImageOffset( Pattern("1512579138496.png").similar(0.50), -50, 130),
                ImageOffset( "1512878613215.png", 0, 0),
                ImageOffset( "1512878584247.png", 0, 0),
        ] 
        bMoveToFighting = False
        monsterRegion = Region(0,89,560,860)
        #monsterRegion = monsterRegion_Up
        bNeedUseOtherBranchServer = True
        bNeedSkip = True
        bSkipBeforeAgain = False
        #autoKills = [0,1,2,3,4,5,-1]
        #autoKills = [5,5,1,3,0,2,0,2,4,]
        #autoKills = [3, 1, 0, 2, -3, 4, -9, 5, -9]  #坦
        #autoKills = [1,0,2,3,5,1,3,-1,4,0,2,1,3,-1,4]  #土單 (無霸劍
        #autoKills = [0,1,2,3,5,4, 0,4,1,3,5,2,4,0,3,1,5,4,2,3,0,4]  #光evp
        #autoKills = [0,1,2,3,4,5, 1,2,3,4, 1,2,3,4,5, 1,2,3,4, 1,2,3,4,5, 1,2,3,4, 1,2,3,4,5, 1,2,3,4]  #土單 
        #autoKills = [0,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4,1,2,3,5,-1,4]  #土單 (霸劍
        #autoKills = [1,2,0,0]   #範圍PK0
        #autoKills = [1,0,2,3,4,2,3,4] #單體PK
        #autoKills = [0,2,5,1,4,2,3,4,1,4,2,3,4,1,4]
        #autoKills = [0,1,2,3,4,5,3,4,-1,3,4,1,2,3,4,5,3,4,1,2,3,4,5,3,4]  #靈刀 
        autoKills = [0,1,5,2,3,4]  #靈刀 (一輪爆發 
        bMoveOnceInMission = True
        locationFixedMoveInMission = Location(115, 431)
        #locationFixedMoveInMission = Location(205, 520)
        bMoveTwiceInMission = False
        locationFixedMoveInMission2 = Location(355, 742)
        nDelayBeforeUsingSkill = 0
        #monsterRegion = monsterRegion_Small
        bNeedTransfer = False
        bMoveALittleAfterFight = True
        bUseGPS = False
        imageBonus1 = imageDropIncrease
        imageBonus2 = imageDoubleExp
        bNeedSayThanks = False

    else:
        Debug.user("error: unknown type");
    Debug.user("mission image length=%d" % len(imageMissions))



def checkMissionTimeOut():
    global imagesOffset
    global nMissionStartTime
    global nEnterMissionTime
    global nMaximunMissionStayTime

    if nMaximunMissionStayTime > 0 and nMaximunMissionStayTime < time.time() - nEnterMissionTime:
        Debug.user("Change imagesOffset to imagesOffset_endMission")        
        imagesOffset = imagesOffset_endMission 
        Debug.user("checkMissionTimeOut, in mission time=%d" % (time.time() - nEnterMissionTime))

# ============================


  
def main():
    global enumType
    global nEnterMissionTime
    isTransfered = False
    isMoved = False
    bLeavingFighting = False

    while True:
        if bNeedSkip:
            d("skip", "1500213106784.png", 2)

        if waitFightingFinished():
            Debug.user("bLeavingFighting = True")
            isMoved = True
            bLeavingFighting = True
        Debug.user("bLeavingFighting = %d" % bLeavingFighting)

        # check current page
        enumPageId = getPageId()
        Debug.user("enumPageId = %d" % enumPageId)

        if enumPageId == PageId.enumPageId_mission:
            
            if bLeavingFighting:
                checkMissionTimeOut()
                bLeavingFighting = False
                if bMoveALittleAfterFight:
                    moveALitte()
                    continue
            
            if not isMoved:
                nEnterMissionTime = time.time()
                refreshSetting()
                if bMoveOnceInMission:               
                    isMoved = True
                    l("locationFixedMoveInMission", locationFixedMoveInMission )
                    sleep(nMoveDelay)
                if bMoveTwiceInMission:               
                    isMoved = True
                    l("locationFixedMoveInMission2", locationFixedMoveInMission2 )
                    sleep(nMoveDelay2)
                
            if bFindTargetInMission:
                c("1499951382722.png", 0)
                sleep(3)
            moveToTaskTargetOnce()
            waitFighting(2)
        elif enumPageId == PageId.enumPageId_fighting:
            # still fighting
            Debug.user("still fighting")
        elif enumPageId == PageId.enumPageId_board:
            enterMission()
            bLeavingFighting = False
        elif enumPageId == PageId.enumPageId_skip:
            d("skip", "1500213106784.png", 2)
        elif (enumPageId == PageId.enumPageId_again) | (enumPageId == PageId.enumPageId_openGift):
            isMoved = False
            if bSkipBeforeAgain:
                d("skip", "1500213106784.png", 2)
            
            #repeat mission
            enterAgain()
            bLeavingFighting = False

            #if bNeedSkip:
            #    d("skip", "1500213106784.png", 2)
            #    sleep(2)
        elif enumPageId == PageId.enumPageId_close:
            d("close some page", imageClose, 0)
        elif enumPageId == PageId.enumPageId_missionClosed:
            # mission closed, go to next mission
            l("click once", Location(266, 505))
            enumType = enumTypeNext
            refreshSetting()
        else: #unknown
           sleep(0.1)
           
    #waitMissionStarted()
    #click( locationFixedMoveInMission )

def enterAgain():
    d( "imageAgain", imageAgain, 2 )
    sleep(3)

    #click all next page
    i = 0
    retry = 0
    while True:
        sleep(1)
        if gameRegion.exists( "1503187522791.png", 0):
            d( "imageAgree", imageAgree, 0 )
            continue
        if gameRegion.exists( "1503186459432.png", 0):
            d( "imageOpenGift", imageOpenGift, 0 )

        if gameRegion.exists(imageGo, 0):
            break
        if gameRegion.exists("1503200826656.png", 0):
            d("click again", "1503200826656.png", 0)
            continue
        
        i = i + 1
        if d( "imageNextPage " + str(i) , imageNextPage1, 1 ):
            retry = 0
        if d( "imageNextPage3" , imageNextPage3, 0 ):
            retry = 0
        retry = retry + 1
        if retry >= 5:
            break;
        if i > 10:  #任務全部完成時, 比較久
            break;
    
#    d( "imageNextPage3", imageNextPage1, 1 )
#    d( "imageOpenGift", imageOpenGift, 2 )
    #if bNeedOpenGift:
    #    d( "imageOpenGift", imageOpenGift, 2 )
    #d( "imageAgain2", imageAgain2, 1 )
    #d( "imageNextPage2", imageNextPage2, 3 )
    #if bNeedAgree:
    #    sleep(1)
    #    d( "imageAgree", imageAgree, 3 )
    if bUseGPS:
        useGPS()
    elif bNeedUseOtherBranchServer:
        changeBranchServer()
    else:
        d( "imageGo", imageGo, 2 )

    Debug.user("bNeedSkip=%d" % bNeedSkip)
    if bNeedSkip:
        d("skip", "1500213106784.png", 10)

    if not waitMissionStarted(10):
        Debug.user("warning: haven't entered again")
        enterMission()
    if bNeedTransfer:
        sleep(2)
        transfer()
    
#***********************************************************************


    


def clickMonster():
    backupDelay = Settings.MoveMouseDelay
    Settings.MoveMouseDelay = 0.02
    for p in monsterPositions:
        if isFighting():
            click(p)
        else:
            break
    Settings.MoveMouseDelay = backupDelay











def changeBranchServer():
    if not d("branch servet button","1499732606430.png"):
        return False

    #sleep(2)
    #click(Location(272, 321))
    #return True
   
    if not clickInRegion(Region(38,570,475,389), "1499732622006.png", 2):
        return False
    return True
#    serversRegion = Region(80,312,389,505)
    
#    servers = [] # an empty list
#    for server in serversRegion.findAll("1499732622006.png"):
#        servers.append(server)

#    if len(server) <= 0:
#        Debug.user("error: can't find server")
#        return False
        
#    num = random.randrange( 0, len(servers) )
#    Debug.user("find %d servers, use %d" % len(server) % num )

#    l("click server", servers[num])

#    return True

# 關掉每天早上的公告
def closeAnnouncement():
    while True :
        if not d("close announcement", "1500854126779.png", 0):
            break
        sleep(1)

# 關掉每天早上的公告 (第2個視窗
def closeAnnouncement2():
    while True :
        if not d2("close announcement 2", "1500854126779.png", 0):
            break
        sleep(2)
        
def enterMission():
    Debug.user("enterMission+") 

    closeAnnouncement()

    d( "imageTaskBoard", imageTaskBoard, 10 )

    if not gameRegion.exists("1511573781918.png", 10):
        if not gameRegion.exists("1515432205825.png", 10):
            Debug.user("error: did not enter mission select page.")
            return False

    bFoundMission = False
    nSteps=len(imageMissions)
    Debug.user("mission steps len=%d" %nSteps)
    i = 0
    swipTimes = 0
    while i < nSteps:
        Debug.user("click mission %d" % i)
        if not d( "select mission", imageMissions[i], 2):
            bFoundMission = False
            Debug.user("can't find mission %d" % i)

            if i==2:
                swipUp()
                swipTimes = swipTimes+1
                if swipTimes > 3:
                    Debug.user("error: can't find mission")
                    return False
                sleep(1)
                continue
            
            if d("click back", "1503880320458.png"):
                i = i - 1
            
        else:
            bFoundMission = True
            sleep(0.5)
        i = i+1
        
    if not bFoundMission:
        Debug.user("not find mission")
        return False

    d("select partner", Pattern("1507126890560.png").exact(), 5 )
    while d("OK partner", Pattern("1507126862134.png").exact() ):
        sleep(1)
    if bUseGPS:
        useGPS()
        d("go", "1498995593560.png" )
        if gameRegion.exists("1498267506267.png"):
            d("go", "1498995593560.png" )
    if bNeedUseOtherBranchServer:
        if not changeBranchServer():
            d("go", "1498995593560.png" )
    else:
        d("go","1498995593560.png" )

    d( "skip", "1500716627071.png", 10 )
    #d( "skip", "1500716627071.png", 0 )
    if not gameRegion.exists(imageFriendMenu, 30):
        return False
    sleep(1)
    closeAnnouncement()
    if bNeedTransfer:
        sleep(2)
        transfer()
    return True

def swipUp():
    mouseMove(Location(283, 633))
    mouseDown(Button.LEFT)
    mouseMove(Location(284, 282))
    mouseUp(Button.LEFT)

def loginGame():
    Debug.user("login game")
    c("1498361652308.png")
    if not c("1498296986692.png"):
        return False
    if not c("1498297048888.png", 5):
        return False
    if not c("1498297969699.png", 30):
        return False  
    if not gameRegion.exists(imageFriendMenu, 30):
        return False
    zoomout()
    return True

def zoomout():
    mouseMove(Location(263, 516))
    mouseDown(Button.LEFT)
    sleep(2)
    mouseMove(Location(263, 800))
    mouseUp(Button.LEFT)



def isOnMission():
    reg = Region(438,23,110,78)
    if reg.exists(Pattern("1499210289316.png").similar(0.80), 0):
        Debug.user("isOnMission=True") 
        return True
    else:
        Debug.user("isOnMission=False") 
        return False


def waitMissionStarted(retry = 10):
    Debug.user("waitMissionStarted+")
    i = 0
    bInMission = False
    for n in range(retry):
        if isOnMission():
            return True
        sleep(1) 
    Debug.user("waitMissionStarted-")
    return False

# 有人喊 有BOSS, 台版比較好用, 日版太多人道謝
def moveToBoss():
    Debug.user("moveToBoss+") 
    
    try:
        monster = monsterRegion.find()
        click(monster.offset(0, 80))
        return True
    except FindFailed:
         return False
        

def moveToFighting():
    Debug.user("moveToFighting+")
    i = 0

    Steps("moveToFighting", [monsterRegion, Images([ Pattern("1507897726703.png").similar(0.90).targetOffset(0,10), Pattern("imageOtherFighting.png").similar(0.85).targetOffset(0,7), Pattern("imageOtherFighting2.png").similar(0.90).targetOffset(0,7), Pattern("imageOtherFighting3.png").similar(0.75), Pattern("1503100614536.png").similar(0.75).targetOffset(0,8), Pattern("1503101128026.png").similar(0.75).targetOffset(0,6), Pattern("1503101630080.png").similar(0.75).targetOffset(0,7), "1503121487310.png", Pattern("1508031407013.png").similar(0.66).targetOffset(0,5), Pattern("1515246341319.png").targetOffset(0,4), Pattern("1515825263702.png").similar(0.80).targetOffset(8,5)]) ]).execute()
    return 

    for image in imageFightings:
        try:
            i = i+1
            Debug.user("moveToFighting %d" % i)
            if not monsterRegion.exists(image, 0):
                continue
            monster = monsterRegion.find(image)
            clickRegionBottom(monster)
            return True
        except FindFailed:
            return False
    return False

def moveToFighting2():
    Debug.user("moveToFighting2+")
    try:
        monster = monsterRegion.find(imageOtherFighting2)
        clickRegionBottom(monster)
        return True
    except FindFailed:
        return False


def moveToMonster(image):
    try:
        if not monsterRegion.exists(image, 0):
            return False
        monster = monsterRegion.find(image)
        clickRegionBottom(monster)
        return True
    except FindFailed:
        return False
    return False

def moveToImageOffset( imageOffset ):
    try:
        if not monsterRegion.exists(imageOffset.image, 0):
            Debug.user("not found on monsterRegion %s" % monsterRegion)
            return False
        target = monsterRegion.find(imageOffset.image)
        offsetX = imageOffset.offsetX 
        offsetY = imageOffset.offsetY 
        if offsetX + target.x < 0:
            #Debug.user("offsetX=%d, target.x=%d" % imageOffset.offsetX , target.x)
            offsetX = -1*target.x + 5 
        if offsetY + target.y < 0:
            #Debug.user("offsetY=%d, target.y=%d" % imageOffset.offsetY , target.y)
            offsetY = -1*target.y + 5 
        if offsetX + target.x >= gameRegion.w:
            offsetX = 0
            target.x = gameRegion.w
        if offsetY + target.y >= gameRegion.h:
            offsetY = 0
            target.y = gameRegion.h
            
        Debug.user("offsetX = %d" % offsetX)
        Debug.user("target.x = %d" % target.x)
        click( target.offset(offsetX, offsetY) )
        return True
    except FindFailed:
        return False
    return False

# 檢查是否在任務中, 是的話就移過去打怪
def moveToTaskTargetOnce():
    Debug.user("moveToTaskTargetOnce+") 
    while (isOnMission() & (not isFighting())):
        if bNeedToEnterEvpRoom:
            moveToEvpTarget()
            break
        
        if bBossMonsterFirst:
            if moveToBoss():
                sleep(2)
                break

        if bMoveToFighting:
            if moveToFighting():
                waitFightingFinished(2)
                break

            
        if bFindMonsterBySelf:
            i = 0

            if len(imagesOffset)>0:
                for imageOffset in imagesOffset:
                    i = i+1
                    Debug.user("move to imageOffset %d" % i)
                    if moveToImageOffset(imageOffset):
                        sleep(2)
                        return True
            else:
                for image in imageMonsters:
                    i = i+1
                    Debug.user("moveToMonster %d" % i)
                    if moveToMonster(image):
                        sleep(2)
                        return True
    

imageNextPage = "1497762347177.png"
imageOpenGift = "1497756359246.png"
friendMenu = "1497755516858.png"

def isFriendMenu():
    if Region(313,25,90,76).exists(friendMenu)!=None:
        Debug.user("isFriendMenu=true")
    else:
        Debug.user("isFriendMenu=false")

def finishMission():
    Debug.user("finishMission+")

    for n in range(2):
        Debug.user("wait next page")
        if not c(imageOpenGift):
            Debug.user("can't find imageOpenGift button")
        if not c(imageNextPage):
            Debug.user("can't find next page button")
        
    return True

def isFighting():
    if bCanEscap:
        if escapeRegion.exists("1497776017507-2.png", 0): 
            Debug.user("isFighting=true")
            return True
    if escapeRegion.exists("1498270581243.png", 0): 
        Debug.user("isFighting=true")
        return True
    Debug.user("isFighting=false")
    return False

def waitFightingVanish( timeout = 0 ):
    if bCanEscap:
        if escapeRegion.waitVanish("1497776017507-2.png", timeout): 
            Debug.user("fighting vanish")
            return True
    if escapeRegion.waitVanish("1498270581243.png", 0): 
        Debug.user("fighting vanish")
        return True
    Debug.user("still isFighting")
    return False

def waitFighting( timeout ):
    Debug.user("waitFighting+")
    if bCanEscap:
        if escapeRegion.exists("1497776017507-2.png", timeout): 
            Debug.user("isFighting=true")
            return True
    if escapeRegion.exists("1498270581243.png", timeout): 
        Debug.user("isFighting=true")
        return True
    Debug.user("isFighting=false")
    return False

def waitFightingFinished( i = nCheckFightingTimes ):
    Debug.user("waitFightingFinished+")
    i = 0
    bFighting = False
    # is finished from fight
    bFought = False
    bSaidThanks = False
    while True:
        if not isFighting():
            bFighting = False
            i = i - 1
            if i <= 0:
                break
            sleep(1)
        else:            
            i = 0
            if not bFighting:
                sleep(1)
                clickMonster()
                bFighting = True
            else:
                sleep(1)
                bFought = True


                if bNeedSayThanks & (not bSaidThanks):
                    bSaidThanks = SayThanksIfRare()
                
                #if Region(398,80,154,71).exists("1502364055024.png", 2):
                #    d("exit", "1502364132345.png")
                #    d("exit2", "1502364152924.png",2)
                autoUseSkill()
    Debug.user("waitFightingFinished-")
    return bFought


imageSkillStandBy = "imageSkillStandBy.png"
regionSkillStandBy = Region(1,560,551,384)
# use a skill on specify position
def useSkill( position ):
    click( position )
    if regionSkillStandBy.exists(imageSkillStandBy, 2):
        Debug.user("A skill is standby");
        sleep(1)
        regionSkillStandBy.waitVanish(imageSkillStandBy, 30)
        sleep(1)
        return True
    else:
        Debug.user("can't find standby skill")
    return False

#戰鬥
def autoUseSkill():
    bWaitFirstEp = True
    #判斷是否在戰鬥
    try:
        reg = Region(9,563,546,375)
        
        Debug.user("Use skill")
        for n in autoKills:
            if isFighting():
                questionMark = Pattern("1511531977194.png").similar(0.97)
                if reg.exists(questionMark,0):
                    
                    firstSkill = reg.find(questionMark)
                    d("click questionMark", questionMark)
                    sleep(1.5)
                    return True
                else:
                    firstSkill = reg.find(Pattern("1497757408206-4.png").similar(0.65))
                if bWaitFirstEp:
                    sleep(nDelayBeforeUsingSkill)
                    bWaitFirstEp = False
                else:
                    sleep(0.5)
                Debug.user("use skill %d", n)
                firstSkill.x = 23
                if n==-1:
                    useSkill(firstSkill.offset(20, -80))
                elif n < -2: #sleep
                    waitFightingVanish(n*-1)
                else: 
                    useSkill(firstSkill.offset(0+n*88, 0))
                    #d("burst bar", Pattern("1499732041383-1.png").similar(0.95), 0)
                    #for i in range(10):
                    #    if not isFighting():
                    #        return False
                    #    sleep(0.2)
            else:
                return False
        
        #sleep(4)
        #return True
    except FindFailed:
        Debug.user("can't find skill panel")
        clickMonster()
        return False

imageFindFriend = "imageFindFriend.png"
imageFriendOK = Pattern("imageFriendOK.png").similar(0.90)
imageClose = "imageClose.png"
imageGpsBonusRemind = "imageGpsBonusRemind.png"
imageGpsGo = "imageGpsGo.png"
def useGPS():
    reg = Region(45,567,468,238)
    if not d("imageFindFriend", imageFindFriend, 3 ):
        d( "imageGo", imageGo, 5 )
        return False
    sleep(1)
    imageFriendDialog = "imageFriendDialog.png"
    imageHasGpsFriend = "imageHasUpsFriend.png"
    while gameRegion.exists(imageFriendDialog, 1):
        if not d( "imageHasUpsFriend", imageHasGpsFriend, 0 ):
            d("imageFriendClose", imageClose, 2 )
        else:
            if reg.exists(imageGpsBonusRemind,2):
                d("imageBonus1", imageBonus1)
                sleep(1)
                if reg.exists(imageGpsBonusRemind):
                    d("imageBonus2", imageBonus2)
                else:
                    Debug.user("no bonus 2")
            else:
                Debug.user("no bonus 1")

    if bNeedUseOtherBranchServer:
        changeBranchServer()

    d("no GPS service", "1505642893410.png", 0)
    
    d( "imageGo", imageGo, 2 )
    d( "imageGpsGo", imageGpsGo, 2 )
    if gameRegion.exists(Pattern("1505664145843.png").exact(), 0):
        d("GPS effect doesn't be used.", Pattern("1505664202573.png").exact())

def moveALitte():
    Debug.user("move a little")    

    i=0
    if bMoveToBoss:
        Debug.user("moveToBoss")
        for image in imageBoss:
            i = i+1
            Debug.user("moveToBoss %d" % i)
            if moveToMonster(image):
                sleep(2)
    
    if isOnMission():
        click(locationUp)
        sleep(1)
        click(locationDown)
        sleep(2)

def fightToPartner():
    closeAnnouncement2()

    click( Location(889, 874) )
    clickInRegion(gameRegion2, "1500853416560.png")
    clickInRegion(gameRegion2, "1498995557445.png" )
    clickInRegion(gameRegion2, "1498995593560.png" )
    sleep(5)
    closeAnnouncement2()
    sleep(1)
    d2( "skipp 2", "1501177588703.png", 5 )
    sleep(3)
    # move a little
    #click( Location(882, 537) )



def transfer_evp():
    l("move to talk", Location(356, 450))
    
    sleep(2)
    if not d("talk", "1502317720357.png", 10):
        l("can't find the guard, click directly", Location(304, 510))

    d("talking", "1502317910399.png", 5)
    sleep(1)
    d("talk to move other place", "1502317951855.png", 5)
    d("talking2", "1502317978971.png", 5)
    #if enumType == enumEVP_6:
    #    d("talk to move other place2", "1502318001566.png")
    #else:
    d("talk to move other place2", "1502368111955.png", 5)
    sleep(4)

def transfer():
    Debug.user("transfer");
    if not isOnMission():
        Debug.user("error: no in a mission");
        
    l("move to talk", Location(343, 501))
    
    sleep(2)
    if not d("talk", "1502752563609.png", 10):
        l("can't find the guard, click directly", Location(329, 457))

    d("talking", "1502752596473.png", 5)
    sleep(1)
    for n in range(2):
        d("talk to next page", "1506294076568.png", 5)
        sleep(1)
        d("talking again", "1502752596473.png", 5)
        sleep(1)
    d("talk to move other place", "1506294278905.png", 5)
    d("talking2", "1506294351532.png", 5)
    d("talk to move other place2", "1506294369543.png", 5)
    sleep(4)
'''
    d("talk to move other place", "1502752617013.png", 5)
    d("talking2", "1502752630300.png", 5)

    #if enumType == enumEVP_6:
    #    d("talk to move other place2", "1502318001566.png", 5)
    #else:
    d("talk to move other place2", "1502752654221.png", 5)
    sleep(4)
'''
    

def getPageId():
    Debug.user("check page id (len=%d)" % len(PageId.imagePages))
    for i in range( len(PageId.imagePages)):
        Debug.user("check %s" % PageId.imagePages[i][3])
        #print PageId.imagePages[i][0]
        #PageId.imagePages[i][0].highlight(1)
        if PageId.imagePages[i][0].exists( PageId.imagePages[i][1], 0):
            Debug.user( PageId.imagePages[i][3] )
            return PageId.imagePages[i][2]
    
    #enumPageId_mission = 1
    #enumPageId_fighting = 2
    #enumPageId_again = 3
    #enumPageId_board = 4  #看板
    #enumPageId_unknown = 99
    
    return PageId.enumPageId_unknown

def minimizeConsole():
    if gameRegion.exists(imageConsole):
        Debug.user("found console")

def clickImageOffsetOrClickLocation(image, offsetX, offsetY, location):
    lib = GaeeryLib()
    lib.setRoi(gameRegion)
    loc = lib.find("imageoffset", image, 1)
    if loc == None:
        l("move to a location instead", location)
    else:
        l("click image offset", loc.offset(offsetX,offsetY) )

def moveToEvpTarget():
    #click(Location(265, 497))

    #sleep(2)
    #d("talk 1", "1512878584247.png", 5 )
    #sleep(2)
    #d("talk 2", "1512878584247.png", 5 )
    #return d("start", "1512878613215.png", 5)
     
    
    clickImageOffsetOrClickLocation( "1508343277513.png", 130, -110, Location(515, 426) )  #wind
    #clickImageOffsetOrClickLocation( Pattern("1507117402718.png").similar(0.95), 145, -60, Location(35, 394) )  #fire
    sleep(1)
    
    if isFighting():
        return True
    imageEnterEvpTarget = "imageEnterEvpTarget.png"
    if d("enter evp room?", imageEnterEvpTarget, 3):
        if d("enter evp room", "1505925536533.png", 3):
            return True
    return False

#moveToTaskTargetOnce()
#fightToPartner()
#moveALitte()
#enterMission()
#transfer()
#enterAgain()
refreshSetting()

while True:
    main()