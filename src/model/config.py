import configparser as cp

from util.double_point import DoublePoint

config = cp.ConfigParser()

PATH = "config.ini"
VALID = "validConfig"
LIGHTBOX = "box"
INTERSECTION_LINE = "line"
INTERSECTION_LINE_PARALLEL = "line parallel"

X1 = "x1"
X2 = "x2"
Y1 = "y1"
Y2 = "y2"

config.add_section(VALID)
config.add_section(LIGHTBOX)
config.add_section(INTERSECTION_LINE)
config.add_section(INTERSECTION_LINE_PARALLEL)

def check_valid():
    isValid = ("True" if (((config.get(LIGHTBOX) != None) and (config.get(INTERSECTION_LINE) != None))) else "False")
    config.set(VALID, "value", isValid)
    return isValid

def reset_config():
    print("Resetting Config Files")
    config.set(VALID, "value", "False")
    _set(LIGHTBOX, DoublePoint((None, None),(None, None)))
    _set(INTERSECTION_LINE, DoublePoint((None, None),(None, None)))
    _write()

def get_valid():
    return config.getboolean(VALID)

def set_box(box: DoublePoint):
    _set(LIGHTBOX, box)
    _write()


def get_box():
    return _get(LIGHTBOX)


def get_line():
    return _get(INTERSECTION_LINE)


def set_line(line: DoublePoint):
    _set(INTERSECTION_LINE, line)
    _write()


def _get(name: str):
    double_point: DoublePoint
    double_point.point1 = (config.get(name, X1), config.get(name, Y1))
    double_point.point2 = (config.get(name, X2), config.get(name, Y2))
    return double_point


def _set(name: str, double_point: DoublePoint):
    config.set(name, X1, str(double_point.point1[0]))
    config.set(name, X2, str(double_point.point1[1]))
    config.set(name, Y1, str(double_point.point2[0]))
    config.set(name, Y2, str(double_point.point2[1]))
    return double_point


def _write():
    with open(PATH, 'w+') as configfile:
        config.write(configfile)
