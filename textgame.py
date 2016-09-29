# Place Creation Mostly By: Aaron Goidel
# Big thanks to him!

from random import randint

class Setting():
    locations = ["cave", "forest", "fork", "camp"]
    events = ["safety", "choice", "fight", "loot"]

    def __init__(self, locationNum, eventNum):
        self.location = self.locations[locationNum]
        self.event = self.events[eventNum]


class Place(object):
    cave = Setting(locationNum=0, eventNum=randint(2, 3))
    forest = Setting(locationNum=1, eventNum=randint(2, 3))
    fork = Setting(locationNum=2, eventNum=1)
    camp = Setting(locationNum=3, eventNum=0 if randint(0, 100) <= 75 else 2)
    settings = [cave, forest, fork, camp]

    def __init__(self, settingId):
        self.setting = self.settings[settingId]

    def __str__(self):
        return "Setting: %s, Event: %s" %(self.setting.location, self.setting.event)

for x in range(0,3):
    print(Place(randint(0, 3)))