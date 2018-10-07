# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

import configparser as cp


config = cp.ConfigParser()

PATH = "./config.ini"
VALID = "validConfig"
LIGHT_BOX = "box"
INTERSECTION_LINE = "line"

X1 = "x1"
X2 = "x2"
Y1 = "y1"
Y2 = "y2"

config.add_section(VALID)
config.add_section(LIGHT_BOX)
config.add_section(INTERSECTION_LINE)


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
    config.set(VALID, "value", "False")
    set_points(LIGHT_BOX, ((None, None), (None, None)))
    set_points(INTERSECTION_LINE, ((None, None), (None, None)))
    write()


def get_valid():
    """
        gets the valid value from the config file

        Returns
        -------
        valid: Boolean
            represents if the config is valid or not
    """
    return config.getboolean(VALID)


def set_box(light_box):
    """
        writes a double point as a box in config file
        if config files doesn't exist, the config file is created

        Parameters
        ----------
        light_box : (int, int)
            the points that make up the box
    """
    set_points(LIGHT_BOX, light_box)
    write()


def get_box():
    """
        gets the light box values from the config file

        Returns
        -------
        light_box: DoublePoint
            two sets of tuples in DoublePoint object representing the two points the light box
    """
    config.read(PATH)
    return _get(LIGHT_BOX)


def get_line():
    """
        gets the intersection line values from the config file

        Returns
        -------
        intersection_line: DoublePoint
            two sets of tuples in DoublePoint object representing the two points of the intersection line

    """
    config.read(PATH)
    return _get(INTERSECTION_LINE)


def set_line(intersection_line):
    """
        writes a double point as a line in config file
        if config files doesn't exist, the config file is created

        Parameters
        ----------
        intersection_line : DoublePoint
            the points that make up the intersection line
    """
    set_points(INTERSECTION_LINE, intersection_line)
    write()


def _get(name: str):
    point1 = (int(config.get(name, X1)), int(config.get(name, Y1)))
    point2 = (int(config.get(name, X2)), int(config.get(name, Y2)))
    return [point1, point2]


def set_points(name: str, double_point):
    config.set(name, X1, str(double_point[0][0]))
    config.set(name, Y1, str(double_point[0][1]))
    config.set(name, X2, str(double_point[1][0]))
    config.set(name, Y2, str(double_point[1][1]))


def write():
    with open(PATH, 'w+') as configfile:
        config.write(configfile)
