class World:
    xmax = 9
    ymax = 9

    well_x = 4
    well_y = 2
    wellt = 5
    well_used = False

    def navigation(self, x, y, p):
        while True:
            c = "[" + str(x) + "|" + str(y) + "] > "
            i = input(c)
            if i is "w" or i is "W":
                v = self.vaild_movement(x, y + 1)
                if v is True:
                    return x, y + 1
                else:
                    print("INVALID MOVEMENT")
            elif i is "d" or i is "D":
                v = self.vaild_movement(x + 1, y)
                if v is True:
                    return x + 1, y
                else:
                    print("INVALID MOVEMENT")
            elif i is "s" or i is "S":
                v = self.vaild_movement(x, y - 1)
                if v is True:
                    return x, y - 1
                else:
                    print("INVALID MOVEMENT")
            elif i is "a" or i is "A":
                v = self.vaild_movement(x - 1, y)
                if v is True:
                    return x - 1, y
                else:
                    print("INVALID MOVEMENT")
            elif i is "3":
                return -1, -1
            else:
                print("INVALID MOVEMENT (Try Using WSAD)")

    def start(self):
        print("STATUS LOG:     UNKNOWN DATE")
        print("----------------------------")
        print("Your Ship Has Crashed On A")
        print("Grassland Planet, Filled  ")
        print("With Rivers And Hills. You")
        print("Only Have A Python, And   ")
        print("Food And Water Is Not A   ")
        print("Problem. Your Goal Is To  ")
        print("Get Off This Planet.")
        print("Good Luck! (PRESS 3 TO EXIT)")
        print("----------------------------")

    def vaild_movement(self, x, y):
        if x > self.xmax:
            return False
        elif y > self.ymax:
            return False
        elif x < 0:
            return False
        elif y < 0:
            return False
        else:
            return True

    def random_encounter(self):
        import random

        rec = 3 #rec stands for random encounter chance

        r = random.randrange(rec-1)
        if r is 0:
            return True
        else:
            return False

    def random_monster(self):
        import random

        ml = 3 #ml is the total monsters/creatures available to fight

        return random.randrange(ml)

    def check_area(self, p):
        self.well_timmer()

        x, y = p.get_cordinates()
        if x is 4 and y is 2:
            if self.well_used is False:
                print("You Find A Well Which Heals You Completely.")
                p.hp = p.hpm
                self.well_used = True
            else:
                print("You Find A Empty Well. Use", self.wellt, "Moves To Use Again")
        elif x is 0 and y is 0:
            print("This Is Your Ship, Or The Ruins Of It")
        elif x is 3 and y is 4:
            v = Village(p, self, "Star Wood")
            del v
        else:
            print("There's Nothing Important Here.")

    def well_timmer(self):
        if self.well_used is True:
            if self.wellt >= 1:
                self.wellt -= 1
            else:
                self.well_used = False


class Village:
    name = ""

    def __init__(self, p, w, name):
        import os
        clear = lambda: os.system("cls")
        clear()

        self.name = name

        print("You Have Entered", self.name)

        while True:
            p.show_stats()
            print("1. Hospital")
            print("2. Brawl")
            print("3. Exit")

            i = input("> ")
            if i is "1":
                a = self.hospital(p)
            elif i is "2":
                a = self.brawl(p, w)

                if a is 0:
                    p.hp = p.hpm
                    print("You Were Sent To The Local Hospital And Didn't Have To Pay A Fee")
                    i = input("PRESS ENTER TO LEAVE")
            elif i is "3":
                break

            clear()

    def brawl(self, p, w):
        import os
        from Scripts import Brawl, Enemy, SaveLoad

        clear = lambda: os.system("cls")
        clear()

        for x in range(2, 100):
            e = Enemy.Enemy("Brawler", 15*x, 20*x, 17*x, 30, 50)
            l = Brawl.brawl(p, e, w)

            if l is 0:
                return 0
            elif l is 2:
                return 1

            clear()

            print("Ready Up For Battle", x)
            print("1. Continue")
            print("2. Leave")

            while True:
                i = int(input("> "))

                if i is 1:
                    break
                elif i is 2:
                    return 1

    def hospital(self, p):
        cost = 20 * p.level
        print("Would You Like To Pay", cost, "Xons To Heal Up? (Y/N)")

        while True:
            i = input("> ")

            if i is "Y" or i is "y":
                if p.xons < cost:
                    print("You Don't Have Enough Money Fool!")
                    i = input("PRESS ENTER TO LEAVE")
                    return 0
                else:
                    break
            elif i is "N" or i is "n":
                return 0

        p.xons -= cost
        p.hp = p.mhp

        print("Thank You For Using", self.name, "Local Hospital!")
        i = input("PRESS ENTER TO LEAVE")
        return 0