from abc import ABC, abstractmethod


class DoublePoint(ABC):

    point1: (float, float)
    point2: (float, float)

    def __init__(self, value):
        self.value = value
        super().__init__()