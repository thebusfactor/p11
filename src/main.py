# MIT License
# Copyright (c) 2018 ENGR301-302-2018 / Project-11

import os
import sys
import threading

from controller.controller import Controller
from model.ai import Ai
from model.model import Model
from ui.debug_ui import DebugGUI
from external.cam import Cam


def main(argv):
    fps: int = 24
    res = (1280, 720)

    try:
        classification_rate = argv[1]
        classification_rate = int(classification_rate)
        mode = str(argv[2])
        weights = int(argv[3])
        ai = Ai(classification_rate, mode, weights)
    except (TypeError, IndexError):
        ai = Ai()

    global path
    try:
        path = argv[4]
        path = int(path)
        cam = Cam(path)
    except IndexError:
        cam = Cam()
    except ValueError:
        cam = Cam(path)
    cam.start()
    model = Model(cam, ai, fps, res)
    view = DebugGUI(cam, model)

    Controller(model, ai, view)

    model.start()
    os.kill(os.getpid(), 1)

    pass


if __name__ == "__main__":
    main(sys.argv)
