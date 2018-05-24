import configparser as cp

from util.double_point import DoublePoint

config = cp.ConfigParser()

PATH = "config.ini"
BOX = "box"
LINE = "line"

X1 = "x1"
X2 = "x2"
Y1 = "y1"
Y2 = "y2"

config.add_section(BOX)
config.add_section(LINE)


def set_box(box: DoublePoint):
    """
        writes a double point as a box in config file
        if config files doesn't exist, the config file is created

        Parameters
        ----------
        box : DoublePoint
            the points that make up the box
    """
    _set(BOX, box)
    _write()


def get_box():
    """
        gets the box values from the config file

        Returns
        -------
        DoublePoint
            two sets of tuples in DoublePoint Object representing the two point to make a box

    """
    return _get(BOX)


def set_line(line: DoublePoint):
    """
        writes a double point as a line in config file
        if config files doesn't exist, the config file is created

        Parameters
        ----------
        line : DoublePoint
            the points that make up the line
    """
    _set(LINE, line)
    _write()


def get_line():
    """
        gets the line values from the config file

        Returns
        -------
        DoublePoint
            two sets of tuples in DoublePoint Object representing the two point to make a line

    """
    return _get(LINE)


def _get(name: str):
    double_point: DoublePoint
    double_point.point1 = (config.get(name, X1), config.get(name, Y1))
    double_point.point2 = (config.get(name, X2), config.get(name, Y2))
    return double_point


def _set(name: str, double_point: DoublePoint):
    config.set
    config.set(name, X1, double_point.point1[0])
    config.set(name, X2, double_point.point1[1])
    config.set(name, Y1, double_point.point2[0])
    config.set(name, Y2, double_point.point2[1])
    return double_point


def _write():
    with open(PATH, 'w+') as configfile:
        config.write(configfile)
