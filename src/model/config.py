import configparser as cp

config = cp.ConfigParser()
PATH = "config.ini"


def set_box():
    config.add_section("Box")
    config.set("Box", "x1", "15")
    write()

def get_box():
    pass


def write():
    with open(PATH, 'w+') as configfile:
        config.write(configfile)


set_box()