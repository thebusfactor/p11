

class Bus:
    tl: (float, float)
    br: (float, float)
    flagged: bool = 0
    dir = "up"

    def __init__(self, tl, br):
        self.tl = tl
        self.br = br

    def set_t1(self, t1):
        self.tl = t1

    def set_br(self, br):
        self.br = br

    def set_flagged(self, change):
        self.flagged = change

    def set_dir(self, new_dir):
        self.dir = new_dir