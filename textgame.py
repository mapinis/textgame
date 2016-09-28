import random as rand

def generateLoot(cls):
    setattr(cls, "healthBuff", 0)
    setattr(cls, "strengthBuff", 0)
    setattr(cls, "lootType", ("health potion", "strength potion", "surprise")[rand.randint(0, 2)])
    if(getattr(cls, "lootType") == "health potion"):
        setattr(cls, "healthBuff", rand.randint(5, 30))
    elif(getattr(cls, "lootType") == "strength potion"):
        setattr(cls, "strengthBuff", rand.randint(5, 30))
    return cls

@generateLoot
class Loot(object):
    pass

def generatePlace(cls):
    setattr(cls, "setting", ("cave", "forest", "fork", "camp")[rand.randint(0, 3)])
    if(getattr(cls, "setting") == "fork"):
        setattr(cls, "event", "choice")
    elif(getattr(cls, "setting") == "camp"):
        setattr(cls, "event", "safety" if rand.randint(0, 100) <= 75 else "fight")
        setattr(cls, "loot", Loot())
    else:
        setattr(cls, "event", ("fight", "loot")[rand.randint(0, 1)])
        setattr(cls, "loot", Loot())
    setattr(cls, "looted", False)
    return cls

@generatePlace
class Place(object):
    pass

place = Place()
print(place.setting, place.event, place.loot.healthBuff, place.loot.strengthBuff)
place1 = Place()
print(place1.setting, place1.event, place1.loot.healthBuff, place1.loot.strengthBuff)
place2 = Place()
print(place2.setting, place2.event, place2.loot.healthBuff, place2.loot.strengthBuff)
        