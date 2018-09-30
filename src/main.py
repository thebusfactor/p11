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

    fixed_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(fixed_path, "../../resources/full_vid.mp4")

    cam = Cam(path)
    ai = Ai()

    model = Model(cam, ai, fps, res)
    view = DebugGUI(cam)

    Controller(model, ai, view)

    model.start()
    os.kill(os.getpid(), 1)

    pass


if __name__ == "__main__":
    main(sys.argv)
