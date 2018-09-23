

class Bus:
    t1_x: int = 0
    tl_y: int = 0
    flagged: bool = 0
    dir = "up"

    def __init__(self, tl_x, tl_y):
        self.tl_x = tl_x
        self.tl_y = tl_y

    def set_t1(self, new_tl_x, new_tl_y):
        self.tl_x = new_tl_x
        self.tl_y = new_tl_y

    def set_flagged(self, change):
        self.flagged = change

    def set_dir(self, new_dir):
        self.dir = new_dir