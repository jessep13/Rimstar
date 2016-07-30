class Enemy:
    name = ""
    hp = 0
    hpm = 0
    at = 0
    df = 0
    xpr = 0
    xons = 0

    def __init__(self, name, hpm, at, df, xpr, xons):
        self.name = name
        self.hpm = hpm
        self.hp = hpm
        self.at = at
        self.df = df
        self.xpr = xpr
        self.xons = xons

    def set_hp(self, h):
        self.hp = h