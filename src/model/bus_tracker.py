from model.bus import Bus
from util.classification import Classification
import math


def calc_distance(tl1, tl2, br1, br2):
    return math.sqrt(math.pow((tl1 - tl2), 2) + math.pow((br1 - br2), 2))


class BusTracker:
    detected_buses = []

    def __init__(self):
        self.update_bus = False

    def update(self, classifications):
        """
        Iterates over the buses already detected and the new ones passed in, to see if the proximity between buses
        is small enough it classes the buses as the same and updates the detected_bus, else adds it as a new bus
        :param classifications: classified buses from camera
        :return:
        """
        distance = 100
        if len(classifications) > 0:
            for classed_bus in classifications:
                self.update_bus = False
                for bus in self.detected_buses:
                    if calc_distance(classed_bus.tl, bus.tl, classed_bus.br, bus.br) < distance:
                        bus.set_flagged(True)
                        bus.set_br(classed_bus.br)
                        bus.set_t1(classed_bus.tl)
                        self.update_bus = True
                        break
                        # make method to calc direction
                if not self.update_bus:
                    self.detected_buses.append(Bus(classed_bus.tl, classed_bus.br))
