def calculateHealth(age,appleamt,cigamt):
    health = (100 - age) + (appleamt * 1.5) - (cigamt * 2)
    print("you will live ",health,"more years")

nandika = [25,1,4]

calculateHealth(nandika[0],nandika[1],nandika[2])
calculateHealth(*nandika)