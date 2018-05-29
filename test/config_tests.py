import unittest

from model import config
from util.double_point import DoublePoint


def run_all():
    test_setting_box()


def test_setting_box():
    box: DoublePoint = DoublePoint((1.0, 2.0), (5.0, 8.0))
    config.set_box(box)
    file_values = _collect_values("box")


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
            collecting.append(float(line[5:-1]))
            count += 1
        if line == "["+name+"]"+"\n":
            collect = True
        print(line)
    return collecting

run_all()