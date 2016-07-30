import os
from Scripts import Battle, CharCreate, Enemy, World, SaveLoad

version = "Pre-Alpha V0.0.6"

item_count = 3

p = CharCreate.Player()
w = World.World()

def scan_items():
    for i in range(item_count):
        pass

def enc(p, w):
    r = w.random_monster()
    if r is 0:
        if p.level <= 5:
            e = Enemy.Enemy("Rat", 5, 0, 1, 3, 0)
        elif p.level > 5 and p.level <= 10:
            e = Enemy.Enemy("Raptor", 8, 15, 3, 15, 15)
        elif p.level > 10 and p.level <= 15:
            e = Enemy.Enemy("Mutant Lizard", 30, 25, 5, 30, 30)
        elif p.level > 15 and p.level <= 20:
            e = Enemy.Enemy("Swarm", 50, 50, 15, 75, 65)
        elif p.level > 20:
            e = Enemy.Enemy("Rouge Pilot", 80, 70, 50, 80, 400)
    elif r is 1:
        if p.level <= 5:
            e = Enemy.Enemy("Cow", 5, 0, 3, 5, 10)
        elif p.level > 5 and p.level <= 10:
            e = Enemy.Enemy("Ox", 20, 35, 20, 20, 30)
        elif p.level > 10 and p.level <= 15:
            e = Enemy.Enemy("Charger", 30, 55, 30, 40, 50)
        elif p.level > 15 and p.level <= 20:
            e = Enemy.Enemy("Cyclone", 40, 65, 50, 90, 85)
        elif p.level > 20:
            e = Enemy.Enemy("Ascari", 100, 85, 80, 200, 100)
    elif r is 2:
        if p.level <= 5:
            e = Enemy.Enemy("Bat", 7, 4, 2, 4, 3)
        elif p.level > 5 and p.level <= 10:
            e = Enemy.Enemy("Energenic Golem", 45, 10, 15, 45, 30)
        elif p.level > 10 and p.level <= 15:
            e = Enemy.Enemy("Zulu", 45, 50, 25, 50, 65)
        elif p.level > 15 and p.level <= 20:
            e = Enemy.Enemy("Yankee", 60, 75, 30, 100, 120)
        elif p.level > 20:
            e = Enemy.Enemy("X-ray", 150, 120, 60, 400, 600)
    Battle.battle(p, e, w)
    del e

def load(p):
    print("What Is The Name Of The Player?")
    i = input("> ")
    a = i + ".txt"
    SaveLoad.load(p, a, w)

while True:
    clear = lambda: os.system("cls")
    clear()

    print("Welcome to RimStar")
    print("------------------")
    print("Input A Number To")
    print("Select A Number.")
    print("1. New Game")
    print("2. Load")
    print("3. Exit \n")
    print("Version:", version)

    i = int(input("> "))
    if i is 1:
        p.New_Player(w)
        w.start()
        a = input("PRESS ENTER TO CONTINUE")
        del a
        break
    elif i is 2:
        load(p)
        break
    elif i is 3:
        exit()

x, y = p.get_cordinates()

while True:
    clear()

    scan_items()

    w.check_area(p)

    p.show_stats()

    x, y = p.get_cordinates()
    x, y = w.navigation(x, y, p)
    if x is -1 and y is -1:
        SaveLoad.save(p, w)
        exit()
    p.set_cordinates(x, y)

    encounter = w.random_encounter()
    if encounter is True:
        enc(p, w)

