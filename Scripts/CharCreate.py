class Player:
    name = ""

    gender = ""

    level = 0
    hp = 0
    hpm = 0
    at = 0
    df = 0

    xp = 0
    xpm = 0

    x = 0
    y = 0

    t = ""

    xons = 0

    def New_Player(self, w):
        from Scripts import SaveLoad

        print("So What Is Your Name?")
        self.name = input("> ")
        print("Your Name Better Be", self.name)
        print("Anyway, Are You Male Or Female? (Type 'M' or 'F')")
        self.gender = input("> ")

        if self.gender is not "M" and self.gender is not "F":
            import antigravity

        self.Default_Stats(i)

        self.t = self.name+".txt"

        SaveLoad.save(self, w)

    def Default_Stats(self):
        self.level = 1
        self.hp = 10
        self.hpm = 10
        self.at = 4
        self.df = 2
        self.xpm = 10

    def show_stats(self):
        print("--------------")
        print("Name:", self.name)
        print("Level:", self.level)
        print("HP:", self.hp, "/", self.hpm)
        print("Attack:", self.at)
        print("Defence:", self.df)
        print("Xp:", self.xp, "/", self.xpm)
        print("Xons:", self.xons)
        print("--------------")

    def get_cordinates(self):
        return self.x, self.y

    def set_cordinates(self, x, y):
        self.x, self.y = x, y

    def set_hp(self, h):
        self.hp = h

    def gain_xp(self, g, w):
        self.xp += g
        if self.xp >= self.xpm:
            self.level_up(w)

    def level_up(self, w):
        import math
        from Scripts import SaveLoad
        print("--LEVEL UP--")
        print("Chose a attribute to focus on")
        self.show_stats()
        print("1. Hp")
        print("2. Attack")
        print("3. Deffense")

        while True:
            i = input("> ")
            if i is "1" or i is "2" or i is "3":
                break

        i = int(i)

        self.hpm += 5
        self.hp = self.hpm
        self.at += 3
        self.df += 3

        if i is 1:
            self.hp += 10
        elif i is 2:
            self.at += 2
        elif i is 3:
            self.df += 2

        self.xp -= self.xpm
        self.xpm += 5 * int(math.ceil(self.level/2))
        self.gain_xp(0, w)

        self.level += 1

        print("LEVEL UP COMPLETE")

        SaveLoad.save(self, w)

    def gain_xons(self, x):
        self.xons += x