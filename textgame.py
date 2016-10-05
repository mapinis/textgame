# Place Creation Mostly By: Aaron Goidel
# Big thanks to him!

from random import randint
from subprocess import call
call("clear", shell=True)
class Loot(object):
    loots = ["health", "strength", "surprise"]
    buff = 0

    def __init__(self, lootNum):
        self.loot = self.loots[lootNum]
        self.buff = randint(1, 10) if lootNum != 2 else None

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
        self.done = False
        if(self.setting.event != "safety" and self.setting.event != "choice"):
            self.loot = Loot(lootNum)


    def __str__(self):
        if(self.loot != None):
            print(self.loot)
            return "Setting: %s, Event: %s" %(self.setting.location, self.setting.event)
        else:
            return "Setting: %s, Event: %s, Loot None" %(self.setting.location, self.setting.event)

def sanitize(string):
    try:
        return int(string)
    except TypeError or ValueError:
        return sanitize(input("Not an integer. Please enter an integer: "))

health = 20
strength = 20

def printStats():
    global health
    global strength
    call("clear", shell = True)
    print("|-------------------------------------|")
    print("|  Health:", health)
    print("|  Strength: ", strength)
    print("|-------------------------------------|")

def fight():
    global health
    global strength
    print("fight")


inventory = []
places = [Place(3, 1, 2, True)]
currentPlace = 0
printStats()
print("\nYou wake up in a safe camp with a sword. There is a path that goes forward.")

def goto(place):
    global health
    global strength
    print("\nYou approach and enter a", place.setting.location)
    if(place.setting.event == "choice"):
        print("There is a choice to make. Right or Left?")
    elif(place.done):
        print("The %s is safe. What do you do?" %(place.setting.location))
    else:
        if(place.setting.event == "safety"):
            print("The %s is safe. What do you do?" %(place.setting.location))
        elif(place.setting.event == "loot"):
            print("You find abandoned loot.")
            if(input("Open it? (y/n): ").lower() == "y"):
                print("You find a", place.loot.loot)
                if(place.loot.loot == "health" or place.loot.loot == "strength"):
                    print("Your %s potion has a buff of %s" %(place.loot.loot, place.loot.buff))
                    if(input("Use it or take it? (use/take) ").lower() == "take"):
                        inventory.append(place.loot)
                    else:
                        if(place.loot.loot == "health"):
                            health += place.loot.buff
                        else:
                            strength += place.loot.buff
                        print("Increased %s by %s" %(place.loot.loot, place.loot.buff))
                    printStats()
                    print("\n")
                else:
                    fight()
                printStats()
        elif(place.setting.event == "fight"):
            fight()
    place.done = True

while(True):
    print("What do you do?")
    print("\t1. Go Forward")
    print("\t2. Go Back")
    print("\t3. View Inventory")
    print("\t4. Kill Yourself")
    inp = input("Please choose a number: ").lower()
    if(inp == "1" or inp == "forward" or inp == "go" or inp == "go forward"):
        if(currentPlace + 1 == len(places)):
            places.append(Place(randint(0, 3), randint(0, 3), randint(0, 2), False))
        currentPlace += 1
        printStats()
        goto(places[currentPlace])
    elif(inp == "2" or inp == "go" or inp == "back" or inp == "go back"):
        currentPlace -= 1 if(currentPlace > 0) else 0
        printStats()
        goto(places[currentPlace])
    elif(inp == "4" or inp == "kill" or inp == "yourself" or inp == "kill yourself"):
        break
    elif(inp == "3" or inp == "view" or inp == "inventory" or inp == "view inventory"):
        if(len(inventory) > 0):
            print("|-------------------------------------|")
            for i in range(len(inventory)):
                print("|  %s. Item: %s potion, Buff: %s" %(i+1, inventory[i].loot, inventory[i].buff))
        else:
            print("|-------------------------------------|")
            print("|  No Inventory Items")
        print("|  %s. Exit" %(len(inventory) + 1))
        print("|-------------------------------------|")
        inp = sanitize(input("Please input the number of an item to use it, or the last number to exit: "))
        if(inp != len(inventory) + 1):
            for i in range(len(inventory)):
                if(inp == i + 1):
                    if(inventory[i].loot == "health"):
                        health += inventory[i].buff
                    else:
                        strength += inventory[i].buff
                    print("Increased %s by %s" %(inventory[i].loot, inventory[i].buff))
                    del inventory[i]
                    break
        printStats()
        print("\n")
    else:
        print("Not an option")

print("You died.")