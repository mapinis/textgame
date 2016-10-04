# Place Creation Mostly By: Aaron Goidel
# Big thanks to him!

from random import randint
class Loot(object):
    loots = ["health", "strength", "surprise"]
    buff = 0

    def __init__(self, lootNum):
        self.loot = self.loots[lootNum]
        self.buff = randint(5, 30) if lootNum != 2 else None

    def __str__(self):
        return("Loot %s, Buff %s" %(self.loot, self.buff))

class Setting():
    locations = ["cave", "forest", "fork", "camp"]
    events = ["choice", "safety", "fight", "loot"]

    def __init__(self, locationNum, eventNum, beginning):
        self.location = self.locations[locationNum]
        if(locationNum == 2):
            self.event = self.events[0]
        elif(locationNum == 3):
            self.event = self.events[1] if randint(0, 100) < 75 else self.events[2]
        else:
            self.event = self.events[eventNum]
        if(beginning):
            self.location = "camp"
            self.event = "safety"


class Place(object):
    def __init__(self, locationNum, eventNum, lootNum, beginning):
        self.setting = Setting(locationNum, eventNum, beginning)
        self.loot = None
        if(self.setting.event != "safety" and self.setting.event != "choice"):
            self.loot = Loot(lootNum)


    def __str__(self):
        if(self.loot != None):
            print(self.loot)
            return "Setting: %s, Event: %s" %(self.setting.location, self.setting.event)
        else:
            return "Setting: %s, Event: %s, Loot None" %(self.setting.location, self.setting.event)


def printStats():
    print("|-------------------------------------|")
    print("|  Health:", health)
    print("|  Strength: ", strength)
    print("|-------------------------------------|")

health = 20
strength = 20
inventory = []
places = [Place(3, 1, 2, True)]
printStats()
print("\nYou wake up in a safe camp with a sword. There is a path that goes forward.")
print("What do you do?")
print("\t1. Go Forward")
print("\t2. Kill Yourself")

while(True):
    inp = input("Please choose a number: ").lower()
    if(inp == "1" or inp == "forward" or inp == "go" or inp == "go forward"):
        while(True):
            places.append(Place(randint(0, 3), randint(0, 3), randint(0, 2), False))
            printStats()
            print("\nYou approach and enter a", places[-1].setting.location)
            if(places[-1].setting.event == "safety"):
                print("The %s is safe. What do you do?" %(places[-1].setting.location))
            elif(places[-1].setting.event == "choice"):
                print("There is a choice to make. Right or Left?")
            elif(places[-1].setting.event == "loot"):
                print("You find abandoned loot.")
                if(input("Open it? (y/n)").lower() == "y"):
                    print("You find a ", places[-1].loot.loot)
                    if(places[-1].loot.loot == "health" or places[-1].loot.loot == "strength"):
                        print("Your %s potion has a buff of %s" %(places[-1].loot.loot, places[-1].loot.buff))
                        if(input("Use it or take it? (use/take) ").lower() == "take"):
                            inventory.append(places[-1].loot)
                        else:
                            print("use")
    elif(inp == "2" or inp == "kill" or inp == "yourself" or inp == "kill yourself"):
        break
    else:
        print("Not an option")

print("You died.")