
    partyMembers = lib.findAll("party members", imageParty)
    if partyMembers != None:
        sortedPartyMembers = sorted(partyMembers, key=by_y)
        locParty = sortedPartyMembers[0]
        #Debug.user("locParty.y=%d", locParty.y)
        nHploc_y = locParty.y + 14
        nMploc_y = nHploc_y + 15
    
    if locParty == None:
        leftRoi = GaeeryLib()
        leftRoi.setRoi(regionLeftScreen)
        characterPage = leftRoi.find("character data", "1513897038903.png")
        if characterPage != None:
            Debug.user("close characterPage")
            click(characterPage)
            return

        menuRoi = GaeeryLib()
        menuRoi.setRoi(Region(1726,47,93,85))
        menuPage = menuRoi.find("menu", "1513897038903.png")
        if menuPage != None:
            Debug.user("close menu")
            click(menuPage)
            return

        #talk
        if Region(1541,670,118,40).exists("1514506603250.png", 0):
            click(Location(1637, 874))
            sleep(1)
            return

        if Region(925,711,294,123).exists( "1514109969796.png", 0):  #mission page
            click( "1514109969796.png" )
            sleep(1)            
            return
            
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
            
            #regionHp.highlight()
            regionStatus.highlight()
            sleep(1)
            #regionHp.highlight()
            regionStatus.highlight()
