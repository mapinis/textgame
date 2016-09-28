import random as rand

class Place(object):
    setting = 0
    lootType = 0
    healthBuff = 0
    strengthBuff = 0
    event = 0
    done = 0

    def generateLoot(self):
        self.lootType = ("health potion", "strength potion", "surprise")[rand.randint(0, 2)]
        if(self.lootType == "health potion"):
            self.healthBuff = rand.randint(5, 30)
        elif(self.lootType == "strength potion"):
            self.strengthBuff = rand.randint(5, 30)
    
    def __init__(self):
        self.setting = ("cave", "forest", "fork", "camp")[rand.randint(0, 3)]
        if(self.setting == "fork"):
            self.event == "choice"
        elif(self.setting == "camp"):
            self.event = "safety" if rand.randint(0, 100) <= 75 else "fight"
            self.generateLoot()
        else:
            self.event = ("fight", "loot")[rand.randint(0, 1)]
            self.generateLoot()

        self.done = False
    
for x in range(0, 3):
    place = Place()
    print(place.setting, place.event, place.lootType, place.healthBuff, place.strengthBuff)
        