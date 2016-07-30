def load(self, l, w):
    load = open(l, "r")

    t = load.read()

    load.close()

    m = 1
    o = 0

    for n in range(len(t)):
        a = t[n]
        if a is "/":
            if m is 1:
                self.name = t[o:(n)]
            elif m is 2:
                self.gender = t[o:(n)]
            elif m is 3:
                self.level = int(t[o:(n)])
            elif m is 4:
                self.hp = int(t[o:(n)])
            elif m is 5:
                self.hpm = int(t[o:(n)])
            elif m is 6:
                self.at = int(t[o:(n)])
            elif m is 7:
                self.df = int(t[o:(n)])
            elif m is 8:
                self.xp = int(t[o:(n)])
            elif m is 9:
                self.xpm = int(t[o:(n)])
            elif m is 10:
                self.x = int(t[o:(n)])
            elif m is 11:
                self.y = int(t[o:(n)])
            elif m is 12:
                self.xons = int(t[o:(n)])
            elif m is 13:
                w.wellt = int(t[o:(n)])
                break
            o = n + 1
            m += 1

def save(self, w):
    l = text(self, w)

    file = self.name + ".txt"

    save = open(file, "w")
    save.write(l)
    save.close()

def text(self, w):
    return self.name + "/" + str(self.gender) + "/" + str(self.level) + "/" + str(self.hp) + "/" + str(self.hpm) + "/" + str(self.at) + "/" + str(self.df) + "/" + str(self.xp) + "/" + str(self.xpm)+ "/" + str(self.x) + "/" + str(self.y) + "/" + str(self.xons) + "/" + str(w.wellt) + "/"

def text_i(i):
    return

def save_i(self, i):
    l = text_i(i)

    file = self.name + "-Inv.txt"

    save = open(file, "w")
    save.write(l)
    save.close()
