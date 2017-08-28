import random
import SwordAndMagicPictures
reload(SwordAndMagicPictures)  # make sure global variables are reloaded
import ControlLib
from SwordAndMagicPictures import *
from ControlLib import *
Settings.MoveMouseDelay = 0.1
gameRegion = Region(0,0,587,1024)

def ArrangeMail():
    with gameRegion:    
        while True:
            d("menu", "1503708173412.png",3)
            d("mailbox", "1503708225124.png", 3)
            if not receiveAllMail():
                break
def receiveAllMail():
    with gameRegion:   
        while True:
            if exists(Pattern("1503708271933.png").similar(0.95), 0):
                d("close popup", "1503709252712.png",1)
                gotoEquipPage()
                sellAll()
                storeAll()
                break
            elif exists( "1503710326304.png", 0):
                d("close popup", "1503709252712.png",1)
                d("next page", "1503710198198.png")
                if not exists( Pattern("1503726855065.png").exact(),2):
                    #no next page
                    gotoEquipPage()
                    sellAll()
                    storeAll()
                    return False
                else:
                    Debug.user("has next page")
            elif exists("1503709252712.png", 0.5):
                d("received", "1503709252712.png",5)
            elif d("receive mail", Pattern("1503709138204.png").similar(0.97), 5):
                sleep(0.5)
                exists("1503709252712.png", 3)
            else:
                sleep(1)
    return True
            
def sellAll():
    with gameRegion: 
        d("sell page", "1503708495938.png", 3)
        while True:
            d("select all", Pattern("1503708529175.png").exact(), 20)
            if d("sold all", "1503708674424.png",1):
                d("leave sell", "1503708342988.png", 3)
                break
            d("sell", "1503708547651.png", 5)
            d("sell2", Pattern("1503708586923.png").similar(0.94), 5)
            d("sell3", Pattern("1503708608570.png").similar(0.90), 5)

def gotoEquipPage():
    with gameRegion:  
        d("leave mail", "1503708342988.png", 3)
        sleep(0.5)
        d("equip", "1503708374841.png", 3)
        sleep(0.5)
        d("equip list", "1503708432656.png", 3)
        sleep(0.5)
        d("equip list", "1503708460080.png", 3) 

def storeAll():
    with gameRegion: 
        d("store page", "1503708850938.png", 3)
        d("store page2", "1503708870724.png", 3)
        while True:
            d("select all", "1503708529175.png", 20)
            if d("stored all", "1503708674424.png",1):
                d("leave store", "1503709049190.png", 3)
                break
            d("store", "1503708937677.png", 5)
            d("store2", Pattern("1503708586923.png").similar(0.94), 5)
                
            d("store3", Pattern("1503708985982.png").similar(0.95), 5)

ArrangeMail()