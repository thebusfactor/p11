

class Bus:
    tl_x: int
    tl_y: int
    br_x: int
    br_y: int
    flagged: bool
    dir = "up"
    has_intersected: bool

    def __init__(self, tl_x, tl_y, br_x, br_y, flagged):
        self.tl_x = tl_x
        self.tl_y = tl_y
        self.br_x = br_x
        self.br_y = br_y
        self.flagged = flagged
        self.has_intersected = False

    def set_t1(self, new_tl_x, new_tl_y, new_br_x, new_br_y):
        self.tl_x = new_tl_x
        self.tl_y = new_tl_y
        self.br_x = new_br_x
        self.br_y = new_br_y

    def set_flagged(self, change):
        self.flagged = change

    def set_dir(self, new_dir):
        self.dir = new_dir

    def get_tl_x(self):
        return self.tl_x

    def set_has_intersected(self, has_intersected):
        self.has_intersected = has_intersected

    def get_has_intersected(self):
        return self.has_intersected
