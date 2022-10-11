import sys
import os

try:
    saveLocation = sys.argv[1]  # drag and drop
    scriptLocation = os.path.abspath(os.getcwd())
except:
    print("No file dropped")
    os.system("pause")
backupLocation = saveLocation + "backup"

with open(saveLocation, 'rb') as rfile:
    fileContent = rfile.read()

lvlist = []
benchlist = []
namelist = []
maxlevel = 99

try:
    gameID = fileContent[0:8].decode('shift-jis')
    if gameID == "MOS_GAME": #
        levelOffset = 337
        partyOffset = 332
        snameOffset = 512
        enameOffset = 531
        addOffset = 360
        maxlevel = 130

        SskillOffset = 534
        EskillOffset = 558
        classOffset = 341
        diction = {
            0:	"Protector",
            1:	"Medic",
            2:	"Survivalist",
            3:	"Ronin",
            4:	"Highlander",
            5:	"Gunner",
            6:	"Sovereign",
            7:	"Zodiac",
            8:	"Ninja",
            9:	"Shogun",
            10:	"Landsknecht",
            11:	"Nightseeker",
            12:	"Imperial",
            13:	"Pugilist",
            14:	"Harbinger",
            15:	"Hero",
            16:	"WarMagus",
            17:	"Arcanist",
            18:	"Farmer",
        }
        skilMult= 27
        skilAdd = 2
        skillNameFile = scriptLocation+'/eox.txt'
        currentspOffset = 339
        retirespOffset = 340
        guildslots = 30

    elif gameID == "MO1RGAME": #
        levelOffset = 2116
        partyOffset = 2112
        snameOffset = 2328
        enameOffset = 2347
        addOffset = 384

        SskillOffset = 2384
        EskillOffset = 2408
        classOffset = 2120
        diction = {
            0:	"Landsknecht",
            1:	"Survivalist",
            2:	"Protector",
            3:	"Dark Hunter",
            4:	"Medic",
            5:	"Alchemist",
            6:	"Troubador",
            7:	"Ronin",
            8:	"Hexer",
            9:	"Highlander",
            10:	"Gunner",
        }
        skilMult = 30
        skilAdd = 6
        skillNameFile = scriptLocation+'/eou.txt'
        currentspOffset = 2118
        retirespOffset = 2119
        guildslots = 25

    elif gameID == "MO2RGAME": #
        levelOffset = 376
        partyOffset = 372
        snameOffset = 564
        enameOffset = 583
        addOffset = 264

        SskillOffset = 588
        EskillOffset = 613
        classOffset = 380
        diction = {
            0:	"Landsknecht",
            1:	"Survivalist",
            2:	"Protector",
            3:	"Dark Hunter",
            4:	"Medic",
            5:	"Alchemist",
            6:	"Troubador",
            7:	"Ronin",
            8:	"Hexer",
            9:	"Gunner",#
            10:	"War Magus",#
            11:	"Beast",#
            12:	"Sovereign",#
            13:	"Highlander",#
            14:	"Fafnir",
        }
        skilMult = 30
        skilAdd = 5
        skillNameFile = scriptLocation+'/eo2u.txt'
        currentspOffset = 378
        retirespOffset = 379
        guildslots = 30

    elif gameID == "MOR4GAME": #
        levelOffset = 199
        partyOffset = 196
        snameOffset = 400
        enameOffset = 419
        addOffset = 364

        SskillOffset = 422
        EskillOffset = 446
        classOffset = 200
        diction = {
            0:	"Landsknecht",
            1:	"Nightseeker",
            2:	"Fortress",
            3:	"Sniper",
            4:	"Medic",
            5:	"Runemaster",
            6:	"Dancer",
            7:	"Arcanist",
            8:	"Bushi",
            9:	"Imperial",
        }
        skilMult = 25
        skilAdd = 2
        skillNameFile = scriptLocation+'/eo4.txt'
        currentspOffset = 420
        retirespOffset = 490
        guildslots = 30

    elif gameID == "MO5_GAME": #
        levelOffset = 328
        partyOffset = 324
        snameOffset = 504
        enameOffset = 523
        addOffset = 336

        SskillOffset = 526
        EskillOffset = 545
        classOffset = 332
        diction = {
            0: "Fencer",
            1: "Dragoon",
            2: "Warlock",
            3: "Rover",
            4: "Masurao",
            5: "Shaman",
            6: "Botanist",
            7: "Pugilist",
            8: "Harbinger",
            9: "Necromancer",
            10: "Phantom Duelist",
            11: "Chain Duelist",
            12: "Shield Bearer",
            13: "Cannon Bearer",
            14: "Omnimancer",
            15: "Elemancer",
            16: "Flying Falcon",
            17: "Hunting Hound",
            18: "Blade Dancer",
            19: "Blade Master",
            20: "Divine Punisher",
            21: "Divine Herald",
            22: "Merciful Healer",
            23: "Graced Poisoner",
            24: "Barrage Brawler",
            25: "Impact Brawler",
            26: "Deathbringer",
            27: "Deathguard",
            28: "Spirit Evoker",
            29: "Spirit Broker",
        }
        skilMult = 20
        skilAdd = 2
        skillNameFile = scriptLocation+'/eo5.txt'
        currentspOffset = 330
        retirespOffset = 331
        guildslots = 30

    else:
        print(fileContent[0:8].decode('shift-jis'))
except ValueError:
    print("Not an EO save")
    os.system("pause")

levelOffsetR = levelOffset
partyOffsetR = partyOffset
snameOffsetR = snameOffset
enameOffsetR = enameOffset
SskillOffsetR = SskillOffset
EskillOffsetR = EskillOffset
classOffsetR = classOffset
currentspOffsetR = currentspOffset
retirespOffsetR = retirespOffset


skillList = []
skillListName = []
classlist = []
currentsplist = []
retiresplist = []

for iniloop in range(guildslots):

    lvlist.append(fileContent[levelOffsetR])
    benchlist.append(fileContent[partyOffsetR])
    classlist.append(fileContent[classOffsetR])
    currentsplist.append(fileContent[currentspOffsetR])
    retiresplist.append(fileContent[retirespOffsetR])

    name = fileContent[snameOffsetR:enameOffsetR].decode('shift-jis')
    namelist.append(name.replace('\x00', ' '))

    levelOffsetR += addOffset
    partyOffsetR += addOffset
    snameOffsetR += addOffset
    enameOffsetR += addOffset

    skillList.append(list(fileContent[SskillOffsetR:EskillOffsetR]))
    SskillOffsetR += addOffset
    EskillOffsetR += addOffset
    classOffsetR += addOffset
    currentspOffsetR += addOffset
    retirespOffsetR += addOffset


def readFile():
    id=0
    for ia, ib, ic, ie in zip(lvlist, namelist, benchlist, classlist):
        print('{:>4}'.format(str(id)+" -"), 
        ib, 
        '{:>4}'.format(str(ia)), 
        '{:>6}'.format("Party" if ic == 3 else ""),
        diction[ie]
        )

        id += 1



readFile()

def saveFile():

    idsave = 0
    save1 = levelOffset
    save2 = partyOffset
    save3 = SskillOffset
    save4 = currentspOffset

    with open(saveLocation, 'rb') as rfile:
        fileContent = rfile.read()
    backup = open(backupLocation, "wb")
    backup.write(fileContent)
    
    fh = open(saveLocation, "r+b")
    for x in range(guildslots):
        fh.seek(save1)
        fh.write(int(lvlist[idsave]).to_bytes(1, 'little'))
        fh.seek(save2)
        fh.write(int(benchlist[idsave]).to_bytes(1, 'little'))
        fh.seek(save3)
        fh.write(bytearray(skillList[idsave]))
        fh.seek(save4)
        fh.write(int(currentsplist[idsave]).to_bytes(1, 'little'))
        
        idsave += 1
        save1 += addOffset
        save2 += addOffset
        save3 += addOffset
        save4 += addOffset
        

while True:

    print("Which ID to edit? (S)ave? (A)dd to party? (R)emove from party? Skill(T)ree?:")
    x = input()


    if x.lower() == "s":
        saveFile()
        print("Saved")


    elif x.lower() == "a":

        if benchlist.count(3) < 6:

            print("Who to add?:")
            addinput = input()

            try:
                if 0 <= int(addinput) <= 59:

                    if benchlist[int(addinput)] == 3:
                        print("Already in party")

                    else:
                        benchlist[int(addinput)] = 3
                        readFile()
                else:
                    print("Not between 0 and 59")

            except ValueError:
                print("That's not an ID")
        else:
            print("Can't add more than 6")


    elif x.lower() == "r":

        if benchlist.count(3) > 1:

            print("Who to remove?:")
            reminput = input()

            try:
                if 0 <= int(reminput) <= 59:
                    if benchlist[int(reminput)] == 1:
                        print("Not in party")
                    else:        
                        benchlist[int(reminput)] = 1
                        readFile()
                else:
                    print("Not between 0 and 59")

            except ValueError:
                print("That's not an ID")
        else:
            print("Can't remove more")


    elif x.isnumeric():

        if 0 <= int(x) <= 59:

            print('To what level?:')
            y = input()

            if 1 <= int(y) <= maxlevel+2:
                lvlist[int(x)] = y
                readFile()

            else:
                print("Not between 1 and",maxlevel+2)
        else:
            print("Not between 0 and 59")


    elif x.lower() == "t":
        print("Whom?:")
        y = int(input())

        def readskill():
            with open(skillNameFile) as eoxf:
                skil = [line.rstrip('\n') for line in eoxf]
            skillListName = skil[(classlist[y]*skilMult)+skilAdd:]

            id=0
            for a, b in zip(skillList[y], skillListName):
                print('{:>4}'.format(str(id)+" -"),
                    '{:<2}'.format(a),
                    b)
                id+=1               
            print("Current SP: "+str(currentsplist[y]))    
        readskill()

        print("Which skill? (R)espec?:")
        skillidinput = input()

        if skillidinput == "r":
            
            skillList[y] = [0]*skilMult
            currentsplist[y] = lvlist[y]+2+retiresplist[y]
            readskill()
            print("Respec'd")

        else:
            print("To what level?:")
            skilllvinput = int(input())
            skillList[y][int(skillidinput)] = skilllvinput
            readskill()
            print("Done")

    else:
        print("Error")



os.system("pause")


