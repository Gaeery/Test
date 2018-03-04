import random
import SwordAndMagicPictures
reload(SwordAndMagicPictures)  # make sure global variables are reloaded
import ControlLib
from SwordAndMagicPictures import *
from ControlLib import *
Settings.MoveMouseDelay = 0.3
gameRegion = Region(0,30,555,990)

imgMenu = "1519039125806.png"

def ArrangeMail():
    with gameRegion:    
        while True:
            d("menu", imgMenu,3)
            d("mailbox", "1503708225124.png", 3)
            if not receiveAllMail():
                break
def receiveAllMail():
    with gameRegion:   
        while True:
            Debug.user("check bag capability")
            if exists(Pattern("1503708271933.png").similar(0.90), 1):
                d("close popup", "1503709252712.png",1)
                gotoEquipPage()
                sellAll()
                storeAll()
                return True
            elif exists( "1503710326304.png", 0):
                d("close popup", "1503709252712.png",1)
                d("next page", "1503710198198.png")
                if not exists( Pattern("1505517915525.png").exact(),2):
                    #no next page
                    gotoEquipPage()
                    sellAll()
                    storeAll()
                    return False
                else:
                    Debug.user("has next page")
            elif exists("1503709252712.png", 0.5):
                d("received", "1503709252712.png",5)
            elif d("receive mail", Pattern("1505517874410.png").exact(), 5):
                sleep(0.5)
                exists("1503709252712.png", 3)
            elif exists("1505517117946.png", 0): 
                if not exists(Pattern("1503708271933.png").similar(0.90), 0):
                    return False
            else:
                sleep(1)
    return True
            
def sellAll():
    with gameRegion: 
        d("sell page", "1503708495938.png", 3)
        while True:
            d("select all", Pattern("1505517689974.png").exact(), 20)
            if d("sold all", "1503708674424.png",1):
                d("leave sell", "1503708342988.png", 3)
                break
            if d("sell", Pattern("1505517742074.png").exact(), 5):
                d("sell2", Pattern("1505517768561.png").exact(), 5)
                d("sell3", Pattern("1503708608570.png").similar(0.90), 5)

def gotoEquipPage():
    with gameRegion:  
        d("menu",  imgMenu, 0)
        d("leave mail", "1503708342988.png", 3)
        sleep(1)
        d("equip", "1519039301576.png", 3)
        sleep(1)
        d("equip list", "1503708432656.png", 3)
        sleep(1)
        d("equip list", "1503708460080.png", 3) 

def storeAll():
    with gameRegion: 
        d("store page", "1503708850938.png", 3)
        d("store page2", "1503708870724.png", 3)
        while True:
            d("select all", "1503708529175.png", 20)
            if d("stored all", "1503708674424.png",1):
                d("leave store", "1519039546940.png", 3)
                break
            d("store", Pattern("1505518002795.png").exact(), 5)
            d("store2", Pattern("1503961294687.png").similar(0.94), 5)
                
            d("store3", Pattern("1505518063648.png").similar(0.95), 5)

def vote():
    region = Region(382,522,174,83)
    if region.exists("1516752267331.png", 0):
        while True:
            print region.getLastMatch()
            click( region.getLastMatch() )
            sleep(0.5)
        
vote()
gotoEquipPage()
sellAll()
storeAll()
ArrangeMail()