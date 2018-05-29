import configparser as cp

from src.util.double_point import DoublePoint

config = cp.ConfigParser()

PATH = "config.ini"
VALID = "validConfig"
LIGHT_BOX = "box"
INTERSECTION_LINE = "line"
INTERSECTION_LINE_PARALLEL = "line parallel"

X1 = "x1"
X2 = "x2"
Y1 = "y1"
Y2 = "y2"

config.add_section(VALID)
config.add_section(LIGHT_BOX)
config.add_section(INTERSECTION_LINE)
config.add_section(INTERSECTION_LINE_PARALLEL)


def check_valid():
    """
        checks if the config is valid

        Returns
        -------
        valid: Boolean
            if the config file is valid or not
    """
    is_valid = ("True" if ((get_box() is not None) and (
                get_line() is not None)) else "False")
    config.set(VALID, "value", is_valid)
    return is_valid


def reset_config():
    """
        resets the config file
    """
    print("reseting config")
    config.set(VALID, "value", "False")
    _set(LIGHT_BOX, DoublePoint((None, None),(None, None)))
    _set(INTERSECTION_LINE, DoublePoint((None, None),(None, None)))
    _write()


def get_valid():
    """
        gets the valid value from the config file

        Returns
        -------
        valid: Boolean
            represents if the config is valid or not
    """
    return config.getboolean(VALID)


def set_box(light_box: DoublePoint):
    """
        writes a double point as a box in config file
        if config files doesn't exist, the config file is created

        Parameters
        ----------
        light_box : DoublePoint
            the points that make up the box
    """
    _set(LIGHT_BOX, light_box)
    _write()


def get_box():
    """
        gets the light box values from the config file

        Returns
        -------
        light_box: DoublePoint
            two sets of tuples in DoublePoint object representing the two points the light box
    """
    return _get(LIGHT_BOX)


def get_line():
    """
        gets the intersection line values from the config file

        Returns
        -------
        intersection_line: DoublePoint
            two sets of tuples in DoublePoint object representing the two points of the intersection line

    """
    return _get(INTERSECTION_LINE)


def set_line(intersection_line: DoublePoint):
    """
        writes a double point as a line in config file
        if config files doesn't exist, the config file is created

        Parameters
        ----------
        intersection_line : DoublePoint
            the points that make up the intersection line
    """
    _set(INTERSECTION_LINE, intersection_line)
    _write()


def _get(name: str):
    point1 = (float(config.get(name, X1)), float(config.get(name, Y1)))
    point2 = (float(config.get(name, X2)), float(config.get(name, Y2)))
    return DoublePoint(point1, point2)


def _set(name: str, double_point: DoublePoint):
    config.set(name, X1, str(double_point.point1[0]))
    config.set(name, Y1, str(double_point.point1[1]))
    config.set(name, X2, str(double_point.point2[0]))
    config.set(name, Y2, str(double_point.point2[1]))
    return double_point


def _write():
    with open(PATH, 'w+') as configfile:
        config.write(configfile)
