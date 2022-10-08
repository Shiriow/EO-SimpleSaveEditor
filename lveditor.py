import sys
import os

try:
    saveLocation = sys.argv[1]  # drag and drop
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

    elif gameID == "MO1RGAME": #
        levelOffset = 2116
        partyOffset = 2112
        snameOffset = 2328
        enameOffset = 2347
        addOffset = 384

    elif gameID == "MO2RGAME": #
        levelOffset = 376
        partyOffset = 372
        snameOffset = 564
        enameOffset = 583
        addOffset = 264

    elif gameID == "MOR4GAME": #
        levelOffset = 199
        partyOffset = 196
        snameOffset = 400
        enameOffset = 419
        addOffset = 364

    elif gameID == "MO5_GAME": #
        levelOffset = 328
        partyOffset = 324
        snameOffset = 504
        enameOffset = 523
        addOffset = 336

    else:
        print(fileContent[0:8].decode('shift-jis'))
except ValueError:
    print("Not an EO save")
    os.system("pause")

levelOffsetR = levelOffset
partyOffsetR = partyOffset
snameOffsetR = snameOffset
enameOffsetR = enameOffset

for x in range(30):

    lvlist.append(fileContent[levelOffsetR])
    benchlist.append(fileContent[partyOffsetR])

    name = fileContent[snameOffsetR:enameOffsetR].decode('shift-jis')
    namelist.append(name.replace('\x00', ' '))
    levelOffsetR += addOffset
    partyOffsetR += addOffset
    snameOffsetR += addOffset
    enameOffsetR += addOffset


def readFile():
    id=0
    for ia, ib, ic in zip(lvlist,namelist,benchlist):
        print('{:>4}'.format(str(id)+" -"), 
        ib, 
        '{:>4}'.format(str(ia)), 
        "Party" if ic == 3 else "")

        id += 1


readFile()

def saveFile():

    idsave = 0
    save1 = levelOffset
    save2 = partyOffset

    with open(saveLocation, 'rb') as rfile:
        fileContent = rfile.read()
    backup = open(backupLocation, "wb")
    backup.write(fileContent)
    
    fh = open(saveLocation, "r+b")
    for x in range(30):
        fh.seek(save1)
        fh.write(int(lvlist[idsave]).to_bytes(1, 'little'))
        fh.seek(save2)
        fh.write(int(benchlist[idsave]).to_bytes(1, 'little'))
        idsave += 1
        save1 += addOffset
        save2 += addOffset
        

while True:

    print("Which ID to edit? (S)ave? (A)dd to party? (R)emove from party?:")
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


    else:
        print("Error")




os.system("pause")


