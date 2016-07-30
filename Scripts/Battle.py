def battle(p, e, w):
    import os

    clear = lambda: os.system("cls")
    clear()

    ed, pd = False, False

    print("You Have Encountered A", e.name)
    while True:
        print("Enemy:", e.name)
        p.show_stats()
        print("1: Attack")
        print("2: Run")
        i = input("> ")
        if i is "1":
            ed = attack(p, e)
            if ed is True:
                break
            pd = deffence(p, e)
            if pd is True:
                break
        elif i is "2":
            r = run()
            if r is True:
                break
            pd = deffence(p, e)
            if pd is True:
                break
        else:
            continue
        i = input("PRESS ENTER TO CONTINUE")
        clear()
    if pd is True:
        print("You Died")
        i = input("PRESS ENTER TO EXIT")
        exit()
    elif ed is True:
        print("You Won")
        victory(p, e, w)
    i = input("PRESS ENTER TO CONTINUE")

def attack(p, e):
    import random

    h = p.at - e.df
    if h <= 0:
        h = 0

    r = random.randrange(10)

    if r is not 0:
        d = e.hp - h
        e.set_hp(d)

        print("You Dealt", h, "Damage To", e.name)
        if e.hp <= 0:
            return True
    else:
        print(e.name, "Dodged Your Attack!")

    return False

def deffence(p, e):
    import random

    h = e.at - p.df
    if h <= 0:
        h = 0

    r = random.randrange(10)

    if r is not 0:
        d = p.hp - h
        p.set_hp(d)

        print(e.name, "Dealt", h, "Damage To You")
        if p.hp <= 0:
            return True
    else:
        print("You Dodged The Enemy's Attack!")

    return False

def victory(p, e, w):
    p.gain_xp(e.xpr, w)
    p.gain_xons(e.xons)

def run():
    import random
    r = random.randrange(10)
    if r < 5:
        print("You Escaped!")
        return True
    else:
        print("You Failed To Escaped.")
        return False