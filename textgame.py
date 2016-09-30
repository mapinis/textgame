# Place Creation Mostly By: Aaron Goidel
# Big thanks to him!

from random import randint
class Loot(object):
    loots = ["health", "strength", "surprise"]
    buff = 0

    def __init__(self, lootNum):
        self.loot = self.loots[lootNum]
        self.buff = randint(5, 30) if lootNum != 2 else None

class Setting():
    locations = ["cave", "forest", "fork", "camp"]
    events = ["choice", "safety", "fight", "loot"]

    def __init__(self, locationNum, eventNum):
        self.location = self.locations[locationNum]
        if(locationNum == 2):
            self.event = self.events[0]
        elif(locationNum == 3):
            self.event = self.events[1] if randint(0, 100) < 75 else self.events[2]
        else:
            self.event = self.events[eventNum]


class Place(object):
    def __init__(self, locationNum, eventNum, lootNum):
        self.setting = Setting(locationNum, eventNum)
        self.loot = None
        if(self.setting.event != "safety" and self.setting.event != "choice"):
            self.loot = Loot(lootNum)

    def __str__(self):
        if(self.loot != None):
            return "Setting: %s, Event: %s, Loot %s, Buff %s" %(self.setting.location, self.setting.event, self.loot.loot, self.loot.buff)
        else:
            return "Setting: %s, Event: %s, Loot None" %(self.setting.location, self.setting.event)

for x in range(0,4):
    print(Place(randint(0, 3), randint(1, 3), randint(0, 2)))