from model.bus import Bus
from util.classification import Classification
import math


def calc_distance(tl1, tl2, br1, br2):
    return math.sqrt(math.pow((tl1 - tl2), 2) + math.pow((br1 - br2), 2))


class BusTracker:
    detected_buses = []

    def __init__(self):
        self.closest_dist = 9999999
        self.threshold_dist = 250

    def update(self, classifications, res):
        """
        Iterates over the buses already detected and the new ones passed in, to see if the proximity between buses
        is small enough it classes the buses as the same and updates the detected_bus, else adds it as a new bus
        :param classifications: classified buses from camera
        :return:
        """
        if len(classifications) > 0:
            for classed_bus in classifications:
                self.closest_dist = 9999999  # largest number
                selected_bus = None

                # Find closest stored bus to classification
                for bus in self.detected_buses:
                    dist = calc_distance(classed_bus.tl["x"], bus.tl_x, classed_bus.tl["y"], bus.tl_y)
                    if dist < self.closest_dist:
                        selected_bus = bus
                        self.closest_dist = dist

                # If the closest bus is sufficiently close enough
                if self.closest_dist < self.threshold_dist:
                    selected_bus.set_t1(classed_bus.tl["x"], classed_bus.tl["y"])
                    print("x +", classed_bus.tl["x"])
                    # print("y +", classed_bus.tl["y"])
                else:
                    # The bus is not very close, so this may be a new bus
                    self.detected_buses.append(Bus(classed_bus.tl["x"], classed_bus.tl["y"]))

        #     remove_buses = []
        #     if len(self.detected_buses) > 0:
        #         for bus in self.detected_buses:
        #             if bus.t1_x == 0:
        #                 remove_buses.append(bus)
        #         if len(remove_buses) > 0:
        #             print(remove_buses)
        #             print(self.detected_buses)
        #             self.detected_buses.remove(remove_buses)
        # # print(len(self.detected_buses))

    def get_detected_buses(self):
        return self.detected_buses
