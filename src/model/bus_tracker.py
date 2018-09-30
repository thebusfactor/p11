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

        # set all flags to false (refactor out to method)
        for bus in self.detected_buses:
            bus.set_flagged(False)
        if classifications is None or len(classifications) == 0:
            # self.detected_buses = []

            remove_buses = []
            remove_bus = None
            if len(self.detected_buses) > 0:
                for bus in self.detected_buses:
                    if not bus.flagged:
                        remove_buses.append(bus)
                if len(remove_buses) > 0:
                    self.detected_buses = [b for b in self.detected_buses if b not in remove_buses]

        elif len(classifications) > 0:
            for classed_bus in classifications:
                self.closest_dist = 9999999  # largest number
                selected_bus = None

                # Find closest stored bus to classification
                for bus in self.detected_buses:
                    # x1, y1 = self.small_box(classed_bus.tl["x"], classed_bus.tl["y"], classed_bus.br["x"], classed_bus.br["y"])
                    # dist = calc_distance(x1, bus.tl_x, y1, bus.tl_y)
                    dist = calc_distance(classed_bus.tl["x"], bus.tl_x, classed_bus.tl["y"], bus.tl_y)
                    if dist < self.closest_dist:
                        selected_bus = bus
                        self.closest_dist = dist

                # If the closest bus is sufficiently close enough
                if self.closest_dist < self.threshold_dist:
                    selected_bus.set_t1(classed_bus.tl["x"], classed_bus.tl["y"],
                                        classed_bus.br["x"], classed_bus.br["y"])
                    selected_bus.set_flagged(True)
                else:
                    # The bus is not very close, so this may be a new bus
                    self.detected_buses.append(Bus(classed_bus.tl["x"], classed_bus.tl["y"],
                                                   classed_bus.br["x"], classed_bus.br["y"], True))

            remove_buses = []
            remove_bus = None

            if len(self.detected_buses) > 0:
                for bus in self.detected_buses:
                    if not bus.flagged:
                        remove_buses.append(bus)
                if len(remove_buses) > 0:
                    self.detected_buses = [b for b in self.detected_buses if b not in remove_buses]

        return self.detected_buses

    def small_box(self, x1: int, y1: int, x2: int, y2: int):
        """
            This returns the top left and bottom right coordinates that define a small bounding box
            that make up a certain percentage. x1, y1 are top left, x2, y2 are bottom right.

            Parameters
            ----------
            x1 : int
                x position of the top left point of the larger, classification box.
            y1 : int
                y position of the top left point of the larger, classification box.
            x2 : int
                x position of the bottom right point of the larger, classification box.
            y2 : int
                y position of the bottom right point of the larger, classification box.

            Returns
            -------
            smallBox : []
                2d array representing the small box
        """
        width = abs(x2-x1)
        height = abs(y2-y1)

        percentage_to_remove = 0.3
        removed_section_width = width * percentage_to_remove
        removed_section_height = height * percentage_to_remove

        new_x1 = int(removed_section_width + x1)
        new_y1 = int(removed_section_height + y1)

        return new_x1, new_y1