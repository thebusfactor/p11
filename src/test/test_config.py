import unittest

from src.model import config
from src.util.double_point import DoublePoint
#MIT License
#Copyright (c) 2018 ENGR301-302-2018 / Project-11

class ConfigTests(unittest.TestCase):

    def test_setting_box(self):
        box: DoublePoint = DoublePoint((1.0, 2.0), (5.0, 8.0))
        config.set_box(box)
        file_point = _get_file_point("box")
        assert file_point == box

    def test_getting_box(self):
        box: DoublePoint = DoublePoint((1.0, 2.0), (5.0, 8.0))
        config.set_box(box)
        get_box = config.get_box()
        assert box == get_box

    def test_setting_line(self):
        line: DoublePoint = DoublePoint((1.0, 2.0), (5.0, 8.0))
        config.set_line(line)
        file_point = _get_file_point("line")
        assert file_point == line

    def test_getting_line(self):
        line: DoublePoint = DoublePoint((1.0, 2.0), (5.0, 8.0))
        config.set_line(line)
        get_line = config.get_line()
        assert line == get_line

    def test_resetting_config(self):
        line: DoublePoint = DoublePoint((1.0, 2.0), (5.0, 8.0))
        box: DoublePoint = DoublePoint((7.0, 6.0), (4.0, 12.0))
        config.set_line(line)
        config.set_box(box)
        config.check_valid()
        config.reset_config()
        line_file_values = _collect_values("line")
        box_file_values = _collect_values("box")
        valid_file_values = _collect_values("valid")
        assert line_file_values == ["None", "None", "None", "None"]
        assert box_file_values == ["None", "None", "None", "None"]
        assert valid_file_values == []


def _get_file_point(name: str):
    file_values = _collect_values(name)
    return DoublePoint((float(file_values[0]), float(file_values[1])), (float(file_values[2]), float(file_values[3])))


def _collect_values(name: str):
    file = open(config.PATH, "r")
    collect = False
    collecting = []
    collect_amount = 4
    count = 0
    for line in file:
        if count >= collect_amount:
            break
        if collect:
            collecting.append(line[5:-1])
            count += 1
        if line == "[" + name + "]" + "\n":
            collect = True
    return collecting
