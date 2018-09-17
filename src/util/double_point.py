# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11


class DoublePoint:
    point1: (float, float)
    point2: (float, float)

    def __init__(self, point1: (float, float), point2: (float, float)):
        self.point1 = point1
        self.point2 = point2

    def __eq__(self, other):
        """
        Overrides the default implementation
        """
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False
